# Рвачёв, §3 «Принцип двойственности», с. 21 — упражнение 3

**Задача.** Описать множество всех логических формул $F(A_1,\dots,A_n)$, для которых $F\cap F^*=\varnothing$. Будет ли при этом $F\cup F^*=I$?

Как и в упражнении 2, равенства понимаются как **тождества**: они должны выполняться при любом выборе множеств $A_1,\dots,A_n\subset I$. Две тождественно равные формулы считаем одной и той же.

---

## 0. Напоминание определений

- $F(A_1,\dots,A_n)$ — формула, составленная из букв $A_1,\dots,A_n$ и символов $\cap,\ \cup,\ \overline{\phantom{A}},\ \varnothing,\ I$.
- $F^*$ — *двойственная* формула: в записи $F$ формально заменяются $\cap\leftrightarrow\cup$ и $\varnothing\leftrightarrow I$; черты дополнения и буквы не меняются.

Примеры: $(A\cap B)^*=A\cup B$; $\big((A\cap\overline B)\cup(\overline A\cap B)\big)^*=(A\cup\overline B)\cap(\overline A\cup B)$; $\varnothing^*=I$; $A^*=A$.

---

## 1. Два инструмента

### 1.1. Лемма о двойственности

> **Лемма (L).** Для любой формулы $F$
> $$F^*(A_1,\dots,A_n)\equiv\overline{F(\overline{A_1},\dots,\overline{A_n})}.$$

Смысл: двойственную формулу можно получить не заменой символов, а подстановкой дополнений вместо всех аргументов с последующим дополнением результата.

*Доказательство* — полная индукция по числу $k(F)$ символов операций $\cap,\cup,\overline{\phantom{A}}$ в $F$. Обозначим $\widehat F=\overline{F(\overline{A_1},\dots,\overline{A_n})}$ и $\overline A=(\overline{A_1},\dots,\overline{A_n})$.

*База $k=0$.* $F=A_i$: $F^*=A_i=\overline{\overline{A_i}}=\widehat F$. $F=\varnothing$: $F^*=I=\overline{\varnothing}=\widehat F$. $F=I$: $F^*=\varnothing=\overline I=\widehat F$.

*Шаг.* Пусть утверждение верно для всех формул с не более чем $k$ операциями, и $k(F)=k+1$. Внешняя операция $F$ — одна из трёх.

- $F=\overline G$, $k(G)=k$. Тогда $F^*=\overline{G^*}=\overline{\overline{G(\overline A)}}=G(\overline A)$, и $\widehat F=\overline{\overline{G(\overline A)}}=G(\overline A)$.
- $F=G\cap H$, $k(G),k(H)\le k$. Тогда $F^*=G^*\cup H^*=\overline{G(\overline A)}\cup\overline{H(\overline A)}=\overline{G(\overline A)\cap H(\overline A)}=\overline{F(\overline A)}=\widehat F$ (закон де Моргана).
- $F=G\cup H$: так же, с другим законом де Моргана. $\square$

### 1.2. Коды точек и булева функция формулы

Для точки $x\in I$ её **код** — набор $\alpha(x)=(\alpha_1,\dots,\alpha_n)\in\{0,1\}^n$, где $\alpha_i=1$, если $x\in A_i$, и $\alpha_i=0$ иначе. Точки с одним кодом $\alpha$ образуют **конституенту** $K_\alpha=A_1^{\alpha_1}\cap\dots\cap A_n^{\alpha_n}$ ($A^1=A$, $A^0=\overline A$); конституент $2^n$, они не пересекаются и покрывают $I$.

Принадлежность $x$ множеству $F(A_1,\dots,A_n)$ зависит только от кода $x$ (индукция по $k(F)$: для букв это так по определению кода, а операции $\cap,\cup,\overline{\phantom A}$ сохраняют это свойство). Поэтому формуле отвечает булева функция $f:\{0,1\}^n\to\{0,1\}$ — её таблица истинности, получаемая заменой $\cap\to\wedge$, $\cup\to\vee$, черта $\to$ отрицание, $\varnothing\to0$, $I\to1$, — и
$$x\in F(A_1,\dots,A_n)\iff f(\alpha(x))=1,\qquad F=\bigcup_{\alpha:\ f(\alpha)=1}K_\alpha .$$

Два факта, которые будут нужны.

**(i) Тождества = равенства функций.** $F\equiv G$ тогда и только тогда, когда $f=g$ как функции на $\{0,1\}^n$. Действительно, если $f=g$, то $F$ и $G$ — одно и то же объединение конституент при любых $A_i$. Если же $f(\alpha_0)\ne g(\alpha_0)$ для какого-то набора $\alpha_0$, возьмём $I=\{0,1\}^n$ и $A_i=\{\alpha:\alpha_i=1\}$; тогда $K_{\alpha_0}=\{\alpha_0\}\ne\varnothing$, и точка $\alpha_0$ лежит ровно в одном из множеств $F$, $G$.

**(ii) Функция двойственной формулы.** Замена $A_i\to\overline{A_i}$ переводит код каждой точки в побитовое дополнение $\bar\alpha=(1-\alpha_1,\dots,1-\alpha_n)$. Поэтому $x\in F(\overline A)\iff f(\bar\alpha(x))=1$, и по лемме (L)
$$x\in F^*(A)\iff x\notin F(\overline A)\iff f(\bar\alpha(x))=0,\qquad\text{т.е.}\qquad f^*(\alpha)=\overline{f(\bar\alpha)} .$$

---

## 2. Решение

### 2.1. Переводим условие на язык функций

По (i) тождество $F\cap F^*=\varnothing$ равносильно тому, что функция формулы $F\cap F^*$ тождественно равна нулю:
$$f(\alpha)\wedge f^*(\alpha)=0\quad\text{для всех }\alpha\in\{0,1\}^n .$$
Подставим (ii): $f(\alpha)\wedge\overline{f(\bar\alpha)}=0$, то есть

$$\text{если } f(\alpha)=1,\ \text{то } f(\bar\alpha)=1 \qquad\text{для всех }\alpha. \tag{1}$$

### 2.2. Условие (1) равносильно симметрии $f(\alpha)=f(\bar\alpha)$

Условие (1) с виду одностороннее, но оно должно выполняться для **всех** наборов, в том числе для $\bar\alpha$ вместо $\alpha$. Поскольку $\overline{\bar\alpha}=\alpha$, получаем: если $f(\bar\alpha)=1$, то $f(\alpha)=1$. Вместе с (1) это даёт
$$f(\alpha)=1\iff f(\bar\alpha)=1,\qquad\text{т.е.}\qquad f(\alpha)=f(\bar\alpha)\ \ \text{для всех }\alpha. \tag{2}$$
Обратно, из (2) следует (1) очевидно. Итак, (1) $\iff$ (2).

На языке множеств (2) означает
$$F(\overline{A_1},\dots,\overline{A_n})\equiv F(A_1,\dots,A_n): \tag{2$'$}$$
**формула не меняется при дополнении всех аргументов.** Назовём такие формулы *чётными* (по аналогии с чётными функциями $\varphi(-x)=\varphi(x)$).

То же рассуждение можно провести прямо в множествах: $F\cap F^*=\varnothing$ означает $F^*\subseteq\overline F$; по (L) $F^*=\overline{F(\overline A)}$, так что $\overline{F(\overline A)}\subseteq\overline{F(A)}$, т.е. $F(A)\subseteq F(\overline A)$ при любых $A$. Подставляя $\overline A$ вместо $A$: $F(\overline A)\subseteq F(A)$. Значит, $F(\overline A)=F(A)$.

### 2.3. Описание всех чётных формул

Наборы $\{0,1\}^n$ разбиваются на $2^{n-1}$ пар противоположных $\{\alpha,\bar\alpha\}$ (набор не может совпадать со своим дополнением). Условие (2) говорит, что $f$ **постоянна на каждой паре**, а значения на разных парах независимы. Отсюда:

> **Теорема.** $F\cap F^*\equiv\varnothing$ тогда и только тогда, когда $F$ тождественно равна объединению **целых пар** конституент:
> $$F\equiv\bigcup_{\alpha\in T}\big(K_\alpha\cup K_{\bar\alpha}\big),\qquad K_\alpha=A_1^{\alpha_1}\cap\dots\cap A_n^{\alpha_n},$$
> где $T$ — произвольное множество представителей пар $\{\alpha,\bar\alpha\}$ (по одному от каждой выбранной пары). Разным наборам выбранных пар отвечают разные формулы, поэтому таких формул ровно $2^{2^{n-1}}$.

*Доказательство.* Если $F\cap F^*\equiv\varnothing$, то по 2.1–2.2 $f$ удовлетворяет (2), и множество $\{\alpha:f(\alpha)=1\}$ вместе с каждым $\alpha$ содержит $\bar\alpha$, т.е. является объединением пар; $F$ — объединение соответствующих $K_\alpha\cup K_{\bar\alpha}$. Обратно, для формулы такого вида $f(\alpha)=f(\bar\alpha)$, откуда $f(\alpha)\wedge f^*(\alpha)=f(\alpha)\wedge\overline{f(\bar\alpha)}=f(\alpha)\wedge\overline{f(\alpha)}=0$, т.е. $F\cap F^*\equiv\varnothing$. Различность — по (i). Число: каждую из $2^{n-1}$ пар либо берём, либо нет. $\square$

**Более удобная (замкнутая) форма.** При $n\ge2$ чётные формулы — это в точности формулы вида
$$\boxed{\;F\equiv H\big(A_1\triangle A_2,\ A_1\triangle A_3,\ \dots,\ A_1\triangle A_n\big)\;}$$
где $H$ — **произвольная** формула от $n-1$ аргументов, а $X\triangle Y=(X\cap\overline Y)\cup(\overline X\cap Y)$ — симметрическая разность.

*Почему.* Во-первых, всякая такая формула чётна: $\overline{A_1}\triangle\overline{A_i}=A_1\triangle A_i$ (точка лежит ровно в одном из двух множеств тогда и только тогда, когда она лежит ровно в одном из их дополнений), поэтому замена $A_i\to\overline{A_i}$ не меняет ни один аргумент $H$. Во-вторых, всякая чётная $F$ так представима: положим $H(B_2,\dots,B_n)=F(\varnothing,B_2,\dots,B_n)$ и проверим тождество $F(A)=H(A_1\triangle A_2,\dots,A_1\triangle A_n)$ поточечно. Пусть $x$ имеет код $\alpha$. Если $\alpha_1=0$, то $x\in A_1\triangle A_i\iff x\in A_i$, так что код $x$ относительно набора $(\varnothing,A_1\triangle A_2,\dots)$ равен $(0,\alpha_2,\dots,\alpha_n)=\alpha$ и правая часть содержит $x$ тогда же, когда $f(\alpha)=1$. Если $\alpha_1=1$, то $x\in A_1\triangle A_i\iff x\notin A_i$, код равен $(0,\bar\alpha_2,\dots,\bar\alpha_n)=\bar\alpha$, и правая часть содержит $x$ тогда же, когда $f(\bar\alpha)=1$; по (2) это то же, что $f(\alpha)=1$. Соответствие $H\mapsto F$ взаимно однозначно ($H$ восстанавливается как $F(\varnothing,B_2,\dots,B_n)$), и снова получаем $2^{2^{n-1}}$ формул.

Неформально: чётная формула «не видит» самих множеств — только то, *совпадают или различаются* состояния принадлежности точки разным множествам.

---

## 3. Ответ на второй вопрос: будет ли $F\cup F^*=I$?

**Да, всегда** — и более того, оба условия равносильны друг другу и равносильны чётности.

По (ii) $f^*(\alpha)=\overline{f(\bar\alpha)}$. Если $F$ чётна, т.е. $f(\bar\alpha)=f(\alpha)$, то
$$f^*(\alpha)=\overline{f(\alpha)}\quad\text{для всех }\alpha,\qquad\text{т.е.}\qquad F^*\equiv\overline F .$$
Тогда $F\cup F^*=F\cup\overline F=I$ и $F\cap F^*=F\cap\overline F=\varnothing$ одновременно.

Обратно, пусть $F\cup F^*\equiv I$. Тогда $f(\alpha)\vee\overline{f(\bar\alpha)}=1$ для всех $\alpha$, т.е. «если $f(\bar\alpha)=1$, то $f(\alpha)=1$»; применяя это к $\bar\alpha$ вместо $\alpha$, получаем и обратную импликацию, откуда $f(\alpha)=f(\bar\alpha)$ — чётность.

Итого для любой формулы $F$ равносильны:
$$F\cap F^*\equiv\varnothing\quad\Longleftrightarrow\quad F\cup F^*\equiv I\quad\Longleftrightarrow\quad F^*\equiv\overline F\quad\Longleftrightarrow\quad F(\overline{A_1},\dots,\overline{A_n})\equiv F(A_1,\dots,A_n).$$

Замечание: для *произвольной* формулы ни из $F\cap F^*=\varnothing$ не следует $F\cup F^*=I$, ни наоборот, «по общим соображениям» — это следует только потому, что каждое из условий влечёт жёсткую симметрию (2). Например, для $F=A\cap B$ имеем $F^*=A\cup B$, $F\cap F^*=A\cap B\ne\varnothing$ и $F\cup F^*=A\cup B\ne I$: ни то, ни другое.

---

## 4. Примеры

### $n=1$
Пары наборов: одна, $\{0,1\}$. Чётные формулы: $\varnothing$ и $I$. Проверка: $\varnothing^*=I$, $\varnothing\cap I=\varnothing$, $\varnothing\cup I=I$. Формулы $A$ и $\overline A$ не подходят: $A\cap A^*=A\cap A=A\ne\varnothing$.

### $n=2$
Пары: $\{00,11\}$ и $\{01,10\}$. Четыре чётные формулы:

| взятые пары | $F$ | $F^*$ (формально) | $F\cap F^*$ | $F\cup F^*$ |
|---|---|---|---|---|
| ни одной | $\varnothing$ | $I$ | $\varnothing$ | $I$ |
| $\{01,10\}$ | $A\triangle B=(A\cap\overline B)\cup(\overline A\cap B)$ | $(A\cup\overline B)\cap(\overline A\cup B)=(A\cap B)\cup(\overline A\cap\overline B)$ | $\varnothing$ | $I$ |
| $\{00,11\}$ | $(A\cap B)\cup(\overline A\cap\overline B)$ | $(A\cup B)\cap(\overline A\cup\overline B)=A\triangle B$ | $\varnothing$ | $I$ |
| обе | $I$ | $\varnothing$ | $\varnothing$ | $I$ |

В форме $H(A\triangle B)$: $H=\varnothing,\ B_2,\ \overline{B_2},\ I$ соответственно. Здесь хорошо видно, что $F^*=\overline F$: двойственная к $A\triangle B$ — её дополнение.

### $n=3$
$2^{4}=16$ формул вида $H(A\triangle B,\ A\triangle C)$, $H$ — любая из 16 формул от двух аргументов. Например, $H=B_2\cap B_3$ даёт $F=(A\triangle B)\cap(A\triangle C)$ — «$B$ и $C$ обе отличаются от $A$ в точке $x$», т.е. $F=(A\cap\overline B\cap\overline C)\cup(\overline A\cap B\cap C)$: объединение пары конституент $K_{100}\cup K_{011}$. Её двойственная $(A\cup\overline B\cup\overline C)\cap(\overline A\cup B\cup C)$ — это дополнение $F$ (шесть остальных конституент).

---

## 5. Связь с упражнением 2

В упражнении 2 самодвойственные формулы ($F\equiv F^*$) оказались формулами с $f(\bar\alpha)=\overline{f(\alpha)}$ — «нечётными». Здесь условие $F\cap F^*=\varnothing$ выделило «чётные» формулы, $f(\bar\alpha)=f(\alpha)$. Это два крайних случая: у самодвойственной формулы $F\cap F^*=F$, у чётной $F\cap F^*=\varnothing$. Классы равномощны ($2^{2^{n-1}}$), и между ними есть простая биекция: $F$ самодвойственна $\iff$ $F\triangle A_1$ чётна (при дополнении всех аргументов и $F$, и $A_1$ дополняются, а симметрическая разность двух дополнений равна симметрической разности самих множеств).

---

## 6. Сводка

- $F\cap F^*\equiv\varnothing$ $\iff$ $F$ не меняется при дополнении всех аргументов: $F(\overline{A_1},\dots,\overline{A_n})\equiv F(A_1,\dots,A_n)$.
- Все такие формулы: объединения целых пар противоположных конституент $K_\alpha\cup K_{\bar\alpha}$; эквивалентно, $F=H(A_1\triangle A_2,\dots,A_1\triangle A_n)$ с произвольной $H$. Их $2^{2^{n-1}}$.
- Для них автоматически $F^*\equiv\overline F$, поэтому $F\cup F^*\equiv I$ — **да**; более того, $F\cup F^*\equiv I$ выделяет ровно тот же класс формул.
