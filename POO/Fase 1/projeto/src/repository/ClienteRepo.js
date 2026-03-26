const fs = require("fs");
const Estudante = require("../models/Estudante");
const Professor = require("../models/Professor");
const Empresa = require("../models/Empresa");

class ClienteRepository {
  static carregar() {
    if (!fs.existsSync("data/clientes.csv")) return [];

    const linhas = fs
      .readFileSync("data/clientes.csv", "utf-8")
      .split("\n")
      .slice(1);

    return linhas
      .map((l) => {
        if (!l) return null;

        const [tipo, nome, documento, extra, saldo] = l
          .split(",")
          .map((v) => v.trim());

        switch (tipo) {
          case "Estudante":
            return new Estudante(nome, documento, extra, Number(saldo));
          case "Professor":
            return new Professor(nome, documento, extra);
          case "Empresa":
            return new Empresa(nome, documento, extra);
          default:
            return null;
        }
      })
      .filter(Boolean);
  }

  static salvar(clientes) {
    let conteudo = "tipo,nome,documento,extra,saldo\n";

    clientes.forEach((c) => {
      let extra = "";
      let saldo = "";

      if (c.constructor.name === "Estudante") {
        extra = c.matricula;
        saldo = c.saldo;
      } else if (c.constructor.name === "Professor") {
        extra = c.matricula;
      } else if (c.constructor.name === "Empresa") {
        extra = c.cnpj;
      }

      conteudo += `${c.constructor.name},${c.nome},${c.documento},${extra},${saldo}\n`;
    });

    fs.writeFileSync("data/clientes.csv", conteudo);
  }
}

module.exports = ClienteRepository;
