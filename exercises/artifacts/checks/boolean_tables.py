"""Brute-force checks for the §3 exercises (p. 21, «Принцип двойственности»).

A formula F(A_1, ..., A_n) is identified with its truth table f: {0,1}^n -> {0,1}
(see the solution of exercise 1, §3).  A table is stored as a tuple of 2^n bits,
indexed by the code alpha read as a binary number with alpha_1 as the most
significant bit.  Complementing all arguments maps alpha to its bitwise
complement; the dual table is f*(alpha) = not f(complement alpha).

Run:  python3 boolean_tables.py
"""

from itertools import product
from math import comb

FULL = {}


def codes(n):
    return list(product((0, 1), repeat=n))


def index(alpha):
    i = 0
    for a in alpha:
        i = 2 * i + a
    return i


def comp(alpha):
    return tuple(1 - a for a in alpha)


def all_tables(n):
    """All 2^(2^n) truth tables of n arguments (only for n <= 4)."""
    return list(product((0, 1), repeat=2 ** n))


def dual(f, n):
    cs = codes(n)
    return tuple(1 - f[index(comp(a))] for a in cs)


def is_selfdual(f, n):
    return dual(f, n) == f


def is_even(f, n):
    return all(f[index(a)] == f[index(comp(a))] for a in codes(n))


def lam(f):
    return sum(f)


def depends_on(f, n, i):
    for a in codes(n):
        b = list(a)
        b[i] = 1 - b[i]
        if f[index(a)] != f[index(tuple(b))]:
            return True
    return False


def essential(f, n):
    return [i for i in range(n) if depends_on(f, n, i)]


def table_of(func, n):
    return tuple(int(bool(func(*a))) for a in codes(n))


def selfdual_tables(n):
    """Enumerate self-dual tables directly: choose f on one code of each pair."""
    cs = codes(n)
    reps = [a for a in cs if a[0] == 0]          # one representative per pair
    out = []
    for vals in product((0, 1), repeat=len(reps)):
        f = [None] * (2 ** n)
        for a, v in zip(reps, vals):
            f[index(a)] = v
            f[index(comp(a))] = 1 - v
        out.append(tuple(f))
    return out


def report(title, ok):
    print(("OK   " if ok else "FAIL ") + title)
    if not ok:
        raise SystemExit(1)


def main():
    # ---------------- exercise 1 (n = 2) ----------------
    sd2 = [f for f in all_tables(2) if is_selfdual(f, 2)]
    names = {
        table_of(lambda a, b: a, 2): "A",
        table_of(lambda a, b: b, 2): "B",
        table_of(lambda a, b: 1 - a, 2): "not A",
        table_of(lambda a, b: 1 - b, 2): "not B",
    }
    print("ex.1: self-dual 2-place tables:", [names.get(f, f) for f in sd2])
    report("ex.1: exactly A, B, not A, not B; none depends on both arguments",
           sorted(names.get(f, "?") for f in sd2) == sorted(names.values())
           and all(len(essential(f, 2)) == 1 for f in sd2))

    # ---------------- exercises 2, 5: mu(n) ----------------
    for n in range(1, 5):
        mu = sum(1 for f in all_tables(n) if is_selfdual(f, n))
        report(f"ex.2/5: mu({n}) = {mu} = 2^(2^{n-1})", mu == 2 ** (2 ** (n - 1)))
    report("ex.5: direct enumeration gives the same mu(5) = 65536",
           len(set(selfdual_tables(5))) == 65536)

    # ex.2: generation F = (A1 & G) | (~A1 & G*), G arbitrary of n-1 args
    for n in range(2, 5):
        gen = set()
        for g in all_tables(n - 1):
            gs = dual(g, n - 1)
            f = tuple(g[index(a[1:])] if a[0] else gs[index(a[1:])] for a in codes(n))
            gen.add(f)
        sd = {f for f in all_tables(n) if is_selfdual(f, n)}
        report(f"ex.2: (A1&G)|(~A1&G*) gives exactly the self-dual tables, bijectively (n={n})",
               gen == sd and len(gen) == 2 ** (2 ** (n - 1)))

    # ex.2: classification for n = 3
    sd3 = [f for f in all_tables(3) if is_selfdual(f, 3)]
    degenerate = [f for f in sd3 if len(essential(f, 3)) <= 1]
    maj = set()
    for s in product((0, 1), repeat=3):
        def m(a, b, c, s=s):
            x, y, z = a ^ (1 - s[0]), b ^ (1 - s[1]), c ^ (1 - s[2])
            return (x & y) | (x & z) | (y & z)
        maj.add(table_of(m, 3))
    parity = {table_of(lambda a, b, c: a ^ b ^ c, 3), table_of(lambda a, b, c: 1 - (a ^ b ^ c), 3)}
    report("ex.2: n=3 -> 16 = 6 degenerate + 8 majorities + 2 parities",
           len(sd3) == 16 and len(degenerate) == 6 and maj <= set(sd3) and len(maj) == 8
           and parity <= set(sd3) and len(set(degenerate) | maj | parity) == 16)

    # ---------------- exercise 3 ----------------
    for n in range(1, 5):
        ok = True
        cnt = 0
        for f in all_tables(n):
            fs = dual(f, n)
            cap_empty = all(x & y == 0 for x, y in zip(f, fs))
            cup_full = all(x | y == 1 for x, y in zip(f, fs))
            dual_is_comp = all(y == 1 - x for x, y in zip(f, fs))
            ev = is_even(f, n)
            ok &= (cap_empty == cup_full == dual_is_comp == ev)
            cnt += ev
        report(f"ex.3: F&F*=0 <=> F|F*=I <=> F*=~F <=> even (all tables, n={n}); "
               f"{cnt} even = 2^(2^{n-1})", ok and cnt == 2 ** (2 ** (n - 1)))
    for n in range(2, 5):
        closed = set()
        for h in all_tables(n - 1):
            closed.add(tuple(h[index(tuple(a[0] ^ a[i] for i in range(1, n)))] for a in codes(n)))
        ev = {f for f in all_tables(n) if is_even(f, n)}
        report(f"ex.3: H(A1^A2, ..., A1^An) gives exactly the even tables (n={n})",
               closed == ev and len(closed) == 2 ** (2 ** (n - 1)))
    # small cases listed in the solution
    ev1 = [f for f in all_tables(1) if is_even(f, 1)]
    report("ex.3: n=1 -> even formulas are exactly the empty set and I", sorted(ev1) == [(0, 0), (1, 1)])

    # ---------------- exercise 4 ----------------
    for n in range(3, 9):
        def Fn(*a):
            p = all(a[1:])
            u = any(a[1:])
            return (a[0] and p) or ((not a[0]) and u)
        f = table_of(Fn, n)
        report(f"ex.4: F_{n} is self-dual and depends on all {n} arguments",
               is_selfdual(f, n) and essential(f, n) == list(range(n)))
    f2 = table_of(lambda a, b: (a and b) or ((not a) and b), 2)
    report("ex.4: for n=2 the same formula degenerates to A_2", f2 == table_of(lambda a, b: b, 2))
    for n in (3, 5, 7):
        f = table_of(lambda *a: sum(a) > n // 2, n)
        report(f"ex.4: majority of {n} sets is self-dual and strictly {n}-place",
               is_selfdual(f, n) and essential(f, n) == list(range(n)))

    # ---------------- exercise 6: tau(n) ----------------
    tau_bf = {}
    for n in range(1, 6):
        tabs = selfdual_tables(n)
        tau_bf[n] = sum(1 for f in tabs if len(essential(f, n)) == n)
    tau = {0: 0}
    for n in range(1, 6):
        tau[n] = 2 ** (2 ** (n - 1)) - sum(comb(n, k) * tau[k] for k in range(n))
    print("ex.6: tau by brute force:", [tau_bf[n] for n in range(1, 6)],
          " by recursion:", [tau[n] for n in range(1, 6)])
    report("ex.6: tau = 2, 0, 10, 208, 64386 (brute force = recursion, n = 1..5)",
           [tau_bf[n] for n in range(1, 6)] == [2, 0, 10, 208, 64386]
           and all(tau_bf[n] == tau[n] for n in range(1, 6)))
    alt = {n: sum((-1) ** (n - k) * comb(n, k) * (2 ** (2 ** (k - 1)) if k else 0)
                  for k in range(n + 1)) for n in range(1, 6)}
    report("ex.6: binomial inversion tau(n) = sum (-1)^(n-k) C(n,k) mu(k) agrees",
           all(alt[n] == tau[n] for n in range(1, 6)))

    # ---------------- exercise 7 ----------------
    for n in range(1, 5):
        tabs = all_tables(n)
        ok = all(lam(f) + lam(dual(f, n)) == 2 ** n for f in tabs)
        bal = [f for f in tabs if lam(f) == lam(dual(f, n))]
        report(f"ex.7: lambda(F)+lambda(F*)=2^n for all F; #balanced = C(2^n,2^(n-1)) = "
               f"{comb(2 ** n, 2 ** (n - 1))} (n={n})",
               ok and len(bal) == comb(2 ** n, 2 ** (n - 1))
               and all(lam(f) == 2 ** (n - 1) for f in bal))
    tabs3 = all_tables(3)
    bal3 = [f for f in tabs3 if lam(f) == 4]
    sd = [f for f in bal3 if is_selfdual(f, 3)]
    ev = [f for f in bal3 if is_even(f, 3)]
    report("ex.7: n=3 -> 70 balanced = 16 self-dual + 6 even + 48 others",
           (len(bal3), len(sd), len(ev), len(bal3) - len(sd) - len(ev)) == (70, 16, 6, 48))
    report("ex.7: every self-dual formula is balanced (n <= 4)",
           all(lam(f) == 2 ** (n - 1) for n in range(1, 5) for f in all_tables(n) if is_selfdual(f, n)))
    report("ex.7: even formulas are balanced only when made of half the pairs: "
           "n=2 -> 2 of 4, n=3 -> 6 of 16; empty set and I are even but not balanced",
           sum(1 for f in all_tables(2) if is_even(f, 2) and lam(f) == 2) == 2
           and sum(1 for f in all_tables(3) if is_even(f, 3) and lam(f) == 4) == 6
           and is_even((0,) * 8, 3) and lam((0,) * 8) != 4)
    g = table_of(lambda a, b, c: 1 - (a ^ (b & c)), 3)
    ones = sorted("".join(map(str, a)) for a in codes(3) if g[index(a)])
    report("ex.7: not(A xor (B&C)) = K000+K111+K001+K010: balanced, neither self-dual nor even",
           ones == ["000", "001", "010", "111"] and not is_selfdual(g, 3) and not is_even(g, 3))

    print("\nall §3 checks passed")


if __name__ == "__main__":
    main()
