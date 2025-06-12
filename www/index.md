---
title: SMIL3D Project Overview
---
Technical Report on Drone Performance and Testing: [Here](Oliver_Technical_Report.html)

Technical Report on Thermal Analysis and Simulation: [Here](Hussain_Technical_Report.html)

Technical documentation on mechanical design and CAD:
* [Design review and initial concept](https://github.com/Technology-for-the-Poorest-Billion/2025-ideabatic-3DPrint/blob/main/www/Design%20review%20and%20initial%20concept%20-%20Iain.md)
* [Prototype V1 Cad and design](https://github.com/Technology-for-the-Poorest-Billion/2025-ideabatic-3DPrint/blob/main/www/Prototype%20V1%20CAD%20and%20design%20-%20Iain.md)
* [Prototype evaluation and recommendation](https://github.com/Technology-for-the-Poorest-Billion/2025-ideabatic-3DPrint/blob/main/www/Prototype%20evaluation%20and%20recommendations%20-%20Iain.md)
* [Bill of materials](https://github.com/Technology-for-the-Poorest-Billion/2025-ideabatic-3DPrint/blob/main/www/Bill%20of%20materials%20-%20Iain.md)

[Icebox V1 Cad on onshape](https://cad.onshape.com/documents/73ee3694d82d5930b59690d2/w/6676daabe459417f310d4151/e/e961ad116b7d00652cd5d247)

[Icebox V2 Cad on onshape](https://cad.onshape.com/documents/1ee9565f677b677fef8eeaaf/w/12e6d9e0f6dfd3fd041557f7/e/68c45bec8085765a59e01fa4)

# Technical overview
The technical overview is broken up into three sections
* Background
* Technical summary
* Next steps and recommendations

## Background
Ideabatic has developed the SMILE icebox for transporting vaccines to remote locations shown below in the image
![image](https://github.com/Technology-for-the-Poorest-Billion/2025-ideabatic-3DPrint/blob/main/Images/Smile%20icebox.png)

This icebox provides significant usability and performance benefits over existing iceboxes, with a vaccine lifespan of 4 days compared to a few hours in conventional vaccine iceboxes through a combination of poor usage and design. However currently these iceboxes are CNCed, which is costly and not scalable.

### Design brief
As such the following design brief was given to help Ideabatic further develop the SMILE icebox. With the four areas highlighted specifically mentioned in the technical summary. 

![image](https://github.com/Technology-for-the-Poorest-Billion/2025-ideabatic-3DPrint/blob/main/www/Images/Design%20brief.png)

In addition to these design considerations, after discussions with Kitty at Ideabatic, drone transportation of the SMILE icebox was also identified as a major opportunity, so lightweighting and downsizing the icebox is a priority.



## Technical summary
The technical summary focuses on the four areas highlighted in the design brief. The goal of low cost manufacture of the SMILE icebox was found to be completely feasible with significant process towards this aim made in the 4 weeks. 
### 1: Manufactured protoypes
Two full function prototypes of the SMILE icebox were developed.

![image](https://github.com/Technology-for-the-Poorest-Billion/2025-ideabatic-3DPrint/blob/main/www/Images/Icebox%20comparison.png) 

These prototypes are built off a general concept [initial concept](https://github.com/Technology-for-the-Poorest-Billion/2025-ideabatic-3DPrint/blob/main/www/Design%20review%20and%20initial%20concept%20-%20Iain.md) of a thin 3d printed shell stiffened and insulated with expanding foam. Unlike the current SMILE design, it is based on a 1L icepack bottle and only has 10 vaccine compartments as opposed to 19. Despite this the later prototype has preserved all of the features present in the large scale SMILE, including a self closing door and carousel. 

In addition the new prototype is significantly lighter weighing just 1.6kg versus 4.5kg for the original design and features mounting for drone transport . 

With an estimated material cost of [£65](https://github.com/Technology-for-the-Poorest-Billion/2025-ideabatic-3DPrint/blob/main/www/Bill%20of%20materials.md) for the prototype we have fully demonstrated the feasiblity of low cost manufacturing and these prototypes can act as a spring broad for future in service designs. 

### 2: Engineering lessons
Alongside the finished prototypes, one of the most useful lessons learnt from this project are the engineering lessons learnt throughout the project. 

* The general concept of a thin 3d print riveted together and filled with expanding foam worked very well,
* A lot was learnt about the constraints of 3D printing
* Care needs to be taken on how to split 3D prints
* Riveting 3D prints together to make larger components works well, but care needs to be taken to avoid cracking.

### 3: Quality control
In order to ensure quality, even if the icebox is locally manufactured.
* Design for 3D printing, avoiding complex features and overhangs.
* Rivets are easy to inspect
* Expanding foam helps hold part together

### 4: Thermodynamics
A key aspect of this project was thermal modelling done by Hussain, this thermal model was validated with a thermal test in the V1 icebox prototype. 

## Next Steps and recommendations:
Clear improvements can be made to the future icebox, especially with regards to refining how the design is split, further expanding on the design approach of printing "accurate" parts in one piece such as the door and inner shell parts shows promise.

There is also scope to refine material choice and thickness and some features like the self closing vaccine door require significantly more engineering work to ensure a seal, and further validation of thermal performance and weather resistance is needed.



Reflective Discussion: Alignment with Sustainable Development Goals and UNICEF Principles for Digital Development
Our "Technology for the Poorest Billion" project, through the "Smile" vaccine cooler and its drone delivery system, addresses critical humanitarian challenges. The work aligns directly with Sustainable Development Goals (SDGs) and key UNICEF Principles for Digital Development. This reflects a commitment to impactful, responsible innovation.

The project aligns with SDG 3: Good Health and Well-being. By maintaining vaccines within the 2 
∘
 C−8 
∘
 C range across demanding terrain, we directly reduce spoilage and improve childhood immunisation rates. This mitigates ineffective doses due to cold chain failures, enhancing health outcomes and child survival in remote areas.

Our efforts also contribute to SDG 9: Industry, Innovation, and Infrastructure. The Smile cooler advances cold chain technology. Our 3D printing approach provides considerably more affordable production (£25-30k per unit vs. £300k for injection moulding), broadening access to this manufacturing method. Focused on drone delivery, it establishes resilient cold chain infrastructure where traditional logistics fail. Thermal modelling, a key component, enables design adaptation to evolving drone capabilities, improving humanitarian logistics.

The project addresses SDG 10: Reduced Inequalities. By enabling effective drone delivery of vaccines to often marginalised communities in Sub-Saharan Africa, the Smile cooler aims to close gaps in essential healthcare access. These communities historically face significant barriers due to isolation and poor infrastructure. Our goal is to ensure equitable access to fundamental vaccination, providing a consistent health baseline and combating national inequalities.

For SDG 12: Responsible Consumption and Production, our design prioritises waste minimisation and resource efficiency. The Smile cooler prevents vaccine spoilage in the field from temperature fluctuations, resulting in significant savings in time, resources, and energy. Our commitment extends to sustainable practices by planning to use recycled materials as 3D printing filaments, actively reducing environmental impact and demonstrating a circular economy approach.

Finally, SDG 17: Partnerships for the Goals is central to our achievements. Our collaboration with Ideabatic demonstrates effective multi-stakeholder engagement, combining academic research with a social enterprise's practical field experience. This fosters shared knowledge and resources towards a common development objective, strengthening implementation and global partnerships for sustainable development.

Our project also aligns closely with UNICEF Principles for Digital Development:

'Design with the User': The self-closing, magnetic lid reduces human error, ensuring vaccine integrity.

'Be Data-Driven': Meticulous thermal modelling guides design decisions through quantitative analysis.

'Understand the Existing Ecosystem': Durable cooler design accommodates challenging transport conditions.

'Design for Scale' & 'Be Sustainable': The cooler's cooling duration and drone adaptability promise long-term impact and resource efficiency.

'Do No Harm': Ensuring vaccine efficacy and safe delivery prioritises recipient well-being.

'Be Collaborative': The partnership fosters a shared mission for global health.

In conclusion, the "Smile" cooler is a comprehensive solution, designed with human well-being and sustainable development as core objectives. Through cold chain technology and delivery innovation, we aim to reduce health inequalities and build a more resilient future for vulnerable communities worldwide.


# Project Strategy: Oliver Griffiths

This project brought together many considerations concerning thermal performance and the use of 3D printing for manufacture, all underpinned by the payload requirements of a selected drone. These factors are closely intertwinned and the project ambitious; this called for effective communication, collaboration and pervasive planning to achieve the outcome we desired. Throughout, we communicated our main ideas and design decisions to Kitty at Ideabatic, to ensure our work culminated in what Ideabatic needed.

Our initial idea was concieved between Oliver, Iain and Hussain during the initial conferance showcasing all available projects. The three of us felt strongly about the use of 3D printing for manufacturing kittys product, and agreed delivery with drones was a compelling idea. This set a clear precident for the project, and we immediately met to discuss our induvidial strengths, weaknesses and aims. Following this, we developed a roadmap for the key deliverables and what we wanted to achieve by the close of the project.

Each team members strengths, weaknesses and aims were summarised:
Oliver has experience with mechanical design and building drones, as well as practical 3D printing knowledge. He has experience programming, but wants to develop those skills and his understanding of GIT for product development. 
Iain is excellent with CAD, and has great knowledge of procurement within the department through his time spent with the formula student team. He wants to develop his understanding of the constraints of 3D printing and how these are best mitigated.
Hussain has good understanding of heat transfer, taking both thermodynamics modules. 

With a good understanding of each others skills and aims, we laid out our ambitions of a complete, working example of a 3D printed vaccine cooler suitable for use with a drone of our choosing. 

To achieve this ambitous goal, a strict plan was set out using a Gantt Chart detailing the timeline of key technical developments, decisions and when manufacturing would have to begin. The plan played to each team members strengths, but also allowed each member to develop and meet their aims of the project. We communicated through a whatsapp group, and made full use of the GIT hub wiki and markdown files to record our research, development and the key lessons learnt. 

Hussain developed the thermal model, using content taught in the heat transfer module to inform the simulation. This tool enabled us to investigate different parameters and weights of payload to make an informed decision with regards to available drones. 

Iain focused on developing the Bulk of the CAD design, investigating ways to downsize the cooler while retaining the many features that make SMILE an effective solution. 

Oliver focused on researching available drones, and any necessary considerations that present themseleves for that use case. He also operated between Hussain and Iain on both the thermal model and CAD, helping bridge all these considerations and bring together the final prototype.

We played to each others strengths well, and were able to learn and develop from each other.

Not everything went smoothly, and in hindsight, the thermal test of our initial prototype should have been better planned, with access to the required equipment proving difficult and requiring some ingenuity. Time should have also been allocated to consider test and failed prints, with hardwork and effective troubleshooting required to develop our initial prototype in time for the interim presentation.  

For the CAD development, we opted to use OnShape - a browser based software that allowed our team to easily share and collaborate on the design. This was very effective, and allowed us to start collaborative CAD development immediately. 

Each team member spent some time becoming familiar with GIT, and this proved very beneficial to our team working abilitiy. In a manner similar to onshape, we were able to quickly develop code, with Oliver and Husaain developing their thermal simulation remotely.The repositry was also incredibly useful as a central hub for all our documentation, and we hope it will become a rich resource for Ideabatic as they continue to develop SMILE.




