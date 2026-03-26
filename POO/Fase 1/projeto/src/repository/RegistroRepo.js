const fs = require("fs");
const Registro = require("../models/Registro");
const Veiculo = require("../models/Veiculo");
const ClienteAvulso = require("../models/ClienteAvulso");

class RegistroRepository {
  static #criarCliente(documento, clientes) {
    if (documento === "000") {
      return new ClienteAvulso("Visitante", "000");
    }

    return clientes.find((cliente) => cliente.documento === documento) || null;
  }

  static #criarRegistroDaLinha(linha, clientes, possuiSaida) {
    if (!linha) return null;

    const partes = linha.split(",").map((v) => v.trim());
    const [placa, documento, entrada, saida = "", valor = "0"] = partes;
    const cliente = this.#criarCliente(documento, clientes);

    if (!cliente || !placa || !entrada) {
      return null;
    }

    return Registro.restaurar(
      new Veiculo(placa),
      cliente,
      new Date(entrada),
      possuiSaida && saida ? new Date(saida) : null,
      Number(valor),
    );
  }

  static carregarHistorico(clientes) {
    if (!fs.existsSync("data/registros.csv")) return [];

    return fs
      .readFileSync("data/registros.csv", "utf-8")
      .split("\n")
      .slice(1)
      .map((linha) => this.#criarRegistroDaLinha(linha, clientes, true))
      .filter(Boolean);
  }

  static carregarAtivos(clientes) {
    if (!fs.existsSync("data/registros_ativos.csv")) return [];

    return fs
      .readFileSync("data/registros_ativos.csv", "utf-8")
      .split("\n")
      .slice(1)
      .map((linha) => this.#criarRegistroDaLinha(linha, clientes, false))
      .filter(Boolean);
  }

  static salvar(registros) {
    let conteudo = "placa,documento,entrada,saida,valor\n";

    registros.forEach((r) => {
      conteudo += `${r.veiculo.placa},${r.cliente.documento},${r.entrada.toISOString()},${r.saida?.toISOString() || ""},${r.valorTotal}\n`;
    });

    fs.writeFileSync("data/registros.csv", conteudo);
  }

  static salvarAtivos(registros) {
    let conteudo = "placa,documento,entrada\n";

    registros.forEach((r) => {
      conteudo += `${r.veiculo.placa},${r.cliente.documento},${r.entrada.toISOString()}\n`;
    });

    fs.writeFileSync("data/registros_ativos.csv", conteudo);
  }
}

module.exports = RegistroRepository;
