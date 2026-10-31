
# Planetary Values
import numpy as np
import Inputs as inp

# JPL Horizons state vectors:
# Epoch: 2026-10-22 00:00:00 TDB
# Reference frame: Ecliptic of J2000.0
# Origin: Solar System Barycenter
# Original units: km and km/s
# Converted units: metres and metres/second

AU = 1.495978707e11  # metres

planets = {
    "rocket": {
        "mass": inp.m,
        "velocity": np.array([0.0, 0.0, 0.0]),
        "position": np.array([0.0, 0.0, 0.0]),
        "radius": 24.0, #random value, not important
        "Engine_acceleration": 0,
        "mass_loss": 0
    },

    "sun": {
        "mass": 1.9885e30,
        "radius": 6.957e8,
        "position": np.array([
            -1.673824792216653e8,
            -7.608554283202318e8,
             1.375493463079934e7
        ]),
        "velocity": np.array([
             10.36885836951787,
              4.630592338646661,
             -0.2242054075319154
        ])
    },

    "earth": {
        "mass": 5.97219e24,
        "radius": 6.37101e6,
        "position": np.array([
             1.310198698925289e11,
             6.968206637440602e10,
             8.594001375053078e6
        ]),
        "velocity": np.array([
            -14569.23473784416,
             26125.95250680299,
            -2.823367554334766
        ])
    },

    "moon": {
        "mass": 7.349e22,
        "radius": 1.7374e6,
        "position": np.array([
             1.313746668927824e11,
             6.952136732370937e10,
             1.340348240799457e7
        ]),
        "velocity": np.array([
            -14212.30581085309,
             27065.02215634798,
             84.79842532906723
        ])
    },

    "mars": {
        "mass": 6.4171e23,
        "radius": 3.38992e6,
        "position": np.array([
            -2.336508048704397e10,
             2.348853598267301e11,
             5.520843977670074e9
        ]),
        "velocity": np.array([
            -23184.77163204428,
             -311.6360904913282,
              561.8914681314046
        ])
    }
}
