while True:
    try:
        altura = float(input("Insira a sua altura em metros ('exemplo: 1.74'): "))
        if altura < 0:
            print("Altura deve ser positiva")
            continue
    except ValueError:
        print("Valor inválido, tente novamente")
        continue
    
    try:
        genero = int(input("Insira seu gênero, use 1 para masculino e 2 para feminino: "))
        if genero not in (1,2):
            print("Use apenas 1 ou 2 para selecionar o gênero")
            continue
    except ValueError:
        print("Valor inválido, tente novamente")
        continue
    break
if genero == 1:
    pesoIdeal = 72.7 * altura - 58
else:
    pesoIdeal = 62.1 * altura - 44.7
        
print(f"Seu peso ideal é {pesoIdeal:2} kg")
