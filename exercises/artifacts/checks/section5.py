"""Checks for §5 (pp. 29-33): the text and the exercises.

text:  (1.17) turns the scheme of Fig. 11a into w1 = x + xy + z^t;
       the two schemes of Fig. 12 compute x^3 + 2x^2 + 3x + 4 with 4 and 2
       multiplications; the formula printed for Fig. 12b, ((x+2)+3)x + 4, is
       a different polynomial.
ex. 2: substituting power series (exact rational arithmetic):
       e^{sin x} = 1 + x + x^2/2 - x^4/8 - x^5/15 + ...;
       1/(1-y) with y = 2x has coefficients 2^k (radius 1/2).
ex. 4: every function of the system (1.9) is expressed through
       H = {x+y, xy, x^y, ln x, sin x, arcsin x} and constants, with the
       same domain; checked at many points, including points outside the
       domains (both sides must be undefined there).
ex. 5: the scheme phi1(x, phi2(y, z)) cannot give f = xy + z: a sample of
       pairs (y,z) != (y',z') shows that u = phi2(y,z) would have to separate
       all points of the plane (u(y,z) = u(y',z') forces f(0,.)=f(0,.) and
       f(1,.)=f(1,.), i.e. z = z', y + z = y' + z');
       one structure on the whole R^n: for f = (x1 - 3x2) e^{x1^2+x2^2} the
       damping factor v(t) = (1+|t|)(1+m(|t|)) gives |f/(v(x1)v(x2))| <
       1/(1 + max|x_p|), also at points coming from the edge of the square.
ex. 6: counting derivatives: the table for phi1(x, phi2(y,z)), the threshold
       s*C(N+2,2) < C(N+3,3) <=> N + 3 > 3s, the same for k < n inputs;
       lemma 2 run on examples: monomials in c_j = P_j(u) (one variable u)
       become linearly dependent and give an equation R(c) = 0 (exact
       rational linear algebra), e.g. c1^3 - c2^2 = 0 for c1 = u^2, c2 = u^3.

Run:  python3 section5.py
"""

import math
import random
from fractions import Fraction

rnd = random.Random(5)


def report(title, ok):
    print(("OK   " if ok else "FAIL ") + title)
    if not ok:
        raise SystemExit(1)


# ------------------------------------------------------------------ text
def check_text():
    def w1_scheme(f, phi, psi):
        return lambda x, y, z, t: f(x, phi(x, y), psi(z, t))

    w1 = w1_scheme(lambda a, b, c: a + b + c, lambda a, b: a * b, lambda a, b: a ** b)
    ok = all(abs(w1(x, y, z, t) - (x + x * y + z ** t)) < 1e-9
             for x, y, z, t in ((rnd.uniform(-2, 2), rnd.uniform(-2, 2),
                                 rnd.uniform(0.1, 3), rnd.uniform(-2, 2)) for _ in range(500)))
    report("(1.17): the scheme of Fig. 11a with f=x+y+z, phi=xy, psi=z^t gives x + xy + z^t", ok)

    # Fig. 12 a: blocks  m1 = x*x, m2 = x*m1, m3 = m1*2, a1 = m2+m3, m4 = 3*x, a2 = m4+4, a3 = a1+a2
    def scheme_a(x):
        mults = 0
        m1 = x * x; mults += 1
        m2 = x * m1; mults += 1
        m3 = m1 * 2; mults += 1
        a1 = m2 + m3
        m4 = 3 * x; mults += 1
        a2 = m4 + 4
        return a1 + a2, mults, 3          # 3 adders

    # Fig. 12 b: a1 = x+2, m1 = x*a1, a2 = m1+3, m2 = x*a2, a3 = m2+4
    def scheme_b(x):
        mults = 0
        a1 = x + 2
        m1 = x * a1; mults += 1
        a2 = m1 + 3
        m2 = x * a2; mults += 1
        return m2 + 4, mults, 3

    p = lambda x: x ** 3 + 2 * x ** 2 + 3 * x + 4
    xs = [Fraction(k, 7) for k in range(-30, 31)]
    ok_a = all(scheme_a(x)[0] == p(x) for x in xs)
    ok_b = all(scheme_b(x)[0] == p(x) for x in xs)
    report("Fig. 12a computes x^3+2x^2+3x+4 with 4 multipliers and 3 adders",
           ok_a and scheme_a(1)[1:] == (4, 3))
    report("Fig. 12b computes the same polynomial with 2 multipliers and 3 adders",
           ok_b and scheme_b(1)[1:] == (2, 3))
    printed = lambda x: ((x + 2) + 3) * x + 4
    report("printed formula ((x+2)+3)x+4 = x^2+5x+4 is a different polynomial",
           all(printed(x) == x * x + 5 * x + 4 for x in xs) and any(printed(x) != p(x) for x in xs))


# ------------------------------------------------------------------ ex. 2
N = 12   # number of coefficients kept


def mul(a, b):
    c = [Fraction(0)] * N
    for i, ai in enumerate(a):
        if ai:
            for j, bj in enumerate(b[:N - i]):
                c[i + j] += ai * bj
    return c


def compose(outer, inner):
    """outer(inner(x)) for formal series, inner[0] must be 0."""
    assert inner[0] == 0
    res = [Fraction(0)] * N
    power = [Fraction(1)] + [Fraction(0)] * (N - 1)
    for k in range(N):
        for i in range(N):
            res[i] += outer[k] * power[i]
        power = mul(power, inner)
    return res


def check_ex2():
    fact = [math.factorial(k) for k in range(N)]
    exp_s = [Fraction(1, fact[k]) for k in range(N)]
    sin_s = [Fraction(0)] * N
    for k in range(N):
        if k % 2 == 1:
            sin_s[k] = Fraction((-1) ** (k // 2), fact[k])
    e_sin = compose(exp_s, sin_s)
    expected = [1, 1, Fraction(1, 2), 0, Fraction(-1, 8), Fraction(-1, 15)]
    report("ex.2: e^{sin x} = 1 + x + x^2/2 + 0x^3 - x^4/8 - x^5/15 + ... (formal substitution)",
           e_sin[:6] == [Fraction(c) for c in expected])
    # numeric agreement of the partial sum with e^{sin x} for small x
    x = 0.1
    approx = sum(float(c) * x ** k for k, c in enumerate(e_sin))
    report("ex.2: the substituted series sums to e^{sin x} at x = 0.1",
           abs(approx - math.exp(math.sin(x))) < 1e-12)
    geo = [Fraction(1)] * N
    two_x = [Fraction(0), Fraction(2)] + [Fraction(0)] * (N - 2)
    report("ex.2: 1/(1-y) with y = 2x gives coefficients 2^k (radius 1/2, not 1)",
           compose(geo, two_x) == [Fraction(2) ** k for k in range(N)])


# ------------------------------------------------------------------ ex. 4
class Undefined(Exception):
    pass


def pw(x, y):
    """two-place power x^y: x > 0 any y; x = 0 only for y > 0 (value 0)."""
    if x > 0:
        return math.exp(y * math.log(x))
    if x == 0 and y > 0:
        return 0.0
    raise Undefined


def ln(x):
    if x > 0:
        return math.log(x)
    raise Undefined


def asin(x):
    if -1 <= x <= 1:
        return math.asin(x)
    raise Undefined


def H_recip(y):          # 1/y = y * (y^2)^(-1)
    return y * pw(y * y, -1)


H_versions = {
    "x - y": lambda x, y: x + (-1) * y,
    "x / y": lambda x, y: x * H_recip(y),
    "x^3": lambda x: x * x * x,
    "x^(-2)": lambda x: H_recip(x) * H_recip(x),
    "x^(1/2)": lambda x: pw(x, 0.5),
    "x^(-1/2)": lambda x: pw(x, -0.5),
    "x^pi": lambda x: pw(x, math.pi),
    "a^x (a=2.5)": lambda x: pw(2.5, x),
    "a^x (a=0.3)": lambda x: pw(0.3, x),
    "e^x": lambda x: pw(math.e, x),
    "log_a x (a=10)": lambda x: (1 / math.log(10)) * ln(x),
    "log_a x (a=0.5)": lambda x: (1 / math.log(0.5)) * ln(x),
    "cos x": lambda x: math.sin(x + math.pi / 2),
    "tg x": lambda x: math.sin(x) * H_recip(math.sin(x + math.pi / 2)),
    "ctg x": lambda x: math.sin(x + math.pi / 2) * H_recip(math.sin(x)),
    "arccos x": lambda x: math.pi / 2 + (-1) * asin(x),
    "arctg x": lambda x: asin(x * pw(1 + x * x, -0.5)),
    "arcctg x": lambda x: math.pi / 2 + (-1) * asin(x * pw(1 + x * x, -0.5)),
}


def ref_power(x, a):
    if float(a).is_integer():
        if a < 0 and x == 0:
            raise Undefined
        return x ** a
    if x > 0:
        return x ** a
    if x == 0 and a > 0:
        return 0.0
    raise Undefined


REF = {
    "x - y": lambda x, y: x - y,
    "x / y": lambda x, y: (x / y) if y != 0 else (_ for _ in ()).throw(Undefined()),
    "x^3": lambda x: ref_power(x, 3),
    "x^(-2)": lambda x: ref_power(x, -2),
    "x^(1/2)": lambda x: ref_power(x, 0.5),
    "x^(-1/2)": lambda x: ref_power(x, -0.5),
    "x^pi": lambda x: ref_power(x, math.pi),
    "a^x (a=2.5)": lambda x: 2.5 ** x,
    "a^x (a=0.3)": lambda x: 0.3 ** x,
    "e^x": lambda x: math.exp(x),
    "log_a x (a=10)": lambda x: math.log10(x) if x > 0 else (_ for _ in ()).throw(Undefined()),
    "log_a x (a=0.5)": lambda x: math.log(x, 0.5) if x > 0 else (_ for _ in ()).throw(Undefined()),
    "cos x": lambda x: math.cos(x),
    "tg x": lambda x: math.tan(x),
    "ctg x": lambda x: (1 / math.tan(x)) if math.sin(x) != 0 else (_ for _ in ()).throw(Undefined()),
    "arccos x": lambda x: math.acos(x) if -1 <= x <= 1 else (_ for _ in ()).throw(Undefined()),
    "arctg x": lambda x: math.atan(x),
    "arcctg x": lambda x: math.pi / 2 - math.atan(x),
}


def evaluate(f, args):
    try:
        return f(*args)
    except (Undefined, ZeroDivisionError, ValueError):
        return None


def check_ex4():
    special = [0.0, 1.0, -1.0, 0.5, -0.5, 2.0, -2.0, 1e-9, -1e-9]
    for name, h in H_versions.items():
        ref = REF[name]
        arity = h.__code__.co_argcount
        pts = []
        for _ in range(3000):
            pts.append(tuple(rnd.uniform(-5, 5) for _ in range(arity)))
        for a in special:
            for b in special[:4]:
                pts.append((a,) if arity == 1 else (a, b))
        ok = True
        for p in pts:
            u, v = evaluate(h, p), evaluate(ref, p)
            if (u is None) != (v is None):
                ok = False
                print("   domain mismatch for", name, "at", p, u, v)
                break
            if u is not None and abs(u - v) > 1e-9 * max(1.0, abs(v)):
                ok = False
                print("   value mismatch for", name, "at", p, u, v)
                break
        report(f"ex.4: {name} is realised through H with the same domain", ok)


# ------------------------------------------------------------------ ex. 5
def check_ex5():
    f = lambda x, y, z: x * y + z
    # f(0,y,z) = z and f(1,y,z) = y + z determine (y, z): the map (y,z) -> (f(0,y,z), f(1,y,z))
    # is injective, so any u with f(x,y,z) = Phi(x, u(y,z)) must be injective in (y, z).
    ok = True
    for _ in range(2000):
        p = (rnd.uniform(-3, 3), rnd.uniform(-3, 3))
        q = (rnd.uniform(-3, 3), rnd.uniform(-3, 3))
        if p != q and (f(0, *p), f(1, *p)) == (f(0, *q), f(1, *q)):
            ok = False
    report("ex.5: for f = xy + z the values at x = 0 and x = 1 separate all points (y, z)", ok)
    # a continuous function on a circle takes some value twice (illustration with a sample u)
    u = lambda a, b: a + 0.3 * b * b
    th = [2 * math.pi * k / 4000 for k in range(4000)]
    vals = [u(math.cos(t), math.sin(t)) for t in th]
    c = (max(vals) + min(vals)) / 2
    crossings = sum(1 for k in range(len(vals)) if (vals[k] - c) * (vals[(k + 1) % len(vals)] - c) < 0)
    report("ex.5: a sample continuous u on the unit circle crosses its mid level at least twice",
           crossings >= 2)


# ------------------------------------------------------------------ ex. 5, whole R^n
def check_ex5_whole_space():
    # f(x1, x2) = (x1 - 3 x2) exp(x1^2 + x2^2); on the box max|x_p| <= R the maximum
    # of |f| is m(R) = 4R exp(2R^2), attained at (R, -R).
    f = lambda x1, x2: (x1 - 3 * x2) * math.exp(x1 * x1 + x2 * x2)
    m = lambda R: 4 * R * math.exp(2 * R * R)
    ok = True
    for R in (0.25, 0.5, 1.0, 2.0, 3.0):
        for _ in range(3000):
            x1, x2 = rnd.uniform(-R, R), rnd.uniform(-R, R)
            if abs(f(x1, x2)) > m(R) * (1 + 1e-12):
                ok = False
        if abs(abs(f(R, -R)) - m(R)) > 1e-9 * m(R):
            ok = False
    report("ex.5: m(R) = 4R e^{2R^2} is the maximum of |f| on the box max|x_p| <= R", ok)

    def log1p_m(R):                      # log(1 + m(R)) without overflow
        if R == 0:
            return 0.0
        lm = math.log(4 * R) + 2 * R * R
        return lm + math.log1p(math.exp(-lm)) if lm > 0 else math.log1p(math.exp(lm))

    def log_v(t):                        # v(t) = (1 + |t|)(1 + m(|t|))
        return math.log1p(abs(t)) + log1p_m(abs(t))

    def log_abs_g(x1, x2):               # g = f / (v(x1) v(x2))
        a = abs(x1 - 3 * x2)
        if a == 0:
            return -math.inf
        return math.log(a) + x1 * x1 + x2 * x2 - log_v(x1) - log_v(x2)

    pts = [(rnd.uniform(-10, 10), rnd.uniform(-10, 10)) for _ in range(20000)]
    hinv = lambda s: math.tan(math.pi * (s - 0.5))
    for _ in range(5000):               # points y near the edge of the unit square
        y1 = rnd.choice([rnd.uniform(1e-7, 1e-2), rnd.uniform(1 - 1e-2, 1 - 1e-7)])
        y2 = rnd.uniform(1e-7, 1 - 1e-7)
        pts.append((hinv(y1), hinv(y2)) if rnd.random() < 0.5 else (hinv(y2), hinv(y1)))
    ok = all(log_abs_g(x1, x2) < -math.log1p(max(abs(x1), abs(x2))) for x1, x2 in pts)
    report("ex.5: |g(x)| < 1/(1 + max|x_p|), also for x = h^{-1}(y) with y near the edge", ok)


# ------------------------------------------------------------------ ex. 6
def poly_mul(a, b):
    c = [Fraction(0)] * (len(a) + len(b) - 1)
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            c[i + j] += ai * bj
    return c


def poly_pow(a, k):
    r = [Fraction(1)]
    for _ in range(k):
        r = poly_mul(r, a)
    return r


def left_kernel_vector(rows):
    """a nonzero rational vector lam with sum_i lam_i * rows[i] = 0, or None."""
    n, width = len(rows), max(len(r) for r in rows)
    # columns of the transposed system: unknowns lam_0..lam_{n-1}
    mat = [[(rows[i][j] if j < len(rows[i]) else Fraction(0)) for i in range(n)] for j in range(width)]
    pivots, r = [], 0
    for c in range(n):
        piv = next((i for i in range(r, width) if mat[i][c] != 0), None)
        if piv is None:
            continue
        mat[r], mat[piv] = mat[piv], mat[r]
        inv = 1 / mat[r][c]
        mat[r] = [v * inv for v in mat[r]]
        for i in range(width):
            if i != r and mat[i][c] != 0:
                fac = mat[i][c]
                mat[i] = [vi - fac * vr for vi, vr in zip(mat[i], mat[r])]
        pivots.append(c)
        r += 1
    free = [c for c in range(n) if c not in pivots]
    if not free:
        return None
    lam = [Fraction(0)] * n
    lam[free[0]] = Fraction(1)
    for row, c in zip(mat, pivots):
        lam[c] = -row[free[0]]
    return lam


def relation_for(P1, P2):
    """lemma 2 with D = 1, E = 2: find a nonzero R(t1,t2) with R(P1(u), P2(u)) = 0."""
    K = max(len(P1), len(P2)) - 1
    for d in range(1, 40):
        monos = [(a, b) for a in range(d + 1) for b in range(d + 1 - a)]
        if len(monos) <= K * d + 1:      # not yet more monomials than the dimension
            continue
        rows = [poly_mul(poly_pow(P1, a), poly_pow(P2, b)) for a, b in monos]
        lam = left_kernel_vector(rows)
        if lam is not None:
            return d, {mono: l for mono, l in zip(monos, lam) if l != 0}
    return None, None


def check_ex6():
    from math import comb
    top = [2 * comb(N + 2, 2) for N in range(7)]
    bottom = [comb(N + 3, 3) for N in range(7)]
    report("ex.6: table for phi1(x, phi2(y,z)): 2C(N+2,2) = 2,6,12,20,30,42,56; C(N+3,3) = 1,4,10,20,35,56,84",
           top == [2, 6, 12, 20, 30, 42, 56] and bottom == [1, 4, 10, 20, 35, 56, 84])
    ok = all((s * comb(N + 2, 2) < comb(N + 3, 3)) == (N + 3 > 3 * s)
             for s in range(1, 80) for N in range(400))
    report("ex.6: s*C(N+2,2) < C(N+3,3) exactly when N + 3 > 3s (s < 80, N < 400)", ok)
    ok = all(any(s * comb(N + k, k) < comb(N + n, n) for N in range(5000))
             for n in range(2, 7) for k in range(1, n) for s in (1, 5, 20, 100))
    report("ex.6: for k < n and s = 1, 5, 20, 100 some N gives s*C(N+k,k) < C(N+n,n)", ok)

    F = Fraction
    examples = [
        ("c1 = u^2, c2 = u^3", [F(0), F(0), F(1)], [F(0), F(0), F(0), F(1)]),
        ("c1 = u + u^2, c2 = u^3 - u", [F(0), F(1), F(1)], [F(0), F(-1), F(0), F(1)]),
        ("c1 = 2u - 1, c2 = u^2/3 + u", [F(-1), F(2)], [F(0), F(1), F(1, 3)]),
    ]
    for name, P1, P2 in examples:
        d, R = relation_for(P1, P2)
        ok = R is not None
        if ok:
            for _ in range(50):
                u = F(rnd.randint(-50, 50), rnd.randint(1, 20))
                c1 = sum(cf * u ** i for i, cf in enumerate(P1))
                c2 = sum(cf * u ** i for i, cf in enumerate(P2))
                if sum(l * c1 ** a * c2 ** b for (a, b), l in R.items()) != 0:
                    ok = False
        report(f"ex.6, lemma 2: {name} satisfy a nonzero rational equation R(c1, c2) = 0"
               f" (found among monomials of degree <= {d})", ok)
    d, R = relation_for([F(0), F(0), F(1)], [F(0), F(0), F(0), F(1)])
    norm = {k: v / R[(3, 0)] for k, v in R.items()} if R and (3, 0) in R else None
    report("ex.6, lemma 2: for c1 = u^2, c2 = u^3 the equation found is c1^3 - c2^2 = 0",
           norm == {(3, 0): 1, (0, 2): -1})


def main():
    check_text()
    check_ex2()
    check_ex4()
    check_ex5()
    check_ex5_whole_space()
    check_ex6()
    print("\nall §5 checks passed")


if __name__ == "__main__":
    main()
