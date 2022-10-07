import datetime

nasc = float(input("Digite o ano do seu nascimento: "))
data = datetime.datetime.now()
ano = data.year
idade1 = ano - nasc
idade2 = 2050 - nasc
print( f"A idade atual é = { idade1 } " )
print( f"A idade em 2050 é = { idade2 } " )