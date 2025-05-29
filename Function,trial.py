import numpy as np
import matplotlib.pyplot as plt
def Rth_radial(r1, r2, k, l):
    return np.log(r2 / r1) / (2 * np.pi * l * k)

def Rth_linear(t, A, k):
    return t / (A * k)

def convection_resistance(r_outer, h, l):
    return 1 / (2 * np.pi * r_outer * l * h)

#nice function. I have modified it though so that m_ice changes with r_ice - will allow us to easily consider effect of different ice masses (for given length)
def estimate_performance(r_ice, l, t_insulation, t_air, t_foam, m_ice=0,
                         k_insulation=0.03, k_air=0.024, k_foam=0.03,
                         h_air=5, h_outer=10, T_e=30, T_ice=0,
                         SLH_ice=334000):
    m_ice = r_ice *r_ice * np.pi *0.1275 * 1000 #added this.
    # Radial distances
    r_insulation = r_ice + t_insulation
    r_air = r_insulation + t_air
    r_foam = r_air + t_foam

    # Radial resistances
    Rth_insulation = Rth_radial(r_ice, r_insulation, k_insulation, l)
    Rth_air = 1 / (2 * np.pi * r_insulation * l * h_air)  # convection
    Rth_foam = Rth_radial(r_air, r_foam, k_foam, l)
    Rth_convection = convection_resistance(r_foam, h_outer, l)

    # Total radial resistance
    Rth_total_radial = Rth_insulation + Rth_air + Rth_foam + Rth_convection

    # Flat surface conduction (ends)
    A = np.pi * r_ice**2
    Rth_flat_insulation = Rth_linear(t_insulation, A, k_insulation)
    Rth_flat_foam = Rth_linear(t_foam, A, k_foam)
    Rth_total_flat = Rth_flat_insulation + Rth_flat_foam

    # Total heat flow
    delta_T = T_e - T_ice
    Q_dot_radial = delta_T / Rth_total_radial
    Q_dot_flat = 2 * delta_T / Rth_total_flat  # two flat ends
    Q_dot_total = Q_dot_radial + Q_dot_flat

    # Time until ice melts
    Q_ice = m_ice * SLH_ice
    t_cool = Q_ice / Q_dot_total
    t_cool_hours = t_cool / 3600

    # Boundary temperatures
    delta_T_insulation = Q_dot_total * Rth_insulation
    T_edge_insulation = delta_T_insulation

    delta_T_air = Q_dot_total * Rth_air
    T_edge_air = delta_T_insulation + delta_T_air

    return {
        "Q_dot_total": Q_dot_total,
        "t_cool_hours": t_cool_hours,
        "T_edge_insulation": T_edge_insulation,
        "T_edge_air": T_edge_air,
        "outer_diameter_cm": 2 * r_foam * 100,
        "Total_mass_of_ice": m_ice
    }

# Example usage
"""
result = estimate_performance(
    r_ice=0.08,
    l=0.2,
    t_insulation=0.005,
    t_air=0.04,
    t_foam=0.08
)
hours = result["t_cool_hours"]
print(hours)"""
#defining variables for plotting
fig, ax = plt.subplots() 
thickness = np.linspace(0,0.1,1000)
hourlistfoam = np.zeros(1000)
totaldiameterfoam = np.zeros(1000)
totaldiameterice = np.zeros(1000)
hourlistmass = np.zeros(1000)
totalmassice = np.zeros(1000)

for i in range(1000):
    result = estimate_performance(
    r_ice=0.05,
    l=0.15,
    t_insulation=0.005,
    t_air=0.04,
    t_foam= thickness[i],
    )
    hours = result["t_cool_hours"]
    hourlistfoam[i] = hours
    totaldiameterfoam[i] = result["outer_diameter_cm"]

for i in range(1000):
    result = estimate_performance(
    r_ice=thickness[i],
    l=0.15,
    t_insulation=0.005,
    t_air=0.04,
    t_foam=0.04,
    )
    hours = result["t_cool_hours"]
    hourlistmass[i] = hours
    totaldiameterice[i] = result["outer_diameter_cm"]
    totalmassice[i] = result["Total_mass_of_ice"]

result = estimate_performance(
    r_ice=0.05,
    l=0.15,
    t_insulation=0.005,
    t_air=0.04,
    t_foam=0.04,
    )

d_ice_one_kg = result["outer_diameter_cm"]
#print(d_ice_one_kg)
#overlay this plot with payload - range data from ISS aerospace to get a feeling for the tradeoff. I think 1kg is a good decision, which last year came to and this verifies that.

ax.plot(totaldiameterfoam, hourlistfoam, label = "changing insulation thickness")
plt.axvline(x = d_ice_one_kg, color='r', linestyle='--', label='M = 1kg')
ax.plot(totaldiameterice, hourlistmass, label = "changing mass of ice")  # Plot some data on the Axes.
#ax.plot(totalmassice, hourlistmass, label = "changing mass of ice")#superpose with iss aerospace data
ax.set_xlabel('Cooler diamter (cm)')  # Add an x-label to the Axes.
ax.set_ylabel('cool life (hours)')  # Add a y-label to the Axes.
ax.set_title("Thermal performance plot")  # Add a title to the Axes.
ax.legend()
ax.grid(True)
plt.show()                           # Show the figure.


"""
for k, v in result.items(): #result is a dictionary 
    print(f"{k}: {round(v, 2)}")

"""