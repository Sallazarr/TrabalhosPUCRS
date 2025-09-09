import random

board = ["","","","","","","","",""]
vitorias = [
    (1, 2, 3), (4, 5, 6), (7, 8, 9),  # Horizontais
    (1, 4, 7), (2, 5, 8), (3, 6, 9),  # Verticais
    (1, 5, 9), (3, 5, 7)             # Diagonais
]
jogadaUsuario = []
jogadaMaquina = []

# Suponha que 'jogadas_do_jogador' seja a lista de jogadas do jogador atual (ex: [1, 5, 9])
# E 'vitorias' é a lista de combinações vencedoras que mostramos acima.

def verificar_vitoria(jogadaUsuario):
    # Percorre cada combinação vencedora
    for combinacao in vitorias:
        # 'all()' retorna True se todos os itens de um iterável forem verdadeiros
        # Aqui, ele checa se todos os números na 'combinacao' estão dentro da lista 'jogadas_do_jogador'
        if all(posicao in jogadaUsuario for posicao in combinacao):
            return True  # Se encontrar uma combinação, a vitória é confirmada

    return False  # Se o loop terminar e nenhuma combinação for encontrada, ninguém venceu

def verificar_empate():
    return len(jogadaUsuario) + len(jogadaMaquina) == 9

def imprimir_board(board):
    print(" " + board[0] + " | " + board[1] + " | " + board[2] + " ")
    print("---+---+---")
    print(" " + board[3] + " | " + board[4] + " | " + board[5] + " ")
    print("---+---+---")
    print(" " + board[6] + " | " + board[7] + " | " + board[8] + " ")
    

imprimir_board(board)
while True:

    try:
        inputJogador = int(input("Insira a posição que deseja jogar (1-9): "))
        
        # AQUI está a lógica unificada:
        # Checa se o número é válido (entre 1 e 9) E se o lugar no board está vazio
        if 1 <= inputJogador <= 9 and board[inputJogador - 1] == "":
            board[inputJogador - 1] = "X"
            jogadaUsuario.append(inputJogador)
        else:
            print("Posição inválida ou já ocupada. Tente novamente.")
            continue # Volta para o início do loop e pede uma nova jogada
    
    except ValueError:
        print("Entrada inválida. Por favor, digite um número de 1 a 9.")
        continue # Volta para o início do loop
          
    vitoriaUsuario = verificar_vitoria(jogadaUsuario)
    
    if vitoriaUsuario == True:
        print("Você ganhou!!!")
        print()
        imprimir_board(board)
        print()
        break
    print()
    imprimir_board(board)
    print()
    while True:
     inputMaquina = random.randint(1,9)
     if inputMaquina not in jogadaMaquina:
        jogadaMaquina.append(inputMaquina)     
     if board[inputMaquina - 1] == "":
        board[inputMaquina - 1] = "O"
        break

     else:
        continue
    
 
    vitoriaMaquina = verificar_vitoria(jogadaMaquina)
    print()
    imprimir_board(board)
    print()
        
    if vitoriaMaquina == True:
        print("A máquina ganhou!!")
        print()
        imprimir_board(board)
        break
    
    empate = verificar_empate()       
    if empate == True:
        print("Deu velha!")
        print()
        imprimir_board(board)
        break
