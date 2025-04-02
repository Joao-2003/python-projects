import random
import numpy as np


# 1. Definição da Mochila e Itens (pode ser pré-definida ou aleatória)
def gerar_itens(num_itens, peso_max=15, valor_max=100):
    return [
        {'peso': random.randint(1, peso_max), 'valor': random.randint(10, valor_max)}
        for _ in range(num_itens)
    ]


# Exemplo de itens pré-definidos (opcional)
# itens = [
#     {'peso': 5, 'valor': 45},
#     {'peso': 8, 'valor': 72},
#     ...
# ]

# 2. Parâmetros do GA
NUM_ITENS = 30
PESO_MAXIMO = 100
TAM_POPULACAO = 100
TAXA_CROSSOVER = 0.7  # 70% do pai, 30% da mãe (e vice-versa)
TAXA_MUTACAO = 0.01  # 10% dos indivíduos sofrem mutação
GERACOES = 200


# 3. Geração de Indivíduos (vetor binário)
def gerar_individuo():
    return [random.randint(0, 1) for _ in range(NUM_ITENS)]


# 4. Função de Fitness (prioriza valor, depois número de itens)
def calcular_fitness(individuo, itens, peso_maximo):
    peso_total = sum(itens[i]['peso'] for i, inclui in enumerate(individuo) if inclui)
    if peso_total > peso_maximo:
        return 0  # Solução inválida
    else:
        num_itens = sum(individuo)
        valor_total = sum(itens[i]['valor'] for i, inclui in enumerate(individuo) if inclui)
        return num_itens +  1000 * valor_total  # Prioriza valor


# 5. Seleção de Pais por Torneio
def selecionar_pais(populacao, fitnesses, tamanho_torneio=3):
    candidatos = random.sample(list(zip(populacao, fitnesses)), tamanho_torneio)
    candidatos.sort(key=lambda x: x[1], reverse=True)
    return candidatos[0][0]


# 6. Crossover com Proporção Definida (70% pai, 30% mãe e vice-versa)
def crossover(pai, mae, taxa_crossover):
    n = len(pai)
    k = int(taxa_crossover * n)  # Número de genes do pai

    # Filho 1: k genes do pai, (n - k) da mãe
    indices_pai = random.sample(range(n), k)
    filho1 = [pai[i] if i in indices_pai else mae[i] for i in range(n)]

    # Filho 2: k genes da mãe, (n - k) do pai
    indices_mae = random.sample(range(n), k)
    filho2 = [mae[i] if i in indices_mae else pai[i] for i in range(n)]

    return filho1, filho2


# 7. Mutação (inverte um gene aleatório se o indivíduo for selecionado)
def mutar(individuo, taxa_mutacao):
    if random.random() < taxa_mutacao:
        idx = random.randint(0, len(individuo) - 1)
        individuo[idx] = 1 - individuo[idx]
    return individuo


# 8. Algoritmo Genético Completo
def algoritmo_genetico(itens, peso_maximo, tam_populacao, taxa_crossover, taxa_mutacao, geracoes):
    populacao = [gerar_individuo() for _ in range(tam_populacao)]
    melhor_individuo = None
    melhor_fitness = 0

    for gen in range(geracoes):
        # Cálculo do fitness
        fitnesses = [calcular_fitness(ind, itens, peso_maximo) for ind in populacao]

        # Atualiza o melhor indivíduo global
        max_fitness = max(fitnesses)
        if max_fitness > melhor_fitness:
            melhor_indice = fitnesses.index(max_fitness)
            melhor_individuo = populacao[melhor_indice].copy()
            melhor_fitness = max_fitness

        # Seleção de pares para crossover
        nova_populacao = []
        for _ in range(tam_populacao // 2):
            pai = selecionar_pais(populacao, fitnesses)
            mae = selecionar_pais(populacao, fitnesses)

            # Gera dois filhos por par
            filho1, filho2 = crossover(pai, mae, taxa_crossover)

            # Aplica mutação
            filho1 = mutar(filho1, taxa_mutacao)
            filho2 = mutar(filho2, taxa_mutacao)

            nova_populacao.extend([filho1, filho2])

        # Elitismo: mantém o melhor indivíduo
        if melhor_individuo is not None:
            # Substitui o pior indivíduo da nova geração
            fitness_novos = [calcular_fitness(ind, itens, peso_maximo) for ind in nova_populacao]
            pior_indice = np.argmin(fitness_novos)
            nova_populacao[pior_indice] = melhor_individuo.copy()

        populacao = nova_populacao[:tam_populacao]

        # Relatório
        peso_total = sum(itens[i]['peso'] for i, inclui in enumerate(melhor_individuo) if inclui)
        valor_total = sum(itens[i]['valor'] for i, inclui in enumerate(melhor_individuo) if inclui)
        print(f"Geração {gen + 1}: Itens={sum(melhor_individuo)}, Peso={peso_total}/{peso_maximo}, Valor={valor_total}")

    return melhor_individuo


# 9. Execução
if __name__ == "__main__":
    itens = gerar_itens(NUM_ITENS)
    solucao = algoritmo_genetico(
        itens=itens,
        peso_maximo=PESO_MAXIMO,
        tam_populacao=TAM_POPULACAO,
        taxa_crossover=TAXA_CROSSOVER,
        taxa_mutacao=TAXA_MUTACAO,
        geracoes=GERACOES
    )

    print("\nMelhor solução encontrada:")
    print("Itens selecionados:", sum(solucao))
    print("Peso total:", sum(itens[i]['peso'] for i, val in enumerate(solucao) if val))
    print("Valor total:", sum(itens[i]['valor'] for i, val in enumerate(solucao) if val))
