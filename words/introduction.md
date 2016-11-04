Introduction
------------

// What is the current state of cosmo sims (re: eos).

Subgrid physics is the key to producing a cosmological simulation that is both efficient and representative. Due to the finite resolution of such a simulation, these subgrid models can allow for unresolved physics to be included in the simulation, in particular the turbulent feedback from star formation. These subgrid models are becoming increasingly important due to the inclusion of hydrodynamics in fully *n-body* simulations, rather than ones specified by *semi-anlaytic* models.

As it turns out, this feedback is incredibly important in helping stable disks form: too little and the disk has an unhelpfully small jeans length and clumps together, too much and the disk is Toumre unstable and is ripped apart by the tidal forces on the disk. Hence, the key to forming a representitve population of galaxies lies within the specified subgrid model.

// Why do we need an improved equation of state?

Current cosmological simulations (<REFERNECES>) utilise an <ADIABATIC?> equation of state,

$$
	P_{eos} \propto \rho_g^{4/3}~,
$$

which ensures that the Jeans mass is independent of density meaning that fragmentation due to the finite simulation resolution is avoided. However, it can be argued that the reason this clumping occurs is due to an incomplete equation of state; if more parameters were specified then perhaps one would find a more representative sample of simulated galaxies <REFERENCES>.

Such a model would need to include other sources of pressure in the gas, and any effects that this would have inside a resolution element.

// Different types of pressure

There are several different forms that this 'extra' pressure can take.

+ Thermal Pressure: caused by the random motions of gas particles
+ Turbulent Pressure: caused by 'stirring' of the gas on different length scales
+ Radiation Pressure: from nearby stars, supernovae, etc.

Several authors <REFERNECES> have argued that the main contribution to the overall pressure in the ISM is due to turbulent pressure acting on various length scales.

// Where can we start?

The issue with this is that it is key that the source of this pressure is discovered, allowing it to be included in the subgrid model. The leading idea is that the overwhelming majority of this turbulent pressure arises from supernova feedback in the ISM, however some authors <REFERENCES> have aruged that this turbulent pressure could arise from gravitational interactions within the gas.

// Layout

The structure of this report is as follows. In section 2, we lay out several models of the interstellar medium. In section 3, we test these models on galactic-scale simulations using the GADGET-2 simulation code. In section 4, we aim to improve these models, combining them where appropriate, testing this result in section 5. In section 6 we return to give an overview of the completed work.
