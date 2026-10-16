"""Numerical checks for the §4 exercises (pp. 28-29).

ex. 1: phi(x, y) = h^{-1}[h(x) * h(y)]; the operations phi_0..phi_3 of the text
       are of this form.
ex. 2: x * y = x|y| is associative but not commutative.
ex. 3: phi_t(x, y) = h_t^{-1}[h_t(x) h_t(y)], h_t(x) = (1-t)e^x + t x,
       with h_t^{-1}(y) = y/t - W((1-t)/t * e^{y/t}) for 0 < t < 1.
ex. 6: psi = x1 - x2 + x3 is a ternary associative operation; in general
       psi = sum zeta^{i-1} x_i with zeta^{n-1} = 1 is n-ary associative.

Run:  python3 associativity.py
"""

import cmath
import math
import random

rnd = random.Random(7)


def close(a, b, tol=1e-8):
    return abs(a - b) <= tol * max(1.0, abs(a), abs(b))


def report(title, ok):
    print(("OK   " if ok else "FAIL ") + title)
    if not ok:
        raise SystemExit(1)


# ---------- Lambert W on (0, inf), given log of the argument ----------
def lambert_w_from_log(L):
    """Principal branch W(s) for s = e^L > 0: solve w + ln w = L (w > 0)."""
    w = L - math.log(L) if L > 1.5 else math.exp(L) / (1 + math.exp(L)) if L < -30 else 0.5
    if L <= 1.5:
        # Newton on w e^w = s
        s = math.exp(L)
        w = s if s < 1 else math.log(s)
        for _ in range(100):
            ew = math.exp(w)
            f = w * ew - s
            w_new = w - f / (ew * (w + 1))
            if abs(w_new - w) < 1e-15 * max(1, abs(w)):
                w = w_new
                break
            w = w_new
        return w
    for _ in range(100):           # Newton on g(w) = w + ln w - L
        w_new = w - (w + math.log(w) - L) / (1 + 1 / w)
        if abs(w_new - w) < 1e-15 * max(1, abs(w)):
            return w_new
        w = w_new
    return w


def h(t, x):
    return (1 - t) * math.exp(x) + t * x


def h_inv(t, y):
    if t == 0:
        return math.log(y)
    if t == 1:
        return y
    L = math.log((1 - t) / t) + y / t
    return y / t - lambert_w_from_log(L)


def phi(t, x, y):
    return h_inv(t, h(t, x) * h(t, y))


def main():
    # ---------------- ex. 1: the operations of the text ----------------
    c = 3.0
    alpha = 0.7
    a = 1.3
    ops = {
        "phi0 (velocities)": (lambda x, y: (x + y) / (1 + x * y / c ** 2),
                              lambda x: math.atanh(x / c), lambda u: c * math.tanh(u), lambda p, q: p + q,
                              (-0.9 * c, 0.9 * c)),
        "phi1 = x+y+a*xy": (lambda x, y: x + y + alpha * x * y,
                            lambda x: 1 + alpha * x, lambda u: (u - 1) / alpha, lambda p, q: p * q,
                            (-1.0, 1.0)),
        "phi2 = sqrt(x^2+y^2+a^2)": (lambda x, y: math.sqrt(x * x + y * y + a * a),
                                     lambda x: x * x + a * a, lambda u: math.sqrt(u - a * a),
                                     lambda p, q: p + q, (0.0, 2.0)),
        "phi3 = xy/(x+y-a*xy)": (lambda x, y: x * y / (x + y - alpha * x * y),
                                 lambda x: 1 / x - alpha, lambda u: 1 / (u + alpha), lambda p, q: p + q,
                                 (0.2, 1.0)),
    }
    for name, (op, hh, hinv, star, (lo, hi)) in ops.items():
        ok_form = ok_assoc = True
        for _ in range(2000):
            x, y, z = (rnd.uniform(lo, hi) for _ in range(3))
            ok_form &= close(op(x, y), hinv(star(hh(x), hh(y))))
            try:
                ok_assoc &= close(op(op(x, y), z), op(x, op(y, z)), 1e-7)
            except (ZeroDivisionError, ValueError):
                pass
        report(f"ex.1: {name} = h^-1[h(x)*h(y)] and is associative", ok_form and ok_assoc)

    # ---------------- ex. 2 ----------------
    star = lambda x, y: x * abs(y)
    ok = all(close(star(star(x, y), z), star(x, star(y, z)))
             for x, y, z in ((rnd.uniform(-5, 5), rnd.uniform(-5, 5), rnd.uniform(-5, 5)) for _ in range(5000)))
    report("ex.2: x*y = x|y| is associative", ok)
    report("ex.2: ... and not commutative: 1*(-1) = 1, (-1)*1 = -1", star(1, -1) == 1 and star(-1, 1) == -1)
    left = lambda x, y: x
    report("ex.2: x*y = x is associative and not commutative",
           left(left(1, 2), 3) == left(1, left(2, 3)) and left(1, 2) != left(2, 1))

    # ---------------- ex. 3 ----------------
    report("ex.3: phi_0 = x + y and phi_1 = xy",
           all(close(phi(0, x, y), x + y) and close(phi(1, x, y), x * y)
               for x, y in ((rnd.uniform(-3, 3), rnd.uniform(-3, 3)) for _ in range(500))))
    ok_inv = ok_comm = ok_assoc = True
    for _ in range(3000):
        t = rnd.uniform(0.02, 0.98)
        x, y, z = (rnd.uniform(-2, 2) for _ in range(3))
        yy = rnd.uniform(-30, 30)
        ok_inv &= close(h(t, h_inv(t, yy)), yy, 1e-7)
        ok_comm &= close(phi(t, x, y), phi(t, y, x))
        ok_assoc &= close(phi(t, phi(t, x, y), z), phi(t, x, phi(t, y, z)), 1e-6)
    report("ex.3: h_t^{-1}(y) = y/t - W((1-t)/t e^{y/t}) inverts h_t (0<t<1)", ok_inv)
    report("ex.3: phi_t is commutative and associative for random t in (0,1)", ok_comm and ok_assoc)
    report("ex.3: h_t is increasing (h_t' = (1-t)e^x + t > 0)",
           all((1 - t) * math.exp(x) + t > 0 for t in (0, 0.3, 1) for x in (-50, 0, 50)))

    # ---------------- ex. 6 ----------------
    psi = lambda x1, x2, x3: x1 - x2 + x3
    ok = True
    for _ in range(3000):
        xs = [rnd.uniform(-5, 5) for _ in range(5)]
        v1 = psi(psi(xs[0], xs[1], xs[2]), xs[3], xs[4])
        v2 = psi(xs[0], psi(xs[1], xs[2], xs[3]), xs[4])
        v3 = psi(xs[0], xs[1], psi(xs[2], xs[3], xs[4]))
        ok &= close(v1, v2) and close(v2, v3)
    report("ex.6: psi = x1 - x2 + x3 is ternary associative", ok)

    def zeta_op(n, zeta):
        return lambda *x: sum(zeta ** i * x[i] for i in range(n))

    for n in range(3, 8):
        for k in range(1, n - 1):                       # all roots zeta^(n-1)=1, zeta != 1
            zeta = cmath.exp(2j * math.pi * k / (n - 1))
            op = zeta_op(n, zeta)
            ok = True
            for _ in range(200):
                xs = [complex(rnd.uniform(-3, 3), rnd.uniform(-3, 3)) for _ in range(2 * n - 1)]
                vals = [op(*(xs[:j] + [op(*xs[j:j + n])] + xs[j + n:])) for j in range(n)]
                ok &= all(abs(vv - vals[0]) < 1e-9 * max(1, abs(vals[0])) for vv in vals)
            report(f"ex.6: n={n}, zeta=exp(2 pi i {k}/{n - 1}): sum zeta^(i-1) x_i is {n}-ary associative", ok)
    for n in (3, 5, 7):
        op = zeta_op(n, -1)
        ok = True
        for _ in range(500):
            xs = [rnd.uniform(-3, 3) for _ in range(2 * n - 1)]
            vals = [op(*(xs[:j] + [op(*xs[j:j + n])] + xs[j + n:])) for j in range(n)]
            ok &= all(close(vv, vals[0]) for vv in vals)
        report(f"ex.6: real alternating sum x1 - x2 + ... + x{n} is {n}-ary associative", ok)
    op4 = zeta_op(4, -1)
    xs = [1, 2, 3, 4, 5, 6, 7]
    vals = [op4(*(xs[:j] + [op4(*xs[j:j + 4])] + xs[j + 4:])) for j in range(4)]
    report("ex.6: for even n the alternating sum is NOT associative (n=4: values differ)",
           len(set(vals)) > 1)

    print("\nall §4 checks passed")


if __name__ == "__main__":
    main()
