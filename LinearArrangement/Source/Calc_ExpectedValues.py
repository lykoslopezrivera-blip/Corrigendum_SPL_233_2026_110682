from Calc_Probabilities import (
    padovan_sequence,
    probability_matrix,
    possible_indices,
    N_stat_k,
    N_seq_k,
)
import sympy as sp
import numpy as np
import math



N_MAX = 300
STEP = 5
n_values_expected = list(range(0, N_MAX, STEP))

expected_seats_sequential = []
for n_seats in n_values_expected:
    if n_seats == 0:
        expected_seats_sequential.append(0)
        continue
    row = probability_matrix[n_seats - 1]   # fila n-1 <-> n asientos
    ev = sum(k * row[k] for k in range(len(row)) if row[k] != 0)
    expected_seats_sequential.append(ev / n_seats)

expected_seats_static = []
for n_seats in n_values_expected:
    if n_seats == 0:
        expected_seats_static.append(0)
        continue
    ks = list(possible_indices(n_seats))
    ev = sum(k * N_stat_k(n_seats, k) for k in ks)
    expected_seats_static.append(float(ev) / n_seats)