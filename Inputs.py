#inputs
planet=str(input("""The program can simulate orbits around:
Earth,
Moon,
Mars,
Sun,
and Jupiter
As isolated bodies in free space (without outside perturbations)
What planet to orbit?""")).lower()
m_d=float(input("Enter Rocket Mass(dry):"))
m_w=float(input("Enter Rocket Mass(wet):"))
mp=float(input("Enter Rocket fuel burn rate (Kg/s):"))
m=m_d+m_w
Vt=float(input("Enter Tangential Velocity:"))
Vr=float(input("Enter Radial Velocity:"))
F_eng_mag=float(input("Enter Burn force provided by engine:"))
t=float(input("Enter the time after which to measure Rocket's speed:"))
updates_per_second=float(input("No of updates per second (higher the value more the accuracy but increases load time):"))#no of updates per second
xPos=float(input("Enter initial position of rocket in x-axis (km)"))*1000
yPos=float(input("Enter initial position of rocket in y-axis (km)"))*1000
burn_time=float(input("Enter time of burn start:"))
burn_body=str(input("Burn relative to which body (earth/moon):")).lower()
burn_dir=float(input("Burn direction (1 = prograde, -1 = retrograde):"))