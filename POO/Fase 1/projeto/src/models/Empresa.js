const Cliente = require('./Cliente')

class Empresa extends Cliente{
    #cnpj

    constructor(nome, documento, cnpj){
        super(nome,documento)
        this.#cnpj = cnpj
    }

    static #inicioDoDia(data){
        return new Date(data.getFullYear(), data.getMonth(), data.getDate())
    }

    get cnpj() { return this.#cnpj }

    calcularTarifa(entrada, saida){
        const VALOR_DIARIA = 60.00
        const diffDias = Math.floor(
            (Empresa.#inicioDoDia(saida) - Empresa.#inicioDoDia(entrada)) / (1000 * 60 * 60 * 24)
        )
        const dias = Math.max(1, diffDias + 1)

        if (diffDias > 0){
            return (dias * VALOR_DIARIA) + 50.00
        }

        return VALOR_DIARIA
    }
}

module.exports = Empresa
