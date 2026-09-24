import numpy as np
import math
r=int(input("Enter Rocket Orbit Radius (km):"))*1000
m=int(input("Enter Rocket Mass:"))
Vt=int(input("Enter Tangential Velocity:"))
Vr=int(input("Enter Radial Velocity:"))
F_eng=int(input("Enter Burn force provided by engine:"))
t=int(input("Enter the time after which to measure Rocket's speed:"))
M=float(5.9722*(10**24))
Vt_Vector=np.array([Vt, 0, 0])
Vr_Vector=np.array([0, Vr, 0])
Pos=np.array([0, r, 0])
V=Vt_Vector+Vr_Vector
Angle_rad=np.arctan2(V[1],V[0])
Angle=np.degrees(Angle_rad)
MagV=np.linalg.norm(V)
G=6.674*(10**(-11))
g=G*M/(r**2)
a=(-g)*np.array([0, 1, 0])
P=m*MagV
L=m*r*Vt
F=m*g
r_vec=np.array([0,r,0])
h=np.cross(V, r_vec)
magh=np.linalg.norm(h)
u=3.986*(10**14)
e=(MagV**2)/2 + (-u)/r
ecc=(1+(2*e*(magh**2))/(u**2))**0.5
new_V=V+a*t
new_Pos=Pos+new_V*t
Vc=((u)/r)**0.5
Vesc= (2*(u/r))**0.5
print("gravity:", g)
print("Velocity of rocket is:", new_V)
print("Angular Momentum of rocket is:", L)
print("Linear Momentum of Rocket is:", P)
print("Position change in small time", t,":", new_Pos)
print("New Angle is:", Angle)
print("Downward force experienced by Rocket:", F)
print("Orbital energy is:", e)
print("Circular velocity is:", Vc)
print("Escape Velocity is:", Vesc)
print("Eccentricity is:", ecc)
if ecc==0:
    print("Orbit is circular")
elif ecc>0 and ecc<1:
    print("Orbit is elliptical")
elif ecc==1:
    print("Orbit is parabolic")
else:
    print("Orbit is hyperbolic")


    