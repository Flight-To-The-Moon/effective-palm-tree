import numpy as np
#inputs
r0x=float(input("Enter initial position w.r.t x-axis:"))
r0y=float(input("Enter initial position w.r.t y-axis:"))
r0z=float(input("Enter initial position w.r.t z-axis:"))
rx=float(input("Enter final position w.r.t x-axis:"))
ry=float(input("Enter final position w.r.t y-axis:"))
rz=float(input("Enter final position w.r.t z-axis:"))
tof=float(input("Enter time required for travel (seconds):"))
r0=np.array([r0x, r0y, r0z])
r=np.array([rx, ry, rz])

def Stumpff(psi, tol=1e-15):
    eta=3
    H0=0.5
    H=H0
    C=H0
    K=2
    L=eta
    for i in range (1,1000):
        H=(-psi*H)/(2*K*L)
        if abs(H)<=tol:
            N=i
            break
        else:
            C=C+H
            K+=1
            L+=2
    C2=C
    eta=5
    H0=(1/6)
    H=H0
    C=H0
    K=2
    L=eta
    for i in range (1,1000):
        H=(-psi*H)/(2*K*L)
        if abs(H)<=tol:
            N=i
            break
        else:
            C=C+H
            K+=1
            L+=2
    C3=C
    return C2, C3

def psi_reducer(psi, psi_m=0.9):
    K=0
    while abs(psi)>psi_m:
        psi=psi/4
        K+=1
    C2, C3= Stumpff(psi)
    for i in range (K):
        C3_new=(C2+C3-(psi*C2*C3))/4
        C2_new=((1-(psi*C3))**2)/2
        C2, C3= C2_new, C3_new
        psi*=4
    return C2, C3
         
def lambert_solver(r0, r, tof, psi0=0.8, psiu=4*((np.pi)**2), psil=-4*((np.pi)**2),tm=1, M=1000, tol=1e-9, mu=3.98600418e14):
    r0_mag=np.linalg.norm(r0)
    r_mag=np.linalg.norm(r)
    gamma=np.dot(r0, r)/((np.linalg.norm(r))*(np.linalg.norm(r0)))
    Beta=tm*((1-(gamma**2))**0.5)
    A=tm*((r_mag*r0_mag*(1+gamma))**0.5)
    psi=psi0
    converge=False
    if A==0:
        raise ValueError("What shitty values are these bro")
    for i in range (1, M):
        C2, C3=psi_reducer(psi)
        B=r0_mag+r_mag+((1/(C2**0.5))*(A*((psi*C3)-1)))
            
        while A>0 and B<0:
            psil=psi
            psi=0.5*(psiu+psil)
            C2, C3= psi_reducer(psi)
            B=r0_mag+r_mag+((1/(C2**0.5))*(A*((psi*C3)-1)))
                
        ki=(B/C2)**0.5
        delta_t=(1/(mu**0.5))*(((ki**3)*C3)+(A*(B**0.5)))
            
        if abs(tof-delta_t)<=tol*tof:
            converge=True
            break
        if delta_t<=tof:
            psil=psi
            psi=0.5*(psiu+psil)
        else:
            psiu=psi
            psi=0.5*(psiu+psil)
    if not converge:
        raise RuntimeError("Convergence Failure")
    F_coeff=1-(B/r0_mag)
    G_coeff=A*((B/mu)**0.5)
    G_dot=1-(B/r_mag)
    r0x=r0[0]
    r0y=r0[1]
    r0z=r0[2]
    rx=r[0]
    ry=r[1]
    rz=r[2]
    v0_x=(1/G_coeff)*(rx-(r0x*F_coeff))
    v0_y=(1/G_coeff)*(ry-(r0y*F_coeff))
    v0_z=(1/G_coeff)*(rz-(r0z*F_coeff))
    vx=(1/G_coeff)*((G_dot*rx)-r0x)
    vy=(1/G_coeff)*((G_dot*ry)-r0y)
    vz=(1/G_coeff)*((G_dot*rz)-r0z)
    V0=np.array([v0_x, v0_y, v0_z])
    V=np.array([vx, vy, vz])
    return V0, V

V0, V= lambert_solver(r0, r, tof)
print("Final Velocity is:", V)
print("Required initial velocity is:", V0)
            
            
            
