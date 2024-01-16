from graphs import ring_lattice, watts_strogatz

import networkx as nx
import numpy as np
import matplotlib.pyplot as plt


if __name__ == '__main__':
    n = 1000
    k = 10
    
    edges_0 = ring_lattice(n, k)
    G_0 = nx.from_edgelist(edges_0)
    L_0 = nx.average_shortest_path_length(G_0)
    C_0 = nx.average_clustering(G_0)
    
    Ls = []
    Cs = []
    
    ps = np.logspace(-4, 0, 14)
    n_runs = 1000
    for p in ps:
        print(p)
        n_Ls = []
        n_Cs = []
        for _ in range(n_runs):
            edges = watts_strogatz(n, k, p)
            G = nx.from_edgelist(edges)
            
            L = nx.average_shortest_path_length(G) / L_0
            C = nx.average_clustering(G) / C_0
            
            n_Ls.append(L)
            n_Cs.append(C)
            
        Ls.append(np.mean(n_Ls))
        Cs.append(np.mean(n_Cs))
    
    fig, ax = plt.subplots()
    ax.scatter(ps, Ls, color='black', label='$L(p) / L(0)$')
    ax.scatter(ps, Cs, marker='s', facecolor='none', color='black', label='$C(p) / C(0)$')
    ax.set_xlabel('$p$')
    ax.set_xscale('log')
    ax.set_ylim(0, 1.1)
    ax.legend()
    fig.savefig('figs/small-world.png')
    plt.show()
