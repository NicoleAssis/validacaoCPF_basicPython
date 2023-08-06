import sys
import random

digit_number =''
for i in range(9):
    digit_number += str(random.randint(0,9))

contador_Regressivo= 10
soma= 0
for digito in digit_number:
    soma+=(int(digito))*contador_Regressivo
    contador_Regressivo-=1
digito_1= (soma*10) % 11 
digito_1= digito_1 if digito_1<=9 else 0

digit_number += str(digito_1)
soma =0
contador_Regressivo= 11

for digito in digit_number:
    soma+=(int(digito))*contador_Regressivo
    contador_Regressivo-=1
digito_2 =(soma*10) % 11 
digito_2= digito_2 if digito_2<=9 else 0
digit_number += str(digito_2)

print(digit_number)
