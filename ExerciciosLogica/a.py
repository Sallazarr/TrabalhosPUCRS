import os

palavra = "python".lower()
letrasCertas = []
letrasErradas = []
tentativasMax = 6
tentativa = 0


while tentativa < tentativasMax:
    if os.name == 'nt':  # Windows
        os.system('cls')

    progresso = ''
    
 
    for letra in palavra:
        if letra in letrasCertas:
            progresso += letra
        else:
            progresso += "_"
            
    if progresso == palavra:
        print("Você descobriu a palavra!!")
        print("Palavra: ", palavra)
        print("Letras erradas: ", letrasErradas)
        break            
            
    print("Progresso: ", progresso)
    print("Letras erradas: ", letrasErradas)
    print(f"Você tem {tentativasMax - tentativa} restantes")
    
    chute = input("Insira uma letra como chute: ").lower()
    if len(chute) > 1:
        print("Só é permitido chute de um caracter, tente novamente")
    else:
        if chute in palavra:
            if chute not in letrasCertas:
                print("Você acertou o chute!")
                letrasCertas.append(chute)
            else:
                print("Você já chutou essa letra, tente novamente.")
        else:
            if chute not in letrasErradas:
                print("Você errou o chute!")
                letrasErradas.append(chute)
                tentativa += 1
            else:
                print("Você já chutou essa letra, tente novamente.")
                

else:
    print("Limite de tentativas excedido!")
    print("Você perdeu!!")
    