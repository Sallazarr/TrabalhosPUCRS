class Veiculo {
    #placa
    #modelo

    constructor(placa, modelo){
        this.#placa = placa
        this.#modelo = modelo
    }

    get placa() { return this.#placa }
    get modelo() { return this.#modelo }
}

module.exports = Veiculo