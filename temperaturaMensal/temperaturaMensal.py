meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"];

temperatura = [];


while True:

    print("==========Menu==========")
    print("1 - Inserir as temperaturas de todos os meses:\n")
    print("2 - Editar a temperatura de um mês especifico:\n")
    print("3 - Exibir os meses e suas temperaturas\n")
    print("4 - calcular e exibir as informações:\n")
    print("0 - Sair:\n")


    try:
        inputOpcao = int(input("Digite o número correspondente da opção desejada: "))
        opcao = inputOpcao
        
    except ValueError:
        print("Valor inválido, utilize apenas números inteiros")
        continue
 
    
    match opcao:
      case 1:
        temperatura.clear()
        for i in range(12):
            while True:
                try:
                    inputTemperatura = float(input(f"\nInsira a temperatura do mês de {meses[i]}: "))
                    if inputTemperatura < -60 or inputTemperatura > 50:
                        print("Temperatura fora do valor permitido (-60°C a 50°C)") 
                        continue
                    temperatura.append(inputTemperatura)
                    break
                except ValueError:
                    print("Valor inválido! (Em caso de temperatura com casa decimal, utilize . ao invés de ,).")
                   
      case 2:
          if not temperatura or len(temperatura) < 12:
            print("Parece que você não inseriu as temperaturas ainda, utilize a opção 1 primeiro.\n")
            continue
          while True:
           try:
              mesSelecionado = int(input("Digite o número do mês que deseja alterar: "))
              if mesSelecionado < 1 or mesSelecionado > 12:
                  print("Insira um mês valido")
                  continue
              print(
                  f"Mês selecionado: {meses[mesSelecionado - 1]}\n"
                  f"Temperatura do mês selecionado: {temperatura[mesSelecionado - 1]}\n")
              while True:
               try:   
                   novaTemperatura = float(input(f"Insira a nova temperatura do mês de {meses[mesSelecionado - 1]}: "))
                   if novaTemperatura < -60 or novaTemperatura > 50:
                      print("Temperatura fora do valor permitido (-60°C a 50°C)") 
                      continue
                   temperatura[mesSelecionado - 1] = novaTemperatura
                   print("Temperatura atualizada")
                   break
               except ValueError:
                     print ("Valor inválido! (Em caso de temperatura com casa decimal, utilize . ao invés de ,).")
                     continue
              break
           except ValueError:
                print("Valor Inválido!")
      case 3:
          try:
              for i in range(12):
                print(
                  f"Mês: {meses[i]} || Temperatura: {temperatura[i]}"
                )
          except Exception as e:
            print("Erro ao exibir os dados:", e)
      case 4:
          media = sum(temperatura) / 12
          print(f"Média das temperaturas máximas informadas: {media}")
          
          mesesEscaldantes = 0
          for temp in temperatura:
              if temp > 33:
                  mesesEscaldantes += 1
                  
          print(f"Quantidade de meses escaldantes: {mesesEscaldantes}")        
            
          indiceEscaldante = temperatura.index(max(temperatura))
          indiceMenosQuente = temperatura.index(min(temperatura))        
          mesMaisQuente = meses[indiceEscaldante]
          mesMenosQuente = meses[indiceMenosQuente]
          
          print(f"Mês mais escaldante do ano: {mesMaisQuente}")
          print(f"Mês menos quente do ano: {mesMenosQuente}")
      case 0:
          print("Finalizando programa...")
          break  