

# formação análise de dados resilia/senac #
# aluno: lenilson reis #
# data: 08/02/2023 #
# projeto 1 - indivudal do modulo 2 #



resultados = ['e5_t9_p8_s8','e7_t7_p5_s8','e6_t7_p5_s6','e7_t8_p8_s9','e9_t9_p9_s9']
candidatos = ['bart','lisa','jorel','fred','patolino']
entrevista = int(input('por favor insira a nota da entrevista:'))
teorica = int(input('por favor insira a nota teorica:'))
pratica = int(input('por favor insisra a nota pratica:'))
soft = int(input('por favor insira a nota soft:'))
for i in resultados:
    if int(i[1]) >= entrevista and int(i[4]) >= teorica and int(i[7]) >= pratica and int(i[10]) >= soft:
        print('Patolino é o seu candidato:')
        print('resultados:',i[1],i[4],i[7],i[10])
    else:
        print(' ')
        print('Bart não é seu candidato:')
        print('resultados:',i[1],i[4],i[7],i[10])
        print(' ')
        print('Lisa não é seu candidato:')
        print('resultados:',i[1],i[4],i[7],i[10])
        print(' ')
        print('Jorel não é seu candidato:')
        print('resultados:',i[1],i[4],i[7],i[10])
        print(' ')
        print('Fred não é seu candidato;')
        print('resultados:',i[1],i[4],i[7],i[10])
        print(' ')
        
        
