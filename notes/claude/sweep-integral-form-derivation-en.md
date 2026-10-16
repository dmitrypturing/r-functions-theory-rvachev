# An exact integral form of the sweeping operation in FRep

*Derivation of the formula*

$$F_p(x)=\Big(\int_a^b \big(f_t^+(x)\big)^{p}\,dt\Big)^{1/p}-\Big(\int_a^b \big(f_t^-(x)\big)^{-p}\,dt\Big)^{-1/p},\qquad p\ge 1,$$

*with closed-form examples for $p=1$ (an interval and a ball moving along $x-t$) and a numerical example (a disk).*

---

## 1. Setting and notation

Let $f_t(x)$, $t\in[a,b]$, be a one-parameter family of defining functions of a moving solid in the FRep sense:

$$f_t(x)>0 \text{ inside the solid at time } t,\qquad f_t(x)=0 \text{ on its boundary},\qquad f_t(x)<0 \text{ outside}.$$

Standing assumptions (they hold for any reasonable rigid or deforming motion of a solid described by a continuous defining function):

- **(A1)** $f$ is jointly continuous in $(x,t)$ on $\mathbb R^d\times[a,b]$;
- **(A2)** $f$ is Lipschitz in $t$, locally uniformly in $x$: for every compact $K\subset\mathbb R^d$ there is $L_K$ with $|f_t(x)-f_s(x)|\le L_K|t-s|$ for $x\in K$.

The **swept solid** is the union of all positions of the moving solid,

$$S=\bigcup_{t\in[a,b]}\lbrace x: f_t(x)\ge 0\rbrace ,$$

and the *ideal* defining function of $S$ is the upper envelope

$$M(x)=\max_{t\in[a,b]} f_t(x).$$

By (A1) and compactness of $[a,b]$ the maximum is attained and $M$ is continuous; $S=\lbrace M\ge0\rbrace $, $\partial S\subseteq\lbrace M=0\rbrace $, and $\lbrace M>0\rbrace $ is the interior of the swept region.

Positive and negative parts:

$$f^+=\max(f,0)\ge 0,\qquad f^-=\max(-f,0)\ge 0,\qquad f=f^+-f^-,\qquad |f|=f^++f^-,\qquad f^+\cdot f^-=0 .$$

Two facts about $M$ that will be used repeatedly:

- $M(x)>0 \iff$ there is a $t_0$ with $f_{t_0}(x)>0 \iff$ (by continuity in $t$) $f_t(x)>0$ on a whole interval of $t$ of positive length;
- $M(x)<0 \iff f_t(x)<0$ for **all** $t \iff \min_t f_t^{-}(x)>0$ (again by compactness).

So the *inside* of the swept solid is an existential statement ($\exists t$), and the *outside* is a universal one ($\forall t$). This asymmetry is the whole difficulty.

## 2. The discrete formula and what happens as $\Delta t\to0$

Take samples $t_1<\dots<t_n$ of $[a,b]$ with spacing $\Delta t$. The union formula from the notebook is

$$F_n(x)=\sum_{i=1}^{n}\big(f_{t_i}+|f_{t_i}|\big)-\prod_{i=1}^{n}\big(|f_{t_i}|-f_{t_i}\big) =2\sum_i f_{t_i}^{+}(x)\;-\;2^{n}\prod_i f_{t_i}^{-}(x). \tag{2.1}$$

It is a legitimate R-disjunction of the $n$ sampled positions: if some $f_{t_i}>0$ the sum is positive and the product vanishes (one factor is $0$), so $F_n>0$; if all $f_{t_i}<0$ the sum vanishes and the product is positive, so $F_n<0$; if all $f_{t_i}\le0$ with equality somewhere, $F_n=0$.

Multiplying by $\Delta t>0$ does not change the sign, so

$$\Delta t\sum_i 2f_{t_i}^{+}\;-\;\Delta t\,2^n\prod_i f_{t_i}^{-}\tag{2.2}$$

describes the same sampled body. The first term is a Riemann sum and converges:

$$\Delta t\sum_i 2f_{t_i}^{+}(x)\;\longrightarrow\;2\int_a^b f_t^{+}(x)\,dt=:2A_1(x).$$

The question in the notebook is what to do with the second term.

### 2.1 The sum term alone is "half" of a defining function

$A_1(x)=\int_a^b f_t^{+}(x)\,dt$ has the properties

- $A_1(x)>0$ if $M(x)>0$ (the integrand is positive on an interval of $t$);
- $A_1(x)=0$ if $M(x)\le0$ (the integrand vanishes identically).

So $A_1$ is correct inside and on the boundary but is identically **zero outside**: it carries no information there, has no negative values, and its zero set is the whole exterior instead of $\partial S$. This is the "trouble outside the body". Whatever replaces the product must be a nonnegative functional $B(x)$ with

$$B(x)>0 \iff M(x)<0,\qquad B(x)=0 \iff M(x)\ge0, \tag{2.3}$$

and then $F=A-B$ has the right sign. The condition $B=0$ on $\lbrace M\ge0\rbrace $ *including the boundary* is what makes $F$ continuous with zero set $\partial S$.

### 2.2 De Morgan does not produce a new outside term

One might hope to obtain a sum-type formula for the exterior by writing it as an intersection of exteriors and negating. The dual (intersection) formula of (2.1) is, by $F_\cap(g)=-F_\cup(-g)$,

$$F_\cap(g_1,\dots,g_n)=\prod_i\big(|g_i|+g_i\big)-\sum_i\big(|g_i|-g_i\big)=2^n\prod_i g_i^+-2\sum_i g_i^- .$$

The exterior of $S$ is $\bigcap_i\lbrace -f_{t_i}>0\rbrace $; substituting $g_i=-f_{t_i}$ and negating,

$$-F_\cap(-f_{t_1},\dots,-f_{t_n})=-\Big(2^n\prod_i f_{t_i}^{-}-2\sum_i f_{t_i}^{+}\Big)=F_n ,$$

identically the original formula. In this pair of formulas $\exists$ is always a sum and $\forall$ is always a product; De Morgan only exchanges their roles. (Checked numerically as well: $1000$ random 5-tuples, exact agreement.) The exterior term therefore has to be constructed by other means.

## 3. The naive limit of the product term, and why it fails

A product of $n\to\infty$ factors not close to $1$ has no limit; the correct normalisation is the geometric mean, i.e. the exponent $\Delta t/(b-a)$:

$$\Big(\prod_i f_{t_i}^{-}\Big)^{\Delta t/(b-a)}=\exp\Big(\frac{1}{b-a}\sum_i\Delta t\,\ln f_{t_i}^{-}\Big)\;\longrightarrow\;\exp\Big(\frac{1}{b-a}\int_a^b\ln f_t^{-}\,dt\Big)=:M_0(x).$$

(With the convention $\ln0=-\infty$, $e^{-\infty}=0$.) This *is* an integral form of the product, and it has the correct sign:

- $M(x)>0$: $f_t^{-}(x)=0$ on an interval, $\ln f_t^{-}=-\infty$ there, the integral is $-\infty$, $M_0(x)=0$;
- $M(x)<0$: $f_t^{-}(x)\ge m>0$, the integral is finite, $M_0(x)>0$.

**But $M_0$ is discontinuous across $\partial S$.** Let $x_0$ be a boundary point at which the maximum $M(x_0)=0$ is attained at a single time $t_0$, with $f_t(x_0)<0$ for $t\neq t_0$. By (A2), $f_t^{-}(x_0)\le L|t-t_0|$, but for a generic sweep also $f_t^{-}(x_0)\ge c\,|t-t_0|^{\alpha}$ with $\alpha=2$ (a nondegenerate maximum in $t$) or $\alpha=1$ (a sweep end-cap). Then $\ln f_t^{-}(x_0)$ has a *logarithmic* singularity at $t_0$, which is **integrable**, so

$$M_0(x_0)=\exp\Big(\frac{1}{b-a}\int_a^b\ln f_t^{-}(x_0)\,dt\Big)>0 .$$

At the same time every interior point $x$ arbitrarily close to $x_0$ has $M_0(x)=0$. So $M_0$ jumps from a positive value on $\partial S$ to $0$ inside; the function $A_1-M_0$ has no zero set at all and is not a defining function in Rvachev's sense (continuity is lost). In the examples of §6–7 the jump is $0\to0.05$ across the side of the sweep and exactly $0\to e^{-1}=0.37$ at its cap.

The diagnosis: a finite product is killed by a *single* zero factor, while the geometric mean (the product's continuum limit) is *not* killed by a zero of $f^-$ at a single time — a zero of measure zero. We need a functional of $f_\cdot^{-}(x)$ that vanishes as soon as $f^-$ vanishes at one time, and does so continuously.

## 4. What any exact integral form must look like

> **Proposition 4.1 (no exact form with bounded integrands).** There do not exist a continuous function $\Psi:\mathbb R^m\to\mathbb R$ and functions $\varphi_1,\dots,\varphi_m$, each bounded on bounded sets, such that
> $$F(x)=\Psi\Big(\int_a^b\varphi_1(f_t(x),t)\,dt,\ \dots,\ \int_a^b\varphi_m(f_t(x),t)\,dt\Big)$$
> satisfies $\operatorname{sign}F(x)=\operatorname{sign}M(x)$ for every family $f$ obeying (A1)–(A2).

*Proof.* Fix $\varepsilon\in(0,\tfrac{b-a}{2})$ and consider (for one point $x$, which is all that matters) the time profile

$$f_t^{(\varepsilon)}=-1+2\,\eta\!\Big(\frac{t-t_m}{\varepsilon}\Big),\qquad t_m=\tfrac{a+b}{2},$$

where $\eta$ is a fixed smooth bump with $\eta(0)=1$, $0\le\eta\le1$, $\eta=0$ outside $[-1,1]$. Then $f_{t_m}^{(\varepsilon)}=+1$, so $M=1>0$ for every $\varepsilon>0$, and we need $F^{(\varepsilon)}>0$. For $\varepsilon=0$ take $f_t^{(0)}\equiv-1$: $M=-1<0$, so we need $F^{(0)}<0$. But $f_t^{(\varepsilon)}\to f_t^{(0)}$ for every $t\neq t_m$, the values stay in $[-1,1]$ where each $\varphi_i$ is bounded, and by dominated convergence

$$\int_a^b\varphi_i\big(f_t^{(\varepsilon)},t\big)\,dt\ \longrightarrow\ \int_a^b\varphi_i(-1,t)\,dt\qquad(\varepsilon\to0).$$

Continuity of $\Psi$ gives $F^{(\varepsilon)}\to F^{(0)}<0$, contradicting $F^{(\varepsilon)}>0$. $\square$

The proposition says exactly where the freedom lies: an exact integral form must use an integrand that is **unbounded** where $f^-\to0$ — and, by §3, unbounded is not enough: the singularity has to be **non-integrable**, so that a single time $t_0$ with $f_{t_0}^{-}=0$ already makes the integral infinite. The logarithm (the product) is unbounded but integrable, hence sign-correct but discontinuous. The next section uses the simplest non-integrable singularity, a negative power.

## 5. The construction and its proof

### 5.1 Power means

For a nonnegative function $u$ on $[a,b]$ and $q\ne0$ define the power mean

$$\mathcal M_q(u)=\Big(\frac{1}{b-a}\int_a^b u_t^{\,q}\,dt\Big)^{1/q},$$

with the conventions $0^{q}=+\infty$ for $q<0$ and $(+\infty)^{1/q}=0$ for $q<0$. Standard facts: $\mathcal M_q(u)$ is nondecreasing in $q$; $\mathcal M_q\to\operatorname{ess\,sup}u$ as $q\to+\infty$; $\mathcal M_q\to\operatorname{ess\,inf}u$ as $q\to-\infty$; and $\lim_{q\to0}\mathcal M_q(u)=\exp\big(\frac{1}{b-a}\int\ln u\big)$ is the geometric mean $M_0$ of §3.

Thus the product term of the notebook is the member $q=0$ of this family, and the exact envelope is the member $q=-\infty$ (for $f^-$) and $q=+\infty$ (for $f^+$). The claim is that every **finite** negative $q\le-1$ already gives an exact result for the outside term, because of the non-integrable singularity.

### 5.2 Definition

For $p\ge1$ put

$$A_p(x)=\Big(\int_a^b\big(f_t^{+}(x)\big)^{p}dt\Big)^{1/p},\qquad B_p(x)=\Big(\int_a^b\big(f_t^{-}(x)\big)^{-p}dt\Big)^{-1/p},\qquad \boxed{\,F_p(x)=A_p(x)-B_p(x)\,}. \tag{5.1}$$

Up to the constant factors $(b-a)^{\pm1/p}$, $A_p=\mathcal M_p(f^+)$ and $B_p=\mathcal M_{-p}(f^-)$. Equivalently, in norm notation, $F_p=\Vert f_\cdot^{+}(x)\Vert _{L^p(a,b)}-1/\Vert 1/f_\cdot^{-}(x)\Vert _{L^p(a,b)}$.

The two terms are the two halves of (2.3): $A_p$ encodes "$\exists t: f_t>0$" through *positivity* of an integral, $B_p$ encodes "$\forall t: f_t<0$" through *finiteness* of an integral. Their supports are disjoint, so they are combined by subtraction, exactly as $\sum g_t-\prod p_t$ in the discrete formula. (A combination by $\min$ or $\max$ would not work: $\min(A_p,-B_p)$ is $0$ inside and $\max(A_p,-B_p)$ is $0$ outside.)

### 5.3 Main theorem

> **Theorem 5.1.** Assume (A1)–(A2) and $p\ge1$. Then for every $x$:
>
> 1. $F_p(x)>0 \iff M(x)>0$;
> 2. $F_p(x)<0 \iff M(x)<0$;
> 3. $F_p(x)=0 \iff M(x)=0$;
> 4. $F_p$ is continuous on $\mathbb R^d$;
> 5. with the normalised means, $\mathcal M_p(f^+)-\mathcal M_{-p}(f^-)\to M(x)$ as $p\to\infty$.
>
> Consequently $\lbrace F_p\ge0\rbrace =S$ for every $p\ge1$, with $\lbrace F_p=0\rbrace =\lbrace M=0\rbrace $: $F_p$ is a defining function of the swept solid.

*Proof of 1.* Let $M(x)>0$. There is an interval $I\subset[a,b]$ of positive length on which $f_t(x)>0$; on $I$, $f_t^{+}(x)>0$ and $f_t^{-}(x)=0$. Hence $\int (f^+)^p\ge\int_I(f^+)^p>0$, so $A_p(x)>0$; and $(f_t^{-})^{-p}=+\infty$ on $I$, so $\int(f^-)^{-p}=+\infty$ and $B_p(x)=0$. Thus $F_p(x)=A_p(x)>0$. Conversely, if $M(x)\le0$ then $f_t^{+}(x)\equiv0$, $A_p(x)=0$ and $F_p(x)=-B_p(x)\le0$.

*Proof of 2.* Let $M(x)<0$. Then $f^+\equiv0$, so $A_p(x)=0$, and $m:=\min_t f_t^{-}(x)=-M(x)>0$. The integrand $(f_t^{-})^{-p}\le m^{-p}$ is bounded, and $\ge (\max_t f_t^{-})^{-p}>0$, so $0<\int(f^-)^{-p}<\infty$ and

$$B_p(x)\in\Big[(b-a)^{-1/p}\min_t f_t^{-}(x),\ (b-a)^{-1/p}\max_t f_t^{-}(x)\Big],\qquad B_p(x)>0 .$$

Hence $F_p(x)=-B_p(x)<0$. Conversely, if $M(x)\ge0$ then either $M>0$ (then $F_p>0$ by 1) or $M=0$ (then $F_p=0$ by 3 below).

*Proof of 3.* Let $M(x)=0$. Then $f^+\equiv0$ and $A_p(x)=0$. Choose $t_0$ with $f_{t_0}(x)=0$. By (A2), for all $t$,

$$f_t^{-}(x)=-f_t(x)=f_{t_0}(x)-f_t(x)\le L|t-t_0|,$$

so

$$\big(f_t^{-}(x)\big)^{-p}\ \ge\ L^{-p}\,|t-t_0|^{-p}.$$

Since $p\ge1$, $\int_a^b|t-t_0|^{-p}dt=+\infty$ (whether $t_0$ is interior to $[a,b]$ or an endpoint). Therefore $\int(f^-)^{-p}=+\infty$, $B_p(x)=0$ and $F_p(x)=0$. Together with 1 and 2 this gives the equivalence.

This is the **only** place where $p\ge1$ is used. For $p<1$ a Lipschitz zero of $f^-$ gives an integrable singularity, $B_p(x_0)>0$ on the boundary, and $F_p$ fails exactly as $M_0$ does in §3.

*Proof of 4.* Continuity of $A_p$: on a compact neighbourhood $K$ of any point, $f^+$ is bounded and jointly continuous, so $x\mapsto\int(f_t^{+}(x))^pdt$ is continuous by dominated convergence, and so is its $1/p$-th power.

Continuity of $B_p$ at a point $x$ with $M(x)>0$: $M$ is continuous, so $M>0$ on a neighbourhood, where $B_p\equiv0$ by the proof of 1.

Continuity of $B_p$ at a point $x$ with $M(x)<0$: on a neighbourhood $U$, $M\le M(x)/2<0$, so $f_t^{-}(y)\ge|M(x)|/2$ for $y\in U$ and all $t$; the integrand $(f_t^{-}(y))^{-p}$ is bounded and continuous in $y$, and dominated convergence gives continuity of the integral, which is positive and finite; hence $B_p$ is continuous at $x$.

Continuity of $B_p$ at a point $x_0$ with $M(x_0)=0$: we know $B_p(x_0)=0$ and $B_p\ge0$, so it suffices to show $\limsup_{y\to x_0}B_p(y)=0$, i.e. $\int(f_t^{-}(y))^{-p}dt\to+\infty$. Let $y_n\to x_0$. For every $t$, $f_t^{-}(y_n)\to f_t^{-}(x_0)$ by (A1), hence $(f_t^{-}(y_n))^{-p}\to(f_t^{-}(x_0))^{-p}$ in $[0,+\infty]$. By Fatou's lemma,

$$\liminf_{n}\int_a^b\big(f_t^{-}(y_n)\big)^{-p}dt\ \ge\ \int_a^b\big(f_t^{-}(x_0)\big)^{-p}dt=+\infty ,$$

the last equality being the computation in the proof of 3. So $B_p(y_n)\to0$.

Therefore $F_p=A_p-B_p$ is continuous everywhere.

*Proof of 5.* $\mathcal M_p(f^+)\to\max_tf_t^{+}=M^+$ and $\mathcal M_{-p}(f^-)\to\min_tf_t^{-}=\max(-\max_tf_t,0)=M^-$ (limits of power means of a continuous function on a compact interval), so the difference tends to $M^+-M^-=M$. $\square$

### 5.4 Remarks

- **Why it works, in one sentence.** The finite product $\prod_i f_{t_i}^{-}$ is zero as soon as one factor is zero; its continuum limit $M_0$ loses this property because a single time has measure zero; $\int(f^-)^{-p}dt$ with $p\ge1$ restores it because a Lipschitz zero of $f^-$ produces a non-integrable singularity. Proposition 4.1 shows that some such singularity is unavoidable.
- **The discrete case.** Replacing integrals by sums over samples in (5.1) gives $\big(\sum_i(f_{t_i}^{+})^p\big)^{1/p}-\big(\sum_i(f_{t_i}^{-})^{-p}\big)^{-1/p}$, which is sign-exact for every $p>0$ (a finite sum is infinite iff one term is) and is Ricci's power blending (1973) of the sampled positions. The continuum version needs $p\ge1$; this is the price of the passage to the limit.
- **Relation to the notebook.** $A_p$ is the $L^p$ version of the sum $\int g_t\,dt$; $B_p$ is what replaces the problematic $dt\prod_t p_t$. The replacement is not the limit of the product ($q=0$ in the power-mean family) but a different member ($q=-p\le-1$) of the same family.
- **Smooth alternatives are not exact.** $\frac1k\ln\int e^{kf_t}dt$ (Kreisselmeier–Steinhauser / LogSumExp) is $C^\infty$ and tends to $M$ as $k\to\infty$, but for finite $k$ its zero set is not $\partial S$ (Proposition 4.1 applies: the integrand is bounded). In the example below it gets the sign wrong on $6.4\%$ of the grid at $k=40$.

## 6. Analytic examples with $p=1$ and the trajectory $x-t$

Everything in this section is in closed form; the quadrature values quoted in brackets were computed with the midpoint rule, $N=200\,001$ samples in $t$, and agree to all printed digits except at the two points discussed in §6.1(d).

### 6.1 One-dimensional "ball": an interval sliding along the line

Take $d=1$, an interval of half-length $r<\tfrac12$ whose centre moves as $c(t)=t$, $t\in[0,1]$:

$$f_t(x)=r-|x-t| .$$

(A2) holds with $L=1$. The exact envelope is $M(x)=r-\operatorname{dist}(x,[0,1])$, so $S=[-r,\,1+r]$.

**(a) The inside term.** $f_t^{+}(x)>0$ exactly for $t\in(x-r,x+r)\cap[0,1]$, and

$$A_1(x)=\int_{\max(0,x-r)}^{\min(1,x+r)}\big(r-|x-t|\big)\,dt .$$

The integrand is a "tent" of height $r$ and base $2r$ centred at $t=x$; its full area is $r^2$. Cutting the tent at $t=0$ gives, for $-r\le x\le r$,

- for $-r\le x\le 0$ (only the right half of the tent, truncated at $t=0$): $A_1(x)=\dfrac{(x+r)^2}{2}$;
- for $0\le x\le r$ (right half complete, left half truncated): $A_1(x)=\dfrac{r^2}{2}+rx-\dfrac{x^2}{2}$;
- $A_1(x)=r^2$ for $r\le x\le 1-r$, and the mirror images ($x\mapsto1-x$) for $1-r\le x\le 1+r$.

Check: the pieces agree at $x=0$ ($r^2/2$) and $x=r$ ($r^2$), and $A_1(-r)=0$.

**(b) The outside term.** For $x>1+r$ we have $f_t^{-}(x)=x-t-r>0$ for all $t\in[0,1]$ and

$$\int_0^1\frac{dt}{x-r-t}=\Big[-\ln(x-r-t)\Big]_0^1=\ln\frac{x-r}{x-r-1},\qquad B_1(x)=\frac{1}{\ln\dfrac{x-r}{x-r-1}} .$$

For $x<-r$, by symmetry, $B_1(x)=1/\ln\dfrac{1-x-r}{-x-r}$. For $-r<x<1+r$ the set $\lbrace t:f_t^{-}(x)=0\rbrace =(x-r,x+r)\cap[0,1]$ has positive length, the integral is $+\infty$ and $B_1(x)=0$.

**(c) The result.** With $\delta=x-(1+r)$ the signed distance to the right end of $S$,

- $x<-r$: $F_1(x)=-\,1\Big/\ln\dfrac{1-x-r}{-x-r}$;
- $-r\le x\le0$: $F_1(x)=\dfrac{(x+r)^2}{2}$;
- $0\le x\le r$: $F_1(x)=\dfrac{r^2}{2}+rx-\dfrac{x^2}{2}$;
- $r\le x\le 1-r$: $F_1(x)=r^2$;
- $1-r\le x\le 1+r$: mirror images of the two previous rows ($x\mapsto 1-x$);
- $x>1+r$: $F_1(x)=-\,1\Big/\ln\Big(1+\dfrac1\delta\Big)$.


Every property of Theorem 5.1 can be read off directly:

- sign: positive on $(-r,1+r)$, negative outside, zero precisely at $x=-r$ and $x=1+r$;
- continuity at the boundary: from inside $F_1=\delta^2/2\to0$; from outside $F_1=-1/\ln(1+1/\delta)\to0$ because the integral $\ln(1+1/\delta)$ **diverges** as $\delta\to0$ — this divergence is the non-integrable singularity of §5 in its simplest form ($f_t^{-}=\delta+(1-t)$ has a simple zero at $t=1$ when $\delta=0$);
- the rate is logarithmic, $F_1\approx-1/\ln(1/\delta)$, because $p=1$ and the zero is at an endpoint (a "cap" in the language of §7);
- far away the form is distance-like: $\ln(1+1/\delta)=\frac1{\delta+1/2}+O(\delta^{-3})$, so $F_1(x)=-(x-r-\tfrac12)+O(1/x)$, i.e. minus the distance to the centre of the sweep.

Some values ($r=0.3$; quadrature in brackets): $F_1(0.5)=0.09$ $[0.090000]$, $F_1(1.2)=0.005$ $[0.005000]$, $F_1(1.31)=-1/\ln 101=-0.216679$ $[-0.216679]$, $F_1(1.4)=-1/\ln 11=-0.417032$ $[-0.417032]$, $F_1(2)=-1/\ln(1.7/0.7)=-1.127010$ $[-1.127010]$, $F_1(5)=-4.180083$ $[-4.180083]$.

**(d) What the product term would have given.** For the same point $x=1+r$ (on the boundary), the geometric mean of §3 is

$$M_0(1+r)=\exp\Big(\int_0^1\ln f_t^{-}(1+r)\,dt\Big)=\exp\Big(\int_0^1\ln(1-t)\,dt\Big)=e^{-1}=0.3679,$$

while $M_0(x)=0$ for every $x<1+r$. So the limit of the product term jumps by exactly $1/e$ at the boundary $[0.367880]$; the value $0.3679$ seen at the cap of the 2-D disk in §7 is this same number, because on the axis of the sweep the disk problem reduces to this one-dimensional one. (At the boundary point itself the quadrature returns $F_1\approx-0.0706$ instead of $0$: with the midpoint rule the smallest value of $f^-$ is $\Delta t/2$ instead of $0$, and $1/\ln(2N)\approx0.078$ — the logarithmic rate again.)

### 6.2 A ball in $\mathbb R^n$ with the squared-distance function

Let $n\ge2$, $x=(x_1,x_\perp)$, $\rho=|x_\perp|$, and let a ball of radius $r<\tfrac12$ move along the $x_1$-axis:

$$f_t(x)=r^2-|x-t\,e_1|^2=r^2-\rho^2-(x_1-t)^2=h^2-(t-x_1)^2,\qquad h^2:=r^2-\rho^2 .$$

The time profile at every point is a downward parabola in $t$ with apex $h^2$ at $t=x_1$, which makes all integrals elementary. (A2) holds on compacts. The exact envelope is $M(x)=h^2-\operatorname{dist}(x_1,[0,1])^2$; $S$ is a cylinder of radius $r$ over $[0,1]$ with two hemispherical caps.

**Case I: $\rho>r$ (beside the cylinder).** Put $\kappa^2=\rho^2-r^2>0$. Then $f_t^{-}=(t-x_1)^2+\kappa^2>0$ for all $t$, $A_1=0$, and

$$\int_0^1\frac{dt}{(t-x_1)^2+\kappa^2}=\frac1\kappa\Big[\arctan\frac{1-x_1}{\kappa}+\arctan\frac{x_1}{\kappa}\Big],\qquad F_1(x)=-\,\frac{\kappa}{\arctan\frac{1-x_1}{\kappa}+\arctan\frac{x_1}{\kappa}} .$$

For $0<x_1<1$ and $\rho\downarrow r$ the bracket tends to $\pi$ and $F_1\approx-\kappa/\pi=-\sqrt{2r\delta}/\pi$ with $\delta=\rho-r$: continuous, with the $\delta^{1/2}$ rate predicted for $p=1$ at a side point. For $x_1>1$ and $\rho\downarrow r$ the bracket tends to $\kappa/(x_1(x_1-1))$ and $F_1\to-x_1(x_1-1)$, which is negative and finite — correct, since such a point is outside $S$ ($M=-(x_1-1)^2<0$).

**Case II: $\rho\le r$ but $x_1>1+h$ (beyond the cap; $x_1<-h$ is the mirror image).** Now $f_t^{-}=(x_1-t)^2-h^2>0$ for all $t\in[0,1]$, $A_1=0$, and with $u=x_1-t$,

$$\int_{x_1-1}^{x_1}\frac{du}{u^2-h^2}=\frac1{2h}\Big[\ln\frac{u-h}{u+h}\Big]_{x_1-1}^{x_1},\qquad F_1(x)=-\,\frac{2h}{\ln\dfrac{(x_1-h)(x_1-1+h)}{(x_1+h)(x_1-1-h)}} .$$

As $x_1\downarrow1+h$ the factor $x_1-1-h$ in the denominator of the logarithm tends to $0$, the logarithm diverges and $F_1\to0$ (logarithmically, as in §6.1). As $h\to0$ the expression tends to $-x_1(x_1-1)$, matching Case I. On the axis ($\rho=0$, $h=r$) this is the exact analogue of §6.1(b) with the squared profile.

**Case III: inside, $-h<x_1<1+h$ with $h>0$.** Here $f_t^{-}=0$ on the interval $(x_1-h,x_1+h)\cap[0,1]$ of positive length, so $B_1=0$, and with $s=t-x_1$

$$F_1(x)=A_1(x)=\int_{\max(-x_1,-h)}^{\min(1-x_1,h)}(h^2-s^2)\,ds ,$$

which gives

- for $-h<x_1<h$: $F_1(x)=\dfrac{2h^3}{3}+h^2x_1-\dfrac{x_1^3}{3}$;
- for $h\le x_1\le 1-h$: $F_1(x)=\dfrac{4h^3}{3}$;
- for $1-h<x_1<1+h$: $F_1(x)=\dfrac{2h^3}{3}+h^2(1-x_1)-\dfrac{(1-x_1)^3}{3}$.


At $x_1=1+h$ the last row gives $\tfrac23h^3-h^3+\tfrac13h^3=0$, matching Case II; at the side, $h\to0$ gives $F_1=\tfrac43h^3\approx\tfrac43(2r|\delta|)^{3/2}$, the $|\delta|^{3/2}$ rate predicted for $p=1$.

**Checks** ($r=0.3$; closed form vs. quadrature): $F_1(0.5,\rho{=}0)=\tfrac43r^3=0.036$ $[0.036000]$; $F_1(0.5,0.29)=0.000604$ $[0.000604]$; $F_1(0.5,0.30)=0$ $[0.000000]$; $F_1(0.5,0.31)=-0.027582$ $[-0.027582]$; $F_1(0.5,1.0)=-0.987976$ $[-0.987976]$; $F_1(1.25,0.2)=-0.177072$ $[-0.177072]$; $F_1(1.5,0.35)=-0.796154$ $[-0.796154]$; the removable case $F_1(1.5,0.3)=-1.5\cdot0.5=-0.75$ $[-0.750000]$.

So for the ball with the squared-distance defining function and the trajectory $x_1-t$, the sweep function (5.1) with $p=1$ is a single explicit piecewise formula built from $\arctan$, $\ln$ and cubic polynomials, and one can verify by hand that it is continuous, vanishes exactly on the cylinder-with-caps, and has the right sign on both sides.

## 7. Numerical example: a disk with the distance function, $p=1,2,4,8$

**Data.** $d=2$, a disk of radius $r=0.3$ described now by the *distance* function (not its square, so the integrals are no longer elementary), moving with its centre $c(t)=(t,0)$, $t\in[0,1]$:

$$f_t(x)=r-\big|x-c(t)\big|=r-\sqrt{(x_1-t)^2+x_2^2}.$$

(A1) holds; (A2) holds with $L=1$ since $|f_t-f_s|\le|c(t)-c(s)|=|t-s|$.

**Exact envelope.** $\max_tf_t(x)=r-\operatorname{dist}\big(x,\text{segment}\big)$, i.e.

$$M(x)=r-\sqrt{(x_1-\operatorname{clip}(x_1,0,1))^2+x_2^2}.$$

$S$ is a stadium: a rectangle $[0,1]\times[-r,r]$ with two half-disk caps.

**Time profile at a point.** Along the side of the stadium take $x=(\tfrac12,x_2)$. With $s=t-\tfrac12$,

$$f_t(x)=r-\sqrt{s^2+x_2^2}=\big(r-|x_2|\big)-\frac{s^2}{2|x_2|}+O(s^4).$$

So near the touching time $t_0=\tfrac12$ the profile is a parabola in $t$ with apex value $M(x)=r-|x_2|$. Write $\delta=|x_2|-r$ for the signed distance to the side boundary ($\delta>0$ outside).

**Outside, $\delta>0$ small.** $f_t^{-}\approx\delta+\frac{s^2}{2r}$ near $s=0$, and the integral $\int(f^-)^{-p}$ is dominated by this neighbourhood:

$$\int\Big(\delta+\frac{s^2}{2r}\Big)^{-p}ds=\sqrt{2r}\;\delta^{\frac12-p}\,\mathrm B\!\big(\tfrac12,\,p-\tfrac12\big)\qquad(p>\tfrac12),$$

hence

$$B_p(x)\approx\Big[\sqrt{2r}\,\mathrm B\big(\tfrac12,p-\tfrac12\big)\Big]^{-1/p}\,\delta^{\,1-\frac{1}{2p}},\qquad F_p\approx-\,C_p^{\mathrm{out}}\,\delta^{\,1-\frac1{2p}} .$$

For $r=0.3$: $C^{\mathrm{out}}_1=0.411$, $C^{\mathrm{out}}_2=0.907$, $C^{\mathrm{out}}_4=1.071$, $C^{\mathrm{out}}_8=1.088$. As $\delta\to0$ the integral diverges like $\delta^{1/2-p}$, so $B_p\to0$ — this is the non-integrable singularity of §5 seen through a limit.

**Inside, $\delta<0$ small.** $f_t^{+}\approx|\delta|-\frac{s^2}{2r}$ on $|s|<\sqrt{2r|\delta|}$ and $0$ elsewhere:

$$\int\Big(|\delta|-\frac{s^2}{2r}\Big)_{+}^{\,p}ds=\sqrt{2r}\;|\delta|^{p+\frac12}\,\mathrm B\big(\tfrac12,\,p+1\big),\qquad A_p(x)\approx C_p^{\mathrm{in}}\,|\delta|^{\,1+\frac1{2p}} .$$

For $r=0.3$: $C^{\mathrm{in}}_1=1.033$, $C^{\mathrm{in}}_2=0.909$, $C^{\mathrm{in}}_4=0.891$, $C^{\mathrm{in}}_8=0.908$.

**At the cap**, $x=(x_1,0)$ with $x_1>1$, the touching time is the endpoint $t_0=1$ and the profile is *linear*, $f_t^{-}=(x_1-t)-r=\delta+(1-t)$ with $\delta=x_1-1-r$. Then $\int_0^1(\delta+u)^{-p}du=\frac{\delta^{1-p}-(1+\delta)^{1-p}}{p-1}$ for $p>1$ and $\ln\frac{1+\delta}{\delta}$ for $p=1$, so

$$B_p\approx(p-1)^{1/p}\,\delta^{\,1-\frac1p}\ (p>1),\qquad B_1\approx\frac{1}{\ln(1/\delta)} .$$

Both tend to $0$, as the theorem requires, but for $p=1$ only logarithmically — which is why $p\ge2$ is the practical recommendation.

**Numerical check.** Midpoint rule with $N=20001$ samples in $t$ for the profiles, $N=4001$ on a $221\times141$ grid over $[-0.6,1.6]\times[-0.7,0.7]$.

Profile across the side, $x_1=\tfrac12$, boundary at $x_2=0.3$:

| $x_2$ | $M$ (exact) | $A_1-M_0$ (geom. mean) | $F_1$ | $F_2$ | $F_4$ | asymptotics for $F_2$ |
|---|---|---|---|---|---|---|
| 0.2000 | 0.1000 | 0.0286 | 0.0286 | 0.0474 | 0.0640 | |
| 0.2900 | 0.0100 | 0.0010 | 0.0010 | 0.0029 | 0.0050 | $0.909\cdot0.01^{1.25}=0.0029$ |
| 0.2990 | 0.0010 | 0.0000 | 0.0000 | 0.0002 | 0.0004 | |
| 0.3000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | boundary |
| 0.3001 | −0.0001 | **−0.0506** | −0.0041 | −0.0009 | −0.0003 | |
| 0.3010 | −0.0010 | −0.0560 | −0.0132 | −0.0051 | −0.0025 | |
| 0.3100 | −0.0100 | −0.0760 | −0.0432 | −0.0282 | −0.0189 | $-0.907\cdot0.01^{0.75}=-0.0287$ |
| 0.4000 | −0.1000 | −0.1739 | −0.1614 | −0.1510 | −0.1368 | |
| 0.6000 | −0.3000 | −0.3596 | −0.3558 | −0.3523 | −0.3459 | |

Profile across the cap, $x_2=0$, boundary at $x_1=1.3$:

| $x_1$ | $M$ (exact) | $A_1-M_0$ (geom. mean) | $F_1$ | $F_2$ | $F_4$ |
|---|---|---|---|---|---|
| 1.2000 | 0.1000 | 0.0050 | 0.0050 | 0.0183 | 0.0376 |
| 1.2900 | 0.0100 | 0.0000 | 0.0000 | 0.0006 | 0.0021 |
| 1.3000 | 0.0000 | **−0.3679** | −0.0843 | −0.0032 | −0.0003 |
| 1.3010 | −0.0010 | −0.3708 | −0.1447 | −0.0316 | −0.0074 |
| 1.3100 | −0.0100 | −0.3891 | −0.2167 | −0.1005 | −0.0416 |
| 1.4000 | −0.1000 | −0.5143 | −0.4170 | −0.3317 | −0.2341 |

Reading the tables:

- the geometric-mean form (the honest limit of the product term) jumps at the boundary: $-0.05$ on the side and $-0.37$ at the cap, one step outside a point where it is $0$;
- $F_p$ passes through $0$ exactly at the boundary for every $p$, with values on both sides matching the asymptotic formulas ($F_2(0.31)=-0.0282$ vs. predicted $-0.0287$; $F_2(0.29)=0.0029$ vs. $0.0029$; $F_4(0.31)=-0.0189$ vs. $-0.0190$);
- the residual $-0.08$ of $F_1$ *at* the cap boundary is the quadrature seeing $\delta\approx\Delta t/2$ instead of $0$ combined with the $1/\ln(1/\delta)$ rate; for $p=2$ the same effect is $-0.003$, for $p=4$ it is $-0.0003$.

On the full grid, excluding a band $|M|\le2\cdot10^{-3}$ around the boundary (30 877 cells): sign agreement between $F_p$ and $M$ is $100\%$ for $p=1,2,4$; for the LogSumExp form with $k=40$ it is $93.6\%$. The largest jump between neighbouring grid cells (step $0.01$) is $0.010$ for $M$, $0.20/0.09/0.04$ for $F_{1}/F_{2}/F_{4}$ (steep but continuous, near the caps), and $0.38$ for the geometric-mean form (a genuine discontinuity).

The figure `sweep_integral_forms.png` shows the four fields (exact $M$, geometric-mean form, $F_2$, $F_4$) with the true boundary dashed and the zero set of each form in green, and the two profiles above with $p=1,2,4,8$.

## 8. Limitations

1. **Not $C^1$ at the boundary, not distance-like.** From the asymptotics: $F_p\sim-\delta^{1-1/(2p)}$ outside (infinite slope) and $\sim|\delta|^{1+1/(2p)}$ inside (zero slope) along the sides; $-\delta^{1-1/p}$ at the caps. $F_p$ is Hölder-continuous with exponent $1-1/(2p)$, and the gradient is not bounded near $\partial S$. Larger $p$ improves this ($F_p\to M$), but no finite $p$ is Lipschitz. This is the same class of behaviour as the degree-$n$ product in the discrete formula, which is also far from normalised; R-functions guarantee sign and continuity, not distance.
2. **Exactness lives in the divergence.** Any quadrature with step $\Delta t$ makes $\int(f^-)^{-p}$ large but finite; the boundary is effectively found where the "well" of $f^-$ around $t_0$ is resolved, i.e. its width $\sqrt{2r\delta}$ is comparable to $\Delta t$, giving a boundary shift $O(\Delta t^2)$ along the sides and $O(\Delta t)$ at the caps — the same resolution limit as any sampled sweep.
3. **Exactness versus smoothness is a real trade-off** (Proposition 4.1): every exact integral form needs an unbounded, non-integrable integrand; every bounded-integrand form (LogSumExp, $L^p$ of the positive part alone, etc.) is approximate for finite parameter.
4. **Hypothesis on $t$-regularity.** If $f$ is only Hölder in $t$ with exponent $\alpha<1$, the proof of 3 needs $p\ge1/\alpha$.

## 9. Summary

Starting from the notebook formula $\sum_t g_t-\prod_t p_t$ with $g_t=2f_t^{+}$, $p_t=2f_t^{-}$:

- the sum term becomes $\int f_t^{+}\,dt$ (or its $L^p$ version) and is exact inside and on the boundary but identically zero outside;
- the product term has an integral form, the geometric mean $\exp\big(\frac{1}{b-a}\int\ln f_t^{-}\,dt\big)$, which has the right sign but is discontinuous on $\partial S$;
- the "sum form for the outside region" exists and is $\int(f_t^{-})^{-p}dt$: the universal quantifier $\forall t$ is encoded by its finiteness, and the non-integrable singularity at a touching time (for $p\ge1$ and Lipschitz motion) makes the resulting term vanish continuously on the boundary;
- the two halves are glued by subtraction, giving (5.1), a continuous defining function of the swept solid with zero set exactly $\partial S$, for every $p\ge1$, converging to $\max_tf_t$ as $p\to\infty$.
