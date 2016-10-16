Particle Theory
===============

Lecture 1
---------

QFT combines special relativity and quantum mechanics. A field theory is a collection of operators at each co-ordiante in spacetime. Why do we need QFT?

1. Fields seem to violate causality. We require that $\left[\hat{O_a}, \hat{O_b}\right] = 0$ if $a$, $b$ are spacelike separated.
2. Quantum mechanics and special relativity imply a multi-particle theory. As we make a box that a particle is in smaller, $\Delta E \rightarrow \infty$.

Lecture 2
---------

### Classical Particle Mechanics

The sate of a system is described by generalised co-ordinates, $q_i$,
$$
	q_a(t) = (q_1(t), q_2(t), q_3(t))~,
$$
for a particle in 3D, for example.

### Principle of Least Action

Physics minimises the action,
$$
	S = \int^{t_1}_{t_2} \mathrm{d}t  ~ L(q_a(t), \dot{q}_a(t))~.
$$

We can do this by deforming the path, $q_a(t)$, by some small amount, $\delta q$, and finding the minimum of this action, leading to the *Euler-Lagrange Equations*
$$
	\frac{\partial L}{\partial q_a} =  \frac{\mathrm{d}}{\mathrm{d}t} \frac{\partial L}{\partial \dot{q}_a}~.
$$

### Constructing a Field Theory

Take the continuum limit of a Lagrangian. Example: springs of length $\ell$ connected to masses $m$ sliding on rods.
$$
	L = \sum_a \frac{1}{2}m\dot{q}_a^2 - \frac{1}{2}k \left(\sqrt{\ell^2 + (q_{a+1} - q_a)^2}\right)^2~.
$$
Here we take the limit where $\ell \rightarrow 0$, fixing $\rho = \frac{m}{\ell}$ and using $k = \frac{\kappa}{\ell}$.

In the continuum limit, we use the field $\phi(x)$ instead of $q_a(t)$,
$$
	L = \int \mathrm{d}x \left[\frac{1}{2}\rho \phi^2 - \frac{1}{2} \kappa (\partial_x \phi)^2\right]~.
$$

We define the *Lagrangian Density* (often referred to as just the Lagrangian)
$$
	L = \int \mathcal{L}(\dot{\phi}, \partial_x \phi) ~ \mathrm{d} x~.
$$

This gives us the Euler-Lagrange equations:
$$
	(\partial_t^2 - c^2 \partial_x^2)\phi = 0~,
$$
after the rescaling $\phi \rightarrow \frac{\phi}{\sqrt{\rho}}$, $\frac{\kappa}{\rho} = c^2$. This is a field - it has a value $\forall x, t$.

### Particle Physics

We will consider only Lorentz Scalar, local Lagrangians of the form
$$
	\mathcal{L} = \mathcal{L}(\phi(x), \partial_\mu\phi(x))~.
$$

Correspondence between field theory and particle mechanics:

| Particle | Field |
|:--------:|:-----:|
| $q_a(t)$ | $\phi(x)$ |
| $S = \int\mathrm{d}t ~ L(q, \dot(q))$ | $S = \int \mathrm{d}^4x ~ \mathcal{L}(\phi(x), \partial_\mu \phi(x))$ |
| $\frac{\partial L}{\partial q_a} = \frac{\mathrm{d}}{\mathrm{d}t}\left(\frac{\partial L}{\partial \dot{q}_a}\right)$ | $\frac{\partial \mathcal{L}}{\partial \phi} = \partial_\mu \left(\frac{\partial \mathcal{L}}{\partial(\partial_\mu\phi)}\right)$ |

