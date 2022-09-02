#strings (str)
nome_1 = 'Eduardo'
nome_2 = 'Eduardo'

if nome_1 == nome_2: #is or ==
    print('iguais')
else:
    print('diferentes')

# find
mensagem = 'string no python'
print(mensagem.find('python')) #10    

nome = 'Daniel'
print(nome[0]) # D
nome = 'Daniel'
print(nome[0:3]) # Dan 
nome = "Daniel"
print(nome[-2]) # e

#função id
nome = 'Eduardo'
print(id(nome))
nome = 'Felipe'
print(id(nome))
nome_1 = 'Rodrigo'
nome_2 = 'Ana'

#função len
print(len(nome_1)) # 7
print(len(nome_2)) # 3

# junção de string
nome = 'Daniel'
sobrenome = 'Silva'

nome_completo = nome + ' ' + sobrenome
print(nome_completo) # Daniel Silva

#find
mensagem = 'string no Python'
print(mensagem.find('Python')) # 10

#replace
mensagem = 'aprendizado de java'
nova_mensagem = mensagem.replace('java', 'python')
print(nova_mensagem)

#split
mensagem = 'aprendendo python'
nova_mensagem = mensagem.split(' ')
print(type(nova_mensagem))
print(nova_mensagem)

mensagem = 'Estou aprendendo Python'
lista_mensagem = mensagem.split(' ')
print(lista_mensagem[1]) # aprendendo

#upper
mensagem = 'aprendendo python'
nova_mensagem = mensagem.upper()
print(nova_mensagem)

#lower
mensagem = 'APRENDENDO PYTHON'
nova_mensagem = mensagem.lower()
print(nova_mensagem)

#acentuação
#coding: utf-8
nome = 'José da Silva'
print(nome)

#lista em py
programadores = ['Victor', 'Juliana', 'Caio', 'Luana']
print(type(programadores)) # type 'list'
print(len(programadores)) # 5
print(programadores[4]) # Luana

programadores = ['Victor', 'Juliana', 'Caio', 'Luana']
print(programadores) # type 'list'

programadores[1] = 'Carolina'
print(programadores)

programadores = ['Victor', 'Juliana', 'Samuel', 'Caio', 'Luana']
print(type(programadores)) # type ‘list’
print(len(programadores)) # 5
print(programadores[4]) # Luana

#adição em lista
programadores = ['Victor', 'Juliana', 'Samuel', 'Caio', 'Luana']
print(programadores) # ['Victor', 'Juliana', 'Samuel', 'Caio', 'Luana

programadores.append('Renato')
print(programadores) # ['Victor', 'Juliana', 'Samuel', 'Caio', 'Luana', 'Renato']

programadores = ['Victor', 'Juliana', 'Samuel', 'Caio', 'Luana']
programadores.remove('Caio')
print(programadores) # ['Victor', 'Juliana', 'Samuel', 'Caio', 'Luana', 'Renato']

programadores = ['Victor', 'Juliana', 'Samuel', 'Caio', 'Luana']
programadores.insert(1, 'Rafael')
print(programadores) # ['Victor', 'Rafael', 'Juliana', 'Samuel', 'Caio', 'Luana']

#retirando item com pop()
programadores = ['Victor', 'Juliana', 'Samuel', 'Caio', 'Luana']
programadores.pop(0)
print(programadores) # ['Victor', 'Juliana', 'Samuel', 'Caio', 'Luana', 'Renato']

#tupla
times_rj = ('Botafogo', 'Flamengo', 'Fluminense', 'Vasco')
print(type(times_rj)) # class=’tuple’
print(times_rj) # ('Botafogo', 'Flamengo', 'Fluminense', 'Vasco')

times_rj = ('Botafogo', 'Flamengo', 'Fluminense', 'Vasco')
print(times_rj[2]) # Fluminense

vogais = ('a', 'e', 'i', 'o', 'u')
print(vogais[1]) # e

objeto_string = ('tesoura')
objeto_tupla = ('tesoura',)

print(type(objeto_string))
print(type(objeto_tupla))

#Alfabeto
dados_cliente = {
    'Nome': 'Renan',
    'Telefone': '47999237700',
    'Endereço': 'Cruzeiro do Sul'
}
print(dados_cliente['Nome'])

print(dados_cliente) 

dados_cliente['Idade'] = 40

print(dados_cliente)

del dados_cliente['Telefone']

print(dados_cliente)

#coleções
numeros = [15, 5, 0, 20, 10]
nomes = ['Caio', 'Alex', 'Renata', 'Patrícia', 'Bruno']

print(min(numeros)) # 0
print(max(numeros)) # 20
print(min(nomes)) # Alex
print(max(nomes)) # Renata

#sum()
numeros = [1,3,6]
print(sum(numeros))
#len()
paises = ['Brasil','Argentina','Portugal','Itália']
print(len(paises))
#type()
professores = ['Carla','Eduardo','Felipe','Lucas']
estacoes = ('Primavera','Outono','Verão')
cliente = {
    'Nome': 'Fabio Garcia',
    'email':'fabiogarcia@gmail.com'
}
print(type(professores)) #list
print(type(estacoes)) #tuple
print(type(cliente)) #dict

#Operadores Aritméticos
numero_1 = 5
numero_2 = 2

soma = numero_1 + numero_2
subtracao = numero_1 - numero_2
multiplicacao = numero_1 * numero_2
divisao = numero_1 / numero_2
divisao_inteira = numero_1 // numero_2
modulo = numero_1 % numero_2
exponenciacao = numero_1 ** numero_2

print(soma) # 7
print(subtracao) # 3
print(multiplicacao)  # 10
print(divisao) # 2.5
print(divisao_inteira) # 2
print(modulo)  # 1
print(exponenciacao) # 25


#OP 1.1
print((2+5)*3)

#OP 1.2
numero = 5
numero += 5
print(numero)
# Operadores de Comparação
numero_1 = 2
numero_2 = 4

soma = numero_1 + numero_2

if soma < 10:
    print("soma não é maior que 10")
else:
    print("soma é maior ou igual a 10")

soma_1 = 7 + 8
soma_2 = 10 + 11

if soma_1 == soma_2:
    print("Os resultados são iguais")
else:
    print("Os resultados são diferentes")    

#Operadores Lógicos

idade_lucas = 21
idade_carolina = 19

# Operador OR
if idade_lucas >= 18 or idade_carolina >= 18:
    print("Pelo menos um dos dois é maior de idade")
else:
    print("Lucas e Carolina não são maiores de idade")

idade_lucas = 21
idade_carolina = 19

#Operador AND
if idade_lucas >= 18 or idade_carolina >= 18:
    print("Pelo menos um dos dois é maior de idade")
else:
    print("Lucas e Carolina não são maiores de idade")    

# Operadores de Identidade
time_carlos = 'Botafogo'
time_luciano = 'Flamengo'
time_fabricia = 'Botafogo'

if time_carlos is time_luciano:
    print("time_carlos - time_luciano = mesmo objeto")
else:
    print("time_carlos - time_luciano = objetos diferentes")

if time_carlos is time_fabricia:
    print("time_carlos - time_fabricia = mesmo objeto")
else:
    print("time_carlos - time_fabricia = objetos diferentes")

# Operadores de Associação
frutas = ['banana', 'maçã','uva','ameixa']

frutas_1 = 'ameixa'
frutas_2 = 'melancia'

print(frutas_1 in frutas) #true
print(frutas_2 in frutas) #false