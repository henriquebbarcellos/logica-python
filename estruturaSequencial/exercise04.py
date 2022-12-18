num = 0
total = 0

while num < 4:

    nota = input(f'Digite a nota da avaliação {num + 1}/4: ').strip()
    nota = int(nota)
    total += nota
    num += 1

media = total/num 
print(f'o total das notas foi "{total}" sua média é {media}')