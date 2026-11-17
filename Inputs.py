#inputs
planet=str(input("""The program can simulate orbits around:
Earth,
Moon,
Mars,
Sun,
and Jupiter
As isolated bodies in free space (without outside perturbations)
What planet to orbit?""")).lower()
target_planet=input("Enter the target planet to orbit/collide:")
m_d=float(input("Enter Rocket Mass (Without fuel) [Kg]:"))
m_w=float(input("Enter Rocket fuel (Kg):"))
mp=float(input("Enter Rocket fuel burn rate (Kg/s):"))
m=m_d+m_w
Vt=float(input("Enter Tangential Velocity (m/s):"))
Vr=float(input("Enter Radial Velocity (m/s):"))
F_eng_mag=float(input("Enter Burn force provided by engine (N):"))
t=float(input("Enter the time after which to measure Rocket's speed (s):"))
updates_per_second=float(input("No of updates per second (higher the value more the accuracy but increases load time):"))#no of updates per second
xPos=float(input("Enter initial position of rocket in x-axis (km)"))*1000
yPos=float(input("Enter initial position of rocket in y-axis (km)"))*1000
burn_list=[]
burn_dir_list=[]
burn_body_list=[]
burn_end_list=[]
print("Enter burn info, type 0 at burn start input to end")
while True:
    burn_time=float(input("Enter time of burn start (s):"))
    if burn_time==0:
        break
    burn_dur=input("Enter burn duration, type end to burn until fuel is empty (s):").lower()
    burn_body=str(input("Burn relative to which body (earth/moon):")).lower()
    burn_dir=float(input("Burn direction (1 = prograde, -1 = retrograde):"))
    if burn_dur=="end":
        burn_dur=m_w/mp
    else:
        burn_dur=float(burn_dur)
    burn_end=burn_time+burn_dur
    burn_list.append(burn_time)
    burn_dir_list.append(burn_dir)
    burn_end_list.append(burn_end)
    burn_body_list.append(burn_body)
    

    
    