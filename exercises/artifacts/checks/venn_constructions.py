"""Numerical checks of the two constructions in §2, exercises 2 and 3.

Exercise 2: n convex regions realising all 2^n membership states.
    Put 2^n points q_alpha on a circle and let A_i be the eps-neighbourhood of
    conv{q_alpha : alpha_i = 1}.  Check that q_alpha has code alpha and that a
    small disc around q_alpha lies in the constituent K_alpha.

Exercise 3: n congruent regions (translates S + v_i) realising all 2^n states.
    Points x_alpha in a disc of radius R, shifts v_i = (3R i, 0).  S must contain
    P+ = {x_alpha - v_i : alpha_i = 1} and avoid P- = {x_alpha - v_i : alpha_i = 0};
    here S is the union of small discs around P+ (the connecting corridors of the
    solution are not modelled: they only make S connected and stay away from P-).

Run:  python3 venn_constructions.py
"""

import math
import random
from itertools import product


def codes(n):
    return list(product((0, 1), repeat=n))


# ---------- geometry helpers ----------
def sub(p, q):
    return (p[0] - q[0], p[1] - q[1])


def cross(o, a, b):
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])


def dist_seg(p, a, b):
    ax, ay = sub(b, a)
    px, py = sub(p, a)
    L = ax * ax + ay * ay
    t = 0.0 if L == 0 else max(0.0, min(1.0, (px * ax + py * ay) / L))
    return math.hypot(px - t * ax, py - t * ay)


def dist_convex(p, poly):
    """Distance from p to the convex polygon poly (vertices in CCW order); 0 inside."""
    if len(poly) == 1:
        return math.hypot(*sub(p, poly[0]))
    if len(poly) == 2:
        return dist_seg(p, poly[0], poly[1])
    inside = all(cross(poly[k], poly[(k + 1) % len(poly)], p) >= 0 for k in range(len(poly)))
    if inside:
        return 0.0
    return min(dist_seg(p, poly[k], poly[(k + 1) % len(poly)]) for k in range(len(poly)))


def ring(c, r, m=24):
    return [c] + [(c[0] + r * math.cos(2 * math.pi * j / m), c[1] + r * math.sin(2 * math.pi * j / m))
                  for j in range(m)]


# ---------- exercise 2 ----------
def convex_case(n):
    cs = codes(n)
    N = len(cs)
    q = {a: (math.cos(2 * math.pi * k / N), math.sin(2 * math.pi * k / N)) for k, a in enumerate(cs)}
    # vertices of conv{q_alpha: alpha_i = 1}, in CCW (angle) order
    hulls = [[q[a] for a in cs if a[i] == 1] for i in range(n)]
    # eps: one third of the smallest distance from an "outside" point to a hull
    eps = min(dist_convex(q[b], hulls[i]) for i in range(n) for b in cs if b[i] == 0) / 3
    member = lambda p, i: dist_convex(p, hulls[i]) <= eps
    ok_codes = all(tuple(int(member(q[a], i)) for i in range(n)) == a for a in cs)
    ok_discs = all(tuple(int(member(p, i)) for i in range(n)) == a
                   for a in cs for p in ring(q[a], eps / 2))
    return ok_codes and ok_discs, eps


# ---------- exercise 3 ----------
def translates_case(n, seed=0):
    rnd = random.Random(seed)
    R = 1.0
    cs = codes(n)
    x = {}
    for a in cs:                      # random distinct points in the disc of radius R
        while True:
            p = (rnd.uniform(-R, R), rnd.uniform(-R, R))
            if math.hypot(*p) < R and all(math.hypot(*sub(p, y)) > 1e-6 for y in x.values()):
                x[a] = p
                break
    v = [(3 * R * (i + 1), 0.0) for i in range(n)]
    Pp = [sub(x[a], v[i]) for a in cs for i in range(n) if a[i] == 1]
    Pm = [sub(x[a], v[i]) for a in cs for i in range(n) if a[i] == 0]
    allpts = [sub(x[a], v[i]) for a in cs for i in range(n)]
    distinct = min(math.hypot(*sub(p, r)) for k, p in enumerate(allpts) for r in allpts[k + 1:])
    delta = min(math.hypot(*sub(p, r)) for p in Pp for r in Pm)
    rad = delta / 3

    def in_S(p):
        return any(math.hypot(*sub(p, c)) < rad for c in Pp)

    def code_of(p):
        return tuple(int(in_S(sub(p, v[i]))) for i in range(n))

    ok_codes = all(code_of(x[a]) == a for a in cs)
    ok_discs = all(code_of(p) == a for a in cs for p in ring(x[a], rad / 2))
    return ok_codes and ok_discs and distinct > 0, delta, distinct


def main():
    for n in range(1, 9):
        ok, eps = convex_case(n)
        print(("OK   " if ok else "FAIL ")
              + f"ex.2: {n} convex regions realise all {2 ** n} states (eps = {eps:.3g})")
        if not ok:
            raise SystemExit(1)
    for n in range(1, 7):
        ok, delta, distinct = translates_case(n)
        print(("OK   " if ok else "FAIL ")
              + f"ex.3: {n} translates realise all {2 ** n} states "
                f"(min |P+ - P-| = {delta:.3g}, all n*2^n points distinct)")
        if not ok:
            raise SystemExit(1)
    # n circles give at most n^2 - n + 2 regions, which is < 2^n from n = 4 on
    print("ex.3: n^2-n+2 vs 2^n:", [(n, n * n - n + 2, 2 ** n) for n in range(1, 7)])
    print("\nall construction checks passed")


if __name__ == "__main__":
    main()
