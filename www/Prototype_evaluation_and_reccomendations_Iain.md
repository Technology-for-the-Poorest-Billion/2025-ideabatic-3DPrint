# Prototype evaluation

Both prototypes are based off the same overall concept outlined in [Design review and initial concept](). Although the second prototype is iterated off the first prototype and it is built off the lessons from the first prototype to explore more of the design space, each prototype has their own strengths and weaknesses. 


# Prototype 1
This first prototype was largely successful in being a proof of concept and demonstrated the feasibility of 3d printing the SMILE icebox.

![image]() 

## Good aspects:

### Overall concept:
The overall concept of filling a thin 3D print with expanding foam is very effective, quick to implement and does add a lot of stiffness and strength to the part. We were able to produce a near working icebox in around a week based on this concept. 
![image](https://github.com/Technology-for-the-Poorest-Billion/2025-ideabatic-3DPrint/blob/main/Images/Filling%20V1%20with%20expanding%20foam.jpeg) 

### Rivet joining method:
Rivets do an excellent job of pulling the part together and holding it together, even if the part is slightly misshapen. 

In addition the rivets are very easy to inspect, very quick to install and can be used in conjuction with other bonding methods like gluing.

### Reinforcing plate:
The reinforcement plate which is riveted on between the outer shell and the inner cylinderical part of the icebox shell does an excellent job of stiffening the part as well as ensuring the part remains the correct shape. Having this part as a seperate piece helps overcome issues with overhangs, while the laser cut manufacturing method allows this plate to span over multiple 3d printed parts ensuring they are all aligned accurately. 

![image](https://github.com/Technology-for-the-Poorest-Billion/2025-ideabatic-3DPrint/blob/main/Images/V1%20reinforcing%20plate.png) 


![image](https://github.com/Technology-for-the-Poorest-Billion/2025-ideabatic-3DPrint/blob/main/Images/Prototype%20V1%20reinforcing%20plate.png) 

### Carousel design:
The carousel design works very well with the two halves threaded on to each other. It spins freely within the part but can be disassembled easily while providing somewhat of a seal.

### Vaccine door design:
The vaccine door works moderately well as a proof of concept, does not close properly though, perhaps magnets can be used to force the door shut, otherwise too much spring preload is needed on the hinge. 

![image](https://github.com/Technology-for-the-Poorest-Billion/2025-ideabatic-3DPrint/blob/main/Images/V1%20vaccine%20door.png)

## Areas of improvement:

### Part splitting strategy:
The way the part is simply split into 4 is bad. Although joining the outside shell is not a problem, it is very difficult to seal the centre carousel section especially in the conical areas, and this results in both possible leaks and is quite a bad bearing surface for the carousel. 


![image](https://github.com/Technology-for-the-Poorest-Billion/2025-ideabatic-3DPrint/blob/main/Images/V1%20Icebox%20center%20seams.png)

In addition the way that the lap joints are designed on the bottom of the part means that an overhang is needed to manufacture them. This results in an inaccurate surface so the part does not fit together properly

### Part rigidity:
The 3d prints are too rigid, this may sound like a good thing, but it means if the part warps while printing it cannot be forced back into place into the right shape. This warping is something which is quite common, as the parts are thin shells which have limited rigidity while printing and tend to move around or deform.

![image](https://github.com/Technology-for-the-Poorest-Billion/2025-ideabatic-3DPrint/blob/main/Images/V1%20Flange%20rigidity%20misalignment.png)

we can see how the upper shell doesn't quite fit together properly, and this is a result of one of its constituent parts warping during printing, and the high rigidity of the part results in the part cracking when being riveted rather than deforming into shape.

This is an additional problem for if the part gets dropped as the high rigidity prevents the inside expanding foam from absorbing any energy.


### Sharp corners on the shell:
The chamfers included in the shell design although necessary for printability result in sharp corners which have multiple drawbacks
* They again make the corners uncessarily rigid, this makes the part difficult to assemble
* This rigidity also reduces the strength of the part, as it prevents the foam from absorbing energy when dropped as well as acts as a stress concentrator
* When 3D printing, the printer tends to overshoot when faced with sharp changes, it is unable to produce the perfect zero radius corner specified in cad, resulting in it being difficult to assemble the part together near the corners.


![image](https://github.com/Technology-for-the-Poorest-Billion/2025-ideabatic-3DPrint/blob/main/Images/V1%20Flange%20rigidity%20misalignment.png)

The cracking here is due to the part being misshapen and having to be forced together by the corners. The corner acts as a stress concentrator which propagates this crack. 

![image](https://github.com/Technology-for-the-Poorest-Billion/2025-ideabatic-3DPrint/blob/main/www/V1%20drop%20test%20corner%20cracking.png)

It can also be seen here how the corners are extra vulnerable when dropped, with the crack propagating along the line of the corner where the stress is highest. 

### Rivet reinforcement plates
The rivet reinforcement plates shown in the CAD file below in purple.

![image](https://github.com/Technology-for-the-Poorest-Billion/2025-ideabatic-3DPrint/blob/main/www/V1%20rivet%20reinforcement%20plate.png)

* These plates did work effectively to prevent the 3D print from cracking as the rivets clinched down.
* However they were laser cut out of plywood which was a poor material choice, as virtually every plate cracked along the plywood grains. MDF or any isentropic material would work better.
* They were also somewhat of a hassle to install should test if it is possible to go without them. 

### Bolt attachment
Only 5 bolts attach between the shells this results in a weaker attachment between the two halves. A method needs to be found to rectify this.



