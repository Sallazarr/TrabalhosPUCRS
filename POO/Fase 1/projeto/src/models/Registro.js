class Registro {
    #veiculo
    #cliente
    #entrada
    #saida
    #valorTotal

    constructor(veiculo, cliente) {
        this.#veiculo = veiculo
        this.#cliente = cliente
        this.#entrada = new Date()
        this.#saida = null
        this.#valorTotal = 0
    }

    static restaurar(veiculo, cliente, entrada, saida = null, valorTotal = 0) {
        const registro = new Registro(veiculo, cliente)
        registro.#entrada = entrada
        registro.#saida = saida
        registro.#valorTotal = valorTotal
        return registro
    }

    get veiculo() { return this.#veiculo }
    get cliente() { return this.#cliente }
    get entrada() { return this.#entrada }
    get saida() { return this.#saida }
    get valorTotal() { return this.#valorTotal }

    finalizar(valor, dataSaida) {
        this.#saida = dataSaida
        this.#valorTotal = valor
    }

    calcularTempoEmMinutos() {
        const fim = this.#saida || new Date()
        const diffMilisegundos = fim - this.#entrada
        return Math.ceil(diffMilisegundos / (1000 * 60))
    }
}

module.exports = Registro
