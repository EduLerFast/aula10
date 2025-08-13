"""6.	Faça um Programa que peça as
 quatro notas de 10 alunos, calcule e 
 armazene num vetor a média de cada aluno,
   imprima o número de alunos 
com média maior ou igual a 7.0."""
cont = 0 
soma = 0
vetormedia = []

for i in range(3):
     
    for j in range(4):
        nota = float(input(f'Digite a {j+1}º Nota do {i+1}º Aluno'))
        soma = soma + nota
    media = soma/4
    soma = 0 
    vetormedia.append(media)
    print('-----')
print(vetormedia)
for i in range(3):
    if vetormedia[i] >=7:
        cont += 1 