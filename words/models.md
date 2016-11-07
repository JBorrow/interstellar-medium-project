Models of the Interstellar Medium
---------------------------------

Ideally, one would like to consider a fully physically-motivated model of the interstellar medium that can be solved analytically to give a simple equation of state,

$$
	P_{eos} \propto \rho^\alpha~.
$$

This, in practice, is not always possible which has lead several authors to run high resolution, small scale simulations of the evolution of supernova remenants (SNRs) which can then be fit to find a subgrid specification.

There are, of course, other authors who have taken the analytical approach. We will analyse both of these approaches in detail in the following sections.


The Fitting Approach
--------------------

Here we will focus on the work of <that paper that I liked>, however similar work is reported in <other references>.

In this approach, many high spatial resolution simulations are performed of relatively small regions containing SNRs. In @joung2009, these simulations had a spatial resolution of 1.95 pc (compared to @schaye2014's ~700 pc resolution for a cosmological simulation). The authors of @joung2009 used varying supernova rates of 1x to 512x the galactic supernova rate in an attempt to make a fit for

$$
	P_{turb} = k \rho^{\alpha}~.
$$

In @joung2009, an isobaric equation of state subgrid model in the high spatial-resolution simulations are used.

// We should find other papers using different initial EOS.

They find, after extensive analysis, that

$$
	P_{turb} = k \rho^{0.88 \pm 0.05}~.
$$

In these models, whether turbulent pressure is gravity or SNR driven is 'built in' as both of these are numerically calulated during the simulation. In pure analytic models, though, this distinction is more tricky.


Analytic Models
---------------

These models, by their natures, are considerably more challenging to construct. There is some tension in the literature <ref> on whether turbulence is driven by SNR feedback (@martizzi2016) or by gravity (@krumholtz2016). It is worth noting that these authors also attempt to compare their models with high resolution simulations, avoiding the fitting parameters that the above models use.

The authors of @martizzi2016 take the approach that turbulence is purely driven by SNR feedback (or, at the very least, that the effect of gravity is negligeable). They write that

$$
	P_{turb} \approx F \dot{\Sigma}_* \left(\frac{P_{fin}}{m_*}\right)~.
$$

They also aim to derive a second equation from hydrostatic equilibrium

$$
	P_{turb} \approx \pi G \Sigma_{gas}\Sigma_*~.
$$

They show that by combining these equations, they can retrieve the Kennicutt-Schmidt law ($\dot{\Sigma}_* \propto \Sigma_{gas}^2$)

$$
	\dot{\Sigma}_* \approx \frac{\pi G}{F\left(\frac{P_{fin}}{m_*}\right) f_{gas}} \Sigma^2_{gas}~,
$$

if the prefactors do not depend on the surface density. This is tenuous at best; previously they had used that

$$
	\left(\frac{P_{fin}}{m_*}\right) = 1,420 ~\mathrm{km/s}~ \left(\frac{n_H}{100 ~\mathrm{cm}^{-3}}\right)^{-0.160}~,
$$

from @martizzi2015 for the momentum injection per supernova. This expression depends directly on the density of hydrogen in the disk. For high gas fractions at the very least this implies that the prefactor depends direcly on $1/\Sigma_{gas}$ leading to $\dot{\Sigma}_* \propto \Sigma_{gas}$.

Their analysis leads to a prediction that the turbulent pressure is a very weak function of the disk properties; every disk should have a similar turbulent pressure. This is in direct tension with @joung2009's work who find that the turbulent pressure should be a realtively strong function of the denisty in the disk. This issue must be resolved; there are two competing subgrid models that both predict very different outcomes. In the next section we test these models in galactic-size simulations.


