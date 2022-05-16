#Ordem de precedência
#1 ()
#2 ** potenciação
#3 * / // divisão inteiro % resto
#4 + -

num1= input('Digite um número: ')
num2= input('Digite o segundo número: ')
pot= num1 ** num2
mult= num1 * num2
div= num1 / num2
divi= num1 // num2
rest= num1 % num2
soma = num1 + num2
sub= num1 - num2
print('O resultado da potência é {} \n O da multiplicação é {}, o da divisão {}, o da divisão inteiro {} e o resto é {}.', end=' ')
print('Já o resultado da soma é {} e o da subtração é {}')