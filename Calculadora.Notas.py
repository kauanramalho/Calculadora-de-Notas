contador = 0
materias = []

while True:
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=')
    print('-----> Menu de Opçôes <----- ')
    print('1 - Nome da Matéria: ')
    print('2 - Nota necessaria para 2°B')
    print('3 - Materias: ')
    print('0 - Sair ....')
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=\n')

    n = int(input('Escolha uma das Opções: '))
    if n == 1:
        contador += 1
        nome = input('Materia: ')
        nota1 = float(input('Nota 1°B: '))
        while nota1 < 0 or nota1 > 10:
            print('=-=-=-=-=-=-=-=-=-=-=')
            print('Valor Invalido!')
            print('Valores de 0 à 10')
            print('=-=-=-=-=-=-=-=-=-=-=-\n')
            nota1 = float(input('Nota 1°B: '))
        nota2 = float(input('Nota 2°B: '))
        while nota2 < 0 or nota2 > 10:
            print('=-=-=-=-=-=-=-=-=-=-=')
            print('Valor Invalido!')
            print('Valores de 0 à 10')
            print('=-=-=-=-=-=-=-=-=-=-=\n')
            nata2 = float(input('Nota 2°B: '))

        media = (nota1 + nota2) / 2
        resultado = " "
        if media >= 7:
            resultado = "APROVADO"

        else:
            resultado = "REPROVADO"


        materia = {'Contador':contador,
                   'Materia':nome,
                   'Media':media,
                   'Resultado':resultado,
                   'NotaNec':None,
                   'Tipo': 1}
        
        materias.append(materia)

        if media < 7:
            notaNec = 10 - media
            print('\n---------------------------------------')
            print('---> RESULTADO <---')
            print(f'{contador}º Materia: {nome}')
            print("RECUPERAÇÃO!")
            print(f'Media 1° e 2° B = {media:.2f}')
            print(f'\nNota necessaria na Prova Final')
            print(f'-----> {notaNec:.2f} pts <-----\n')
            print('---------------------------------------\n')

        else:
            print('\n---------------------------------------')
            print('---> RESULTADO <---')
            print(f'{contador}º Materia: {nome}')
            print('APROVADO!')
            print(f'Media 1° e 2° B = {media:.2f}')
            print('---------------------------------------\n')

    elif n == 2:
        contador += 1
        nome = input('Materia: ')
        nota1 = float(input('Nota 1°B: '))
        while nota1 < 0 or nota1 > 10:
            print('----------------')
            print('Valor Invalido!')
            print('Valores de 0 à 10')
            print('----------------')
            nota1 = float(input('Nota 1°B: '))

        notaNec2 = 14 - nota1
        print('\n---------------------------------------')
        print(f'Nota necessaria 2°B para APROVADO >= {notaNec2:.2f}')
        print('---------------------------------------\n')

        materia2 = {'Contador':contador,
                   'Materia':nome,
                   'Media':None,
                   'Resultado':None,
                   'NotaNec2':notaNec2,
                   'Tipo': 2}
        materias.append(materia2)

    elif n == 3: 
        print('RESUMO SOBRE AS MATERIAS CALCULADAS...\n')
        if materias == []:
            print('----------------')
            print('Insira alguma materia!')
            print('----------------')

        else:
            for materia in materias:
                print('\n----------------')
                print(f'{materia["Contador"]}º Matéria: {materia["Materia"]}')

                if materia["Tipo"] == 1:
                    print(f'Média: {materia["Media"]:.2f}')
                    print(f'Resultado: {materia["Resultado"]}')
                    print('----------------\n')

                elif materia["Tipo"] == 2:
                    print(f'Nota necessária 2ºB para APROVADO >= {materia["NotaNec2"]:.2f}')
                    print('----------------\n')

    elif n == 0:
        print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=')
        print('ENCERRANDO .....\n')
        break

    else:
        print('=-=-=-=-=-=-=-=-=-=-=')
        print('Opção invalida!')
        print('=-=-=-=-=-=-=-=-=-=-=')