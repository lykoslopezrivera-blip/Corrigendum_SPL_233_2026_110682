import math
import numpy as np

from Calc_Probabilities import (
    possible_indices,
    N_stat_k,
    probability_matrix_list,
)


TOLERANCE = 1e-10


def is_dominant(a, b, tol=TOLERANCE):
    return a >= b - tol


max_n = len(probability_matrix_list)


accumulated_data = {}

for n in range(1, max_n + 1):
    ks = list(possible_indices(n))
    stat_probs = [N_stat_k(n, k) for k in ks]

    seq_probs = probability_matrix_list[n - 1]
    seq_probs = seq_probs[ks[0]:ks[0] + len(ks)]

    cumulative_stat = np.cumsum(stat_probs)
    cumulative_seq = np.cumsum(seq_probs)

    accumulated_data[n] = {
        "ks": ks,
        "cumulative_stat": cumulative_stat,
        "cumulative_seq": cumulative_seq,
    }

    d1_holds = all(
        is_dominant(cumulative_stat[i], cumulative_seq[i])
        for i in range(len(cumulative_seq))
    )

    if d1_holds:
        print(f"n = {n}: D_1 holds")
    else:
        print(f"n = {n}: D_1 fails")
        
print("\nSummary of D_1 dominance checks:")
for n in range(1, max_n + 1):
    d1_holds = all(
        is_dominant(
            accumulated_data[n]["cumulative_stat"][i],
            accumulated_data[n]["cumulative_seq"][i],
        )
        for i in range(len(accumulated_data[n]["cumulative_seq"]))
    )
    
    if  not d1_holds: 
        print(f"n = {n}: D_1 fails")

print("\nAll D_1 dominance checks completed.")