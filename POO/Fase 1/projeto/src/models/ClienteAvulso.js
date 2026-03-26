const CalculadoraTarifa = require('../services/CalculadoraTarifa')
const Cliente = require('./Cliente')

class ClienteAvulso extends Cliente {
    constructor(nome, documento) {
        super(nome, documento)
    }

    // A tarifa do avulso será calculada com baase em tempo
    calcularTarifa(entrada, saida){
        return CalculadoraTarifa.calcularAvulso(entrada, saida)
    }
}

module.exports = ClienteAvulso