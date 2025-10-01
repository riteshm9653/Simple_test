# Apriori Algorithm
from itertools import combinations

T = [
    ['A','B','C','D'],
    ['A','C','D'],
    ['B','C','E'],
    ['A','B','C','E'],
    ['B','C','D'],
    ['A','B','C'],
    ['A','C','E'],
    ['B','C','D','E']
]

min_sup = 0.5

def support(itemset):
    count = sum(1 for t in T if set(itemset).issubset(t))
    return count / len(T)

items = sorted(set(item for transaction in T for item in transaction))

freq_itemsets = [{item} for item in items if support([item]) >= min_sup]
final_freq = []

k = 1
while freq_itemsets:
    final_freq.extend([(list(itemset), support(itemset)) for itemset in freq_itemsets])
    candidates = []
    for i in range(len(freq_itemsets)):
        for j in range(i+1, len(freq_itemsets)):
            union_set = freq_itemsets[i] | freq_itemsets[j]
            if len(union_set) == k+1 and union_set not in candidates:
                # Prune: keep only if all subsets are frequent
                if all(set(subset) in freq_itemsets for subset in combinations(union_set, k)):
                    candidates.append(union_set)

    # Filter candidates by support
    freq_itemsets = [c for c in candidates if support(c) >= min_sup]
    k += 1

# Print results
print("Frequent Itemsets with Support:")
for itemset, sup in final_freq:
    print(itemset, "->", round(sup, 3))
