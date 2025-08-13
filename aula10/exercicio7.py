#Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.
vetor=[]
soma=0
multi = 1
for i in range(5):
    n= int (input(f'digite o {i+1}º numero inteiro'))
    vetor.append(n)
    soma+=n
    multi *= n


print ('os numeros sao....')
for i in range(5):
 print (f'{i+1}º numero: {vetor[i]}')
print(f'a soma é {soma} e a multiplicaçao {multi}' )