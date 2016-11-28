# Plugs together writer.py and gen.py *and* dists.py. Wow. What a day.

from gen import Generator
from writer import *
import h5py

filename = "TestICs.0.h5py"
n_DM = int(1e5)
n_gas = int(1e6)
M_halo = 1e40
M_disk = 1e30
R_NFW = 10
c_NFW = 40
R_gas = 30
max_gas = 10
Z_gas = 4
G = 1

print("Generating particles, this may take some time")
gen = Generator(n_DM, n_gas, M_halo, M_disk, R_NFW, c_NFW, R_gas, max_gas, Z_gas, G)

print("Writing to HDF5")
op = h5py.File(filename, 'w')

print("Writing head")
write_head(op, [n_gas, n_DM, 0, 0, 0, 0], [M_disk/n_gas, M_hal/n_DM, 0, 0, 0, 0], 0, z=1)
print("Writing gas")
write_block(op, 0, [gen.gas_x, gen.gas_y, gen.gas_z], [gen.gas_v_x, gen.gas_v_y, gen.gas_v_z], np.arange(0, n_gas))
print("Writing dm")
write_block(op, 1, [gem.dm_x, gen.dm_y, gen.dm_z], [gen.dm_v_x, gen.dm_v_y, gen.dm_v_z], np.arange(n_gas, n_gas + n_DM))
