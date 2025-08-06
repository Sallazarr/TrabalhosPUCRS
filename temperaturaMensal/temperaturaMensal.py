
# Lista dos meses e lista das temperaturas #
meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"];
temperatura = [];

#While True para manter um loop de menu#
while True:

    print("\n====== MENU ======")
    print("1 - Inserir temperaturas")
    print("2 - Editar temperatura de um mês")
    print("3 - Exibir dados")
    print("4 - Calcular informações")
    print("0 - Sair")
    print("==================")


#Pega a entrada do usuário e envia para o case correspondente#
    try:
        inputOpcao = int(input("Digite o número correspondente da opção desejada: "))
        opcao = inputOpcao
        
    except ValueError:
        print("Valor inválido, utilize apenas números inteiros")
        continue
 
    #Case 1: faz um loop de 12x, permitindo o usuário inserir 12 temperaturas diferentes, uma para cada mês#
    match opcao:
      case 1:
          if temperatura:
              confirmar = input("Temperaturas já foram inseridas. Deseja Sobrescrever? (s/n)").lower()
              if confirmar != "s":
                  continue
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
                    
      
      #Case 2: Valida se o usuário já inseriu as temperaturas, se sim, permiti o usuário escolher um mês para alterar sua temperatura             
      case 2:
          if not temperatura:
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
                
      #Case 3: Valida se o usuário já inseriu as temperaturas, se sim, exibe todos os meses e suas temperaturas correspondentes#          
      case 3:
          if not temperatura:
           print("Parece que você não inseriu as temperaturas ainda, utilize a opção 1 primeiro.\n")
           continue    
          try:
              for i in range(12):
                print(
                  f"Mês: {meses[i]} || Temperatura: {temperatura[i]}"
                )
          except Exception as e:
            print("Erro ao exibir os dados:", e)
      
      #Case 4: Valida se o usuário já inseriu as temperaturas, se sim, calcula e exibe a média das temperaturas, meses escaldantes, mês mais quente e mês menos quente      
      case 4:
          if not temperatura:
           print("Parece que você não inseriu as temperaturas ainda, utilize a opção 1 primeiro.\n")
           continue    
          media = sum(temperatura) / 12
          print(f"\nMédia atual das temperaturas: {media:.2f}°C")
          
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
      
      #Finaliza o programa quebrando o loop#    
      case 0:
          print("Finalizando programa...")
          break  