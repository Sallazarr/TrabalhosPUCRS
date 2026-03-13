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

        calcularTarifas() {
            throw new Error("O método calcularTarifas deve ser implementado nas subclasses.")
        }
}

module.exports = Cliente