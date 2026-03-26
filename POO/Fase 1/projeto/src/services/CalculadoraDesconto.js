class CalculadoraDesconto {
  // Regra: ClienteFrequente - 20% de desconto
  static aplicarDescontoFrequente(valor) {
    const identificador = "ClienteFrequente" 
    const desconto = valor * 0.20
    return {
      valorComDesconto: valor - desconto,
      valorDesconto: desconto,
      id: identificador
    }
  }

  // Retorno padrão caso não aplique desconto
  static obterDescontoPadrao(valor) {
    return { valorComDesconto: valor, valorDesconto: 0, id: "nenhum" }
  }
}

module.exports = CalculadoraDesconto