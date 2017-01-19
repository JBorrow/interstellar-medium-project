# The equation of state test for the project
# That was descriptive...

import numpy as np
import matplotlib.pyplot as plt

G = 6.67e-8 # cgs
Pfin = 5.568e43 # cgs
F = 0.15
prefactor = (3./2.)*np.log10(10/F) + (3./4.)*np.log10(G) + (1./2.)*np.log10(Pfin)

mh = 1.67e-24

def model(log_nh):
    # Direct from Robertson, Yoshida, Springel, Hernquist 2004
    # Returns in log(erg/cm3)
    return 0.05*(log_nh**3) - 0.246*(log_nh**2) + 1.749*(log_nh) - 10.6


def my_model(log_nh):
    return prefactor + (5./4.)*(log_nh + np.log10(mh))
    


if __name__ == "__main__":
    xs = np.arange(-2.5, 4, 0.01)
    plt.yscale('log')
    plt.xscale('log')
    plt.plot(10**(xs), 10**(model(xs)), label="Robertson et. al, 2004", color="#950F2C")
    plt.plot(10**(xs), 10**(my_model(xs)), label="This work", color="#006388")
    plt.xlim(10**(-2), 10**(3))
    #plt.ylim(10**(-16), 10**(-6))

    plt.xlabel("$n_H$  [cm$^{-3}$]")
    plt.ylabel("$P$  [erg cm$^{-3}$]")

    plt.legend(loc='best')


    plt.show()


