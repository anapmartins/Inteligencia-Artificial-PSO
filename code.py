import random
import math


gB = []
vMax = [-25, 25]
valor_gB = 100000000


def calcula_aptidao(populacao):
	aptidao = []
	for i in range(len(populacao)):
		aptidao.append(0.5 + ((math.sin(math.sqrt(populacao[i][0]**2 + populacao[i][1]**2))**2 - 0.5) / ((1 + 0.001*(populacao[i][0]**2 + populacao[i][1]**2))**2)))
	
	return aptidao


def atualiza_velocidade(pB, velocidade, populacao):
	global vMax
	global gB
	
	for i in range(len(velocidade)):
		nova_velocidade = velocidade[i][0] + (2.5 * random.random() * (pB[i][0] - populacao[i][0])) + (2.5 * random.random() * (gB[0] - populacao[i][0]))
		if nova_velocidade < vMax[0]:
			velocidade[i][0] = vMax[0]
			
		elif nova_velocidade > vMax[1]:
			velocidade[i][0] = vMax[1]
		
		else:
			velocidade[i][0] = nova_velocidade
		 
		nova_velocidade = velocidade[i][1] + (2.5 * random.random() * (pB[i][1] - populacao[i][1])) + (2.5 * random.random() * (gB[1] - populacao[i][1]))
		if nova_velocidade < vMax[0]:
			velocidade[i][1] = vMax[0]
			
		elif nova_velocidade > vMax[1]:
			velocidade[i][1] = vMax[1]
		
		else:
			velocidade[i][1] = nova_velocidade
		

def atualiza_posicao(velocidade, populacao):
	for i in range(len(populacao)):
		populacao[i][0] = populacao[i][0] + velocidade[i][0]
		populacao[i][1] = populacao[i][1] + velocidade[i][1]


def cria_populacao_inicial(num_particulas):
	populacao = []
	for i in range(num_particulas):
		pos = []
		x1 = random.uniform(-100, 100)
		x2 = random.uniform(-100, 100)
		pos.append(x1)
		pos.append(x2)
		populacao.append(pos)
	
	return populacao


def inicia_aptidao_pbest(aptidao):
	aptidao_pb = []
	for i in range(len(aptidao)):
		aptidao_pb.append(aptidao[i])
	
	return aptidao


def atribui_velocidade_inicial(num_particulas):
	v = random.uniform(-15, 15)
	velocidade = []
	for i in range(num_particulas):
		pos = []
		pos.append(v)
		pos.append(v)
		velocidade.append(pos)
	
	return velocidade


def atualiza_melhor_posicao_pb(pb, populacao, aptidao, aptidao_pb):
	for i in range(len(populacao)):
		if aptidao[i] < aptidao_pb[i]:
			pb[i][0] = populacao[i][0]
			pb[i][1] = populacao[i][1]
	
		
def inicia_melhor_posicao(populacao):
	pb = []
	for i in range(len(populacao)):
		pos = []
		pos.append(populacao[i][0])
		pos.append(populacao[i][1])
		pb.append(pos)
		
	return pb


def acha_melhor_aptidao(aptidao, populacao):
	global gB
	global valor_gB
	
	for i in range(len(aptidao)):
		if aptidao[i] < valor_gB:
			valor_gB = aptidao[i]
			gB = [populacao[i][0], populacao[i][1]]
			
			
def main():
	arq = open("resultado.txt", "w")
	
	global gB
	global valor_gB
	
	for i in range(10): 	
		gB = []
		valor_gB = 100000000

		numero_particulas = 20
		num_iteracoes = 100
		populacao = cria_populacao_inicial(numero_particulas)
		velocidade = atribui_velocidade_inicial(numero_particulas)
		pbest = inicia_melhor_posicao(populacao)
		aptidao = calcula_aptidao(populacao)
		ap_pb = inicia_aptidao_pbest(aptidao)


		i = 0
		while i < num_iteracoes:
			aptidao = calcula_aptidao(populacao)
			atualiza_melhor_posicao_pb(pbest, populacao, aptidao, ap_pb)
			acha_melhor_aptidao(aptidao, populacao)
			atualiza_velocidade(pbest, velocidade, populacao)
			atualiza_posicao(velocidade, populacao)
			i = i + 1

		arq.write(str(valor_gB).replace(".", ",") + "\n")
	

	arq.close()

if __name__ == '__main__':
	main()
