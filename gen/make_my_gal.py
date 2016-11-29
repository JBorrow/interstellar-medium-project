# Plugs together writer.py and gen.py *and* dists.py. Wow. What a day.

from gen import Generator
from writer import *
import h5py

filename = "TestICs.0.hdf5"
n_DM = int(1e5)
n_gas = int(1e5)
M_halo = 1e12
M_disk = 1e10
R_NFW = 20
c_NFW = 40
R_gas = 10
max_gas = 30
Z_gas = 2
G = 4.302e-6 # kpc Ms km/s 

print("Generating particles, this may take some time")
gen = Generator(n_DM, n_gas, M_halo, M_disk, R_NFW, c_NFW, R_gas, max_gas, Z_gas, G)

print("Writing to HDF5")
op = h5py.File(filename, 'w')

print("Writing head")
write_head(op, [n_gas, n_DM, 0, 0, 0, 0], [M_disk/n_gas, M_halo/n_DM, 0, 0, 0, 0], 0, z=1)
print("Writing gas")
write_block(op, 0, np.array([gen.gas_x, gen.gas_y, gen.gas_z]).T, np.array([gen.gas_v_x, gen.gas_v_y, gen.gas_v_z]).T, np.arange(0, n_gas))
print("Writing dm")
write_block(op, 1, np.array([gen.dm_x, gen.dm_y, gen.dm_z]).T, np.array([gen.dm_v_x, gen.dm_v_y, gen.dm_v_z]).T, np.arange(n_gas, n_gas + n_DM))
