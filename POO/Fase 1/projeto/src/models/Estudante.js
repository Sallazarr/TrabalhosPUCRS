const Cliente = require('./Cliente')

class Estudante extends Cliente {
    #matricula
    #saldo

    constructor(nome, documento, matricula, saldoInicial = 0){
        super(nome, documento)
        this.#matricula = matricula
        this.#saldo = saldoInicial
    }

    get matricula() { return this.#matricula }
    get saldo() { return this.#saldo }

    debitarSaldo(valor) {
        this.#saldo -= valor
    }

    calcularTarifa(entrada, saida){
        const valorIngresso = 5.00
        const virouODia =
            entrada.getFullYear() !== saida.getFullYear() ||
            entrada.getMonth() !== saida.getMonth() ||
            entrada.getDate() !== saida.getDate()

        if (virouODia){
            return valorIngresso * 2
        }

        return valorIngresso
    }
}

module.exports = Estudante;
