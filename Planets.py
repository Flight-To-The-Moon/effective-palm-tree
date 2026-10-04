#Planetary Values
import numpy as np
import Inputs as inp
planets = {
    "rocket": {
        "mass": inp.m,
        "velocity": np.array([0.0, 0.0, 0.0]),
        "position": np.array([0.0, 0.0, 0.0]),
        "radius": 24.0,
    },

    "earth": {
        "mass": 5.9722e24,
        "radius": 6.371e6,
        "velocity": np.array([-11.79, 0.0, 0.0]),
        "position": np.array([0, 0.0, 0.0]), 
    },
    "moon": {
        "mass":  7.347e22,
        "radius": 1737400,
        "velocity": np.array([958.2, 0, 0]),
        "position": np.array([0, 405500000, 0])
    }
}
