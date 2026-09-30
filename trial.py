import numpy as np
import Physics
from Planets import planets
import Inputs as inp
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
#initial vectors as given by input
Vt_Vector=np.array([inp.Vt, 0, 0])
Vr_Vector=np.array([0, inp.Vr, 0])
Pos=np.array([inp.xPos, inp.yPos, 0])
# known constant values for formulas
crashed=False
x=[]
y=[]
time=0
dt=1/inp.updates_per_second
#formulas to claculate stuff:
V=Vt_Vector+Vr_Vector #Velocity vector
if Physics.crash(Pos, inp.planet):
    Pos1=Pos
    V1=V
else:
    Pos1,V1=Physics.RK4(Pos, V, inp.planet)
    x.append(Pos1[0]/1000)
    y.append( Pos1[1]/1000)
    time+=dt
for i in range (int(inp.t/dt)-1):
    if Physics.crash(Pos1, inp.planet):
        print("!!Calculations failed!!. Rocket has crashed into the celestial body!!")
        crashed=True
        break
    else:
        Pos1,V1=Physics.RK4(Pos1, V1, inp.planet)
        x.append(Pos1[0]/1000)
        y.append( Pos1[1]/1000)
        time+=dt
if crashed:
    print()
    print("Rocket crashed at:", Pos1, "after time", time)
    plt.plot(x,y)
    radius = planets[inp.planet]["radius"] / 1000
    planet = Circle((0, 0), radius, fill=False)
    ax=plt.gca()
    ax.add_patch(planet)
    plt.axis("equal")
    plt.show()
else:
    r_updated=np.linalg.norm(Pos1) #final radius    
    #Velocity Magnitude and angles    
    MagV1=np.linalg.norm(V1)
    Angle_rad=np.arctan2(V1[1],V1[0])
    Angle=np.degrees(Angle_rad)

    #Orbit type and properties Calculations
    P=inp.m*MagV1 #linear momentum
    g=Physics.acc(Pos1, inp.planet)
    F=inp.m*g #Gravitational force
    h=np.cross(Pos1, V1)
    magh=np.linalg.norm(h)
    L=inp.m*magh #angular momentum
    u=Physics.G*(planets[inp.planet]["mass"])
    e=(MagV1**2)/2 + (-u)/r_updated
    ecc=(1+(2*e*(magh**2))/(u**2))**0.5
    Vc=((u)/r_updated)**0.5
    Vesc= (2*(u/r_updated))**0.5

    #Outputs
    print("gravity:", g)
    print("Final Velocity of rocket is:", MagV1)
    print("Angular Momentum of rocket is:", L)
    print("Linear Momentum of Rocket is:", P)
    print("New Position after time", inp.t,":", Pos1)
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
    plt.plot(x,y)
    radius = planets[inp.planet]["radius"] / 1000
    planet = Circle((0, 0), radius, fill=False)
    ax=plt.gca()
    ax.add_patch(planet)
    plt.axis("equal")
    plt.show()
        
    


    
