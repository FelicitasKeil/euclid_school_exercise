"""Cosmology.

This module implements various cosmology routines.

"""
import numpy as np
from .constants import Mpc, G

def hubble(redshift, cosmo_dict):
    """Hubble Parameter.
     Calculate the Hubble parameter at a given redshift using the cosmological parameter values provided.

    Parameters
    ----------
    redshift : float or numpy.ndarray
        Redshift(s) at which the Hubble parameter should be calculated
    cosmo_dict : dict
        Dictionary of cosmological constants. 
    """
    hubble_const = cosmo_dict["H0"]
    matter = cosmo_dict["omega_m_0"] * (1 + redshift) ** 3
    curvature = cosmo_dict["omega_k_0"] * (1 + redshift) ** 2
    dark_energy = cosmo_dict["omega_lambda_0"]

    return np.sqrt(hubble_const**2 * (matter + curvature + dark_energy))

def critical_density(redshift, cosmo_dict):
    H_z_si = hubble(redshift, cosmo_dict) * 1e3 / Mpc

    return (3.0 * H_z_si**2) / (8.0 * np.pi * G)

"""
    cosmo_dict : dict
        Dictionary of cosmological constants. Must contain the following keys:

        * ``H0``: The Hubble parameter value at redshift zero.
        * ``omega_m_0``: The matter density at redshift zero.
        * ``omega_k_0``: The curvature density at redshift zero.
        * ``omega_lambda_0``: The dark energy density at redshift zero.
"""

fid_cosmo = {
        "H0": 70,
        "omega_m_0": 0.3,
        "omega_k_0": 0.0,
        "omega_lambda_0": 0.7,
        }
crit_dens = critical_density(1.0, fid_cosmo)
print(crit_dens)
# %%
