import numpy as np
#inputs
planet=str(input("""The program can simulate orbits around:
Earth,
Moon,
Mars,
Sun,
and Jupiter
As isolated bodies in free space (without outside perturbations)
What planet to orbit?""")).lower()
r=float(input("Enter Rocket Orbit Radius (km):"))*1000
m=float(input("Enter Rocket Mass:"))
Vt=float(input("Enter Tangential Velocity:"))
Vr=float(input("Enter Radial Velocity:"))
F_eng_mag=float(input("Enter Burn force provided by engine:"))
t=float(input("Enter the time after which to measure Rocket's speed:"))
updates_per_second=float(input("No of updates per second (higher the value more the accuracy but increases load time):")) #no of updates per second
#Planetary Values
planets={
    "earth": {
        "mass":5.9722*(10**24),
        "radius":6.371*(10**6)
    },
    "moon": {
        "mass": 7.3476*(10**22),
        "radius": 1737400
        },
    "mars": {
        "mass": 6.4171*(10**23),
        "radius": 3389500
    },
    "sun": {
        "mass":  1.98892*(10**30),
        "radius": 6.957*(10**8)
    },
    "jupiter": {
        "mass": 1.89813*(10**27),
        "radius": 6.9886*(10**7)
    }
}
        
#initial vectors as given by input
Vt_Vector=np.array([Vt, 0, 0])
Vr_Vector=np.array([0, Vr, 0])
Pos=np.array([0, r, 0])
# known constant values for formulas
G=6.674*(10**(-11))
r_vec=np.array([0,r,0])
crashed=False
dt=1/updates_per_second
#formulas to claculate stuff:
V=Vt_Vector+Vr_Vector #Velocity vector

#Acceleration due to gravity and rocket burns function
def acc_with_F_eng(Position, V, target_planet):
    r_mag=np.linalg.norm(Position)
    g_dir=-Position/r_mag
    M=planets[target_planet]["mass"]
    g_mag=G*M/(r_mag**2)
    F_eng=F_eng_mag*V/(np.linalg.norm(V)) #burn force
    a_eng=F_eng/m
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
    
#calculating position and velocity (i.e orbit) across given time frame
Pos1,V1=RK4(Pos, V, planet)
for i in range (int(t/dt)-1):
    Pos1,V1=RK4(Pos1, V1, planet)
    if crash(Pos1, planet):
        print("!!Calculations failed!!. Rocket has crashed into the celestial body!!")
        crashed=True
        break
if crashed:
    print()
else:
    r_updated=np.linalg.norm(Pos1) #final radius    
    #Velocity Magnitude and angles    
    MagV1=np.linalg.norm(V1)
    Angle_rad=np.arctan2(V1[1],V1[0])
    Angle=np.degrees(Angle_rad)

    #Orbit type and properties Calculations
    P=m*MagV1 #linear momentum
    g=acc(Pos1, planet)
    F=m*g #Gravitational force
    h=np.cross(Pos1, V1)
    magh=np.linalg.norm(h)
    L=m*magh #angular momentum
    u=G*(planets[planet]["mass"])
    e=(MagV1**2)/2 + (-u)/r_updated
    ecc=(1+(2*e*(magh**2))/(u**2))**0.5
    Vc=((u)/r_updated)**0.5
    Vesc= (2*(u/r_updated))**0.5

    #Outputs
    print("gravity:", g)
    print("Final Velocity of rocket is:", MagV1)
    print("Angular Momentum of rocket is:", L)
    print("Linear Momentum of Rocket is:", P)
    print("New Position after time", t,":", Pos1)
    print("New Angle is (relative to x-axis):", Angle)
    print("Downward force experienced by Rocket:", F)
    print("Specific Orbital energy is:", e)
    print("Circular velocity is:", Vc)
    print("Escape Velocity is:", Vesc)
    print("Eccentricity is:", ecc)

    #Determining type of orbit
    if ecc==0:
        print("Orbit is circular")
    elif ecc>0 and ecc<1:
        print("Orbit is elliptical")
    elif ecc==1:
        print("Orbit is parabolic")
    else:
        print("Orbit is hyperbolic")
    
    #Determining if escape velocity is reached
    if MagV1>Vesc:
        print("Rocket has exceeded escape velocity for the orbit.")
    else:
        print("Rocket is below escape velocity for the orbit.")
    
    #checking orbit stability
    if e<0:
        print("Rocket is bound to earth.")
    elif e==0:
        print("Rocket is in parabolic escape trajectory.")
    else:
        print("Rocket is in hyperbolic escape trajectory.")
        
    


    
