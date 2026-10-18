from Planets import planets
import Inputs as inp
import Physics
from matplotlib.patches import Circle
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
def solar_system(position, velocity):
    
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
    a_dict["rocket"] += Physics.engine_acc(position, velocity)

    return a_dict
def RK4_solar():
    positions={}
    velocities={}
    dt=1/inp.updates_per_second
    for planet in planets:
        velocities[planet]=planets[planet]["velocity"].copy()
        positions[planet]=planets[planet]["position"].copy()
    a1=solar_system(positions, velocities)
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
    p2={}
    v2={}
    for planet in planets:
        p2[planet]=velocities[planet]+ v1[planet]*(dt/2)
    a2=solar_system(positions2, p2)
    for planet in planets:
        v2[planet]=a2[planet]
        
    positions3={}
    for planet in planets:
        positions3[planet]=positions[planet]+ p2[planet]*(dt/2)
    p3={}
    v3={}
    #K3
    for planet in planets:
        p3[planet]=velocities[planet] + v2[planet]*(dt/2)
    a3=solar_system(positions3, p3)
    for planet in planets:
        v3[planet]=a3[planet]
    positions4={}
    for planet in planets:
        positions4[planet]=positions[planet]+ p3[planet]*(dt)
    p4={}
    v4={}
    #k4
    for planet in planets:   
        p4[planet]=velocities[planet]+ v3[planet]*(dt)
    a4=solar_system(positions4, p4)
    for planet in planets: 
        v4[planet]=a4[planet]
        
    #final values after step
    pos_final={}
    v_final={}
    for planet in planets:
        pos_final[planet]=positions[planet]+(p1[planet]+2*p2[planet]+2*p3[planet]+p4[planet])*(dt/6)
        v_final[planet]=velocities[planet]+(v1[planet]+2*v2[planet]+2*v3[planet]+v4[planet])*(dt/6)
    planets["rocket"]["velocity"]=v_final["rocket"]        
    return pos_final, v_final
def animate(position_list, burn_flags=None, max_points=1500):

    fig, ax = plt.subplots()

    # ---- prepare data ONCE (km, subsampled) ----
    data = {}
    step = 1
    for planet in position_list:
        if len(position_list[planet]) == 0:
            continue
        arr = np.array(position_list[planet]) / 1000
        step = max(1, len(arr) // max_points)
        data[planet] = arr[::step]

    # burn flags subsampled the same way as the positions
    burn_mask = None
    if burn_flags is not None and "rocket" in data:
        burn_mask = np.array(burn_flags, dtype=bool)[::step]
        burn_mask = burn_mask[:len(data["rocket"])]

    frames = max(len(d) for d in data.values())

    circles, labels = {}, {}
    trail_lines = {}   # the already-travelled part of each path
    burn_line = None   # the already-travelled part of the burn

    for planet in data:
        # full path = the "not yet travelled" path (blue)
        ax.plot(data[planet][:, 0], data[planet][:, 1],
                color="tab:blue", alpha=0.35, zorder=1)

        # travelled part, starts empty and grows each frame
        (trail,) = ax.plot([], [], color="tab:orange", lw=1.8, zorder=2)
        trail_lines[planet] = trail

        circle = Circle((0, 0), planets[planet]["radius"] / 1000, fill=False)
        ax.add_patch(circle)
        circles[planet] = circle

        labels[planet] = ax.text(0, 0, planet)

    # burn segments get their own colour, drawn on top of the travelled path
    if burn_mask is not None:
        (burn_line,) = ax.plot([], [], color="lime", lw=2.5, zorder=3)
        rocket_xy = data["rocket"]
        # NaN breaks the line wherever the engine wasn't firing
        burn_x = np.where(burn_mask, rocket_xy[:len(burn_mask), 0], np.nan)
        burn_y = np.where(burn_mask, rocket_xy[:len(burn_mask), 1], np.nan)

    ax.set_aspect("equal")
    ax.set_xlim(-500000, 500000)
    ax.set_ylim(-500000, 500000)

    def update(frame):
        for planet, d in data.items():
            k = min(frame, len(d) - 1)
            circles[planet].center = (d[k, 0], d[k, 1])
            labels[planet].set_position((d[k, 0], d[k, 1]))
            trail_lines[planet].set_data(d[:k + 1, 0], d[:k + 1, 1])

        artists = (list(circles.values()) + list(labels.values())
                   + list(trail_lines.values()))

        if burn_line is not None:
            k = min(frame, len(burn_x) - 1)
            burn_line.set_data(burn_x[:k + 1], burn_y[:k + 1])
            artists.append(burn_line)

        return artists

    ani = FuncAnimation(fig, update, frames=frames, interval=20, blit=True)
    plt.show()
    return ani