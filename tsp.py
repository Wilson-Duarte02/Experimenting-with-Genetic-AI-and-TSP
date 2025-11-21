import random

def generate_initial_population(num_nodes, pop_size):
    nodes = [i for i in range(1, num_nodes)] #excluding start node (A)
    population = []

    for i in range(pop_size):
        random.shuffle(nodes)
        population.append(nodes.copy())
    
    return population

def fitness(chromosome, m):
    #distance matrix, m

    score = 0
    for i, gene in enumerate(chromosome):
        if i == 0:
            score += m[0, gene] #edge between start node and first in chromosome
        else:
            score += m[gene, chromosome[i-1]] #edge between any other pair of nodes
    
    score += m[0, chromosome[-1]] #edge connecting back to the start node

    return 100/score #take the reciprocal and scale

def main():
    node_labels = {0: "A", 1: "B", 2: "C", 3: "D", 4: "E", 5: "F", 6: "G", 7: "H", 8: "I", 9: "J"}

    #generate the graph (distance matrix)

    m = generate_graph(num_nodes = 10)

if __name__ == "__main__":
    main()    
    input("Press the Enter key to end program.")