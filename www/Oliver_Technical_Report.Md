[link](/2025-ideabatic-3DPrint/linkedpage.html)
# Oliver Griffiths Technical Report
Author: Oliver Griffiths
This project has considered a range of technical areas. This report gives a brief overview of some of these aspects, looking at the key considerations made when selecting a suitable drone and the thermal and destruction testing of our initial prototype. The work will be summarised, and the key takeaways presented, serving as a basis for further development of this project. 

Where appropriate, links will be provided to other pages containing more detail. 

## Drone Performance and Regulation considerations:
One of the main objectives of this project is to develop a suitable vaccine cooler that could be delieverd on foot or by drone. Ideabatic were keen to explore this avenue. As dronesare becoming bigger, flying further and falling in price, they are becoming better positioned for this use. There are many aspects beyond technical design to enable these drone deliveries, with regulation being a big factor that will need to be explored further if this work develops.

Having experience developing a large drone for offshore windturbing inspections, I was well placed to lead this research with a good understanding of the currently available technology. After speaking with kitty, I developed a good understanding of a typical vaccine delivery journey and the limitations of current infrastructure. 

These vaccines are typically driven to a location as a close to the final location as possible, before being hiked for several hours to their final destination.  As such, the opportunity to use a drone that was small enough to fit in the bed of a truck seemed ideal, especially as these larger drones could carry a payload of the size needed. Kitty felt that the current solution carrying 500 doses was excessive, relaxing the constraint on the number of vaccines that needed to be carried. There are several things to note here: Driving the majority of the journey massively relaxes the range requirement of the drone, and the nature of delivery with drones meant that multiple vaccine deliveries could be easily made at little marginal cost, meaning the number of vaccines taken by the drone could be reduced.

With an idea of the kind of solution that could be made and the size of drone that would be used, we began researching possible drones that could be used to inform our decisions on the design of the cooler. Immediately we were lead to ISS aerospace, and their Sensus M aircraft. The specs are as follows: 

> Max Flight time (No Payload): 45 minutes

> Max Flight time (5kg Payload): 25 minutes

> Range: 67.5km

From this information alone, we were able to make an informed decision of a rough weight of the payload, aiming to keep it below 2.5kg and have a flight time above 30 minutes, and range of 30km (round trip). With ISS aerospace based in the UK, they seemed like a good option to aid in the development of the payload. 

After getting in touch, they kindly arranged for us to meet with one of their engineers to further discuss the project. The interview was filled with great information and advice, and has been documented in the wiki: https://github.com/Technology-for-the-Poorest-Billion/2025-ideabatic-3DPrint/wiki/Drone-Sizing-,-constraints-and-regulation. 

To summarise, they felt their drone was a suitable choice and that our prototype cooler would work well with their drone. They spent a long time informing us of regulation and using the drone, and the snags we could expect to meet. Their largest concern was the nature of the operation being BVLOS (Beyond Visual Line of Sight). Whilst they didnt comment on any specific regions, they had operated in rural Africa before and stated that regulation often wasn't in place, or was only partially in place for BVLOS. However, they had stated they had been granted special clearance before, and felt the nature of our use could be granted similar special permissions to operate in these remote regions. 

They were also wary of landing the drone for a number of reasons. These are listed fully in the link above, but they felt there may be issues with landing and safely removing the coolbox, but there are ways to easily address these problems. They felt our current solution of strapping the payload onto the bottom of the drone was suitable, with it being intuitive and secure. A more complex arrangement could be made, but both we and them felt this would be unnecessary. It is important regulations and operating processes for areas where smile would deploy this solution are looked at more closely, to ensure the operation is both safe and legal.

Finally, the cost of the drone with everything needed to fly would cost around £30 000. Next steps should do a deeper analysis into the cost of using the drone versus traditional means, to understand if there are any cost savings in the long run. I believe if ideabatic wants to implement a larger scale operation for delivering vaccines, then drones offer the best choice and should be pursued. However, no significant analysis of the associated costs has been completed. 

Unfortunately, we were not able to conduct a test flight with our final prototype, but ISS aerospace said they would be happy to do a demonstration flight. Kitty intends to do this with ISS over the summer, and something our group hopes to be a part of. 

For anyone continuing this work, I would strongly recommend ISS aerospace as a partner, who have been very generous with their advice.

## Thermal Test
![image](https://github.com/Technology-for-the-Poorest-Billion/2025-ideabatic-3DPrint/blob/main/Images/IMG_7425.jpeg?raw=true)
With our initial prototype built, we wanted to compare the thermal performance of the prototype to the simulation created by myself and Hussain. With a tight schedule, I had to develop a suitable experiment with accurate temperature and timing, with limited hardware. Using a buzzer, arduino Uno and a temperature sensor, I wrote suitable firmware that would sound the buzzer when the temperature went above 10 degrees centigrade. For timing, I couldn't rely on the uno timing function as this was inaccurate over long time periods. Instead, I set up the experiment in my Gyp and kindly asked my flatmates to note down the time and date when it started buzzing. 

Our initially prototype had a mistake, with the ice container being too small for the 1 litre bottle we were using. We resorted to using crushed up ice, placing this directly in the slot for the bottle. Whilst there were no explicit gaps, this was not water tight and led to all water draining as the ice melted. Being short on time and needing to complete further tests, I decided to continue this test and see if the ice box would still exhibit good performance. The vaccines were held at suitable temperature for 27 hours and 23 minutes, despite the water draining from the cool section. Whilst this is still impressive, it is not the performance we were expecting. I believe the leak was responsible for a significant drop in performance from the simulated 88 hour cool life, with conduction to the vaccine chamber being decreased. After the test, a significant amount of ice was still present. 

Going forward, it is important this test is repeated to better validate our thermal model. The code used for my temperature sensor can be found in the GIT hub repositry (https://github.com/Technology-for-the-Poorest-Billion/2025-ideabatic-3DPrint/blob/main/Temperature_sensor.cpp) to allow the temperature monitor to be quickly rebuilt. 

## Drop Test and Cool box protection.

With smile being deployed to remote, rugged locations, we wanted to understand any weaknesses in the design of our initial prototype. Formed mainly of 3D prints filled with foam, we expected the exterior to be susceptible to cracks. To test this, we found a hard concrete cloor and dropped the cooler from a measured height of 1m. See the results of the initial drop below:

We were impressed with the results of this test, with the damage being localised to one panel and the coolbox still working as intended. We believe having the prints being rivited together limits crack propagation, as well as the foam interior absorbing most of the impact. To better understand the performance, we increased the height we dropped from, dropping from 1m, 2m and 3m on both grass and concrete. The final state of the coolbox can be seen:

Overall, we were very impressed with how the coolbox performed. At the end of this "destruction" testing, the coolbox still operated as intended, with all features working and the foam interior in tact. There was significant aesthatic damage to the 3D prints, something we wanted to mitiage with our next prototype. With most of the damage beign concentrated on the corners, I designed up some TPU bumpers (TPU is a flexible plastic that can be 3D pritned) that would rivet from the inside and be secured to each corner. See the CAD preview below:


Initially, with an infill of 15%, these parts were stiff and did not seem appropriate. Reducing the infill to 5% and using a honeycomb infill pattern rsulted in significantly more compliant bumpers that easily deform when the coolbox is dropped onto a cooler. These parts have not been extensively tested, and weigh a significant amount. Further field testing should be performed to further optimise the design of these bumpers and check their performance. 

Another possibility from the results of the test and observations during assembly, is to change the material of the exterior walls of the cool box to be constructed from TPU. We didnt have time to do this during this prototyping phase, due to PLA being easier to print. However, In assembly the PLA parts would often crack when being riveted, and this was especially true with our most recent prototype where we significantly reduced the wall thickness. As most of the structure of the product comes from the expanding foam and the centre carousel parts (which should be kept as a stiff material), the exterior walls really only serve as a means to apply expanding foam to the interior for insulation. 

Switching to TPU for these exterior shells is a promising route - the foam could still be accurately applied, but the assembly would be significantly more compliant with reduced risk of cracking during assembly, as well as improved resilience to impacts and no need for the TPU bumpers we have designed (and thus saving a lot of weight). I believe this is an interesting avenue that should be explored with anyone continuing this project, with the biggest difficulty in using such a material is achieving consistent printing performance. 
