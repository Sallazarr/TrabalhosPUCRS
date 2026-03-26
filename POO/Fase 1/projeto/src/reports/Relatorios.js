class Relatorios {
  static #mesmoDia(data, ano, mes, dia) {
    return (
      data.getFullYear() === ano &&
      data.getMonth() === mes &&
      data.getDate() === dia
    );
  }

  static #dentroDoPeriodo(registro, inicio, fim) {
    return registro.entrada >= inicio && registro.saida && registro.saida <= fim;
  }

  static totalArrecadado(registros) {
    return registros.reduce((total, r) => total + r.valorTotal, 0);
  }

  static totalArrecadadoPorPeriodo(registros, inicio, fim) {
    return registros
      .filter((r) => this.#dentroDoPeriodo(r, inicio, fim))
      .reduce((total, r) => total + r.valorTotal, 0);
  }

  static porCategoria(registros) {
    const mapa = {};

    registros.forEach((r) => {
      const tipo = r.cliente.constructor.name;
      mapa[tipo] = (mapa[tipo] || 0) + r.valorTotal;
    });

    return mapa;
  }

  static porCategoriaNoPeriodo(registros, inicio, fim) {
    return this.porCategoria(
      registros.filter((r) => this.#dentroDoPeriodo(r, inicio, fim)),
    );
  }

  static situacaoCliente(cliente, registrosAtivos, bloqueadosSet, historico) {
    const registroAtivo = registrosAtivos.find(
      (registro) => registro.cliente.documento === cliente.documento,
    );

    const totalVisitas = historico.filter(
      (registro) => registro.cliente.documento === cliente.documento,
    ).length;

    return {
      nome: cliente.nome,
      documento: cliente.documento,
      tipo: cliente.constructor.name,
      bloqueado: bloqueadosSet.has(cliente.documento),
      noPatio: Boolean(registroAtivo),
      placaAtiva: registroAtivo ? registroAtivo.veiculo.placa : null,
      saldo: typeof cliente.saldo === "number" ? cliente.saldo : null,
      totalVisitas,
    };
  }

  static clientePorPeriodo(registros, documento, inicio, fim) {
    return registros.filter(
      (r) => r.cliente.documento === documento && this.#dentroDoPeriodo(r, inicio, fim),
    );
  }

  static avulsosPorPeriodo(registros, inicio, fim) {
    return registros.filter(
      (r) =>
        r.cliente.constructor.name === "ClienteAvulso" &&
        this.#dentroDoPeriodo(r, inicio, fim),
    );
  }

  static clientesBloqueados(bloqueadosSet) {
    return Array.from(bloqueadosSet);
  }

  static top10DoAno(registros, ano = new Date().getFullYear()) {
    const mapa = {};

    registros
      .filter((r) => r.saida && r.saida.getFullYear() === ano)
      .forEach((r) => {
        const chave = `${r.cliente.nome} (${r.cliente.documento})`;
        mapa[chave] = (mapa[chave] || 0) + 1;
      });

    return Object.entries(mapa)
      .sort((a, b) => b[1] - a[1])
      .slice(0, 10);
  }
}

module.exports = Relatorios;
