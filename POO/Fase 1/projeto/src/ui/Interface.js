const readline = require("readline");
const Veiculo = require("../models/Veiculo");
const Relatorios = require("../reports/Relatorios");
const Estudante = require("../models/Estudante");
const Professor = require("../models/Professor");
const Empresa = require("../models/Empresa");
const ClienteAvulso = require("../models/ClienteAvulso");
const ClienteRepo = require("../repository/ClienteRepo");
const RegistroRepo = require("../repository/RegistroRepo");

class Interface {
  constructor(sistema, clientes) {
    this.sistema = sistema;
    this.clientes = clientes;

    this.rl = readline.createInterface({
      input: process.stdin,
      output: process.stdout,
    });
  }

  iniciar() {
    console.log("Sistema iniciado");
    this.menu();
  }

  menu() {
    console.log("\n1 - Entrada");
    console.log("2 - Saida");
    console.log("3 - Relatorios");
    console.log("4 - Cadastrar cliente");
    console.log("0 - Sair");

    this.rl.question("Escolha: ", (op) => {
      switch (op) {
        case "1":
          return this.entrada();
        case "2":
          return this.saida();
        case "3":
          return this.menuRelatorios();
        case "4":
          return this.cadastrarCliente();
        case "0":
          return this.rl.close();
        default:
          return this.menu();
      }
    });
  }

  #salvarDados() {
    ClienteRepo.salvar(this.clientes);
    RegistroRepo.salvar(this.sistema.historico);
    RegistroRepo.salvarAtivos(this.sistema.registrosAtivos);
  }

  #perguntar(texto) {
    return new Promise((resolve) => {
      this.rl.question(texto, resolve);
    });
  }

  #lerData(dataTexto, finalDoDia = false) {
    const [ano, mes, dia] = dataTexto.split("-").map(Number);

    if (!ano || !mes || !dia) {
      return null;
    }

    if (finalDoDia) {
      return new Date(ano, mes - 1, dia, 23, 59, 59, 999);
    }

    return new Date(ano, mes - 1, dia, 0, 0, 0, 0);
  }

  #mostrarRegistros(registros) {
    if (!registros.length) {
      console.log("Nenhum registro encontrado.");
      return;
    }

    registros.forEach((registro) => {
      console.log(
        `${registro.cliente.nome} | ${registro.cliente.documento} | ${registro.veiculo.placa} | Entrada: ${registro.entrada.toLocaleString()} | Saida: ${registro.saida ? registro.saida.toLocaleString() : "-"} | Valor: R$ ${registro.valorTotal.toFixed(2)}`,
      );
    });
  }

  cadastrarCliente() {
    console.log("\nTipos de cliente:");
    console.log("1 - Estudante");
    console.log("2 - Professor");
    console.log("3 - Empresa");

    this.rl.question("Escolha o tipo: ", (tipo) => {
      this.rl.question("Nome: ", (nome) => {
        this.rl.question("Documento: ", (doc) => {
          if (this.clientes.some((c) => c.documento === doc)) {
            console.log("Cliente ja existe");
            return this.menu();
          }
          let cliente;

          switch (tipo) {
            case "1":
              this.rl.question("Matricula: ", (mat) => {
                this.rl.question("Saldo inicial: ", (saldo) => {
                  cliente = new Estudante(nome, doc, mat, Number(saldo));
                  this.clientes.push(cliente);
                  ClienteRepo.salvar(this.clientes);
                  console.log("Estudante cadastrado!");
                  this.menu();
                });
              });
              break;

            case "2":
              this.rl.question("Matricula: ", (mat) => {
                cliente = new Professor(nome, doc, mat);
                this.clientes.push(cliente);
                ClienteRepo.salvar(this.clientes);
                console.log("Professor cadastrado!");
                this.menu();
              });
              break;

            case "3":
              this.rl.question("CNPJ: ", (cnpj) => {
                cliente = new Empresa(nome, doc, cnpj);
                this.clientes.push(cliente);
                ClienteRepo.salvar(this.clientes);
                console.log("Empresa cadastrada!");
                this.menu();
              });
              break;

            default:
              console.log("Tipo invalido");
              this.menu();
          }
        });
      });
    });
  }

  entrada() {
    this.rl.question("Documento do cliente (ou AVULSO): ", (doc) => {
      let cliente;

      if (doc.toUpperCase() === "AVULSO") {
        cliente = new ClienteAvulso("Visitante", "000");
      } else {
        cliente = this.clientes.find((c) => c.documento === doc);

        if (!cliente) {
          console.log("Cliente nao encontrado");
          return this.menu();
        }
      }

      this.rl.question("Placa: ", (placa) => {
        const entradaRegistrada = this.sistema.registrarEntrada(new Veiculo(placa), cliente);

        if (entradaRegistrada) {
          this.#salvarDados();
        }

        this.menu();
      });
    });
  }

  saida() {
    this.rl.question("Placa: ", (placa) => {
      const saidaRegistrada = this.sistema.registrarSaida(placa);

      if (saidaRegistrada) {
        this.#salvarDados();
      }

      this.menu();
    });
  }

  menuRelatorios() {
    console.log("\nRelatorios:");
    console.log("1 - Total arrecadado por periodo");
    console.log("2 - Total arrecadado por categoria em um periodo");
    console.log("3 - Situacao de cliente cadastrado");
    console.log("4 - Registros de cliente cadastrado por periodo");
    console.log("5 - Registros de cliente nao cadastrado por periodo");
    console.log("6 - Clientes impedidos de entrar");
    console.log("7 - Top 10 clientes mais frequentes do ano");
    console.log("0 - Voltar");

    this.rl.question("Escolha: ", async (op) => {
      switch (op) {
        case "1":
          await this.relatorioTotalPorPeriodo();
          return this.menu();
        case "2":
          await this.relatorioCategoriaPorPeriodo();
          return this.menu();
        case "3":
          await this.relatorioSituacaoCliente();
          return this.menu();
        case "4":
          await this.relatorioClientePorPeriodo();
          return this.menu();
        case "5":
          await this.relatorioAvulsosPorPeriodo();
          return this.menu();
        case "6":
          this.relatorioBloqueados();
          return this.menu();
        case "7":
          await this.relatorioTop10Ano();
          return this.menu();
        case "0":
          return this.menu();
        default:
          return this.menuRelatorios();
      }
    });
  }

  async relatorioTotalPorPeriodo() {
    const inicioTexto = await this.#perguntar("Data inicial (AAAA-MM-DD): ");
    const fimTexto = await this.#perguntar("Data final (AAAA-MM-DD): ");
    const inicio = this.#lerData(inicioTexto);
    const fim = this.#lerData(fimTexto, true);

    if (!inicio || !fim) {
      console.log("Periodo invalido.");
      return;
    }

    const total = Relatorios.totalArrecadadoPorPeriodo(
      this.sistema.historico,
      inicio,
      fim,
    );

    console.log(`Total arrecadado no periodo: R$ ${total.toFixed(2)}`);
  }

  async relatorioCategoriaPorPeriodo() {
    const inicioTexto = await this.#perguntar("Data inicial (AAAA-MM-DD): ");
    const fimTexto = await this.#perguntar("Data final (AAAA-MM-DD): ");
    const inicio = this.#lerData(inicioTexto);
    const fim = this.#lerData(fimTexto, true);

    if (!inicio || !fim) {
      console.log("Periodo invalido.");
      return;
    }

    console.log(
      Relatorios.porCategoriaNoPeriodo(this.sistema.historico, inicio, fim),
    );
  }

  async relatorioSituacaoCliente() {
    const documento = await this.#perguntar("Documento do cliente: ");
    const cliente = this.clientes.find((c) => c.documento === documento);

    if (!cliente) {
      console.log("Cliente nao encontrado.");
      return;
    }

    console.log(
      Relatorios.situacaoCliente(
        cliente,
        this.sistema.registrosAtivos,
        this.sistema.bloqueados,
        this.sistema.historico,
      ),
    );
  }

  async relatorioClientePorPeriodo() {
    const documento = await this.#perguntar("Documento do cliente: ");
    const inicioTexto = await this.#perguntar("Data inicial (AAAA-MM-DD): ");
    const fimTexto = await this.#perguntar("Data final (AAAA-MM-DD): ");
    const inicio = this.#lerData(inicioTexto);
    const fim = this.#lerData(fimTexto, true);

    if (!inicio || !fim) {
      console.log("Periodo invalido.");
      return;
    }

    this.#mostrarRegistros(
      Relatorios.clientePorPeriodo(this.sistema.historico, documento, inicio, fim),
    );
  }

  async relatorioAvulsosPorPeriodo() {
    const inicioTexto = await this.#perguntar("Data inicial (AAAA-MM-DD): ");
    const fimTexto = await this.#perguntar("Data final (AAAA-MM-DD): ");
    const inicio = this.#lerData(inicioTexto);
    const fim = this.#lerData(fimTexto, true);

    if (!inicio || !fim) {
      console.log("Periodo invalido.");
      return;
    }

    this.#mostrarRegistros(
      Relatorios.avulsosPorPeriodo(this.sistema.historico, inicio, fim),
    );
  }

  relatorioBloqueados() {
    console.log(
      "Clientes bloqueados:",
      Relatorios.clientesBloqueados(this.sistema.bloqueados),
    );
  }

  async relatorioTop10Ano() {
    const anoTexto = await this.#perguntar("Ano (AAAA): ");
    const ano = Number(anoTexto);

    if (!ano) {
      console.log("Ano invalido.");
      return;
    }

    console.log(Relatorios.top10DoAno(this.sistema.historico, ano));
  }
}

module.exports = Interface;
