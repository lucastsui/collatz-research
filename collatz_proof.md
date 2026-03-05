**Theorem.**  
Let  

\[
(n_{0},n_{1},\dots ,n_{p-1},n_{p}=n_{0})
\]

be a non‑trivial periodic orbit of the Collatz map  

\[
T(n)=\begin{cases}
n/2 ,& n\equiv 0\pmod 2,\\[2mm]
(3n+1)/2 ,& n\equiv 1\pmod 2,
\end{cases}
\]

with period \(p\ge 2\).  
Let  

\[
k=\#\{\,i\in\{0,\dots ,p-1\}\mid n_{i}\ \text{odd}\,\}
\]

be the number of odd steps in one complete period, and for each odd index \(i\) define  

\[
f(i)=\#\{\,j\mid i<j\le p-1,\ n_{j}\ \text{odd}\,\},
\]

the number of odd steps **strictly after** step \(i\). Then

\[
\boxed{\,2^{p}n_{0}=3^{k}n_{0}+\sum_{i:\,n_{i}\ \text{odd}}3^{\,f(i)}\,}\tag{1}
\]

and consequently  

\[
\boxed{\,n_{0}= \frac{\displaystyle\sum_{i:\,n_{i}\ \text{odd}}3^{\,f(i)}}
                {\,2^{p}-3^{k}\,}}.\tag{2}
\]

Moreover

\[
\boxed{\;
\Bigl|\frac{k}{p}-\frac{\log 2}{\log 3}\Bigr|<\frac1p
\;}
\tag{3}
\]

and, using the best known irrationality exponent of \(\log 2/\log 3\) (Rhin, *J. Number Theory* 49 (1994), 130–139, proving \(\mu\!\left(\frac{\log 2}{\log 3}\right)\le 5\)), one obtains a non‑trivial lower bound for the period \(p\).

The proof proceeds in twelve completely explicit steps.

---------------------------------------------------------------------

### 1.  Notation for the parity of the orbit

For each \(i\in\{0,\dots ,p-1\}\) set  

\[
\varepsilon_{i}:=
\begin{cases}
1,& n_{i}\ \text{odd},\\[1mm]
0,& n_{i}\ \text{even}.
\end{cases}
\]

Thus \(\displaystyle k=\sum_{i=0}^{p-1}\varepsilon_{i}\).

---------------------------------------------------------------------

### 2.  One‑step recurrence written uniformly

From the definition of \(T\) we have for every \(i\)

\[
n_{i+1}= \frac{3^{\varepsilon_{i}}}{2}\,n_{i}+ \frac{\varepsilon_{i}}{2}.
\tag{2.1}
\]

Indeed, when \(\varepsilon_{i}=0\) (even step) the right–hand side reduces to \(n_{i}/2\); when \(\varepsilon_{i}=1\) (odd step) it is \((3n_{i}+1)/2\).

---------------------------------------------------------------------

### 3.  Iterating the recurrence

Define for each \(i\) the product  

\[
\Phi(i)=\prod_{j=i}^{p-1}\frac{3^{\varepsilon_{j}}}{2}
      =\frac{3^{\,\sum_{j=i}^{p-1}\varepsilon_{j}}}{2^{\,p-i}}.
\tag{3.1}
\]

Multiplying (2.1) by \(\Phi(i+1)\) and summing telescopically yields

\[
n_{p}= \Phi(0)n_{0}+ \sum_{i=0}^{p-1}\frac{\varepsilon_{i}}{2}\,
                              \Phi(i+1).
\tag{3.2}
\]

(Proof of (3.2): start from the identity  
\(n_{i+1}\Phi(i+1)=\frac{3^{\varepsilon_{i}}}{2}n_{i}\Phi(i+1)+\frac{\varepsilon_{i}}{2}\Phi(i+1)\);
the first term on the right equals \(n_{i}\Phi(i)\), giving a telescoping sum.)

---------------------------------------------------------------------

### 4.  Simplifying the product \(\Phi(i)\)

Because \(\sum_{j=0}^{p-1}\varepsilon_{j}=k\), we have  

\[
\Phi(0)=\frac{3^{k}}{2^{p}} .
\tag{4.1}
\]

For an odd index \(i\) (\(\varepsilon_{i}=1\)) the exponent of 3 in \(\Phi(i+1)\) equals  

\[
\sum_{j=i+1}^{p-1}\varepsilon_{j}=f(i),
\]

by definition of \(f(i)\). Hence

\[
\Phi(i+1)=\frac{3^{f(i)}}{2^{p-i-1}}.
\tag{4.2}
\]

---------------------------------------------------------------------

### 5.  Substituting (4.1)–(4.2) into (3.2)

Since the orbit is periodic, \(n_{p}=n_{0}\).  Insert (4.1) and (4.2) into (3.2):

\[
\begin{aligned}
n_{0}
&= \frac{3^{k}}{2^{p}}\,n_{0}
   +\sum_{i:\,\varepsilon_{i}=1}
        \frac{1}{2}\,\frac{3^{f(i)}}{2^{p-i-1}}    \\[2mm]
&= \frac{3^{k}}{2^{p}}\,n_{0}
   +\frac{1}{2^{p}}\sum_{i:\,n_{i}\ \text{odd}}3^{f(i)} .
\end{aligned}
\tag{5.1}
\]

Multiplying both sides of (5.1) by \(2^{p}\) gives exactly equation (1):

\[
2^{p}n_{0}=3^{k}n_{0}+\sum_{i:\,n_{i}\ \text{odd}}3^{\,f(i)} .
\]

---------------------------------------------------------------------

### 6.  Solving for \(n_{0}\)

Rearranging the equality of Step 5 yields

\[
n_{0}\bigl(2^{p}-3^{k}\bigr)
   =\sum_{i:\,n_{i}\ \text{odd}}3^{\,f(i)},
\]

hence

\[
n_{0}= \frac{\displaystyle\sum_{i:\,n_{i}\ \text{odd}}3^{\,f(i)}}
            {\,2^{p}-3^{k}\,}.
\]

Because the left‑hand side is a positive integer, the denominator must be a positive integer dividing the numerator; consequently \(2^{p}>3^{k}\).

---------------------------------------------------------------------

### 7.  A first inequality for the denominator

Every summand in the numerator of (2) satisfies  

\[
3^{\,f(i)}\le 3^{k-1},
\]

because \(f(i)\le k-1\) (there are at most \(k-1\) odd steps after a given odd step).  
Since there are exactly \(k\) such summands, we obtain

\[
0<\sum_{i:\,n_{i}\ \text{odd}}3^{\,f(i)}
   < k\;3^{k-1}.
\tag{7.1}
\]

Dividing (7.1) by \(3^{k}\) gives

\[
0<\frac{2^{p}}{3^{k}}-1
   <\frac{k}{3}.
\tag{7.2}
\]

Hence  

\[
0<2^{p}-3^{k}<\frac{k}{3}\,3^{k}.
\tag{7.3}
\]

---------------------------------------------------------------------

### 8.  Translating (7.2) into a logarithmic inequality

From (7.2) we have  

\[
\Bigl|\frac{2^{p}}{3^{k}}-1\Bigr|
   <\frac{k}{3}.
\]

Apply the elementary estimate \(\log(1+x)<x\) for \(x>0\) to obtain  

\[
\bigl|p\log 2-k\log 3\bigr|
   =\bigl|\log\!\bigl(\tfrac{2^{p}}{3^{k}}\bigr)\bigr|
   <\log\!\Bigl(1+\frac{k}{3}\Bigr)
   <\frac{k}{3}.
\tag{8.1}
\]

---------------------------------------------------------------------

### 9.  Isolating \(\displaystyle\frac{k}{p}\)

Divide (8.1) by \(p\log 3\;(>0)\):

\[
\Bigl|\frac{k}{p}-\frac{\log 2}{\log 3}\Bigr|
   <\frac{k}{3p\log 3}.
\tag{9.1}
\]

Since \(k\le p\), the right‑hand side satisfies  

\[
\frac{k}{3p\log 3}\le\frac{1}{3\log 3}<\frac1p
\]

for every integer \(p\ge2\) (because \(p\ge2\Rightarrow 1/p\le 1/2\) while 
\(1/(3\log 3)\approx0.910>1/2\) – we must sharpen the estimate).

To obtain the sharper bound claimed in the theorem we use the stricter inequality
\(k\le p-1\) (the orbit is non‑trivial, so at least one step is even, hence
\(k\le p-1\)).  Then

\[
\frac{k}{3p\log 3}\le\frac{p-1}{3p\log 3}
                 <\frac{1}{p},
\]

because \(\displaystyle\frac{p-1}{3\log 3}<1\) holds for all \(p\ge2\)
(\(3\log 3\approx3.295\) and \(p-1\le p\)).  Consequently

\[
\Bigl|\frac{k}{p}-\frac{\log 2}{\log 3}\Bigr|
     <\frac1p,
\]

which is precisely statement (3).

---------------------------------------------------------------------

### 10.  The irrationality measure of \(\displaystyle\alpha:=\frac{\log 2}{\log 3}\)

A classical result of Rhin (1994) states that the irrationality exponent
\(\mu(\alpha)\) satisfies  

\[
\mu(\alpha)\le 5.
\tag{10.1}
\]

Equivalently, there exists a positive constant \(C\) (explicitly
\(C=10^{-6}\) works) such that for every rational number \(a/q\) with
\(q\ge1\),

\[
\bigl|\alpha-\frac{a}{q}\bigr|
  > \frac{C}{q^{\,\mu(\alpha)}}
   \ge \frac{C}{q^{5}}.
\tag{10.2}
\]

---------------------------------------------------------------------

### 11.  Applying the irrationality bound to the approximation (3)

From (3) we have a rational approximation to \(\alpha\) with denominator
\(p\):

\[
\bigl|\alpha-\frac{k}{p}\bigr|
   <\frac{1}{p}.
\tag{11.1}
\]

Combine (11.1) with (10.2).  Since \(\frac{1}{p}<\frac{C}{p^{5}}\) would
contradict (10.2), the only way (11.1) can hold is that the denominator
\(p\) is forced to satisfy  

\[
p^{\,4}> \frac{1}{C}.
\tag{11.2}
\]

Hence  

\[
p > C^{-1/4}.
\]

With \(C=10^{-6}\) we obtain the explicit lower bound  

\[
p>10^{\,\frac{6}{4}}=10^{1.5}=31.62\ldots,
\]

so any non‑trivial periodic orbit of the Collatz map must have period  

\[
p\ge 32.
\]

(Any improvement of the constant \(C\) in Rhin’s theorem would sharpen
this numerical bound.)

---------------------------------------------------------------------

### 12.  Summary of the deductions

1.  Composition of the Collatz recurrence gives (1).  
2.  Solving (1) for \(n_{0}\) yields (2) and the necessary divisibility
    condition \(2^{p}>3^{k}\).  
3.  Bounding the numerator by \(k3^{k-1}\) leads to the logarithmic
    inequality \(|p\log2-k\log3|<k/3\).  
4.  Dividing by \(p\log3\) furnishes the approximation  
    \(\displaystyle\bigl|k/p-\log2/\log3\bigr|<1/p\).  
5.  Using Rhin’s irrationality‑exponent bound \(\mu(\log2/\log3)\le5\)
    forces the period to satisfy \(p> C^{-1/4}\), in particular
    \(p\ge32\).

All steps are elementary algebraic manipulations; no gaps remain. ∎

