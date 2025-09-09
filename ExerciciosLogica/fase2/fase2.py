# Importa a biblioteca para gerar gráficos
import matplotlib.pyplot as plt

# Função para carregar e tratar os dados do arquivo CSV.
def carregar_dados(caminho_arquivo='Anexo_Arquivo_Dados_Projeto_Logica_e_programacao_de_computadores.csv'):
    registros = []
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
            # Pula a primeira linha que contém o cabeçalho.
            next(arquivo)
            
            # Percorre cada linha do arquivo.
            for linha in arquivo:
                partes = linha.strip().split(',')
                
                # Pula a linha se ela não tiver o número esperado de colunas.
                if len(partes) < 8:
                    continue

                try:
                    # Trata o formato da data de DD/MM/AAAA para AAAA-MM-DD.
                    data_original = partes[0]
                    dia, mes, ano = data_original.split('/')
                    data_formatada = f"{ano}-{mes}-{dia}"

                    # Monta um dicionário com os dados da linha.
                    registro = {
                        'data': data_formatada,
                        'precipitacao': float(partes[1]),
                        'temp_max': float(partes[2]),
                        'temp_min': float(partes[3]),
                        'umidade': float(partes[6]), # Índice correto para umidade.
                        'vento': float(partes[7])    # Índice correto para vento.
                    }
                    registros.append(registro)
                except (ValueError, IndexError):
                    # Ignora a linha caso haja erro na conversão dos dados.
                    continue

    except FileNotFoundError:
        print(f"Erro: O arquivo '{caminho_arquivo}' não foi encontrado.")
        return None
        
    return registros

# Pede e valida uma entrada numérica do usuário.
def obter_input_numerico_validado(prompt, min_val, max_val):
    # Loop para garantir que a entrada seja válida.
    while True:
        try:
            valor_str = input(prompt)
            valor_int = int(valor_str)
            
            # Verifica se o valor está dentro do intervalo permitido.
            if min_val <= valor_int <= max_val:
                return valor_int
            else:
                print(f"Erro: O valor deve estar entre {min_val} e {max_val}. Tente novamente.")
        
        except ValueError:
            print("Erro: Entrada inválida. Por favor, insira um número inteiro.")

# Mostra os dados de um período escolhido pelo usuário.
def visualizar_dados_periodo(dados):
    if not dados:
        print("Não há dados para visualizar.")
        return

    # Valida se o período informado é lógico (data final > data inicial).
    while True:
        print("\nInforme o período que deseja visualizar.")
        mes_ini = obter_input_numerico_validado("Informe o mês inicial (1-12): ", 1, 12)
        ano_ini = obter_input_numerico_validado("Informe o ano inicial (1961-2016): ", 1961, 2016)
        mes_fim = obter_input_numerico_validado("Informe o mês final (1-12): ", 1, 12)
        ano_fim = obter_input_numerico_validado("Informe o ano final (1961-2016): ", 1961, 2016)

        if ano_fim < ano_ini or (ano_fim == ano_ini and mes_fim < mes_ini):
            print("\nErro: O período final não pode ser anterior ao período inicial. Tente novamente.")
            continue
        else:
            break

    print("\nEscolha o tipo de dado para visualizar:")
    print("1) Todos os dados")
    print("2) Apenas precipitação")
    print("3) Apenas temperaturas (máx e mín)")
    print("4) Apenas umidade e vento")
    
    # Valida a opção de visualização (1 a 4).
    while True:
        escolha = input("Opção: ")
        if escolha in ['1', '2', '3', '4']:
            break
        else:
            print("Opção inválida. Escolha entre 1, 2, 3 ou 4.")
    
    data_inicio_str = f"{ano_ini:04d}-{mes_ini:02d}"
    data_fim_str = f"{ano_fim:04d}-{mes_fim:02d}"

    # Define o cabeçalho da tabela de acordo com a escolha.
    header = ""
    if escolha == '1':
        header = f"{'Data':<12} | {'Precipit.(mm)':>14} | {'Temp. Max (°C)':>15} | {'Temp. Min (°C)':>15} | {'Umidade (%)':>13} | {'Vento (m/s)':>13}"
    elif escolha == '2':
        header = f"{'Data':<12} | {'Precipit.(mm)':>14}"
    elif escolha == '3':
        header = f"{'Data':<12} | {'Temp. Max (°C)':>15} | {'Temp. Min (°C)':>15}"
    elif escolha == '4':
        header = f"{'Data':<12} | {'Umidade (%)':>13} | {'Vento (m/s)':>13}"
    
    print("\n" + header)
    print("-" * len(header))

    # Percorre todos os registros e imprime os que estão no período selecionado.
    resultados_encontrados = False
    for registro in dados:
        if data_inicio_str <= registro['data'][:7] <= data_fim_str:
            resultados_encontrados = True
            
            data = registro['data']
            prec = f"{registro['precipitacao']:.1f}"
            tmax = f"{registro['temp_max']:.1f}"
            tmin = f"{registro['temp_min']:.1f}"
            umid = f"{registro['umidade']:.1f}"
            vent = f"{registro['vento']:.1f}"

            if escolha == '1':
                print(f"{data:<12} | {prec:>14} | {tmax:>15} | {tmin:>15} | {umid:>13} | {vent:>13}")
            elif escolha == '2':
                print(f"{data:<12} | {prec:>14}")
            elif escolha == '3':
                print(f"{data:<12} | {tmax:>15} | {tmin:>15}")
            elif escolha == '4':
                print(f"{data:<12} | {umid:>13} | {vent:>13}")
    
    if not resultados_encontrados:
        print("-" * len(header))
        print("Nenhum registro encontrado para o período informado.")

# Encontra e exibe o mês com maior precipitação em todo o período.
def encontrar_mes_chuvoso(dados):
    if not dados:
        print("Não há dados para analisar.")
        return
        
    # Dicionário para guardar a soma da chuva de cada mês.
    precipitacao_mensal = {}

    # Soma a precipitação por mês/ano.
    for registro in dados:
        mes_ano = registro['data'][:7]
        
        if mes_ano in precipitacao_mensal:
            precipitacao_mensal[mes_ano] += registro['precipitacao']
        else:
            precipitacao_mensal[mes_ano] = registro['precipitacao']
    
    if not precipitacao_mensal:
        print("Não foi possível calcular a precipitação mensal.")
        return

    # Encontra o mês com o maior valor de chuva.
    mes_mais_chuvoso = max(precipitacao_mensal, key=precipitacao_mensal.get)
    maior_precipitacao = precipitacao_mensal[mes_mais_chuvoso]

    ano, mes = mes_mais_chuvoso.split('-')
    
    print("\n--- Mês Mais Chuvoso ---")
    print(f"O mês com maior precipitação acumulada foi {mes}/{ano}.")
    print(f"Total de precipitação: {maior_precipitacao:.2f} mm")

# Calcula a média da temperatura mínima para um mês específico entre 2006 e 2016.
def calcular_media_temp_minima_mes(dados):
    if not dados:
        print("Não há dados para analisar.")
        return None

    mes_usuario = obter_input_numerico_validado("Informe o mês para análise (1-12): ", 1, 12)
    mes_str = f"{mes_usuario:02d}"
    
    temps_por_ano = {}
    # Filtra os dados pelo período (2006-2016) e pelo mês escolhido.
    for registro in dados:
        ano = int(registro['data'][:4])
        mes = registro['data'][5:7]

        if 2006 <= ano <= 2016 and mes == mes_str:
            if ano not in temps_por_ano:
                temps_por_ano[ano] = []
            temps_por_ano[ano].append(registro['temp_min'])

    if not temps_por_ano:
        print(f"Nenhum dado encontrado para o mês {mes_usuario} entre 2006 e 2016.")
        return None

    # Calcula a média para cada ano e armazena no dicionário.
    medias_anuais = {}
    print(f"\n--- Média da Temperatura Mínima para o Mês {mes_usuario} (2006-2016) ---")
    for ano, temperaturas in sorted(temps_por_ano.items()):
        media = sum(temperaturas) / len(temperaturas)
        chave = f"{mes_usuario}/{ano}"
        medias_anuais[chave] = media
        print(f"{chave}: {media:.2f}°C")
        
    return medias_anuais

# Gera o gráfico de barras com as médias de temperatura.
def gerar_grafico_medias(dados_medias):
    if not dados_medias:
        print("Não há dados para gerar o gráfico.")
        return

    mes_ano = list(dados_medias.keys())
    medias = list(dados_medias.values())

    plt.figure(figsize=(12, 6))
    plt.bar(mes_ano, medias, color='skyblue', edgecolor='black')
    
    # Adiciona rótulos, título e formatações no gráfico.
    plt.xlabel("Mês/Ano")
    plt.ylabel("Temperatura Mínima Média (°C)")
    plt.title(f"Média da Temperatura Mínima para o Mês {mes_ano[0].split('/')[0]} (2006-2016)")
    plt.xticks(rotation=45, ha="right")
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    
    # Exibe o gráfico.
    print("\nExibindo o gráfico de barras. Feche a janela do gráfico para continuar.")
    plt.show()

# Calcula a média geral das temperaturas a partir do dicionário de médias.
def calcular_media_geral(dados_medias):
    if not dados_medias:
        return

    media_geral = sum(dados_medias.values()) / len(dados_medias.values())
    mes = list(dados_medias.keys())[0].split('/')[0]
    
    print("\n--- Média Geral do Período ---")
    print(f"A média geral da temperatura mínima para o mês {mes} entre 2006 e 2016 foi de {media_geral:.2f}°C.")

# Função principal que organiza a execução do programa e mostra o menu.
def main():
    print("Carregando dados meteorológicos. Aguarde...")
    dados = carregar_dados()
    if not dados:
        print("Não foi possível carregar os dados. Encerrando o programa.")
        return
    print(f"{len(dados)} registros carregados com sucesso!")

    # Loop principal do menu.
    while True:
        print("\n===== ANÁLISE DE DADOS METEOROLÓGICOS DE PORTO ALEGRE =====")
        print("1. Visualizar dados de um período")
        print("2. Ver mês mais chuvoso de toda a série histórica")
        print("3. Analisar temperatura mínima de um mês (2006-2016)")
        print("0. Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            visualizar_dados_periodo(dados)
        elif opcao == '2':
            encontrar_mes_chuvoso(dados)
        elif opcao == '3':
            medias_do_mes = calcular_media_temp_minima_mes(dados)
            if medias_do_mes:
                calcular_media_geral(medias_do_mes)
                gerar_grafico_medias(medias_do_mes)
        elif opcao == '0':
            print("Encerrando o programa. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Executa a função principal quando o script é iniciado.
if __name__ == "__main__":
    main()