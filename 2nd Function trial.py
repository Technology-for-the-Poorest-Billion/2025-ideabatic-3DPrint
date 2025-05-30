import numpy as np
import matplotlib.pyplot as plt

def Rth_radial(r1, r2, k, l):
    return np.log(r2 / r1) / (2 * np.pi * l * k)

def Rth_linear(t, A, k):
    return t / (A * k)

def convection_resistance(r_outer, h, l):
    return 1 / (2 * np.pi * r_outer * l * h)

def estimate_performance(r_ice, l, t_insulation, t_air, t_foam, m_ice=0,
                         k_insulation=0.03, k_air=0.024, k_foam=0.03,
                         h_air=5, h_outer=10, T_e=30, T_ice=0,
                         SLH_ice=334000):
    m_ice = r_ice**2 * np.pi * l * 917  # More accurate ice mass calculation (917 kg/m³ ice density)
    
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

    return {
        "Q_dot_total": Q_dot_total,
        "t_cool_hours": t_cool_hours,
        "outer_diameter_cm": 2 * r_foam * 100,
        "Total_mass_of_ice": m_ice,
        "insulation_thickness": t_insulation
    }

def analyze_insulation_performance(base_params):
    """Analyze how insulation thickness affects cooling performance"""
    # Vary insulation thickness from 1mm to 10cm
    insulation_thicknesses = np.linspace(0.001, 0.1, 100)
    
    results = []
    for t_ins in insulation_thicknesses:
        params = base_params.copy()
        params['t_insulation'] = t_ins
        result = estimate_performance(**params)
        results.append(result)
    
    return results

def find_diminishing_returns(results, threshold=0.1):
    """Find the point where adding more insulation gives < threshold% improvement"""
    max_hours = max(r['t_cool_hours'] for r in results)
    for i, r in enumerate(results):
        if i == 0:
            continue
        improvement = (r['t_cool_hours'] - results[i-1]['t_cool_hours']) / results[i-1]['t_cool_hours']
        if improvement < threshold/100:
            return results[i-1]
    return None

def plot_insulation_analysis(results, diminishing_point=None):
    """Plot the performance vs insulation thickness"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    # Plot cooling time vs insulation thickness
    thickness = [r['insulation_thickness']*1000 for r in results]  # in mm
    hours = [r['t_cool_hours'] for r in results]
    ax1.plot(thickness, hours)
    ax1.set_xlabel('Insulation Thickness (mm)')
    ax1.set_ylabel('Cooling Time (hours)')
    ax1.set_title('Cooling Performance vs Insulation Thickness')
    ax1.grid(True)
    
    # Plot cooling time vs outer diameter
    diameters = [r['outer_diameter_cm'] for r in results]
    ax2.plot(diameters, hours)
    ax2.set_xlabel('Outer Diameter (cm)')
    ax2.set_ylabel('Cooling Time (hours)')
    ax2.set_title('Cooling Performance vs Container Size')
    ax2.grid(True)
    
    if diminishing_point:
        ax1.axvline(x=diminishing_point['insulation_thickness']*1000, color='r', linestyle='--', 
                   label=f"Diminishing returns at {diminishing_point['insulation_thickness']*1000:.1f}mm")
        ax1.legend()
        
        ax2.axvline(x=diminishing_point['outer_diameter_cm'], color='r', linestyle='--',
                   label=f"Diameter at diminishing returns: {diminishing_point['outer_diameter_cm']:.1f}cm")
        ax2.legend()
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    # Base parameters
    base_params = {
        'r_ice': 0.05,      # 5cm ice radius
        'l': 0.15,          # 15cm length
        't_insulation': 0.005,  # 5mm insulation (will be varied)
        't_air': 0.04,      # 4cm air gap
        't_foam': 0.04      # 4cm foam
    }
    
    # Analyze insulation performance
    results = analyze_insulation_performance(base_params)
    
    # Find point of diminishing returns
    diminishing_point = find_diminishing_returns(results, threshold=1)  # 1% improvement threshold
    
    # Print key findings
    if diminishing_point:
        print(f"Point of diminishing returns at {diminishing_point['insulation_thickness']*1000:.1f}mm insulation")
        print(f"  - Cooling time: {diminishing_point['t_cool_hours']:.1f} hours")
        print(f"  - Outer diameter: {diminishing_point['outer_diameter_cm']:.1f}cm")
        print(f"  - Ice mass: {diminishing_point['Total_mass_of_ice']:.2f}kg")
    else:
        print("No clear point of diminishing returns found in the tested range")
    
    # Plot results
    plot_insulation_analysis(results, diminishing_point)