const Estacionamento = require("./src/controller/Estacionamento");
const ClienteRepo = require("./src/repository/ClienteRepo");
const RegistroRepo = require("./src/repository/RegistroRepo");
const Interface = require("./src/ui/Interface");

console.log("Carregando dados...");

const clientes = ClienteRepo.carregar();
const sistema = new Estacionamento();
const historico = RegistroRepo.carregarHistorico(clientes);
const registrosAtivos = RegistroRepo.carregarAtivos(clientes);

sistema.carregarHistorico(historico);
sistema.carregarRegistrosAtivos(registrosAtivos);

const ui = new Interface(sistema, clientes);

ui.iniciar();

process.on("exit", () => {
  console.log("Salvando dados...");
  ClienteRepo.salvar(clientes);
  RegistroRepo.salvar(sistema.historico);
  RegistroRepo.salvarAtivos(sistema.registrosAtivos);
});
