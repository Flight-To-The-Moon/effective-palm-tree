import numpy as np
#inputs
Vt=float(input('enter velocity'))
a_eng=float(input('enter engine acceleration')) #this variable is not used here as this is just a trial ptogram
r=float(input('enter orbit radius (km)'))*1000
t=float(input('enter time after which to measue values'))
#initial vectors, known values
Pos=np.array([0,r,0])
V=np.array([Vt,0,0])
G=6.674*(10**(-11))
M=float(5.9722*(10**24))
dt=60#time step length
#graviy function
def acceleration(Pos):
    g=G*M/(np.linalg.norm(Pos)**2)
    g_dir=-Pos/np.linalg.norm(Pos)
    a_total=g*g_dir
    return a_total
#RK4 function
def RK4(Pos, V):
    Pos_final,V_final=Pos.copy(), V.copy()
    for i in range(int(t/dt)):
        #k1
        Pos_k1,V_k1=V_final,acceleration(Pos_final)
        #k2
        Pos_k2=V_final+V_k1*(dt/2)
        V_k2=acceleration(Pos_final+(Pos_k1)*dt/2)
        #k3
        Pos_k3=V_final+V_k2*(dt/2)
        V_k3=acceleration(Pos_final+(Pos_k2)*(dt/2))
        #k4
        Pos_k4=V_final+V_k3*dt
        V_k4=acceleration(Pos_final+(Pos_k3)*dt)
        #final
        Pos_final=Pos_final+(Pos_k1+2*Pos_k2+2*Pos_k3+Pos_k4)*(dt/6)
        V_final=V_final+(V_k1+2*V_k2+2*V_k3+V_k4)*(dt/6)
        return (Pos_final,V_final)
#final outputs
j,l=RK4(Pos,V)
magl=np.linalg.norm(l)
print(j, "is the final position after time", t)
print(magl, "is the final speed")
print(l, "is the final velocity")