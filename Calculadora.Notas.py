contador = 0
materias = []

while True:
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=')
    print('-----> Menu de Opçôes <----- ')
    print('1 - Nome da Matéria: ')
    print('2 - Materias: ')
    print('0 - Sair ....')
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=\n')

    n = int(input('Escolha uma das Opções: '))
    if n == 1:
        contador += 1
        nome = input('Materia: ')
        nota1 = float(input('Nota 1°B: '))
        while nota1 < 0 or nota1 > 10:
            print('----------------')
            print('Valor Invalido!')
            print('Valores de 0 à 10')
            print('----------------')
            nota1 = float(input('Nota 1°B: '))
        nota2 = float(input('Nota 2°B: '))
        while nota2 < 0 or nota2 > 10:
            print('----------------')
            print('Valor Invalido!')
            print('Valores de 0 à 10')
            print('----------------')
            nata2 = float(input('Nota 2°B: '))

        media = (nota1 + nota2) / 2
        resultado = " "
        if media >= 7:
            resultado = "APROVADO"

        else:
            resultado = "REPROVADO"


        materia = {'Materia:':nome,
                   'Nota 1°B:':nota1,
                   'Nota 2°B:':nota2,
                   'Media:':media,
                   'Resultado:':resultado}
        materias.append(materia)

        if media < 7:
            notaNec = 10 - media
            print('\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=')
            print('---> RESULTADO <---')
            print(f'{contador}º Materia: {nome}')
            print("RECUPERAÇÃO!")
            print(f'Media 1° e 2° B = {media:.2f}')
            print(f'\nNota necessaria na Prova Final')
            print(f'-----> {notaNec} pts <-----\n')
            print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=\n')

        else:
            print('\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=')
            print('---> RESULTADO <---')
            print(f'{contador}º Materia: {nome}')
            print('APROVADO!')
            print(f'Media 1° e 2° B = {media:.2f}')
            print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=\n')

    elif n == 2:
        if materias == []:
            print('----------------')
            print('Insira alguma materia!')
            print('----------------')

        else:
            for materia in materias:
                print('\n----------------\n')
                print(f'Matéria: {materia["Materia:"]}')
                print(f'Nota 1°B: {materia["Nota 1°B:"]}')
                print(f'Nota 2°B: {materia["Nota 2°B:"]}')
                print(f'Média: {materia["Media:"]}')
                print(f'Resultado: {materia["Resultado:"]}')
                print('----------------')

    elif n == 0:
        print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=')
        print('ENCERRANDO .....\n')
        break

    else:
        print('----------------')
        print('Opção invalida!')
        print('----------------')