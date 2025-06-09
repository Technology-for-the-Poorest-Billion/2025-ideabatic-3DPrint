# Current Progress
At this stage (01/06/2025), we have developed an initial prototype of a smaller, 3D printed vaccine cooler. 

![](https://github.com/Technology-for-the-Poorest-Billion/2025-ideabatic-3DPrint/blob/main/Images/Comparison%201.jpg)

Using our own thermal simulation, we have sized the cooler with consideration of cool life, weight and size; all in the context of being used as a payload for a selected drone. 

The last week, we have developed the CAD model and have 3D printed the initial design. We are currently reviewing this design, and throughout the next week, we will be updating and refining it based on the key takeaways. Experimentation of the cool life will also be performed, to verify our thermal simulations.

We will also be speaking to ISS aerospace, a British drone manufacturer who have a suitable drone platform and may be a suitable partner for Ideabatic in the long run.
 
Throughout, we have logged our work and findings within the wiki section of GIThub, ensuring our decisions are fully explained.

## Drone suitability review
One of the key aims of this project is to provide a cooler that can be delivered by drone. We have completed market research on this area to explore different drone options, and the key considerations one should make when selecting a suitable drone platform. This has been compiled and put into a separate wiki, but a brief overview is provided here: 

Disk loading = Total Weight / Rotor disk area 

Low disk loading - large rotors spread weight over more air, resulting in more efficient flight. 

To maximise flight time, disk loading should be minimised; 
- rotor size limited by transport considerations.
- minimise the payload weight.

We have reviewed the market for drones that will be small enough for transport by car/ truck, before exploring the impact different weights have on range. 

ISS aerospace offers a range of drone platforms. We believe their sensus M4 will be a good choice, considering its size and payload capabilities. 
Its specs are as follows:
> Max Flight time (No Payload): 45 minutes

> Max Flight time (5kg Payload): 25 minutes

> Range: 67.5km

![](https://www.unmannedsystemstechnology.com/wp-content/uploads/2023/03/M4-P-1024x558.jpg)

Considering our basic thermal model and the reduced need for cooling due to faster delivery, we concluded using a 1 litre bottle with 1kg of ice was the best middle ground in terms of range and cool life, close to two days. We expect a flight time of approximately 35 - 40 minutes, which should enable a delivery distance of around 30km. We are meeting with ISS Aerospace later this week to discuss further the use of this drone, and understand any regulatory hurdles we may face. 

It is worth noting that the operator can use less ice if further range is required.  

## Python Thermal Simulation
# **Project Progress: Python Thermal Simulation**  
*Contributor: Hussain Khan* and Oliver Griffiths

## **Objective**  
Developed a Python-based thermal model to:  
- Predict cooling performance of the vaccine container   
- Ensure vaccines remain within safe temperature ranges (2°C to 8°C)
- Optimize ice mass and insulation thickness   

## **Key Developments**  

### **1. Model Correction**  
- **Initial Issue:**  
  - Original model predicted air gap temperatures of **25.8°C** (would destroy vaccines)  
  - Root cause: Incorrectly assumed **conductive** heat transfer in still air  
- **Solution:**  
  - Updated to account for **convective** heat transfer (dominant in air gaps)  
  - Resulted in stable **11°C** prediction (realistic for our design)  

### **2. Design Adaptation**  
- Refactored model to accept **variable ice pack dimensions**:  
  ```python
  def calculate_ice_mass(radius, length):
      # Returns ice mass in grams based on geometry

## **Simulation Capabilities**  
- **Enabled simulations for:**  
  - Different container sizes  
  - Various insulation thicknesses  

## **Performance Optimization**  
- **Identified diminishing returns for:**  
  - Ice mass vs. cooling duration  
  - Insulation thickness vs. weight  
- **Key Outcome:**  
  - Provides drone-compatible design guidelines  

## **Impact**  
- **Thermal Safety Validation:**  
  - Prevents vaccine spoilage by verifying safe temperature maintenance  
- **Design Scalability:**  
  - Serves as baseline for future designs (adaptable for larger payloads)  


<!-- ## **Visualization**  
![Temperature Simulation Output](/images/thermal_model_results.png)  
*Example: Predicted air gap temperature over time*  

## **Code Reference**  
[View thermal_model.py](/scripts/thermal_model.py)   -->







![Diminishing returns graph](https://github.com/Technology-for-the-Poorest-Billion/2025-ideabatic-3DPrint/blob/main/Images/Diminishing%20returns%20case.png?raw=true)

## **Next Steps: Experimental Validation**  

### **Phase 1: Real-World Testing**  
- **Instrumented Prototype Testing**  
  - Deploy thermometers to track:  
    - Cooling duration (ice pack performance)  
    - Vaccine compartment temperature stability  
- **Model Calibration**  
  - Modify Python code based on experimental data  
  - Identify discrepancies between simulation and reality  

### **Phase 2: Iterative Development**  
- **Field-Informed Updates**  
  - Adjust convection parameters for different climate conditions  
  - Validate insulation performance under humidity/wind  
- **Practical Benchmarking**  
  - Compare simulation results against:  
    - Laboratory-controlled tests  
    - Short-range field deliveries  

### **Long-Term Vision**  
*While our simulation provides essential theoretical grounding, real-world deployment across diverse environments will require adaptive learning. This experimental phase bridges our Python model with the complexities of:*
- *Tropical vs. arid climates*  
- *Urban vs. rural transport conditions*  
- *Varying drone payload configurations*  

*Current work establishes the framework for this vital feedback loop.*




## Initial CAD design


## Key considerations for DFM with 3D printing
The printers have been running all weekend, with a number of lessons learnt.
Some of these issues can be solved through tuning of the printer settings, and other issues must be solved through re design. 
### What went well:
![3D printed Thread](https://github.com/Technology-for-the-Poorest-Billion/2025-ideabatic-3DPrint/blob/main/Images/IMG_7386.jpg)
![hole](https://github.com/Technology-for-the-Poorest-Billion/2025-ideabatic-3DPrint/blob/main/Images/IMG_7387.jpg)
Parts produced generally to a good standard, with key surfaces sized accordingly. Parts designed to screw together did so. It will be important to get good, consistent parts from a variety of different printers.
### Areas for improvement:
Generally, part quality suffered at overhangs and slight warping at walls. 
![Overhang](https://github.com/Technology-for-the-Poorest-Billion/2025-ideabatic-3DPrint/blob/main/Images/IMG_7385.jpg)
To speed up printing, we didn't use any supports on our parts. There are a few areas where this can be tolerated, but many parts will need re designing to solve this problem, using less aggressive overhangs. If we cannot achieve good results in this manner, we will opt to use support structures to help with the print. 
The most important areas where this is a problem are at part interfaces, where we are using a simple lap joint and riveting/bolting parts together. It is important a good fit is achieved here, and we have a few ideas for how these parts can be better joined together. 

This will be a key area of focus for the rest of the week. 


# Personal Development

## Oliver Griffiths 
Worked between Iain and Hussain on both CAD and thermal model, filling a range of roles. 
Reached out to ISS aerospace and developed technical requirements of drone, guiding overall direction of current development. 
Worked to 3D print model and address any issues of 3D printing as they presented themselves, as well as evaluating the current prototype. 

Learnt to better communicate on technical projects in a short time span, utilising GIT and whatsapp for effective communication and progress tracking.

## Hussain Khan
## **Technical Skills**
- **Advanced Python Proficiency**
  - Developed better functions, loops, and array manipulation
  - Implemented physical equations (conduction/convection)
- **Model Validation**
  - Debugged thermal models
  - Verified output realism

## **Non-Technical Skills**
* Problem-Solving
  * Resolved unexpected outputs
* Communication
  * Explained technical problems clearly






## Iain Lam

# Updated Project Plan
![](https://github.com/Technology-for-the-Poorest-Billion/2025-ideabatic-3DPrint/blob/main/Images/gantt%20chart.png)
We have been slightly behind on the previous plan, with 3D printing taking longer than expected. We have worked hard over the weekend to ensure we are up to date, and to enable development of the final iteration to go ahead this week.

Tomorrow, We will be filling the prototype with foam and performing the thermal test overnight to validate our thermal model. The hole for the bottle is slightly too small, so it will require an inventive approach to fill it with ice.

Towards the end of the week, when all thermal tests have been complete, we will perform a drop test to understand any weaknesses in the design. This will be used to inform the design of soft flexible parts made from TPU designed to protect from knocks and bumps.

The key CAD features to be developed:
- Key mating components to be redesigned to be printed in one piece. Ensures good, consistent fit. 
- Wall thickness and other weight saving measures to be made. Will need to fill with foam first to evaluate effect on printed parts, as well as reducing number of rivets where possible.
- Re design shell mounting method, and develop TPU (flexible material) parts to ensure rivets do not crack printed parts. These parts will also offer drop protection. 
- Add additional strengthening brackets to improve mating between two halves of the shell. 
- Re-design carousel to reduce weight.
- Add mounting points to allow the cooler to be worn as a sling, or to be attached to a drone.



