from graphs import watts_strogatz, disease_spreading

import numpy as np
import networkx as nx
import matplotlib.pyplot as plt


if __name__ == '__main__':
    n = 1000
    k = 10
    
    ps = np.logspace(-4, 0, 14)
    rs = np.linspace(0.1, .5, 100)
    crs = []
    n_runs = 1000
    for p in ps:
        print(p)
        for r in rs:
            n_inf = []
            for _ in range(n_runs):
                edges = watts_strogatz(n, k, p)
                G = nx.from_edgelist(edges)
                
                _, num_infected = disease_spreading(G, r)
                n_inf.append(num_infected)
            
            mean = np.mean(n_inf)
            if mean >= n / 2:
                crs.append(r)
                break
    
    fig, ax = plt.subplots()
    ax.scatter(ps, crs, color='black')
    ax.set_xlabel('$p$')
    ax.set_ylabel('$r_{half}$')
    ax.set_xscale('log')
    ax.set_ylim(0.15, 0.4)
    fig.savefig('figs/critical-infection.png')
    plt.show()

