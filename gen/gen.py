import numpy as np
import dists


class Generator:
    def __init__(self, n_DM, n_gas, M_halo, M_disk, R_NFW, c_NFW, R_gas, max_gas, Z_gas, G=1):
        self.n_DM = n_DM
        self.n_gas = n_gas
        self.M_halo = M_halo
        self.M_disk = M_disk
        self.R_NFW = R_NFW
        self.c_NFW = c_NFW
        self.R_gas = R_gas
        self.max_gas = max_gas
        self.Z_gas = Z_gas
        self.G = G

        self._gen_dm()
        self._gen_gas()
        
        return 0

    
    def _gen_dm(self):
        nfw_gen = dists.NFW(self.R_NFW, self.c_NFW)
        
        self.dm_theta = 2*np.pi*np.random.rand(self.n_DM)
        self.dm_phi = np.pi*np.random.rand(self.n_DM)
        self.dm_r = nfw_gen.gen(self.n_DM)

        return self.dm_theta, self.dm_phi, self.dm_r


    def _gen_gas(self):
        gas_gen_r = dists.GasR(self.R_gas, self.max_gas)
        gen_gas_z = dists.GasZ(self.Z_gas)
        
        self.gas_theta = 2*np.pi*random.rand(self.n_gas)
        self.gas_z = gen_gas_z.gen(self.n_gas)
        self.gas_r = gen_gas_r.gen(self.n_gas)

        return self.gas_theta, self.gas_z, self.gas_r


    def _m_in_r(self, r):
        prefactor = self.M_halo/(np.log(self.c_NFW + 1) - self.c_NFW/(self.c_NFW + 1))
        return prefactor*(np.log((self.R_NFW + r)/self.R_NFW) - r/(self.R + r))


    def _mod_v(self, r):
        return np.sqrt(self.G * self._m_in_r(r)/r)

