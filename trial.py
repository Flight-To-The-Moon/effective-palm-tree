import numpy as np
import Orbit_Map as orb
import Physics
from Planets import planets
import Inputs as inp
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
#initial vectors as given by input
Pos_list={}
for planet in planets:
    Pos_list[planet]=planets[planet]["position"]
Pos=np.array([inp.xPos, inp.yPos, 0])+ planets[inp.planet]["position"]
planets["rocket"]["position"]=Pos
rel_Pos= Pos- planets[inp.planet]["position"]
Vt_Vector=np.array([-rel_Pos[1]/np.linalg.norm(rel_Pos), rel_Pos[0]/np.linalg.norm(rel_Pos), 0])
Vr_Vector=np.array([rel_Pos[0]/np.linalg.norm(rel_Pos), rel_Pos[1]/np.linalg.norm(rel_Pos), 0])
Vt_Vector*=inp.Vt
Vr_Vector*=inp.Vr
# known constant values for formulas
crashed=False
x=[]
y=[]
time=0
dt=1/inp.updates_per_second
#formulas to claculate stuff:
V=Vt_Vector+Vr_Vector + planets[inp.planet]["velocity"]#Velocity vector
planets["rocket"]["velocity"]=V
if Physics.crash(Pos):
    Pos1=Pos
    V1=V
    crashed=True
else:
    Pos_list,V_list=orb.RK4_solar()
    Pos1=Pos_list["rocket"]
    V1=V_list["rocket"]
    time+=dt
    plot_list={planet: [] for planet in planets}
    for planet in planets:
        planets[planet]["position"]= Pos_list[planet]
        planets[planet]["velocity"]= V_list[planet]
    for i in range (int(inp.t/dt)-1):
        if Physics.crash(Pos1):
            print("!!Calculations failed!!. Rocket has crashed into the celestial body!!")
            crashed=True
            break
        else:
            Pos_list,V_list=orb.RK4_solar()
            Pos1=Pos_list["rocket"]
            V1=V_list["rocket"]
            time+=dt
            for planet in planets:
                planets[planet]["position"]= Pos_list[planet]
                planets[planet]["velocity"]= V_list[planet]
                plot_list[planet].append(Pos_list[planet].copy())
if crashed:
    print()
    print("Rocket crashed at:", Pos1, "after time", time)
    orb.animate(plot_list)
else:
    Pos1=Pos1-Pos_list[inp.planet]
    V1=V1-V_list[inp.planet]
    r_updated=np.linalg.norm(Pos1) #final radius    
    #Velocity Magnitude and angles    
    MagV1=np.linalg.norm(V1)
    Angle_rad=np.arctan2(V1[1],V1[0])
    Angle_Pos=np.arctan2(Pos1[1], Pos1[0])
    Angle=np.degrees(Angle_rad)

    #Orbit type and properties Calculations
    P=inp.m*MagV1 #linear momentum
    g=9.8 #temporary value, change it
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
    print("New Position after time", inp.t,":", Pos1, "corresponding to angle:", Angle_Pos)
    print("New Angle is (relative to x-axis):", Angle)
    print("Downward force experienced by Rocket:", F)
    print("Specific Orbital energy is:", e)
    print("Circular velocity is:", Vc)
    print("Escape Velocity is:", Vesc)
    print("Eccentricity is:", ecc)
    print("Distance from", inp.planet, "is", r_updated)

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
        print("Rocket is bound to", inp.planet)
    elif e==0:
        print("Rocket is in parabolic escape trajectory.")
    else:
        print("Rocket is in hyperbolic escape trajectory.")
    orb.animate(plot_list)


    
