# Prior-art search log (16–17 September 2026)

Question asked of every item: *does it contain a continuous-parameter integral of a negative power (or reciprocal) of the negative part of a signed implicit function — or any equivalent construction — that vanishes exactly on the boundary of a union over the parameter?*

Six sub-area campaigns were run (web search, arXiv, Semantic Scholar, publisher abstract pages, full texts where open). Only items actually seen in a result page were recorded. Verdict codes: **yes** = same result; **partial** = one ingredient present; **no** = related but different.

Overall result: **no "yes" anywhere.** The construction $F_p=\|f^+\|_{L^p}-1/\|1/f^-\|_{L^p}$, the key lemma (Lipschitz zero ⇒ $\int u^{-p}=\infty$ for $p\ge1$ ⇒ exact zero of the mean) applied to envelopes, and the obstruction for bounded integrands were not found.

## A. Sweeps in F-rep / implicit modelling (7)

| ref | how the sweep is represented | verdict |
|---|---|---|
| Sourin & Pasko 1995/1996 (SMA; TVCG 2(1)) | $\max_t f_t$ by numerical search, or R-union of sampled instances | no |
| Schmidt & Wyvill 2005 (GRAPHITE) | sweep template at the closest path parameter, ordinary CSG union of samples; avoids R-functions | no |
| Pasko et al. 1995 (Visual Computer) | F-rep framework; sweeping listed as an operation, no formula | no |
| Pasko, Adzhiev, Schmitt, Schlick 2001 (Graphical Models) | hypervolumes, time as extra coordinate; projection left numerical | no |
| Sherstyuk 1999; McCormack & Sherstyuk 1998; Bloomenthal & Shoemake 1991 | ∫ positive kernel along skeleton, thresholded | partial (positive-part integral only) |

## B. R-function theory (13)

Rvachev 1967, 1971, 1982; Rvachev & Slesarenko 1973; Rvachev & Sheiko 1995; Rvachev, Sheiko & Shapiro 1999; Shapiro 1991, 2007; Shapiro & Tsukanov 1999; Biswas & Shapiro 2004; Akleman & Chen 1999; Proskurin 2016 (arXiv:1603.00320); Fryazinov, Pasko, Adzhiev (bounded blending).
All finite-arity; $p$-norm systems appear (R_p; Akleman–Chen generalized distance functions) with positive exponents only; no continuum-of-arguments or integral R-functions. **Closest: Akleman & Chen 1999 (partial), Sourin & Pasko 1996 (partial).**

## C. Blending, soft Booleans, smooth max (17)

Ricci 1973; Blinn 1982; Wyvill–McPheeters–Wyvill 1986; Wyvill–Guy–Galin 1999; Pasko & Savchenko 1994; Hoffmann & Hopcroft 1985; Rockwood 1989; Dekkers et al. 2004; Barthe et al. 2003; Bernhardt et al. 2010; Gourmel et al. 2013; Kreisselmeier–Steinhauser 1979; Poon & Martins 2007; Duysinx & Sigmund 1998; Boyd & Vandenberghe 2004; Asadi & Littman 2017; Quilez (smooth min).
Ricci's $(\sum f_i^{-\alpha})^{-1/\alpha}$ is the discrete ancestor of the outside term but is used as a blend of nonnegative fields (bulges at finite α); all aggregators are exact only in a limit; none splits $f=f^+-f^-$ with opposite exponents; none has a continuous index. **Closest: Ricci 1973 (partial); Bernhardt et al. 2010 documents Rvachev's exact two-argument union.**

## D. Analysis: means, limits, product integrals, barriers (11)

Hardy–Littlewood–Pólya 1934; Bullen 2003; Kufner–Maligranda–Persson 2006 (Hardy inequality history); de Bruijn 1958 (Laplace's method); Dollard & Friedman 1979 and Slavík 2007 (product integrals); Moreau 1965; Rockafellar & Wets 1998; Carroll 1961; Fiacco & McCormick 1968; den Hertog et al. 1994 (inverse barriers).
Power means with negative exponents and their limits are textbook; inverse barriers $1/g$ are pointwise penalties; product integrals give $\exp\int\ln$ (the discontinuous member). **No source uses divergence of $\int u^{-p}$ as an exact zero detector for envelopes.**

## E. Offsets, Minkowski sums, morphology, integral surfaces (15)

Rossignac & Requicha 1986; Varadhan & Manocha 2006; Lien 2009; Frisken et al. 2000; Serra 1982; Maragos 2001; Sapiro et al. 1993; Kuosmanen & Astola 1995; Angulo 2010; Masci, Angulo & Schmidhuber 2013; Gonzalez & Woods (contra-harmonic filter); Bloomenthal & Shoemake 1991; McCormack & Sherstyuk 1998; Sherstyuk 1999; Zanni et al. 2013.
Exact dilation/erosion are sup/inf-convolutions; counter-harmonic means $\int u^{P+1}/\int u^{P}$ approach max/min only as $P\to\pm\infty$ and are presented as smooth surrogates. **Closest: Angulo 2010 / Masci et al. 2013 (partial).**

## F. Swept-volume SDFs, spacetime and neural methods, 2015–2026 (9)

Sellán, Aigerman, Jacobson 2021 (spacetime continuation); "Swept volume computation with enhanced geometric detail preservation" arXiv:2509.09325; Wang et al. 2024 Implicit SVSDF (GSIP minimisation over t per query); NeuralSVCD arXiv:2509.00499 (time optimisation); Joho et al. 2024 ICRA (neural, trained on discrete unions); SN Computer Science 2024 (IGR-trained SDF); Chiang et al. IJRR (deep estimator); Ratliff et al. 2009 CHOMP; Li et al. 2023 RDF.
Time is resolved by continuation, optimisation, sampling or learning — never by an integral. **All "no".**

## Classical swept-volume geometry (added by hand, 12)

Wang & Wang 1986; Weld & Leu 1990; Martin & Stephenson 1990; Blackmore & Leu 1992; Blackmore, Leu & Wang 1997; Abdel-Malek & Yeh 1997; Abdel-Malek et al. 2006 (survey); Peternell et al. 2005; Ilieş & Shapiro 1999 ("The dual of sweep": sweep = ∪, unsweep = ∩, PMC via inverse trajectories — verified from the ScienceDirect abstract); Ilieş & Shapiro 2000; Erdim & Ilieş 2008; Rossignac et al. 2007; Abrams & Allen 2000; Kim et al. 2004; Adsul et al. 2016; JCDE 2023 (vector-valued envelope functions).
Boundary/envelope/ODE/PMC methods; none gives an implicit function of the sweep.

## Residual risks

- Russian-language Rvachev literature reached only through translations/secondary citations; check Rvachev 1971 and the 1982 monograph (a PDF is in this papers folder) page by page.
- Full texts of Sourin & Pasko 1996, Pasko et al. 2001 and Schmitt's thesis not accessible during the search.
- The key lemma is elementary and may exist as an exercise; the claim is its *use* for exact envelopes.
- Bibliographic metadata in `refs.bib` were partly reconstructed from snippets and memory; verify every DOI/volume/page before submission. Two entries (JCDE 2023; SN Computer Science 2024) carry author placeholders.

## G. Lipschitz / global optimisation and guaranteed methods in graphics (added by hand, 9)

Piyavskii 1972; Shubert 1972; Hansen, Jaumard & Lu 1992 (survey); Jones, Perttunen & Stuckman 1993 (DIRECT, "without the Lipschitz constant"); Pintér 1996; Sergeyev & Kvasov 2017; Snyder 1992 (interval analysis for graphics); Kalra & Barr 1989 (guaranteed ray intersections); Hart 1996 (sphere tracing).
These are the competitors to the integral form on the *guarantee* axis: the max formulation can be made rigorous, but only with a Lipschitz constant or inclusion function, per-point adaptive branch-and-bound, and $O(1/\varepsilon)$ evaluations. Framing adopted in the plan (§1.1): from a per-point global optimisation to a per-point quadrature — exact R-function of the sampled union at every $N$, $\omega_f(\Delta t/2)$ bound without a Lipschitz constant, no branching, robustness to null sets, smooth dependence on data; conceded: same resolution requirement at the boundary, $p$-controlled difficulty (Laplace concentration), curse of dimensionality in $k$ parameters.
