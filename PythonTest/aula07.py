#Ordem de precedência
#1 ()
#2 ** potenciação
#3 * / // divisão inteiro % resto
#4 + -

num1 = int(input('Digite um número: '))
num2 = int(input('Digite o segundo número: '))
pot = num1 ** num2
mult = num1 * num2
div = num1 / num2
divi = num1 // num2
rest = num1 % num2
soma = num1 + num2
sub = num1 - num2
print(f'O resultado da potência é {pot} \n O da multiplicação é {mult}, o da divisão {div:.3f}, o da divisão inteiro {divi} e o resto é {rest}.', end=' ')
print(f'Já o resultado da soma é {soma} e o da subtração é {sub}')