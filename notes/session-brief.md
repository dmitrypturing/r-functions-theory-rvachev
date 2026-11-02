# Session brief: reading Rvachev's «Теория R-функций и некоторые её приложения» (1982)

It was a study session with Dmitry. He is reading В. Л. Рвачёв, «Теория R-функций и некоторые её приложения» (Киев, Наукова думка, 1982) page by page to understand the theory. He asks two kinds of things: (a) full solutions of the book's exercises («Упражнения и задачи» at the end of each §), and (b) questions about specific passages: notation, terminology, a step he doesn't follow, a suspected misprint. This brief tells you how the previous session worked, what Dmitry asked for along the way, and where the reading stands.

---

## 1. Materials and how to get to them

- **The book** is a scanned PDF with **no text layer** (pdftotext returns nothing). It is on Dmitry's computer: `/Users/dmitrypopov/Desktop/fxcad/docs/papers/Рвачев В.Л. - Теория R-функций и некоторые ее приложения (1982).pdf`. It has 553 pages. To read a page, stage the file into the cloud workspace with `device_stage_files` and open pages with `Read` (`pages: "21-22"`). **PDF page N = printed book page N.**
- Dmitry often attaches a screenshot of the passage he is asking about. Still open the surrounding pages yourself: the context (the definitions a page or two earlier, the exercise list, the next page) often settles the question.
- **The project** ("Rvacher R-functions theory book") holds the written solutions (§6 below). Read the relevant ones before building on them. Docs named `sweep-*` belong to a different line of work; ignore them unless asked.
- In the previous session the artifact **"The Code Map α"** was published: a picture of the map from points of the universe to codes in {0,1}³, the "Level 2" picture (§5).

---

## 2. Deliverables and language

- **Each exercise gets its own project doc**, `claude/p<page>-task<k>-<slug>.md`, written **in Russian**, using the book's notation, published with `project_write` and `present_to_user: true`. The doc must be **self-contained**.
- **The chat reply is in English.** It names the file and gives a short account of the argument and the answer: what the key idea is and how the proof runs. It is not a copy of the doc.
- **Questions about the text** are answered in the chat, in English, without a doc, unless Dmitry asks for one.
- When Dmitry catches an error, say plainly that he is right, fix the doc, and say what changed. He reads carefully and has caught real mistakes (§5).

---

## 3. Writing style for solutions (Dmitry's explicit request)

Dmitry named two models for the level of detail and the flow of the narrative: **С. А. Теляковский, «Курс лекций по математическому анализу. Семестр I»** and **Feynman's Lectures on Physics.** In practice this means:

1. **It is a lecture, not a stack of lemmas.** Continuous prose with formulas set into it. Each step is motivated *before* it is carried out: "this suggests…", "let us check…", "it remains to…". Proofs run inline in the text. Theorem and lemma headings are used sparingly. The main statement or answer may be set off in a `>` block.
2. **Begin with concrete trials.** Before the general argument, try the simplest cases (n = 1, 2, the formula from the book, A∩B, A△B…), compute them explicitly, notice a pattern, state the guess, then prove it. Feynman's "let's see what happens".
3. **Recast the question in a form that can be checked.** For example, "strictly n-place" (no Φ with fewer arguments exists) becomes "depends essentially on each argument", which one substitution verifies.
4. **Small cases in full.** For n = 2 (and n = 3 when feasible) give the complete enumeration as a table, with each row checked.
5. **General construction, then verification.** Explain where a construction comes from, then verify it directly, ideally once more by a computation in the book's own manner (expanding the formula), in addition to the structural argument.
6. **No unexplained jumps.** No «нетрудно заметить» or «очевидно» over a real step. When a fact is genuinely routine, say why in one sentence.
7. **Self-contained, with explicit recaps.** Dmitry's rule: *you may refer to an earlier result, but if it is "old", restate it explicitly.* In practice, restate the needed fact with its one-paragraph reason and point to where the full proof is ("доказано в упражнении 1, §2").
8. **No "future ideas".** Do not add sections on where the topic leads (R-functions, Post classes, applications) unless asked. The doc ends with a **«Ответ»** section that answers exactly what was asked.
9. Do the exploratory analysis in your own thinking. The written response should be detailed, orderly and consistent.

**Induction must be in the standard form.** Name an explicit natural parameter (for example k(F) = the number of operation symbols ∩, ∪, ‾ in the formula), state P(k), prove the base case, then prove P(k+1) from the hypothesis. If the step needs the hypothesis for all m ≤ k (as for F = G ∩ H, where the subformulas can be much shorter), say so: this is complete induction, which is equivalent to ordinary induction. Dmitry objected to an unlabelled "induction on the construction of the formula".

---

## 4. How to approach the exercises (method that worked)

- **Translate set formulas into codes and truth tables.** Each point x gets a code α ∈ {0,1}ⁿ (α_i = 1 iff x ∈ A_i). Regions (constituents) K_α = A₁^{α₁} ∩ … ∩ Aₙ^{αₙ}. A formula is a union of regions, i.e. a truth table f. Two formulas are identical exactly when their tables coincide. To show that different tables give non-identical formulas, use a configuration with all regions non-empty: two or three intersecting circles, or the universe U = {0,1}ⁿ with A_i = {strings whose i-th digit is 1}. **Call that universe U, not I**: Dmitry was confused by the clash with the constant I.
- **Key identity of §3:** F\*(A₁,…,Aₙ) ≡ ¬F(Ā₁,…,Āₙ). On tables, f\*(α) = ¬f(ᾱ). Complementing all arguments flips every bit, α ↦ ᾱ, so regions swap in 2ⁿ⁻¹ antipodal pairs. Almost every exercise on p. 21 reduces to "what does the condition say about each pair {α, ᾱ}?".
- **Shannon expansion** F = (A₁ ∩ F(I, …)) ∪ (Ā₁ ∩ F(∅, …)) gives constructive descriptions: self-dual ⇔ F = (A₁∩G) ∪ (Ā₁∩G\*).
- **Counting arguments** are often the cleanest route and a good cross-check (μ(n) = μ(n−1)², sorting formulas by their set of essential arguments, binomial recursions).
- **Verify numerically.** Before writing, brute-force small cases with a short Python script (enumerate truth tables for n ≤ 4). In the previous session this confirmed τ = 2, 0, 10, 208.
- **Check every class-inclusion claim on the extreme cases.** Dmitry caught a wrong statement that "all even formulas are balanced". ∅ and I are even but not balanced. Test such claims on ∅, I, and on n = 1, 2 before writing them.
- **Know what kind of exercise it is.** The preface says some exercises are problems whose solutions the author does not know. An exercise can be a quick check, a pointer to a standard theory (the p. 21 exercises sit inside classical Boolean function theory: Post's class S, perfect DNF), or an open problem. If one resists everything, check whether the main text flags it as unsolved.
- Answer what is literally asked, then the intended question. Example: exercise 1 literally has the answer "yes, Ā and B̄", but the real point is that no self-dual operation depends essentially on both arguments.

---

## 5. Notation, conventions and misprints already settled

- **⊂ means ⊆** in this book (the Russian, Bourbaki and Kolmogorov–Fomin convention). Strict relations are written in words or by negation, as in ⊅ on p. 26. The definitions of closed and complete systems only make sense with the non-strict reading.
- **Three levels** used when explaining §3: (1) sets: universe, A_i, F(A); (2) codes: the map α: I → {0,1}ⁿ; (3) the truth table f: {0,1}ⁿ → {0,1} read off the formula. "The Code Map α" artifact illustrates level 2.
- **Конституента**: an atom of the Euler diagram, an intersection in which every A_i appears once, plain or complemented. There are 2ⁿ of them, and they partition I. λ(F) = the number of constituents in F.
- **p. 22**, «уравнения с элементарными коэффициентами»: mainly differential (also algebraic and transcendental) equations written with elementary functions whose solutions are not elementary (Airy, Bessel, Riccati, Abel–Ruffini, Kepler).
- **p. 23**, «алфавит 𝔛»: just the set of values. A proper map 𝔛ⁿ → 𝔛ᵐ has inputs and outputs in the same set, so superposition always makes sense. Words of length n over the alphabet are the elements of 𝔛ⁿ, the operands. Operations are not letters. «Алгебраическая операция» is the general-algebra term (any map 𝔛ⁿ → 𝔛). Ref. [45] is Каргаполов–Мерзляков, «Основы теории групп».
- **p. 25, item 5)**: the set is introduced as T_a and then called 𝔐_a. This is a misprint; read 𝔐_a throughout (T is used on p. 26 for the «признак»).
- **p. 25, Example 2**: "𝔛 = {0, 1]" is a misprint for the interval [0, 1]. Continuity on {0,1} would be vacuous. This is the Kolmogorov–Arnold theorem (Hilbert's 13th problem). It transfers to any [a, b] by an affine change of scale. On ℝⁿ the classical proof fails, because it needs boundedness and uniform continuity, i.e. compactness. The extension to ℝⁿ was stated in the previous session as "if I remember correctly, R. Doss, 1977"; verify before relying on it.

---

## 6. Progress: exercises solved (p. 21, §3 «Принцип двойственности»)

All solution docs are in the project, in Russian, in the style above. Exercises 1–3 were rewritten in this style at the end of the previous session.

| Ex. | Question | Result | Project doc |
|---|---|---|---|
| 1 | A self-dual 2-place F(A,B) other than A, B? | Exactly four self-dual 2-place formulas: A, B, Ā, B̄. Literally "yes" (Ā, B̄), but none depends on both arguments. Contains the full induction proof of F\* ≡ ¬F(Ā). | `claude/p21-task1-binary-selfdual.md` |
| 2 | Describe all self-dual F(A₁,…,Aₙ). | F(Ā) ≡ ¬F(A). Equivalently: unions of regions taking one from each antipodal pair, or F = (A₁∩G) ∪ (Ā₁∩G\*) with G arbitrary. There are 2^{2^{n−1}} of them. n = 3: 6 degenerate, 8 majorities, 2 parities. | `claude/p21-selfdual-formulas.md` |
| 3 | Formulas with F ∩ F\* = ∅; then F ∪ F\* = I? | Exactly the "even" formulas F(Ā) ≡ F(A): unions of whole antipodal pairs, equivalently H(A₁△A₂, …, A₁△Aₙ). For them F\* ≡ F̄, so yes. Moreover F∩F\*=∅ ⇔ F∪F\*=I ⇔ F\*=F̄ ⇔ even. | `claude/p21-task3-F-cap-Fstar.md` |
| 4 | For which n do strictly n-place self-dual formulas exist? | n = 1 and all n ≥ 3; n = 2 is the only exception. Example: F_n = (A₁∩…∩Aₙ) ∪ (Ā₁∩(A₂∪…∪Aₙ)). Counting cross-check: μ(n) = μ(n−1)² versus at most n·μ(n−1) degenerate formulas. | `claude/p21-task4-strictly-n-place.md` |
| 5 | μ(n) is non-decreasing. | Embedding argument (an n-place self-dual formula is (n+1)-place). μ(n) = 2^{2^{n−1}}, μ(n+1) = μ(n)². | `claude/p21-task5-mu-monotone.md` |
| 6 | τ(2) = 0; for which other n is τ(n) = 0? | None among n ≥ 1. Recursion μ(n) = Σ C(n,k)·τ(k) gives τ = 2, 0, 10, 208, 64 386 (n = 1…5; brute-force checked to n = 4). | `claude/p21-task6-tau.md` |
| 7 | Class with λ(F) = λ(F\*). | Always λ(F) + λ(F\*) = 2ⁿ, so the class is λ(F) = 2ⁿ⁻¹ ("balanced", half the diagram); there are C(2ⁿ, 2ⁿ⁻¹). It contains all self-dual formulas, only those even formulas made of exactly half the pairs, and many others. n = 3: 70 = 16 + 6 + 48. | `claude/p21-task7-lambda.md` |

**Reading position:** §4 «Композиция и суперпозиция. Замкнутые множества функций», around pp. 25–26: closed sets, Theorem 1, complete systems, the basis. Exercises after §4 have not been started.

---

## 7. To start

Ask nothing up front. When Dmitry names an exercise or a passage, open the page(s) of the PDF, read the surrounding definitions, check the project docs you will build on, verify any counts by a quick script, write the solution doc in the style of §3, and reply in English with the file name and a short account of the argument.
