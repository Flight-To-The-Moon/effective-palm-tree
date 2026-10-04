from Planets import planets
import Inputs as inp
import Physics
from matplotlib.patches import Circle
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
def solar_system(position):
    
    a_dict = {}
    
    for i, planet in enumerate(planets):
        a_dict[planet] = np.zeros(3)

    for i, planet in enumerate(planets):
        for j, planet2 in enumerate(planets):

            if j <= i:
                continue

            pos1 = position[planet]
            pos2 = position[planet2]

            a1, a2 = Physics.acc(pos1, pos2, planet, planet2)

            a_dict[planet] += a1
            a_dict[planet2] += a2

    return a_dict
def RK4_solar():
    positions={}
    velocities={}
    dt=1/inp.updates_per_second
    for planet in planets:
        velocities[planet]=planets[planet]["velocity"].copy()
        positions[planet]=planets[planet]["position"].copy()
    a1=solar_system(positions)
    #k1
    p1={}
    v1={}
    for planet in planets:
        #k1
        p1[planet],v1[planet]=velocities[planet], a1[planet]
        
        #k2
    positions2={}
    for planet in planets:
        positions2[planet]=positions[planet] + p1[planet]*(dt/2)
    a2=solar_system(positions2)
    p2={}
    v2={}
    for planet in planets:
        p2[planet]=velocities[planet]+ v1[planet]*(dt/2)
        v2[planet]=a2[planet]
        
    positions3={}
    for planet in planets:
        positions3[planet]=positions[planet]+ p2[planet]*(dt/2)
    a3=solar_system(positions3)
    p3={}
    v3={}
    #K3
    for planet in planets:
        p3[planet]=velocities[planet] + v2[planet]*(dt/2)
        v3[planet]=a3[planet]
    positions4={}
    for planet in planets:
        positions4[planet]=positions[planet]+ p3[planet]*(dt)
    a4=solar_system(positions4)
    p4={}
    v4={}
    #k4
    for planet in planets:   
        p4[planet]=velocities[planet]+ v3[planet]*(dt)
        v4[planet]=a4[planet]
        
    #final values after step
    pos_final={}
    v_final={}
    for planet in planets:
        pos_final[planet]=positions[planet]+(p1[planet]+2*p2[planet]+2*p3[planet]+p4[planet])*(dt/6)
        v_final[planet]=velocities[planet]+(v1[planet]+2*v2[planet]+2*v3[planet]+v4[planet])*(dt/6)
    return pos_final, v_final

def plotter(position_list):
    for planet in position_list:
        if len(position_list[planet])==0:
            continue
        positions= np.array(position_list[planet])
        x = (positions[:, 0])/1000
        y = (positions[:, 1])/1000

        plt.plot(x, y)

def add_circles(position_list):
    for planet in position_list:
        x = position_list[planet][0]/1000
        y = position_list[planet][1]/1000

        radius = planets[planet]["radius"]/1000

        circle = Circle((x, y), radius, fill=False)
        plt.gca().add_patch(circle)
        plt.text(x, y, planet)
def animate(position_list, max_points=1500):

    fig, ax = plt.subplots()

    # ---- prepare data ONCE (km, subsampled) ----
    data = {}
    for planet in position_list:
        if len(position_list[planet]) == 0:
            continue
        arr = np.array(position_list[planet]) / 1000
        step = max(1, len(arr) // max_points)
        data[planet] = arr[::step]

    frames = max(len(d) for d in data.values())

    lines, circles, labels = {}, {}, {}
    for planet in data:
        line, = ax.plot([], [], label=planet)
        lines[planet] = line

        circle = Circle((0, 0), planets[planet]["radius"] / 1000, fill=False)
        ax.add_patch(circle)
        circles[planet] = circle

        labels[planet] = ax.text(0, 0, planet)

    ax.set_aspect("equal")
    ax.set_xlim(-500000, 500000)
    ax.set_ylim(-500000, 500000)

    def update(frame):
        for planet, d in data.items():
            k = min(frame, len(d) - 1)
            lines[planet].set_data(d[:k + 1, 0], d[:k + 1, 1])
            circles[planet].center = (d[k, 0], d[k, 1])
            labels[planet].set_position((d[k, 0], d[k, 1]))
        return (list(lines.values())
                + list(circles.values())
                + list(labels.values()))

    ani = FuncAnimation(fig, update, frames=frames, interval=20, blit=True)
    plt.show()
    return ani