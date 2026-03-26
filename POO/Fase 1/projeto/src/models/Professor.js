const Cliente = require('./Cliente')

class Professor extends Cliente {
    #matricula

    constructor(nome, documento, matricula) {
        super(nome, documento)
        this.#matricula = matricula
    }

    get matricula() { return this.#matricula }

    calcularTarifa(){
        return 0
    }
}

module.exports = Professor