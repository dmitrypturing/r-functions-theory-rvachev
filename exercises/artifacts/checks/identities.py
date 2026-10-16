"""Truth-table checks of the set identities used in §1, §2 and in the text of §3.

Two formulas are identical iff they agree on every code (alpha_1, ..., alpha_n),
alpha_i = 1 meaning "the point lies in A_i" (see the solutions, §3 ex. 1).
Sets are modelled as bits: & = intersection, | = union, 1-x = complement.

Run:  python3 identities.py
"""

from itertools import product
from fractions import Fraction
import random


def comp(x):
    return 1 - x


def sd(x, y):            # symmetric difference (1.2)
    return (x & comp(y)) | (y & comp(x))


def minus(x, y):         # difference (1.1)
    return x & comp(y)


def identical(lhs, rhs, n):
    bad = [a for a in product((0, 1), repeat=n) if lhs(*a) != rhs(*a)]
    return bad


def check(title, lhs, rhs, n, expect=True):
    bad = identical(lhs, rhs, n)
    ok = (not bad) == expect
    tag = "identity" if not bad else "NOT an identity, differs at codes " + ", ".join(
        "".join(map(str, b)) for b in bad)
    print(("OK   " if ok else "FAIL ") + f"{title}: {tag}")
    if not ok:
        raise SystemExit(1)


def main():
    I = 1  # the universe

    print("--- §1, exercise 1: identities (1.4)")
    check("A△B ≡ (A∪B)\\(A∩B)", lambda a, b: sd(a, b), lambda a, b: minus(a | b, a & b), 2)
    check("A∪B ≡ (A△B)△(A∩B)", lambda a, b: a | b, lambda a, b: sd(sd(a, b), a & b), 2)
    check("A\\B ≡ A△(A∩B)", lambda a, b: minus(a, b), lambda a, b: sd(a, a & b), 2)
    check("(A∩B)∪B ≡ B", lambda a, b: (a & b) | b, lambda a, b: b, 2)
    check("(A∪B)∩B ≡ B", lambda a, b: (a | b) & b, lambda a, b: b, 2)
    check("(A∩B)∪(A∩B̄) ≡ A", lambda a, b: (a & b) | (a & comp(b)), lambda a, b: a, 2)
    check("(A∪B)∩(A∪B̄) ≡ A", lambda a, b: (a | b) & (a | comp(b)), lambda a, b: a, 2)
    check("(Ā∩B)∪(A∩B̄) ≡ (A∪B)∩(Ā∪B̄)", lambda a, b: (comp(a) & b) | (a & comp(b)),
          lambda a, b: (a | b) & (comp(a) | comp(b)), 2)

    print("--- §1, exercise 2: symmetric difference")
    check("A△B ≡ B△A", lambda a, b: sd(a, b), lambda a, b: sd(b, a), 2)
    check("A△(B△C) ≡ (A△B)△C", lambda a, b, c: sd(a, sd(b, c)), lambda a, b, c: sd(sd(a, b), c), 3)
    check("A△(B△C) = 'odd number of the three sets'", lambda a, b, c: sd(a, sd(b, c)),
          lambda a, b, c: (a + b + c) % 2, 3)
    check("the book's final form K100∪K111∪K010∪K001", lambda a, b, c: sd(a, sd(b, c)),
          lambda a, b, c: (a & comp(b) & comp(c)) | (a & b & c) | (comp(a) & b & comp(c))
          | (comp(a) & comp(b) & c), 3)
    check("§1 worked example (p. 15) with ∪: (A∩B̄∩C)∪(A∩C) ≡ A∩C",
          lambda a, b, c: (a & comp(b) & c) | (a & c), lambda a, b, c: a & c, 3)
    check("§1 example as printed with ∩ is not ≡ A∩C",
          lambda a, b, c: (a & comp(b) & c) & (a & c), lambda a, b, c: a & c, 3, expect=False)

    print("--- §1, exercise 3: intervals on the line (random tests, exact arithmetic)")
    rnd = random.Random(1)

    def interval(lo, hi):
        return (Fraction(lo), Fraction(hi))

    def cap(p, q):
        lo, hi = max(p[0], q[0]), min(p[1], q[1])
        return (lo, hi) if lo <= hi else None

    def contains(big, small):
        return small is None or (big[0] <= small[0] and small[1] <= big[1])

    holds_iff_subset = True
    sufficient = True
    necessary_if_nonempty = True
    for _ in range(20000):
        a, b, c, d, e, f = (rnd.randint(-6, 6) for _ in range(6))
        if a > b or c > d or e > f:
            continue
        A, B, C = interval(a, b), interval(c, d), interval(e, f)
        AB = cap(A, B)
        # (A∩B)∪C = C∪(B∩C)  <=>  (A∩B)∪C = C  <=>  A∩B ⊂ C  (B∩C ⊂ C)
        equality = contains(C, AB)
        cond = e <= max(a, c) and f >= min(b, d)
        holds_iff_subset &= True  # equality is by definition A∩B ⊂ C here
        if cond and not equality:
            sufficient = False
        if AB is not None and equality and not cond:
            necessary_if_nonempty = False
    print(("OK   " if sufficient else "FAIL ") + "conditions e<=max(a,c), f>=min(b,d) imply the equality")
    print(("OK   " if necessary_if_nonempty else "FAIL ")
          + "and are necessary when A∩B is non-empty")
    if not (sufficient and necessary_if_nonempty):
        raise SystemExit(1)

    print("--- §1, exercise 4: De Morgan for n components")
    for n in range(2, 7):
        check(f"complement of A1∩...∩A{n} ≡ union of complements",
              lambda *a: comp(min(a)), lambda *a: max(comp(x) for x in a), n)
        check(f"complement of A1∪...∪A{n} ≡ intersection of complements",
              lambda *a: comp(max(a)), lambda *a: min(comp(x) for x in a), n)

    print("--- §2, exercise 1: identities via Euler diagrams")
    check("(A∪C)∩B ≡ (A∩B)∪(Ā∩B∩C)", lambda a, b, c: (a | c) & b,
          lambda a, b, c: (a & b) | (comp(a) & b & c), 3)
    check("[A∩(B∪C)]∪(Ā∩C) ≡ C∪(A∩B)", lambda a, b, c: (a & (b | c)) | (comp(a) & c),
          lambda a, b, c: c | (a & b), 3)
    check("(A∩C)∪(B∩C)∪(C\\A) ≡ C", lambda a, b, c: (a & c) | (b & c) | minus(c, a),
          lambda a, b, c: c, 3)
    check("A△B ≡ (A∪B)\\(A∩B)", lambda a, b, c: sd(a, b), lambda a, b, c: minus(a | b, a & b), 3)
    check("[A∩(B△C)]∪(B△C) ≡ B△C", lambda a, b, c: (a & sd(b, c)) | sd(b, c),
          lambda a, b, c: sd(b, c), 3)
    check("as printed: A∪[(B\\Ā)△C] ≡ (A∩B)△C", lambda a, b, c: a | sd(minus(b, comp(a)), c),
          lambda a, b, c: sd(a & b, c), 3, expect=False)
    check("restored: A∩[(B\\Ā)△C] ≡ (A∩B)△(A∩C)", lambda a, b, c: a & sd(minus(b, comp(a)), c),
          lambda a, b, c: sd(a & b, a & c), 3)
    check("∩ distributes over △: A∩(X△Y) ≡ (A∩X)△(A∩Y)", lambda a, x, y: a & sd(x, y),
          lambda a, x, y: sd(a & x, a & y), 3)

    # region numbers of Fig. 3б: 1=111, 2=110, 3=011, 4=101, 5=010, 6=001, 7=100, 8=000
    num = {(1, 1, 1): 1, (1, 1, 0): 2, (0, 1, 1): 3, (1, 0, 1): 4,
           (0, 1, 0): 5, (0, 0, 1): 6, (1, 0, 0): 7, (0, 0, 0): 8}

    def regions(func):
        return sorted(num[a] for a in product((0, 1), repeat=3) if func(*a))

    print("    region sets (Fig. 3б numbering) used in the solution:")
    for name, func in [("A", lambda a, b, c: a), ("B", lambda a, b, c: b), ("C", lambda a, b, c: c),
                       ("A∪C", lambda a, b, c: a | c), ("(A∪C)∩B", lambda a, b, c: (a | c) & b),
                       ("A∩B", lambda a, b, c: a & b), ("Ā∩B∩C", lambda a, b, c: comp(a) & b & c),
                       ("A∩(B∪C)", lambda a, b, c: a & (b | c)), ("Ā∩C", lambda a, b, c: comp(a) & c),
                       ("A∩C", lambda a, b, c: a & c), ("B∩C", lambda a, b, c: b & c),
                       ("C\\A", lambda a, b, c: minus(c, a)), ("A△B", lambda a, b, c: sd(a, b)),
                       ("A∪B", lambda a, b, c: a | b), ("B△C", lambda a, b, c: sd(b, c)),
                       ("A∩(B△C)", lambda a, b, c: a & sd(b, c)),
                       ("(B\\Ā)△C", lambda a, b, c: sd(minus(b, comp(a)), c)),
                       ("A∪[(B\\Ā)△C]", lambda a, b, c: a | sd(minus(b, comp(a)), c)),
                       ("(A∩B)△C", lambda a, b, c: sd(a & b, c)),
                       ("A∩[(B\\Ā)△C]", lambda a, b, c: a & sd(minus(b, comp(a)), c)),
                       ("(A∩B)△(A∩C)", lambda a, b, c: sd(a & b, a & c))]:
        print(f"      {name:16s} {regions(func)}")

    print("--- text of §3 (pp. 19-21)")
    maj = lambda a, b, c: (a & b) | (a & c) | (b & c)
    majd = lambda a, b, c: (a | b) & (a | c) & (b | c)
    check("(1.6) is self-dual: (A∩B)∪(A∩C)∪(B∩C) ≡ (A∪B)∩(A∪C)∩(B∪C)", maj, majd, 3)
    check("warm-up: (A∩B)∪(Ā∩I) vs its dual (A∪B)∩(Ā∪∅) — not self-dual",
          lambda a, b: (a & b) | (comp(a) & I), lambda a, b: (a | b) & (comp(a) | 0), 2, expect=False)
    check("  ... (A∩B)∪(Ā∩I) ≡ Ā∪B", lambda a, b: (a & b) | (comp(a) & I),
          lambda a, b: comp(a) | b, 2)
    check("  ... (A∪B)∩(Ā∪∅) ≡ Ā∩B", lambda a, b: (a | b) & (comp(a) | 0),
          lambda a, b: comp(a) & b, 2)
    M = lambda a1, a2, a3: (a1 & comp(a2) & comp(a3)) | (a1 & a2) | comp(
        comp(a1 & a3 & I) & comp(a2 & a3))
    check("Example 2 (p. 20): M ≡ A1∪(A2∩A3)", M, lambda a1, a2, a3: a1 | (a2 & a3), 3)
    Md = lambda a1, a2, a3: (a1 | comp(a2) | comp(a3)) & (a1 | a2) & comp(
        comp(a1 | a3 | 0) | comp(a2 | a3))
    check("Example 2, dual identity: M* ≡ A1∩(A2∪A3)", Md, lambda a1, a2, a3: a1 & (a2 | a3), 3)

    print("\nall identity checks passed")


if __name__ == "__main__":
    main()
