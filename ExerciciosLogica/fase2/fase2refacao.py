def carregarArquivo(caminhoCSV='Anexo_Arquivo_Dados_Projeto_Logica_e_programacao_de_computadores.csv'):
    registros = []
    try:
        with open(caminhoCSV, 'r', encoding='utf-8') as arquivo:
            for linha in arquivo:
                parte = linha.strip().split(',')
                
                
                try:  
                    registro = {
                    'data': parte[0],
                    'precipitacao': float(parte[1]),
                    'temp_max': float(parte[2]),
                    'temp_min': float(parte[3]),
                    'umidade': float(parte[6]), 
                    'vento': float(parte[7])  
                }
                    registros.append(registro)
                
                except(ValueError, IndexError):
                    continue
 
    except FileNotFoundError:
        print(f"Erro: O arquivo '{caminhoCSV}' não foi encontrado.")
        return None
        
    return registros