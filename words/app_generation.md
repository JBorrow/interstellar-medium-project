Generating Initial Conditions
-----------------------------

To simulate galaxies, we must generate initial conditions such that they can be time-evolved with GADGET. These initial conditions need not be perfect, as we can always run the simulation for a few rotations of the disk so that it can 'sort itself out', but we need a rough approximation of a disk's gas and dark matter with their associated velocities to begin a simulation.

The probability of finding a particle at some position $\vec{x}$ is given by:

$$
	p(\vec{x})\mathrm{d}\vec{x} = \rho(\vec{x})\mathrm{d}V~,
$$

where $\mathrm{d}V$ is a volume element. There are several important density profiles

|   Name   |  Type of Matter  |              Density               | System of Co-ordinates |
|:--------:|:----------------:|:----------------------------------:|:----------------------:|
| NFW Profile | Dark matter | $\rho(r) \propto \frac{R}{r\left(1 + \frac{r}{R}\right)^2}$ | Spherical polar |
| Radial Gas  | Gas | $\rho(r) \propto e^{-r/R}$ | Cylindrical polar |
| Vertical Gas | Gas | $\rho(z) \propto \mathrm{sech}^2\left(\frac{z}{z_0}\right)$ | Cylindrical polar |

We will assume that all other profiles are uniform (for example, $\theta,$ $\phi$ for the NFW profile). To actually generate the particle distributions, though, we need the jacobians such that we can write, for example

$$
	p(r)\mathrm{d}r = \rho(r) f(r) \mathrm{d}r~,
$$

where $f(r)$ is some arbritary function of $r$ that is given by the jacobian. Here we use

$$
	\mathrm{d}V_{r, \theta, \phi} = r^2\sin\phi\mathrm{d}r\mathrm{d}\theta\mathrm{d}\phi ~ ~ ~ \rightarrow ~ ~ ~ \mathrm{d}V_{r} = 4\pi r^2~,
$$
$$
	\mathrm{d}V_{r, \theta, z} = r\mathrm{d}r\mathrm{d}\theta\mathrm{d}z ~ ~ ~ \rightarrow ~ ~ ~ \mathrm{d}V_{r} = 2\pi r \mathrm{d}r ~ ~ ~ \mathrm{d}V_z = 2\pi z \mathrm{d}z~.
$$

### Easy Distributions - Analytical Solution

For the $\rho(z)$ gas profile, it is relatively simple to generate numbers that follow this distribution. This is performed by finding the cumulative distribution function,

$$
	P(z) = \int_{-\infty}^z p(z') \mathrm{d}z'~,
$$

which by definition is bounded by [0, 1]. Hence we can invert the equation for $P(z)$, i.e. find $z(P)$, and generate random numbers uniformly $U(0, 1)$ (which is trivial computationally) and calculate $z(U(0, 1))$ which will generate random numbers with the distribution $p(z)$^[clearly, these are pseudorandom numbers, but this is not important for the discussion here.].

This all hinges on being able to both

+ Calculate $P(z)$ analytically
+ Invert $P(z)$,

which clearly is not a given. For a more complicated distribution, we will need to use the rejection method.

### Hard Distributions - The Rejection Method

The rejection method relies on you being able to find some distribution $f(x)$ that is always above your distribution $p(x)$ which in theory should always be possible as your $p(x)$ must be normalisable, however in practice this is somewhat complicated. The algorithm to generate random variates with the distribution of $p(x)$ is then as follows:

1. Generate random variate $x$ from $f(x)$
2. Generate $f(x) \cdot U(0, 1) = y$
3. If $y \leq p(x)$ keep $x$ else reject $x$.

This has the efficiency $p(x)/f(x)$ where these values represent the total areas under the curves. It is also useful if your $f(x)$ has an invertible $F(x)$ such that it is easy to generate numbers within this distribution, else you will have to use the rejection method to find *those* which becomes very computationally expensive.
