"""Independent real exterior-algebra audit; no STW formula is used.

Set dz_r=dx_r+i dy_r and gamma=2 sum dx_r wedge dy_r.
The real metric is 2 I, hence on degree k forms its Hodge star is
2**(n-k) times the ordinary Euclidean real Hodge star. All arithmetic
below is with exactly representable Gaussian integers and dyadic values.
"""
import itertools
import json
import math
from pathlib import Path


def add(*forms):
    out = {}
    for form in forms:
        for inds, value in form.items():
            out[inds] = out.get(inds, 0) + value
    return {inds: value for inds, value in out.items() if value != 0}


def scale(form, scalar):
    return {inds: value * scalar for inds, value in form.items() if value * scalar != 0}


def parity(inds):
    return (-1) ** sum(a > b for k, a in enumerate(inds) for b in inds[k + 1 :])


def wedge(left, right):
    out = {}
    for ii, a in left.items():
        for jj, b in right.items():
            if set(ii).intersection(jj):
                continue
            kk = tuple(sorted(ii + jj))
            out[kk] = out.get(kk, 0) + a * b * parity(ii + jj)
    return {inds: value for inds, value in out.items() if value != 0}


def star(form, n):
    out = {}
    for inds, value in form.items():
        comp = tuple(r for r in range(2 * n) if r not in inds)
        out[comp] = value * parity(inds + comp) * 2 ** (n - len(inds))
    return out


def delta3(upper, lower):
    return sum(
        parity(perm) * math.prod(int(upper[r] == lower[perm[r]]) for r in range(3))
        for perm in itertools.permutations(range(3))
    )


def six_bracket(n, i, j, p, b, c, a):
    # T has its sole independent entry T_bcbar a=1 and T_cbbar a=-1.
    def torsion(x, y, z):
        return int((x, y, z) == (b, c, a)) - int((x, y, z) == (c, b, a))

    return (
        int(i == j) * sum(torsion(p, k, k) for k in range(n))
        - int(p == i) * sum(torsion(j, k, k) for k in range(n))
        - torsion(p, j, i)
    )


results = []
for n in range(2, 7):
    dz = [{(2 * r,): 1, (2 * r + 1,): 1j} for r in range(n)]
    db = [{(2 * r,): 1, (2 * r + 1,): -1j} for r in range(n)]
    basis = {(i, j): scale(wedge(dz[i], db[j]), 1j) for i in range(n) for j in range(n)}
    gamma = add(*(basis[i, i] for i in range(n)))
    powers = [{(): 1}]
    for degree in range(1, n):
        powers.append(wedge(powers[-1], gamma))
    assert star(powers[n - 1], n) == scale(gamma, math.factorial(n - 1))

    # star(H wedge gamma^(n-2))=(n-2)! ((tr H)gamma-H).
    p_checks = 0
    for i, j in itertools.product(range(n), repeat=2):
        actual = star(wedge(basis[i, j], powers[n - 2]), n)
        expected = scale(add(scale(gamma, int(i == j)), scale(basis[i, j], -1)), math.factorial(n - 2))
        assert actual == expected, ("P identity", n, i, j)
        p_checks += 1

    hodge_checks = 0
    if n >= 3:
        for p, a, b, c in itertools.product(range(n), repeat=4):
            form = wedge(wedge(wedge(wedge(dz[p], dz[a]), db[b]), db[c]), powers[n - 3])
            actual = star(form, n)
            expected = add(*(
                scale(basis[i, j], math.factorial(n - 3) * delta3((p, a, j), (b, c, i)))
                for i, j in itertools.product(range(n), repeat=2)
            ))
            assert actual == expected, ("Hodge contraction", n, p, a, b, c)
            hodge_checks += 1

    torsion_checks = 0
    zero_checks = 0
    for b, c in itertools.combinations(range(n), 2):
        for a, p, i, j in itertools.product(range(n), repeat=4):
            determinant_sum = delta3((p, a, j), (b, c, i)) - delta3((p, a, j), (c, b, i))
            bracket = six_bracket(n, i, j, p, b, c, a)
            assert determinant_sum == 2 * bracket, ("six terms", n, p, a, b, c, i, j)
            if p == j:
                assert bracket == 0, ("forbidden holomorphic coefficient", n, i, j)
                zero_checks += 1
            if i == j:
                expected = 0
                for k in range(n):
                    if p != i and k != i:
                        expected += int((p, k, k) == (b, c, a)) - int((p, k, k) == (c, b, a))
                assert bracket == expected, ("diagonal exclusion", n, i, p)
                zero_checks += 1
            if n == 2:
                assert bracket == 0, ("dimension two cancellation", i, j, p, a, b, c)
            torsion_checks += 1
    results.append({"n": n, "star_normalization": "passed", "P_basis_checks": p_checks,
                    "Hodge_contraction_monomials": hodge_checks,
                    "independent_torsion_coefficient_checks": torsion_checks,
                    "vanishing_coefficient_checks": zero_checks, "status": "passed"})

payload = {"method": "Direct real-basis wedge algebra and metric Hodge star; exact dyadic equality without numerical tolerances", "dimensions": results,
           "scope": "Finite-dimensional independent corroboration. The report also gives the general-n exterior-algebra proof."}
Path(__file__).with_name("exterior_audit.json").write_text(json.dumps(payload, indent=2) + "\n")
print(json.dumps(payload, indent=2))
