import numpy as np

def Rth_radial(r1, r2, k, l):
    return np.log(r2 / r1) / (2 * np.pi * l * k)

def Rth_linear(t, A, k):
    return t / (A * k)

def convection_resistance(r_outer, h, l):
    return 1 / (2 * np.pi * r_outer * l * h)

def estimate_performance(r_ice, l, t_insulation, t_air, t_foam,
                         k_insulation=0.03, k_air=0.024, k_foam=0.03,
                         h_air=5, h_outer=10, T_e=30, T_ice=0,
                         m_ice=2.5, SLH_ice=334000):
    
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
        "outer_diameter_cm": 2 * r_foam * 100
    }

# Example usage
result = estimate_performance(
    r_ice=0.08,
    l=0.2,
    t_insulation=0.005,
    t_air=0.04,
    t_foam=0.08
)

for k, v in result.items():
    print(f"{k}: {round(v, 2)}")

