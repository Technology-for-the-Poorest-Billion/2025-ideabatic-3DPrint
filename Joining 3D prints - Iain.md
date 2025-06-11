# Prototype V1 CAD + Design
This page outlines the developement of the first prototype icebox, the design decisions made and a guide to how the CAD for the icebox is developed to help future work. 

Onshape is used as the CAD software of choice mainly due to the fact that is it free, making it widely accessible even in the developing world. 

The aim of this prototype is to explore possible issues with the overall concept of a multi segment 3d printed shell filled with expanding foam. Precise features such as gaskets are not included. 


# Constraints and overall concept
The icebox is based off the overall concept of 


Things to be aware off is how foam is trimmed off

How everything needs to be at at least a 30 degree angle to prevent overhang


# CAD

The full can be seen above, this outlines all the steps in onshape to make the model.
## Step 1 Manufacturing carousel
The first step in the cad is producing the carousel that houses the vaccines. The dimensions of this is enforced by the size of our icepack, and we are trying to keep the slots where the vaccines sit the same as the existing model.

This is made with a revolve pattern with care made to include chamfers to avoid the need for supports

![image](https://github.com/Technology-for-the-Poorest-Billion/2025-ideabatic-3DPrint/blob/main/Images/Prototype%20V1%20Carousel.png)

Unfortunately due to our 175x175x175 part size limit, we are unable to manufacture the carousel in one piece. This means a separate cap is needed. 


![image](https://github.com/Technology-for-the-Poorest-Billion/2025-ideabatic-3DPrint/blob/main/Images/Prototype%20V1%20carousel%20cap.png)

This cap is designed to be filled with foam, trimmed flush and then threaded onto the carousel body. It is also designed to provide somehwat of a seal with the icebox with the two conical features.

The idea with the thread is that the spacing between the conical features can be adjusted to provide the best seal without restricting rotation.

![image](https://github.com/Technology-for-the-Poorest-Billion/2025-ideabatic-3DPrint/blob/main/Images/Prototype%20V1%20Carousel%20bolts.png)

Finally bolt features are produced in the cap so to prevent the cap from rotating once threaded in

## Step 2 Shell features
The general shape of the main shell is then produced as a revolve and the same hexagonal shape is used as in the existing SMILE icebox. 

Note that instead of fillets, chamfers are used, this is to enable printability, as fillets will result in steep overhangs which are difficult to print. The thickness of this shell is enforced by the insulation thickness which was chosen to be 34mm after modelling by Hussain. The Icebox is asymmetric to enable more insulation by the vaccine door. 


![image](https://github.com/Technology-for-the-Poorest-Billion/2025-ideabatic-3DPrint/blob/main/Images/Prototype%20V1%20carousel%20main%20shape.png)

Additional features are then added to this solid shell body, first including the icepack door. This part is hollow to be filled with foam, with a small hole at the top to allow for this. It seals against the main shell using taper feature with attention paid for printability


[Image]

The cutout for the door to make the vaccines is made, with the geometery designed as such so the door separates cleanly from the body. The door in indented into the body to avoid danamge, and the tapered entry to to help with both sealing and printability. This is mainly created using a boolean feature, to cut out the correct size opening, shelled to allow the door to be filled with expanding foam.

The door here is meant purely as a test, the next prototype will explore how to properly design this door so it seals well with the body. 

[Image]

A slot is added to help open the door

## Step 3 Splitting shell
Currently in the cad, the shell is a solid body. Our design concept just like the current smile design will consist of two thin 3d printed shells which can be taken apart and are filled with foam. 

As such this step focuses on making the features that enable this, with the same focus on printability (so avoiding overhangs that are hard to print and take very time intensive supports), rigidity and ensuring the two halves can locate and join together.

### Splitting and shelling

[Image]

Firstly 5 bolt holes are featured into the shell to enable the two halves to be jointed together. The bolts are positioned at the corners, as here the 3d print is locally very stiff, and it also avoids comprimising the insulation thickness of the icebox. Unfortunately as one corners is used as the hinge for the vaccine door, only 5 bolts can be used. 

### Flange and joining shell halves
One pertinant question is how we want to two halves to connect together. We need a reliable locating feature to allow both shell halves to connect and bolt together. 

In the previous prototype shown in the [design review](https://github.com/Technology-for-the-Poorest-Billion/2025-ideabatic-3DPrint/blob/main/Design%20review%20-%20Iain.md) many small locating lips were used on the outside shell as well as a foam prutrusion 

[Image]


Due to how we are filing the 3d prints with expanding foam (which is already quite soft), and then trimming the top surface, it is not feasible to include the same foam features. In addition the thin locating lips was found to be difficult to use as well as fragile on the existing part. As such a new locating method is needed.

[Image]

For this prototype we have settled on making a flange on the upper lid, which then bolts onto the bottom lid. There are holes in this flange so a reinforcing plate can be riveted on. This both helps to reinforce the structure ensuring the central round section and the outer hexagonal section are stiffly connected, but also helps to ensure the mating surfaces between the two shells are the right shape.

This flange is chamferred on the bottom side so no support is needed.

[Image]

The same flange can be seen on the bottom lid, without the offset as it does not have the same reinforcing plate. There are indentations to allow for the rivets between the reinforcing plate and upper shell.

[Image]

The reinforcing plate can be seen above, in our prototype it is laser cut out of 3 mm MDF and it is mainly designed to stiffen the structure. There are holes to rivet this plate onto the upper shell as seen, as well as additional holes designed to accept locating pins from the lower shell. The sketch for these locating pin holes can be seen.

[Image]

And the locating pins on the lower shell

[Image]

Finally the last features on the lower shell are pockets to accept thread inserts so we can bolt the upper shell and lower shell together. Note that the thread inserts stick up, this is to located into the reinforcing plate, there are also a few chamfer features and this is to ensure printability by avoiding overhangs. 

