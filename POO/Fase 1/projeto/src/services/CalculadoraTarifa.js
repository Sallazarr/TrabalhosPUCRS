class CalculadoraTarifa {
  static VALOR_HORA = 10.00
  static VALOR_DIARIA = 40.00
  static LIMITE_HORAS_DIARIA = 6

  static #inicioDoDia(data) {
    return new Date(data.getFullYear(), data.getMonth(), data.getDate())
  }

  static calcularAvulso(entrada, saida) {
    const diasDiferenca = Math.floor(
      (this.#inicioDoDia(saida) - this.#inicioDoDia(entrada)) / (1000 * 60 * 60 * 24)
    )

    if (diasDiferenca > 0) {
      return (diasDiferenca + 1) * this.VALOR_DIARIA
    }

    const diffMs = saida - entrada
    const horas = Math.ceil(diffMs / (1000 * 60 * 60))

    if (horas > this.LIMITE_HORAS_DIARIA) {
      return this.VALOR_DIARIA
    }

    return horas * this.VALOR_HORA
  }
}

module.exports = CalculadoraTarifa
