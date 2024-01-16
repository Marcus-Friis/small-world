from graphs import ring_lattice, watts_strogatz, disease_spreading

import numpy as np
import networkx as nx
import matplotlib.pyplot as plt


if __name__ == '__main__':
    n = 1000
    k = 10
    r = 1
    
    edges_0 = ring_lattice(n, k)
    G_0 = nx.from_edgelist(edges_0)
    L_0 = nx.average_shortest_path_length(G_0)
    t_0, _ = disease_spreading(G_0, r)
    
    Ls = []
    ts = []
    
    ps = np.logspace(-4, 0, 14)
    n_runs = 1000
    
    for p in ps:
        print(p)
        
        n_ts = []
        n_Ls = []
        for _ in range(n_runs):
            edges = watts_strogatz(n, k, p)
            G = nx.from_edgelist(edges)
            
            L = nx.average_shortest_path_length(G) / L_0
            t, _ = disease_spreading(G, r)
            t =  t / t_0
            n_Ls.append(L)
            n_ts.append(t)
            
        Ls.append(np.mean(n_Ls))
        ts.append(np.mean(n_ts))
        
    fig, ax = plt.subplots()
    ax.scatter(ps, ts, marker='s', facecolor='none', color='black', label='$T(p) / T(0)$')
    ax.scatter(ps, Ls, color='black', label='$L(p) / L(0)$')
    ax.set_xlabel('$p$')
    ax.set_xscale('log')
    ax.set_ylim(0, 1.1)
    ax.legend()
    fig.savefig('figs/disease-spreading.png')
    plt.show()
    