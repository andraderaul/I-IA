from random import random 

''' funcao pra ler arquivo e retornar uma lista de x e y '''
def leArquivo(nome):
	f = open(nome)
	x = []
	y = []
	
	for linha in f:
		linha = linha.split(',')
		x.append(float(linha[0]))
		y.append(float(linha[1]))
	
	f.close()	
	return (x,y)

''' funcao que recebe um inteiro e retorna uma lista de valores aleatorios'''
def iniciaK(K):
	lista = []
	for i in range(K):
		lista.append(random())	
	return lista	

''' funcao que recebe uma lista de X e parametros P, e retorna os valores dos polinomios'''	
def poly(X,P):	
	lista = []
	for i in range(len(X)):
		soma = 0
		for j in range(len(P)):
			soma += P[j] * (X[i] ** j)
		lista.append(soma)
	return lista

''' funcao que calcula o erro dado os pontos X Y e o parametro'''
def erro(X,Y,P):
	lista = []
	P = poly(X,P)	
	for i in range(len(Y)):
		lista.append(Y[i] - P[i])
	return lista

''' funcao que retorna a soma dos erros ao quadrado '''
def erroTotal(X,Y,P):
	erros = erro(X,Y,P)
	soma = 0
	for e in erros:
		soma += e ** 2
	return ((1/2)*soma)

''' funcao que calcula as derivadas parciais do erro com relacao a cada um dos parametros'''
def parcial(X,Y,P): #verificar isso depois
	e = erro(X,Y,P)
	lista = []
	p1 = 0
	p2 = 0
	p3 = 0
	
	for i in range(len(e)):
		p1 += e[i]
		
	for i in range(len(e)):
		p2 += (i * e[i] )
	
	for i in range(len(e)):
		p3 += ( e[i] * X[i]**2 )
		
	return [-p1,-p2,-p3]
	
''' funcao que atualiza os parametros'''
def atualiza(X,Y,P,alfa): #verificar isso depois
	pParcial = parcial(X,Y,P)
	pAtt = []
	for i in range(len(P)):
		pAtt.append(P[i] - (alfa * pParcial[i]))
	return pAtt
def ajusta(nome, K, M, alpha):		
	
	SEQ = 0
	X, Y = leArquivo(nome)
	erro_aceitavel = 3
	parametros = iniciaK(K+1) # K + 1 pq polinomio de grau K tem K + 1 parametros
#	P =  [1,2,0.5]
	P = parametros
	i = 0
	while i < M :		
		SEQ = erroTotal(X,Y,P)
		if i %100 == 0:
			print('Valor da seq %f: ' %SEQ)
			print('Parâmetros:', P)		
		P = atualiza(X,Y,P,alpha)				
		i += 1	
	
	return  SEQ, P

def main():
	
	#nome = input()
	#K = int(input())
	#M = int(input())
	#alpha = float(input())
	#SEQ, P = ajusta(nome,K,M,alpha)
	#teste
	SEQ, P = ajusta('entrada.txt',2,10000,0.001)
	print('Valor final da seq: %f' %SEQ)
	print('Parâmetros Final:', P)
	
main()
