# Computational Verification of Stochastic Domination in a Discrete Parking Process

This repository contains a direct computational verification of the stochastic domination of the sequential random variable over the static random variable in the discrete parking process, for all \(n \leq 300\).

The repository provides a table organizing the computational results for each value of \(n\), as well as a plot comparing the expected values of the two random variables. The computations are implemented in Python and are organized into source code and a Jupyter notebook.

## Authors

- Robinson Higuita Diaz
- Alejandro Roldán Correa
- Lykos López Rivera

## Repository Structure

```text
.
├── .gitignore
├── README.md
└── LinearArrangement/
    ├── Notebooks/
    │   └── [verification notebook].ipynb
    └── Source/
        ├── Calc_Probabilities.py
        ├── Calc_ExpectedValues.py
        └── Verify_D_1.py
```

## Contents

### Notebook

The `Notebooks` directory contains a Jupyter notebook presenting the computational verification. It includes:

- A table of the results for some values of n.
- A plot comparing the expected values of the sequential and static random variables.
- The computational verification of stochastic domination for the considered values of \(n\) up to \(300\).

### Source Code

The `Source` directory contains the following Python scripts:

| Script | Description |
|---|---|
| `Calc_Probabilities.py` | Computes the probabilities of the sequential and static random variables in the linear arrangement. |
| `Calc_ExpectedValues.py` | Computes the expected values of the sequential and static random variables. |
| `Verify_D_1.py` | Verifies the stochastic domination of the sequential random variable over the static random variable for \(n \leq 300\). |

## Scope

The purpose of this repository is to provide computational evidence for the stochastic domination of the sequential random variable over the static random variable in the linear arrangement, for all \(n = 1, \ldots, 300\).

The results are intended as a direct computational verification over this finite range and should not be interpreted as a proof of stochastic domination for arbitrary \(n\).