# 3) Crie uma função que calcule a idade de uma pessoa em dias, baseada no ano de nascimento.


from datetime import datetime
def calcula_idade(ano_nascimento):
	ano_atual = datetime.now().year
	idade=int(ano_atual)-ano_nascimento
	return idade * 365
print(calcula_idade(1990))