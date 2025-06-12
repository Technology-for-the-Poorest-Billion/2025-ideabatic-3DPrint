Individual Report: Thermal Performance Modelling and Optimisation
Author: Hussain Ahmed Khan

1. Introduction: Addressing the Cold Chain Challenge
The "Technology for the Poorest Billion" project addresses the need for reliable cold chain solutions where infrastructure is limited. The "Smile" cooler aims to keep vaccines cool and ensure their safe transport over long, difficult journeys.

Previous designs failed due to human error, such as frequent lid opening, causing vaccine exposure and potency loss. The Smile cooler includes an internal carousel. This allows vaccine access without fully opening the main cooler, reducing heat exposure.

Vaccines require 2∘C − 8∘C. Deviations outside this range degrade vaccines, so precise temperature control is critical.

The cooler targets Sub-Saharan Africa. This region typically has high ambient temperatures and humidity. Journeys are demanding, involving rough terrain and significant vibration. The carousel is rubber-tipped to absorb shocks, protecting vaccine bottles.

My contribution focused on developing and refining a thermal simulation model. This model predicts cooler performance and optimises insulation for challenging, off-grid vaccine transport. This report details the model's technical aspects, capabilities, design influence, and future development.

2. Technical Presentation of the Solution (Handover Notes for Partner: Ideabatic)
The thermal model simulates heat transfer through a multi-layered cylindrical cooler. Its main purpose is to predict heat ingress and the duration ice maintains the cooler's internal temperature at approximately 0∘ C. This enables rapid virtual prototyping, reduces expensive physical tests, allows performance prediction, and aids material/dimension selection.

The model considers two fundamental heat transfer modes:

Conduction: Heat transfer through solid insulation layers.

Natural Convection: Heat transfer across the internal air gap and from the external surface to the ambient air.

The analysis uses the Ohm's Law Analogy for heat transfer, where heat flow (Q dot) is proportional to the temperature difference (ΔT) divided by the total thermal resistance (Rth):


Qdot = ΔT/Rth 
​
 
Model Components and Calculations:

Radial Heat Transfer (Cylindrical Sides):
The model calculates heat flow through the side walls using the Rth radial function. This applies the standard formula for cylindrical shell thermal resistance:

R th, radial = 2πLk ln(r2/r1)
​
 

where r1 is the inner radius, r2  is the outer radius, L is the length, and k is the thermal conductivity.

Radial layers include:

Inner Insulation Layer: Outside the ice container. Thermal conductivity (k insulation, inner) set to 0.03 W/mK.

Air Gap: Modelled as convective resistance. Natural convection coefficient (h_{\text{air_gap}}) set to 3.0 W/m2 K.

Outer Foam Layer: Outermost insulation. Thermal conductivity (k 
foam, outer) set to 0.03 W/mK.
External convection from the cooler's outer surface to ambient air is also included, using an empirical relationship based on external air speed.

Planar Heat Transfer (Top and Bottom):
Heat flow through the flat top and bottom surfaces is calculated using the Rth linear function. This applies the standard formula for flat slab thermal resistance:


Rth,linear  = t/ A⋅k

 

where t is the thickness, A is the area, and k is the thermal conductivity.

Linear layers (top and bottom) include:

Flat Inner Insulation: Same thermal conductivity as radial inner insulation (k_{\text{flat, insulation, top_bottom}}) set to 0.03 W/mK.

Flat Outer Foam: Same thermal conductivity as radial outer foam (k_{\text{flat, foam, top_bottom}}) set to 0.03 W/mK.

Phase Change Calculation: Total heat ingress determines ice duration. The model estimates time until all ice melts by dividing the energy to melt ice (ice mass × specific latent heat) by the total heat ingress rate.

Boundary Temperature Calculations: The model predicts temperatures at insulation layer interfaces. This is vital for vaccine safety, ensuring the vaccine container interface stays within the 2∘C − 8∘C range, preventing freezing while optimising cooling duration.

Baseline Model Parameters:

Initial "baseline" cooler design characteristics:

Mass of ice (m ice): 2.5 kg

Length of cylindrical container (L container): 0.2 m

Radius of inner ice container (rice ): 0.08 m

Thickness of inner insulation (tinsulation, inner): 0.005 m

Thickness of air gap (t_{\text{air_gap}}): 0.04 m

Thickness of outer foam (t foam, outer): 0.08 m

Thickness for flat inner insulation (t_{\text{flat, insulation, top_bottom}}): 0.005 m

Thickness for flat outer foam (t_{\text{flat, foam, top_bottom}}): 0.05 m.

Specific Latent Heat of Fusion for ice (SLH ice): 334000 J/kg

Environment Temperature (T environment): 30∘C (test condition)

Ice Temperature (T ice, temp): 0∘C (constant for melting ice)

External Air Speed (v external, air): 1.0 m/s (test condition)

Key Assumptions and Simplifications:

Steady-State Heat Transfer: Model assumes constant temperatures.

Ignoring Radiation: Radiation heat transfer not explicitly included.

Ignoring Plastic Conduction: Plastic casing thermal contribution deemed negligible.

Uniform Material Properties: Thermal conductivities and convection coefficients assumed constant.

Simplified Geometry for Flat Sections: Flat top and bottom areas approximated using inner ice container's cross-sectional area.

Empirical Convection Correlations: Model uses estimated or empirical convection coefficients.

3. Description of Data/Code/Blueprints Available in the Repository
The Python code for the thermal model is on GitHub:
https://github.com/Technology-for-the-Poorest-Billion/2025-ideabatic-3DPrint/blob/64eca1a5af41744abf37b80db37fa1698ad59f40/Hussain-Thermal-Model-Kitty.ipynb

The code uses Python, mainly numpy for calculations. matplotlib is imported for potential future visualisation.

The model's core logic is in the calculate_cooler_performance function. This function takes design and environmental parameters for simulations. Output includes:

total_heat_loss_W

cooling_duration_hours

total_outer_diameter_cm

temp_at_insulation_edge_degC

temp_at_air_edge_degC (boundary temperatures for safety analysis).

An example of function use is in the if __name__ == "__main__": block of the Jupyter notebook. This aids testing and design verification.

4. Design Background and Iteration
The initial baseline cooler aimed for high vaccine capacity. However, project needs, particularly drone delivery, required significant size and weight reduction.

The cooler's overall size and shape changed, impacting insulation thicknesses, ice container radius, and length. These changes affected thermal performance.

A key decision was to fix the ice bottle size, building layers around it. This led to a smaller cooler. As a trade-off, ice duration reduced, and transportable vaccine doses decreased from approximately 540 to 270.

For the shrunk design, fixed ice bottle parameters were:

Length (Lcontainer): 0.155 m

Radius (rice): 0.045 m

Mass (mice): 1 kg

The objective for this smaller shape was to maximise cooling time for drone delivery. This involved iterating on insulation layer thicknesses:

t insulation, inner  (inner insulation)

t_{\text{air_gap}} (air gap)

t foam, outer (outer foam)

t_{\text{flat, insulation, top_bottom}} (flat inner insulation)

t_{\text{flat, foam, top_bottom}} (flat outer foam)

Material thermal conductivities (k values) and convection coefficients (h values) remained constant during optimisation, focusing on physical dimensions.

5. Experimental Setup (for Virtual Simulations) and Results
The calculate_cooler_performance function ran simulations to explore the design space around the smaller cooler's fixed inner dimensions (L container  = 0.155 m, r ice = 0.045 m, 1 kg ice).

Insulation layer thicknesses were systematically varied to observe their impact on cooling duration and total heat loss. This identified trade-offs between insulation effectiveness and cooler size. Iteration increments were managed by other team members, with variations within 3D printing capabilities (FDM tolerances typically ±0.1 mm to ±0.5 mm).

The optimised smaller cooler achieved a cooling life significantly greater than the 24-hour drone delivery minimum, indicating robust thermal performance.

Diminishing Returns Analysis ("Python Profile"):
A 'python profile' analysis was conducted to understand insulation efficiency. This script takes ice container dimensions and identifies the point where adding more insulation yields diminishing returns in cooling performance. It systematically varies an insulation thickness (e.g., t 
insulation from 0.001 m to 0.1 m) and calculates marginal cooling time gain.

The 'python profile' is a future design tool. It allows teams or Ideabatic to quickly calculate optimal insulation thickness for coolers with different internal dimensions (e.g., for larger drone payloads). It helps identify the 'sweet spot' for insulation, avoiding unnecessary material cost, weight, or size for minimal thermal gain.

Optimal Design Parameters and Performance:
The optimised 'current design' achieved:

Cooling Duration: 85 hours

Total Outer Diameter: 31.8 cm

The specific insulation thicknesses for this optimal design were determined by the optimisation process.

6. Instructions on Manufacturing and Assembly (Informed by Model)
Direct manufacturing and assembly are handled by the CAD group. My thermal modelling provides quantitative specifications that directly inform their design and production.

The thermal model's output, including identified 'optimal' dimensions (e.g., inner insulation, air gap, outer foam thicknesses, and overall cooler diameter), acts as a blueprint for thermal performance. The model dictates:

Precise length (0.155 m) and radius (0.045 m) for the central ice bottle.

Required thicknesses for each insulation layer to achieve target cooling duration.

Necessary thermal conductivity values (k) for sourced materials (e.g., 0.03 W/mK for foam and inner insulation).

The model ensures physical dimensions and material choices from CAD/manufacturing yield desired cold chain performance. Components produced to specified dimensions (within typical 3D printing tolerances, e.g., ±0.1 mm to ±0.5 mm) with specified thermal properties are predicted to perform as intended.

7. Suggestions for Improvement (If more time)
For Ideabatic (Immediate/Near-Term Improvements):

Cost-Benefit Analysis Integration: Integrate a basic cost model into the simulation to optimise based on cooling duration per unit cost or volume.

Material Library Expansion: Develop a comprehensive, externally accessible database of common insulation materials (thermal conductivities, densities, approximate costs) relevant to Ideabatic's supply chain.

User-Friendly Interface: Develop a simplified front-end (e.g., web tool or interactive Jupyter dashboard) for the thermal model.

For Future Students (Longer-Term Research/Development):

Radiation Heat Transfer: Incorporate a robust model for radiation heat transfer, particularly for coolers exposed to direct sunlight or warm surfaces.

Transient Thermal Analysis: Extend the steady-state model to a transient analysis. This would simulate the cooler's internal temperature profile over time as ice melts, providing granular data on vaccine temperature ranges.

Advanced Convection Modelling: Investigate and implement more sophisticated empirical correlations for natural and forced convection, especially for complex geometries or varying external air flow conditions.

Multi-Objective Optimisation: Explore advanced optimisation algorithms (e.g., genetic algorithms, scipy.optimize) to simultaneously optimise conflicting objectives (e.g., maximising cooling duration, minimising size/weight, and minimising material cost).

Physical Validation: Design and conduct controlled physical experiments on prototype coolers to rigorously validate model predictions.

Phase Change Material (PCM) Integration: Extend the model to simulate different Phase Change Materials (PCMs) beyond ice. This could allow for maintaining different temperature ranges (e.g., 4∘
 C without freezing) or achieving longer durations.

Vibration and Structural Analysis: While rubber tips mitigate vibration, a future model could explore thermal implications of repeated mechanical stresses on insulation or the effectiveness of vibration dampening materials.
