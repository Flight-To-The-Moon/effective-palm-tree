# Planetary Values
import numpy as np
import Inputs as inp

AU = 1.495978707e11  # metres

planets = {
    "rocket": {
        "mass": inp.m,
        "velocity": np.array([0.0, 29780.0, 0.0]),
        "position": np.array([0.0, 0.0, 0.0]),
        "radius": 24.0,
        "Engine_acceleration": 0
    },

    "sun": {
        "mass": 1.9885e30,
        "radius": 6.9634e8,
        "velocity": np.array([0.0, 0.0, 0.0]),
        "position": np.array([-AU, 0.0, 0.0])
    },

    "earth": {
        "mass": 5.9722e24,
        "radius": 6.371e6,
        "velocity": np.array([0.0, 29780.0, 0.0]),
        "position": np.array([0.0, 0.0, 0.0])
    },

    "moon": {
        "mass": 7.347e22,
        "radius": 1.7374e6,
        "velocity": np.array([958.2, 29780.0, 0.0]),
        "position": np.array([0.0, 405500000.0, 0.0])
    },

    "mars": {
        "mass": 6.4171e23,
        "radius": 3.3895e6,
        "velocity": np.array([0.0, 24130.0, 0.0]),
        "position": np.array([0.524 * AU, 0.0, 0.0])
    }
}

# Shift every velocity into the system's centre-of-mass frame.
# This guarantees total linear momentum is zero.
total_mass = sum(body["mass"] for body in planets.values())

total_momentum = sum(
    (body["mass"] * body["velocity"] for body in planets.values()),
    start=np.zeros(3)
)

com_velocity = total_momentum / total_mass

for body in planets.values():
    body["velocity"] -= com_velocity

