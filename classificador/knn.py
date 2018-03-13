from math import pow, sqrt

class Individuo:
	def __init__(self, a, b, c ,d, classe):
		self.a = a
		self.b = b
		self.c = c
		self.d = d
		self.classe = classe
	
	def getClasse(self):
		return self.classe
	def getA(self):
		return self.a
	def getB(self):
		return self.b
	def getC(self):
		return self.c
	def getD(self):
		return self.d				
		
#distancia minha cidade
def distEuclidiana(ind1, ind2):
	soma = pow(ind1.getA() - ind2.getA(),2) + pow(ind1.getB() - ind2.getB(),2) + pow(ind1.getC() - ind2.getC(),2) +	pow(ind1.getD() - ind2.getD(),2)
	return sqrt(soma)
	
def classificarAmostra(individuos, novo_exemplo, K	):
	tam_vet = len(individuos)
	dist_individuos = set()
	temp = dict()
	for i in range(tam_vet):
		dist = distEuclidiana(individuos[i], novo_exemplo)
		temp[dist] = i
		dist_individuos.union(temp)
	
	cont_class = [0 for i in range(3)]	
	contK = 0
	for ind in individuos:
		if contK == K:
			break
		classe = ind.getClasse()
		if classe == 'Iris-Setosa':
			cont_class[0]+=1 
		elif classe == 'Iris-versicolor':
			cont_class[1]+=1
		else:
			cont_class[2]+=1
		contK+=1
	
	classe_classificacao = ''
	
	if cont_class[0] >= cont_class[1] and cont_class[0] >= cont_class[2]:
		classe_classificacao = 'Iris-setosa'
	elif cont_class[1] >= cont_class[0] and cont_class[1] >= cont_class[2]:
		classe_classificacao = 'Iris-versicolor'
	else:
		classe_classificacao = 'Iris-virginica'
	
	return classe_classificacao			

def lerarquivo():
	amostras = []
	with open('dataset.data', 'r') as f:
		for linha in f.readlines():
			atrib = linha.replace('\n', '').split(',')
			ind = Individuo(float(atrib[0]), float(atrib[1]), float(atrib[2]), float(atrib[3]), (atrib[4]))
			amostras.append(ind)

	return amostras
        
def main():
	K = 3
	entrada = lerarquivo()

	ind1 = Individuo(3,3,3,3,'nao_sei')
	ind2 = Individuo(-1,0,1,2,'nao_sei')
	
	print(classificarAmostra(entrada, ind1, K))
	print(classificarAmostra(entrada, ind2, K))
	
	
	
main()	
	
	
