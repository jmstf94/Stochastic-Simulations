import numpy as np
import seaborn as sns

#we denote the connections with a symmetric matrix of 10000x10000
#with zeros in the diagonal elements
#if element 12 or 21 of the matrix has 1 it means that nod 1 is connected
#to nod 2
def simulation(n_nodes, one_prob):
    z = np.random.choice([0,1],p = [1-one_prob,one_prob], size = [n_nodes,n_nodes])
    np.fill_diagonal(z,0)
    z = np.tril(z)
    z = z+z.T
    n_edges = np.sum(z,axis=1)
    return n_edges

######experiment######
exps = 1000
n_nodes = 10000
probability = 0.15
means = [0]*n_nodes
mean_k = 0
for i in range(exps):
    x = simulation(n_nodes,probability)
    mean_k+=sum(x)/n_nodes/exps
    for j in range(n_nodes):
        means[j]+=x[j]/exps

sns.displot(means, kind="kde")
print(mean_k)
