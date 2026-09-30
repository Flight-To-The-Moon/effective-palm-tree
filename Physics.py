import numpy as np
from Planets import planets
import Inputs as inp
G=6.674*(10**(-11))
dt=1/inp.updates_per_second
#Acceleration due to gravity and rocket burns function
def acc_with_F_eng(Position, V, target_planet):
    r_mag=np.linalg.norm(Position)
    g_dir=-Position/r_mag
    M=planets[target_planet]["mass"]
    g_mag=G*M/(r_mag**2)
    F_eng=inp.F_eng_mag*V/(np.linalg.norm(V)) #burn force
    a_eng=F_eng/inp.m
    a=g_mag*g_dir+a_eng
    return a

#pure gravity function (useful for future implementations)
def acc(Position, target_planet):
    r_mag=np.linalg.norm(Position)
    g_dir=-Position/r_mag
    M=planets[target_planet]["mass"]
    g_mag=G*M/(r_mag**2)
    a=g_mag*g_dir
    return a
    
#function to check for crashes
def crash(Position, planet):
    r_orbit=np.linalg.norm(Position)
    r_planet=planets[planet]["radius"]
    if r_orbit<r_planet:
        return True
    else:
        return False

#Position and Velocity Calculation function (per timestep)
def RK4(position, velocity, target_planet):
    pos_final, V_final=position.copy(), velocity.copy() #initial values
    #k1
    pos_k1,V_k1=V_final, acc_with_F_eng(pos_final, V_final, target_planet)
        
    #k2
    pos_k2=V_final+V_k1*(dt/2)
    V_k2=acc_with_F_eng(pos_final+pos_k1*(dt/2), pos_k2, target_planet)
        
    #k3
    pos_k3=V_final+V_k2*(dt/2)
    V_k3=acc_with_F_eng(pos_final+pos_k2*(dt/2), pos_k3, target_planet)
        
    #k4
    pos_k4=V_final+V_k3*(dt)
    V_k4=acc_with_F_eng(pos_final+ pos_k3*(dt), pos_k4, target_planet)
        
    #final values after step
    pos_final=position+(pos_k1+2*pos_k2+2*pos_k3+pos_k4)*(dt/6)
    V_final=velocity+(V_k1+2*V_k2+2*V_k3+V_k4)*(dt/6)
    return pos_final, V_final
    