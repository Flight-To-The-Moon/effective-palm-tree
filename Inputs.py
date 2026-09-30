#inputs
planet=str(input("""The program can simulate orbits around:
Earth,
Moon,
Mars,
Sun,
and Jupiter
As isolated bodies in free space (without outside perturbations)
What planet to orbit?""")).lower()
m=float(input("Enter Rocket Mass:"))
Vt=float(input("Enter Tangential Velocity:"))
Vr=float(input("Enter Radial Velocity:"))
F_eng_mag=float(input("Enter Burn force provided by engine:"))
t=float(input("Enter the time after which to measure Rocket's speed:"))
updates_per_second=float(input("No of updates per second (higher the value more the accuracy but increases load time):"))#no of updates per second
xPos=float(input("Enter initial position of rocket in x-axis (km)"))*1000
yPos=float(input("Enter initial position of rocket in y-axis (km)"))*1000