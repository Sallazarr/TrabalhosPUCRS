while True:
    horaInicio = int(input("Insira a hora de inicio do jogo: "))
    minutoInicio = int(input("Insira o minuto de inicio do jogo: "))
    
    print(f"O jogo começou em {horaInicio}:{minutoInicio}")
    
    horaFim = int(input("Insira a hora de termino do jogo: "))
    minutoFim = int(input("Insira o minuto de termino do jogo: ")) 
       
    inicioTotal = horaInicio * 60 + minutoInicio
    fimTotal = horaFim * 60 + minutoFim

    
    if fimTotal < inicioTotal:
        duracao = (fimTotal + 1440) - inicioTotal
    else:
        duracao = fimTotal - inicioTotal
        
        
    duracaoH = duracao // 60
    duracaoM = duracao % 60
        
    print(f"o jogo durou {duracaoH} hora(s) e {duracaoM} minuto(s).")
    break
  