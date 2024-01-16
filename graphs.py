from random import random, choice


def ring_lattice(n, k):
    assert k % 2 == 0
    assert k < n
    
    nodes = range(n)
    edges = set()
    
    k_half = int(k / 2)
    for u in nodes:
        for v in range(1, k_half + 1):
            edge = (u, (u + v) % n)
            edges.add(edge)
    
    return edges

def watts_strogatz(n, k, p):
    assert p >= 0 and p <= 1
    
    nodes = range(n)
    edges = ring_lattice(n, k)
    k_half = int(k / 2)
    
    for v in range(1, k_half + 1):
        for u in range(n):
            if random() <= p:
                edge = (u, (u + v) % n)
                
                while True:
                    new_edge = (u, choice(nodes))
                    if new_edge not in edges and (new_edge[1], new_edge[0]) not in edges and new_edge[0] != new_edge[1]:
                        edges.add(new_edge)
                        edges.remove(edge)
                        # print(edge, '->', new_edge)
                        break

    return edges

def disease_spreading(G, r):
    assert r >= 0 and r <= 1
    
    all_infected = set({0})
    infected = set({0})
    newly_infected = set({})
    t = 0
    
    while True:
        for node in infected:
            neighbors = list(G[node].keys())
            for neighbor in neighbors:
                if random() <= r and neighbor not in all_infected:
                    newly_infected.add(neighbor)
            
        # print(infected, newly_infected)
        
        if len(newly_infected) == 0:
            return t, len(all_infected)
        
        t += 1
        infected = newly_infected
        all_infected = all_infected.union(infected)
        newly_infected = set({})


if __name__ == '__main__':    
    import networkx as nx
    import matplotlib.pyplot as plt
    
    n = 20
    k = 4
    p = 0
    edges = watts_strogatz(n, k, p)
    
    G = nx.Graph()
    for u in range(n):
        G.add_node(u)
    for edge in edges:
        G.add_edge(edge[0], edge[1])
    
    pos = nx.circular_layout(G)
    nx.draw(G, pos=pos)
    plt.show()