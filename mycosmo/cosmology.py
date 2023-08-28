#%%
import numpy as np
from mycosmo.constants import Mpc, G

def hubble(redshift, cosmo_dict):
    hubble_const = cosmo_dict["H0"]
    matter = cosmo_dict["omega_m_0"] * (1 + redshift) ** 3
    curvature = cosmo_dict["omega_k_0"] * (1 + redshift) ** 2
    dark_energy = cosmo_dict["omega_lambda_0"]

    return np.sqrt(hubble_const**2 * (matter + curvature + dark_energy))

def critical_density(redshift, cosmo_dict):
    H_z_si = hubble(redshift, cosmo_dict) * 1e3 / Mpc

    return (3.0 * H_z_si**2) / (8.0 * np.pi * G)

fid_cosmo = {
        "H0": 70,
        "omega_m_0": 0.3,
        "omega_k_0": 0.0,
        "omega_lambda_0": 0.7,
        }
crit_dens = critical_density(1.0, fid_cosmo)
print(crit_dens)
# %%
