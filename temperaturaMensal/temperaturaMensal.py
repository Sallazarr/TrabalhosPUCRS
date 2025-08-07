# Lista com os nomes dos meses e uma lista vazia para armazenar as temperaturas
meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
         "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
temperatura = []


# Loop principal,exibe o menu e trata as escolhas do usuário
while True:
    print("\n====== MENU ======")
    print("1 - Inserir temperaturas")
    print("2 - Editar temperatura de um mês")
    print("3 - Exibir dados")
    print("4 - Calcular informações")
    print("0 - Sair")
    print("==================")

    # Valida a entrada da opção do usuário
    try:
        opcao = int(input("Digite o número correspondente da opção desejada: "))
    except ValueError:
        print("Valor inválido, utilize apenas números inteiros.")
        continue

    # Verifica qual opção o usuário escolheu
    match opcao:

        # Opção 1: Inserção das 12 temperaturas
        case 1:
             # Caso já exista alguma temperatura cadastrada, pede confirmação para sobrescrever
            if temperatura:
                confirmar = input("Temperaturas já foram inseridas. Deseja sobrescrever? (s/n): ").strip().lower()
                if confirmar != "s":
                    continue
            temperatura.clear()

            for i in range(12):
                while True:
                    try:
                        inputTemperatura = float(input(f"\nInsira a temperatura do mês de {meses[i]}: "))
                        if inputTemperatura < -60 or inputTemperatura > 50:
                            print("Temperatura fora do intervalo permitido (-60°C a 50°C).")
                            continue
                        temperatura.append(inputTemperatura)
                        break
                    except ValueError:
                        print("Valor inválido! Utilize ponto (.) para casas decimais.")

        # Opção 2: Alterar a temperatura de um mês específico
        case 2:
            # Verifica se as temperaturas já foram inseridas antes de permitir edição
            if not temperatura:
                print("Você ainda não inseriu as temperaturas. Utilize a opção 1 primeiro.\n")
                continue

            while True:
                try:
                    mesSelecionado = int(input("Digite o número do mês que deseja alterar (1 a 12): "))
                    if mesSelecionado < 1 or mesSelecionado > 12:
                        print("Número inválido. Escolha um valor entre 1 e 12.")
                        continue

                    print(
                        f"Mês selecionado: {meses[mesSelecionado - 1]}\n"
                        f"Temperatura atual: {temperatura[mesSelecionado - 1]}°C\n"
                    )

                    while True:
                        try:
                            novaTemperatura = float(input(f"Insira a nova temperatura para {meses[mesSelecionado - 1]}: "))
                            if novaTemperatura < -60 or novaTemperatura > 50:
                                print("Temperatura fora do intervalo permitido (-60°C a 50°C).")
                                continue
                            temperatura[mesSelecionado - 1] = novaTemperatura
                            print("Temperatura atualizada com sucesso.")
                            break
                        except ValueError:
                            print("Valor inválido! Utilize ponto (.) para casas decimais.")
                    break
                except ValueError:
                    print("Entrada inválida. Digite apenas números inteiros.")

        # Opção 3: Exibição das temperaturas cadastradas
        case 3:
            if not temperatura:
                print("Você ainda não inseriu as temperaturas. Utilize a opção 1 primeiro.\n")
                continue

            try:
                print("\nTemperaturas por mês:")
                for i in range(12):
                    print(f"Mês: {meses[i]} || Temperatura: {temperatura[i]}°C")
            except Exception as e:
                print("Erro ao exibir os dados:", e)

       # Opção 4: Calcular e mostrar média, meses escaldantes e meses mais quentes e menos quentes
        case 4:
            if not temperatura:
                print("Você ainda não inseriu as temperaturas. Utilize a opção 1 primeiro.\n")
                continue

            # Cálculo da média das temperaturas
            media = sum(temperatura) / 12
            print(f"\nMédia anual das temperaturas: {media:.2f}°C")

            # Contagem de meses com temperaturas acima de 33°C
            mesesEscaldantes = sum(1 for temp in temperatura if temp > 33)
            print(f"Quantidade de meses escaldantes: {mesesEscaldantes}")

            # Identificação da maior e menor temperatura
            temperaturaMax = max(temperatura)
            temperaturaMin = min(temperatura)

            # Identificação dos nomes dos meses de maior e menor temperatura
            mesesMaisQuentes = [meses[i] for i, temp in enumerate(temperatura) if temp == temperaturaMax]
            mesesMenosQuentes = [meses[i] for i, temp in enumerate(temperatura) if temp == temperaturaMin]

            print(f"Mês(es) mais quente(s) com {temperaturaMax}°C: {', '.join(mesesMaisQuentes)}")
            print(f"Mês(es) menos quente(s) com {temperaturaMin}°C: {', '.join(mesesMenosQuentes)}")

        # Opção 0: Finalização do programa
        case 0:
            print("Finalizando o programa...")
            break

        # Caso inválido: opção não reconhecida
        case _:
            print("Opção inválida. Escolha uma opção entre 0 e 4.")
