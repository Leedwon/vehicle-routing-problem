import random


def reproduce(parent1, parent2):
    """creates new child from parents"""

    gene_probability = 0.5

    child = []
    for gene1, gene2 in zip(parent1, parent2):
        if random.random() < gene_probability:
            child.append(gene1)
        else:
            child.append(gene2)
    return child
