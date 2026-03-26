const Registro = require("../models/Registro");
const CalculadoraDesconto = require("../services/CalculadoraDesconto");

class Estacionamento {
  #registrosAtivos;
  #historico;
  #bloqueados;
  #placasAtivas;

  constructor() {
    this.#registrosAtivos = new Map();
    this.#historico = [];
    this.#bloqueados = new Set();
    this.#placasAtivas = new Set();
  }

  get bloqueados() {
    return this.#bloqueados;
  }

  get historico() {
    return this.#historico;
  }

  get registrosAtivos() {
    return Array.from(this.#registrosAtivos.values()).map((item) => item.registro);
  }

  carregarHistorico(registros) {
    this.#historico = registros;
  }

  carregarRegistrosAtivos(registros) {
    this.#registrosAtivos = new Map();
    this.#placasAtivas = new Set();

    registros.forEach((registro) => {
      this.#registrosAtivos.set(registro.veiculo.placa, {
        registro,
        cliente: registro.cliente,
      });
      this.#placasAtivas.add(registro.veiculo.placa);
    });
  }

  registrarEntrada(veiculo, cliente) {
    if (this.#placasAtivas.has(veiculo.placa)) {
      console.log(
        `Erro: O veiculo com placa ${veiculo.placa} ja esta no estacionamento.`,
      );
      return false;
    }

    if (cliente.constructor.name === "Estudante" && cliente.saldo < 0) {
      this.#bloqueados.add(cliente.documento);
      console.log(`[NEGADO] Estudante ${cliente.nome} com saldo negativo.`);
      return false;
    }

    this.#bloqueados.delete(cliente.documento);

    if (cliente.constructor.name === "Professor") {
      const jaTemProfessor = Array.from(this.#registrosAtivos.values()).some(
        (item) => item.cliente.documento === cliente.documento,
      );

      if (jaTemProfessor) {
        console.log(
          `[NEGADO] Professor ${cliente.nome} ja possui um veiculo no patio.`,
        );
        return false;
      }
    }

    const novoRegistro = new Registro(veiculo, cliente);
    this.#registrosAtivos.set(veiculo.placa, {
      registro: novoRegistro,
      cliente,
    });
    this.#placasAtivas.add(veiculo.placa);

    console.log(
      `[ENTRADA] Veiculo: ${veiculo.placa} | Cliente: ${cliente.nome}`,
    );
    return true;
  }

  registrarSaida(placa, dataForcada = new Date()) {
    if (!this.#placasAtivas.has(placa)) {
      console.log(`Erro: Veiculo com placa ${placa} nao encontrado.`);
      return false;
    }

    const { registro, cliente } = this.#registrosAtivos.get(placa);
    const dataSaida = dataForcada;

    let valorBase = cliente.calcularTarifa(registro.entrada, dataSaida);
    let idDesconto = "nenhum";
    let valorFinal = valorBase;

    if (cliente.constructor.name === "ClienteAvulso") {
      const resultado = CalculadoraDesconto.obterDescontoPadrao(valorBase);
      valorFinal = resultado.valorComDesconto;
      idDesconto = resultado.id;
    }

    if (cliente.constructor.name === "Estudante") {
      cliente.debitarSaldo(valorFinal);

      if (cliente.saldo < 0) {
        this.#bloqueados.add(cliente.documento);
      }
    }

    registro.finalizar(valorFinal, dataSaida);
    this.#historico.push(registro);
    this.#registrosAtivos.delete(placa);
    this.#placasAtivas.delete(placa);

    console.log(`--- COMPROVANTE DE SAIDA ---`);
    console.log(
      `Placa: ${placa} | Valor: R$ ${valorFinal.toFixed(2)} | Desconto: ${idDesconto}`,
    );
    return true;
  }
}

module.exports = Estacionamento;
