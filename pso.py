#PSO
import numpy as np

class Particula:
  def __init__(self):
        self.lista_posicao = []
        self.lista_velocidade = []
        self.fitness = np.inf
        self.fitness_pbest = np.inf
        self.lista_posicao_pbest = []

w = 0.8 #coeficiente de inércia
c1 = 2.05 #fator de individualidade
c2 = 2.05 #fator de sociabilidade

bound = [-100,100]
velocidade_max = [-6,6]
dimensao = 30 #2
numero_particulas = 30 #2
qtd_iteracoes = 10000 #2
swarm = []

#Inicialização

for i in range(numero_particulas):
  p = Particula()
  for i in range (dimensao):
    p.lista_posicao.append(random.uniform(bound[0], bound[1]))
    p.lista_velocidade.append(random.uniform(velocidade_max[0], velocidade_max[1]))
  swarm.append(p)

#Exibição

print(numero_particulas)
for i in range (numero_particulas): #(numero_particulas):
    p = swarm[i]
    d1,d2,d3,d4,d5,d6,d7,d8,d9,d10,d11,d12,d13,d14,d15,d16,d17,d18,d19,d20,d21,d22,d23,d24,d25,d26,d27,d28,d29,d30 = zip(p.lista_posicao)
    plt.plot(d1,d2,d3,d4,d5,d6,d7,d8,d9,d10,d11,d12,d13,d14,d15,d16,d17,d18,d19,d20,d21,d22,d23,d24,d25,d26,d27,d28,d29,d30, marker='o')
plt.plot(0,0, marker='*')
plt.axis([-100, 100, -100, 100])
plt.show()

#Fitness

def funcao_fitness(lista_solucao):
  total = 0
  for i in range (dimensao):
      total += lista_solucao[i]**2
  return total

#Cálculo

def calculo_fitness(particula):
  particula.fitness = funcao_fitness(particula.lista_posicao)
  if (particula.fitness < particula.fitness_pbest):
    particula.fitness_pbest = particula.fitness
    particula.lista_posicao_pbest = list (particula.lista_posicao)

#Velocidade

def atualizacao_velocidade_global(particula, lista_gbest):
  for i in range(dimensao):
    e1 = random.random()
    e2 = random.random()
    velocidade_cognitiva = c1*e1* (particula.lista_posicao_pbest[i] - particula.lista_posicao[i])
    velocidade_social = c2*e2* (lista_gbest[i] - particula.lista_posicao[i])
    v = w * particula.lista_velocidade[i] + velocidade_cognitiva + velocidade_social
    if v>bound[1]:
      v = bound[1]
    elif v<bound[0]:
      v = bound[0]
    particula.lista_velocidade[i] = v

#Atualização da partícula

def atualiza_posicao(particula, bound):
  for i in range(dimensao):
      novo_valor = particula.lista_posicao[i] + particula.lista_velocidade[i]
      if novo_valor > bound[1]:
          novo_valor =  bound[1]
      if novo_valor < bound[0]:
          novo_valor = bound[0]
      particula.lista_posicao[i] = novo_valor

#PSO

fitness_gbest = float('inf')
lista_posicao_gbest = []
lista_valores_gbest = []
for i in range(qtd_iteracoes):
  for j in range(numero_particulas):
     calculo_fitness(swarm[j])
     if  swarm[j].fitness < fitness_gbest:
      fitness_gbest = swarm[j].fitness
      lista_posicao_gbest = list (swarm[j].lista_posicao)
  for j in range(numero_particulas):
    atualizacao_velocidade_global(swarm[j],lista_posicao_gbest)
    atualiza_posicao(swarm[j],bound)
  lista_valores_gbest.append(fitness_gbest)
  for i in range(numero_particulas):
    p = swarm[i]
    d1,d2,d3,d4,d5,d6,d7,d8,d9,d10,d11,d12,d13,d14,d15,d16,d17,d18,d19,d20,d21,d22,d23,d24,d25,d26,d27,d28,d29,d30 = zip(p.lista_posicao)
    plt.plot(d1,d2,d3,d4,d5,d6,d7,d8,d9,d10,d11,d12,d13,d14,d15,d16,d17,d18,d19,d20,d21,d22,d23,d24,d25,d26,d27,d28,d29,d30, marker='o')
  plt.plot(0,0, marker='*')
  plt.plot(lista_posicao_gbest[0],lista_posicao_gbest[1], marker='x')
  plt.axis([-100, 100, -100, 100])
  plt.show()

#Resultado

plt.plot(lista_valores_gbest)
plt.title("Convergence Curve of the PSO")
plt.xlabel("Iterations")
plt.ylabel("Best Fitness")
plt.tight_layout()

print('Valor gbest:',fitness_gbest)