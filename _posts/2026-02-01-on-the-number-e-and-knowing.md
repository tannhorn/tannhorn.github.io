---
layout: post
title: "On the number e and knowing"
display_title: "On the number $e$ and knowing"
date: 2026-02-01
---

From a recent <a href="https://youtu.be/JJz5D9txeGA?si=3di4x8ydba_lEuDk" aria-label="Angela Collier — Brought to you by the number e (YouTube video)">YouTube video</a>, I learned that <a href="https://en.wikipedia.org/wiki/Jacob_Bernoulli" aria-label="Jacob Bernoulli on Wikipedia">Jacob Bernoulli</a> discovered the number $e$ in the late 17th century while studying a problem of compound interest. It goes something like this: if an account has yearly compound interest of 100%, depositing an amount $y_0$ will lead to the value in the account being $y_1 = (1+1)y_0 = 2y_0$ at the end of the year. However, if I withdraw the money in the middle of the year and then immediately deposit it again, the result will be:

$$y_1 = \bigg(1+\frac{1}{2}\bigg)\bigg(1+\frac{1}{2}\bigg)y_0 = 2.25y_0,$$

since I compound twice with 100% yearly interest over a period of half a year. But why stop at two periods? I could go ahead and do:

$$y_1 = \bigg(1+\frac{1}{3}\bigg)^3 \approx 2.37 y_0,$$

or:

$$y_1 = \bigg(1+\frac{1}{4}\bigg)^4 \approx 2.44 y_0,$$

and so on. If you took a calculus class, you probably know where I am going with this, i.e.:

$$y_1 = \lim_{n\rightarrow\infty}\bigg(1+\frac{1}{n}\bigg)^n y_0.$$

And maybe you even remember that this limit turns out to be one of the definitions of the Euler's number $e$, i.e.:

$$\frac{y_1}{y_0} = \lim_{n\rightarrow\infty}\bigg(1+\frac{1}{n}\bigg)^n  = e\approx 2.718.$$

Chances are you haven't seen this limit in a long time. For sure _I_ haven't seen it for more than a decade. To be perfectly honest, when looking at this expression, it is not 100% clear to me how this even relates to the exponential function and its base.

One corollary of the above is that, if we change the compounding period from $1$ to $x$, we immediately get:

$$\lim_{n\rightarrow\infty}\bigg(1+\frac{x}{n}\bigg)^n  = e^x.$$

After I learned about limits, the next topic in college were derivatives; if I diferentiate the above expression with respect to $x$ I get:

$$
\begin{aligned}
\frac{d}{dx}e^x
&= \frac{d}{dx}\lim_{n\rightarrow\infty}\bigg(1+\frac{x}{n}\bigg)^n 
= \lim_{n\rightarrow\infty}\frac{d}{dx}\bigg(1+\frac{x}{n}\bigg)^n \\
&= \lim_{n\rightarrow\infty}\frac{n}{n}\bigg(1+\frac{x}{n}\bigg)^{n-1} =\lim_{n\rightarrow\infty}\bigg(1+\frac{x}{n}\bigg)^{n-1}\\
&= \lim_{n\rightarrow\infty}\bigg(1+\frac{x}{n}\bigg)^n \bigg/ \lim_{n\rightarrow\infty}\bigg(1+\frac{x}{n}\bigg). \\
&= e^x / 1 = e^x.
\end{aligned}
$$

Here is the connection to the exponential function! Still further, I did differential equations and their numerical solutions. If I take the equation $dy/dx = y$ and approximate its solution starting at $x_0=0$ with the forward Euler method (this is basically straight from the definition of a derivative, just forgetting the limit $h\rightarrow0$):

$$y(h) \approx y(0) + h y(0) = (1+h)y(0).$$

Seems like I could do this $n$ times in a row to get:

$$y(nh)= (1+h)^ny(0),$$

and if I conveniently choose $nh=1$ and then send $n\rightarrow\infty$, I am basically back where I started:

$$y(1) = \lim_{n\rightarrow\infty}\bigg(1+\frac{1}{n}\bigg)^n y(0) = e\cdot y(0).$$

Thus, $y(x)=e^x$ solves the differential equation $dy/dx=y$. And so it all hangs together very nicely, the limit, the derivative, and the differential equation.

In the two derivations above, I was not very rigorous. I swapped a limit with a derivative, assumed that a limit of a ratio is a ratio of limits and also that a repeated forward Euler step will converge to the true solution with infinitesimal stepping. It was about intuition and showing connections between concepts. But this is not how mathematics is taught. In Calculus 1, I learned about limits, including the one of $(1+1/n)^n$ as $n\rightarrow\infty$. Some months later, I learned about derivatives; some further months later, about differential equations. At no point we circled back to put things back together; in fact, as far as I remember, this is the first time I have done either of the two above derivations.

Of course, there are hundreds of things that have to be taught during calculus classes, it would be impossible to dwell on every concept and discuss subtle connections, especially in a large classroom setting. In fact, I don't even blame professors for introducing:

$$\lim_{n\rightarrow\infty}\bigg(1+\frac{1}{n}\bigg)^n  = e$$

as a context-less definition. When I was taking Calculus 1, if someone had been telling a story about how one of the Bernoullis studied a problem from financial mathematics, I would have nodded along, noted the limit from above and, instead of pondering the ancient masters, focused on the X other topics I had to face as a physics freshman. Then, during the exam, if the professor were to ask what is the definition of $e$, I would have been perfectly capable to write down the limit and likely prove some sort of existence and finiteness. I would have known that limit of $(1+1/n)^n$ as $n\rightarrow\infty$ but I would not have _known_ it. There is a difference between learning and deep, intuitive understanding; the latter being accessible only through careful, active examination and repeated use of knowledge.

Watching a lecturer derive a math identity won't be enough for you to reproduce it two weeks later. Knowing the identity without using it in a broader context will also not be particularly useful. It is the connections between concepts and their applicability in novel settings which make knowledge valuable. Maybe I don't know how to solve ordinary differential equations, but if I know how derivatives of inverse functions work, I can turn $dy/dx=y$ into:

$$\frac{dx}{dy} = \frac{1}{y},$$

getting $x(y)=\log(y)$ and $y(x)=e^x$. Without having some sort of intuition on how to approach a given problem, any number of passed calculus classes won't help much.

Mathematics, especially its more established branches such as undergrad calculus and linear algebra, are built up in classes rigorously, step-by-step, as if one was climbing a well-sculpted staircase. However, one likely doesn't learn that it has taken centuries to chisel it. Calculus has been in use since it was invented in the 17th century by <a href="https://en.wikipedia.org/wiki/Leibniz%E2%80%93Newton_calculus_controversy" aria-label="Leibniz–Newton calculus controversy on Wikipedia">Isaac Newton and Gottfrield Wilhelm Leibniz</a> -- but it was made rigorous only in the 19th century, in particular by <a href="https://en.wikipedia.org/wiki/Karl_Weierstrass" aria-label="Karl Weierstrass on Wikipedia">Karl Weierstrass</a>. Henri Poincaré famously said <a href="https://en.wikiquote.org/wiki/Henri_Poincar%C3%A9" aria-label="Henri Poincaré quote on Wikiquote">"It is by logic that we prove, but by intuition that we discover"</a>. Intuitive understanding precedes rigorous formalism; thus, mathematics are taught in reverse order to its discovery and we can ask the uncomfortable question: at the end of the last class, how much do the students _know_? Has classroom instruction prepared them for technical problem solving or is it detached from real-world use and thus ineffective? 

If you have read so far, you might be expecting me to come up with some sort of solution. Alas, having done only limited teaching, I can only talk from my personal experience. I did about four years of pure classroom instruction and yes, some of the classes I would happily have exchanged for something more practical; nevertheless, many of them were indispensable. Both tacit and explicit knowledge seem to be necessary, it is just that teaching the latter is way easier than the former. Richard Hamming wrote a book on the <a href="https://en.wikipedia.org/wiki/The_Art_of_Doing_Science_and_Engineering" aria-label="The Art of Doing Science and Engineering on Wikipedia">"art of doing science and engineering"</a>. George Pólya presented a system of principles how to approach mathematical problems in <a href="https://en.wikipedia.org/wiki/How_to_Solve_It" aria-label="How to Solve It on Wikipedia">"How to solve it"</a>. Reading both books, I nodded along: these two managed to capture a big chunk of the essence of problem solving, writing it down as accessible knowledge. And yet I doubt I would have understood it---_really understood it_---in my early college years. Hence, a  bit of catch-22: with multiple solved problems under your belt, you can start appreciating Pólya's succinct writing describing the procedure or Hamming's discussion of "style".

Problem solving is both the means and the end of turning knowing into _knowing_ and can be honed only through years of practice. It cannot be taught in clasrooms but that does not mean there is no way of teaching it at all: working along and learning from the experts of the craft is one way. The books of Hamming and Pólya are another: if you use them as companions on your journey, they will help you on a meta level, giving advice on how to turn accidental successes into repeatable ones, systematising the whole process. Assisted by books such as these or not, problem by problem, one makes progress: internalising explicit knowledge and gaining tacit understanding, building a toolbox for tackling technical problems and becoming a skilled person of the craft -- and maybe even teaching someone else along the way. And sometimes, just for the fun of it, one can take their tools out for a small hobby project on the side, like revisiting that somehow arcane definition of the Euler's number all the way back from Calculus 1.

---

### Coda

This short essay started with a recreational math problem and so it will be only fitting if it ends with one, too. Consider the family of power functions $f(x) = x^a$. These have the simple property that:

$$ f'(x) \propto f(x)/x, $$

and:

$$ \int f(x) dx \propto f(x)\cdot x,$$

so one can build the tower of powers from negative infinity to positive infinity...except no. If I take $a=\pm\varepsilon$, the derivative of $x^{\pm\varepsilon}$ is indeed proportional to $x^{\pm\varepsilon-1}$ and I can happily keep differentiating. But if somehow $\varepsilon$ ends up being _exactly_ zero, the derivative of $x^0$ is not a non-trivial function of $1/x$, but rather constant zero! What's even worse, the _integral_ of $1/x$ is $\log(x)$, the natural logarithm. Where did that come from? How does the logarithm relate to the powers of $x$? Somehow, the symmetry of differentiation and integration breaks around $a=0$. Does that mean anything? Is there a way around it? I would imagine if you ask a math specialist, they will have an answer ready to any and all of these questions. But think about them yourself for a bit -- later we can compare our notes.
