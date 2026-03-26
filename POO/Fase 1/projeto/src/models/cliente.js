class Cliente {
    #nome;
    #documento;

        constructor(nome, documento){
            if (this.constructor === Cliente){
throw new Error("Classe Cliente não pode ser instanciada diretamente.")
            }
            this.#nome = nome
            this.#documento = documento
        }

        get nome() { return this.#nome }
        get documento() { return this.#documento }

        calcularTarifa(entrada, saida) {
            throw new Error("O método calcularTarifa deve ser implementado nas subclasses.")
        }
}

module.exports = Cliente