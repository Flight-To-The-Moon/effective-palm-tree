#reading/writing json files
from pathlib import Path
import json
folder=Path(__file__).parent/"Mission-data" #folder path
use_manual=False
#using previous inputs
choice=input("Use previous values? (y/n):").lower()
if choice=="y" or choice=="yes":
    while True:
        try:
            file_name=input("Enter file name to load inputs from (without .json):")+".json"
            path=folder/ file_name
            with open(path, "r") as mission_file:
                mission_data=json.load(mission_file)
            break
        #catching errors
        except FileNotFoundError:
            print("This file doesn't exist. Please enter another file name. (or check spelling)")
            choice=input("Do you want to enter input manually? (y/n):").lower()
            if choice=="y" or choice=="yes":
                use_manual=True
                break
        except json.JSONDecodeError:
            print("This json file is corrupted. It cannot be used. Please manually fix it.")
            choice=input("Do you want to enter input manually? (y/n):").lower()
            if choice=="y" or choice=="yes":
                use_manual=True
                break
    if not use_manual:
        #loading json values into variables
        planet=mission_data["planet"]
        target_planet=mission_data["target_planet"]
        m_d=mission_data["m_d"]
        m_w=mission_data["m_w"]
        mp=mission_data["mp"]
        m=m_d+m_w
        Vt=mission_data["Vt"]
        Vr=mission_data["Vr"]
        F_eng_mag=mission_data["F_eng_mag"]
        t=mission_data["t"]
        updates_per_second=mission_data["updates_per_second"]
        xPos=mission_data["xPos"]
        yPos=mission_data["yPos"]
        burn_list=mission_data["burn_list"]
        burn_dir_list=mission_data["burn_dir_list"]
        burn_body_list=mission_data["burn_body_list"]
        burn_end_list=mission_data["burn_end_list"]
else:
    use_manual=True
#asking for user input
if use_manual:   
    planet=str(input("""The program can simulate orbits around:
    Earth,
    Moon,
    Mars,
    Sun,
    and Jupiter
    As isolated bodies in free space (without outside perturbations)
    What planet to orbit?""")).lower()
    target_planet=input("Enter the target planet to orbit/collide:").lower()
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
        burn_body=str(input("Burn relative to which body (earth, moon etc.) [type rocket if burning in direction of rocket velocity]:")).lower()
        burn_dir=float(input("Burn direction (1 = prograde, -1 = retrograde):"))
        if burn_dur=="end":
            burn_dur=m_w/mp
        else:
            burn_dur=float(burn_dur)
    #appending burns to list   
        burn_end=burn_time+burn_dur
        burn_list.append(burn_time)
        burn_dir_list.append(burn_dir)
        burn_end_list.append(burn_end)
        burn_body_list.append(burn_body)
    
#saving input
    choice=input("Do you want to save these inputs? (y/n):").lower()
    if choice=="y" or choice=="yes":
        mission_data={
            "planet": planet,
            "target_planet": target_planet,
            "m_d": m_d,
            "m_w": m_w,
            "mp": mp,
            "Vt": Vt,
            "Vr": Vr,
            "F_eng_mag": F_eng_mag,
            "t": t,
            "updates_per_second": updates_per_second,
            "xPos": xPos,
            "yPos": yPos,
            "burn_list": burn_list,
            "burn_dir_list": burn_dir_list,
            "burn_body_list": burn_body_list,
            "burn_end_list": burn_end_list
            }
        
#creating file
        while True:
            file_name=input("Enter name for the save file:")+".json"
            path=folder/file_name
            try:
                with open(path, "x") as mission_file:
                    json.dump(mission_data, mission_file)
                break
    #catching errors
            except FileExistsError:
                print('This file already exists! Please choose a new name.')
            
    