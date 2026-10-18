import numpy as np
from Planets import planets
import Inputs as inp
G=6.674*(10**(-11))
dt=1/inp.updates_per_second
#gravity function
def acc(position1, position2, planet, planet2):       
    position=position2-position1
    r_mag=np.linalg.norm(position)
    g_dir=position/r_mag
    M1=planets[planet]["mass"]
    M2=planets[planet2]["mass"]
    a1=(G*M2/(r_mag**2))*g_dir
    a2=(-G*M1/(r_mag**2))*g_dir
    return a1, a2
#Engine burn calculation
def engine_acc(position, velocity):
    a_eng_mag=planets["rocket"]["Engine_acceleration"]
    if a_eng_mag==0:
        return np.zeros(3)
    planet=inp.burn_body
    rel_pos = position["rocket"] - position[planet]
    rel_vel = velocity["rocket"] - velocity[planet]
    r_dir = rel_pos / np.linalg.norm(rel_pos)
    tangent = rel_vel - np.dot(rel_vel, r_dir) * r_dir
    n = np.linalg.norm(tangent)
    nr = np.linalg.norm(rel_vel)
    if n == 0:
        return np.zeros(3)
    return inp.burn_dir * a_eng_mag * rel_vel / nr
    
#function to check for crashes
def crash(position):
    for planet in planets:
        if planet== "rocket":
            continue
        crash_position=position-planets[planet]["position"]
        crash_mag=np.linalg.norm(crash_position)
        r_planet=planets[planet]["radius"]
        if crash_mag<=r_planet:
            print("Crashed with:", planet)
            return True
            break

    return False

def fuel_burner(m_d, m_w, mp, F_eng_mag):
    dt=1/inp.updates_per_second
    m_w-=mp*dt
    m=m_d+m_w
    if m_w<0:
        a_eng_mag=0
        m=m_d
        empty=True
    else:
        a_eng_mag=F_eng_mag/(m+mp*dt)
        """here +mp is used as the acceleration is calculated
        before fuel is spent. You cannot burn fuel then calculate acceleration
        for mass whole fuel was already burnt."""
        empty=False
    return m, a_eng_mag, m_w, empty