#%%
import numpy as np
import numpy.testing as npt
#import pytest

from mycosmo.cosmology import hubble, critical_density


class TestCosmology:
    fid_cosmo = {
        "H0": 70,
        "omega_m_0": 0.3,
        "omega_k_0": 0.0,
        "omega_lambda_0": 0.7,
    }
    H_tolerance = 0.01
    z_range = np.array([0.0, 0.5, 1.0])
    H_expect = np.array([70, 91.60, 123.24])
    cd_expect = np.array([9.2e-27, 1.6e-26, 2.9e-26])
    cd_tolerance = 1e-26

    def test_hubble(self):
        H_vals = hubble(self.z_range, self.fid_cosmo)

        npt.assert_allclose(
            H_vals,
            self.H_expect,
            atol=self.H_tolerance,
            err_msg=(
                "The H(z) differs from expected values by more than "
                f"{self.H_tolerance} decimal places."
            ),
        )

    def test_crit_dens(self):
        cd_vals = critical_density(self.z_range, self.fid_cosmo)
        npt.assert_allclose(
            cd_vals,
            self.cd_expect,
            atol=self.cd_tolerance,
            err_msg=(
                "The critical density of z differs from expected values by more than "
                f"{self.cd_tolerance} decimal places."
            ),
        )

# %%
