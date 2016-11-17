Proofs
======

Proof of $p_T = F \dot{\Sigma}_*\left(\frac{P_{fin}}{m_*}\right)$
------------------------------------------------------------------

This equation is rather complicated at a first glance; why should this be the case? One can consider dimensional grounds:

$$
	[p_T] = \frac{[M][L]}{[T]^2[L]^2}~,
$$

$$
	[\dot{\Sigma}_*] = \frac{[M]}{[L]^2[T]}~,
$$

$$
	\left[\frac{P_{fin}}{m_*}\right] = \frac{[L]}{[T]}~,
$$

from which it is obvious that the 'units match' and there must just be some numerical factor $F$ that 'makes it work'. However, this is not a satisfactory 'proof', and some conceptual insight would be helpful so that we can consider where this equation is appropriate. 

Under normal conditions, at least in disk galaxies, one would assume that the supernova rate (here $\dot{\Sigma}_s$) is simply proportional to the star formation rate (i.e. stars that die are replaced by an equal number of stars over time)^[note that this corresponds to a rate of change of surface density of each respective variable].

$$
	\dot{\Sigma}_s = K_1 \dot{\Sigma}_*~.
$$

To deal with the fact that this is a surface density, instead of a surface number density, we will set

$$
	m_s = K_2 m_*~,
$$

and hence

$$
	\dot{\Sigma}_{s, ~num. ~density} = \frac{K_1}{K_2} \dot{\Sigma}_*~.
$$

If each supernova injects $P_{fin}$ of momentum, then the rate of momentum injection (i.e. a force) by $n$ supernovae is (up to an efficiency factor $K_3$)

$$
	F = K_3\dot{n}P_{fin}~,
$$

Now, using the above surface number density, we can retrive an effective pressure:

$$
	p_T = \frac{K_1 K_3}{K_2} \dot{\Sigma}_* \left(\frac{P_{fin}}{m_*}\right)~,
$$

which recovers Marizzi's result. The issue here is that @martizzi2016 argues that the factor,

$$
	F = \frac{K_1 K_3}{K_2}~,
$$

is of order unity. Is this reasonable? Let us examine:

$$
	F = \frac{(\mathrm{SFR ~to ~SNR}) (\mathrm{efficiency ~of ~p ~to ~F ~conversion})}{(\mathrm{m_s/m_*})}~.
$$

There is no reason at all that this $F$ should be of order unity.

