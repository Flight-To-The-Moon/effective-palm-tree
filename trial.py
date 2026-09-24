import numpy as np
import math
#inputs
r=float(input("Enter Rocket Orbit Radius (km):"))*1000
m=float(input("Enter Rocket Mass:"))
Vt=float(input("Enter Tangential Velocity:"))
Vr=float(input("Enter Radial Velocity:"))
F_eng=float(input("Enter Burn force provided by engine:"))
t=float(input("Enter the time after which to measure Rocket's speed:"))
#initial vectors as given by input
Vt_Vector=np.array([Vt, 0, 0])
Vr_Vector=np.array([0, Vr, 0])
Pos=np.array([0, r, 0])
# known constant values for formulas
G=6.674*(10**(-11))
M=float(5.9722*(10**24))
r_vec=np.array([0,r,0])
R_Earth=6.371*(10**6)
#formulas to claculate stuff:
V=Vt_Vector+Vr_Vector #Velocity vector
#Force calculations
g=G*M/(r**2)
#Position Calculations
dt=0.1 #no of updates per second
for i in range (int(t/dt)):
    r_updated=np.linalg.norm(Pos)
    if r_updated<R_Earth:
        crashed=True
        break
    
    else:
        
         g=G*M/(r_updated**2)
         g_dir=-Pos/r_updated
         a=g*g_dir 
         V=V+a*dt 
         Pos=Pos+V*dt
if crashed:
    print("!!Calculations failed!!. Rocket has crashed into the earth!!.")
else:
    r_updated=np.linalg.norm(Pos) #final radius    
    #Velocity Magnitude and angles    
    MagV=np.linalg.norm(V)
    Angle_rad=np.arctan2(V[1],V[0])
    Angle=np.degrees(Angle_rad)     
    #Orbit type and properties Calculations
    P=m*V[0] #linear momentum
    F=m*g #Gravitational force
    h=np.cross(Pos, V)
    magh=np.linalg.norm(h)
    L=m*magh #angular momentum
    u=G*M
    e=(MagV**2)/2 + (-u)/r_updated
    ecc=(1+(2*e*(magh**2))/(u**2))**0.5
    Vc=((u)/r_updated)**0.5
    Vesc= (2*(u/r_updated))**0.5
    #Outputs
    print("gravity:", g)
    print("Final Velocity of rocket is:", MagV)
    print("Angular Momentum of rocket is:", L)
    print("Linear Momentum of Rocket is:", P)
    print("New Position after time", t,":", Pos)
    print("New Angle is (relative to x-axis):", Angle)
    print("Downward force experienced by Rocket:", F)
    print("Orbital energy is:", e)
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
    if MagV>Vesc:
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
    


    
