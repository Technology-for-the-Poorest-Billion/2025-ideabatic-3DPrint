# Prototype V1 CAD + Design
This page outlines the developement of the first prototype icebox, the design decisions made and a guide to how the CAD for the icebox is developed to help future work. 

Onshape is used as the CAD software of choice mainly due to the fact that is it free, making it widely accessible even in the developing world. 

The aim of this prototype is to explore possible issues with the overall concept of a multi segment 3d printed shell filled with expanding foam. Precise features such as gaskets are not included. 


# Constraints and overall concept
The design is based on an overall concept of a thin 3D print filled with expanding foam. It will have the same features as the existing smile icebox, with a carousel, an outer shell that splits in half, and door to access both the ice pack and vaccines stored in the carousel.

Unlike the existing smile icebox, the shell splits asymmetrically with a main shell and a cap which is bolted ontop via the corners. 


### 3D printing constraints:
The fact we are 3D printing comes with a few constraints, the following are taken into account during the design process.
* Setting a part size cap of 175x175x175mm, this is the print size of a Bambu A1 mini
* Avoiding the use of supports, can print overhangs up to 60 degrees with a degree of quality, up to 75 degrees will not fail. 
* 3D prints are anisotropic, much weaker along layer lines




# CAD
![image](https://github.com/Technology-for-the-Poorest-Billion/2025-ideabatic-3DPrint/blob/main/Images/Prototype%20V1%20CAD.png)

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

Additional features are then added to this solid shell body, first including the icepack door. This part is hollow to be filled with foam, with a small hole at the top to allow for this. It seals against the main shell using taper feature with attention paid for printability. A high pitch multi start thread is used so the door can screw on easily, as well as a thread tolerance. 


![image](INSERT)

The cutout for the door to make the vaccines is made, with the geometery designed as such so the door separates cleanly from the body. The door in indented into the body to avoid danamge, and the tapered entry to to help with both sealing and printability. This is mainly created using a boolean feature, to cut out the correct size opening, shelled to allow the door to be filled with expanding foam.

![image](https://github.com/Technology-for-the-Poorest-Billion/2025-ideabatic-3DPrint/blob/main/Images/Prototype%20V1%20door%20cutout.png)

The door here is meant purely as a test, the next prototype will explore how to properly design this door so it seals well with the body. 

![image](https://github.com/Technology-for-the-Poorest-Billion/2025-ideabatic-3DPrint/blob/main/Images/Prototype%20V1%20Vaccine%20door.png)

A slot is added to help open the door

![image](https://github.com/Technology-for-the-Poorest-Billion/2025-ideabatic-3DPrint/blob/main/Images/Prototype%20V1%20door%20opening%20slot.png)

## Step 3 Splitting shell
Currently in the cad, the shell is a solid body. Our design concept just like the current smile design will consist of two thin 3d printed shells which can be taken apart and are filled with foam. 

As such this step focuses on making the features that enable this, with the same focus on printability (so avoiding overhangs that are hard to print and take very time intensive supports), rigidity and ensuring the two halves can locate and join together.

### Splitting and shelling

![image](https://github.com/Technology-for-the-Poorest-Billion/2025-ideabatic-3DPrint/blob/main/Images/Prototype%20V1%20shelling%20.png)

Firstly 5 bolt holes are featured into the shell to enable the two halves to be jointed together. The bolts are positioned at the corners, as here the 3d print is locally very stiff, and it also avoids comprimising the insulation thickness of the icebox. Unfortunately as one corners is used as the hinge for the vaccine door, only 5 bolts can be used. The model is then shelled to a **thickness of 1.5mm**.

### Flange and joining shell halves
One pertinant question is how we want to two halves to connect together. We need a reliable locating feature to allow both shell halves to connect and bolt together. 

In the previous prototype shown in the [design review](https://github.com/Technology-for-the-Poorest-Billion/2025-ideabatic-3DPrint/blob/main/Design%20review%20-%20Iain.md) many small locating lips were used on the outside shell as well as a foam prutrusion 

![image](https://github.com/Technology-for-the-Poorest-Billion/2025-ideabatic-3DPrint/blob/main/Images/Original%20smile%20shell%20interface.png)


Due to how we are filing the 3d prints with expanding foam (which is already quite soft), and then trimming the top surface, it is not feasible to include the same foam features. In addition the thin locating lips was found to be difficult to use as well as fragile on the existing part. As such a new locating method is needed.

![image](https://github.com/Technology-for-the-Poorest-Billion/2025-ideabatic-3DPrint/blob/main/Images/Prototype%20V1%20upper%20shell%20flange.png)

For this prototype we have settled on making a flange on the upper lid, which then bolts onto the bottom lid. There are holes in this flange so a reinforcing plate can be riveted on. This both helps to reinforce the structure ensuring the central round section and the outer hexagonal section are stiffly connected, but also helps to ensure the mating surfaces between the two shells are the right shape.

This flange is chamferred on the bottom side so no support is needed.

![image](https://github.com/Technology-for-the-Poorest-Billion/2025-ideabatic-3DPrint/blob/main/Images/Prototype%20V1%20lower%20shell%20flange.png)

The same flange can be seen on the bottom lid, without the offset as it does not have the same reinforcing plate. There are indentations to allow for the rivets between the reinforcing plate and upper shell.

![image](https://github.com/Technology-for-the-Poorest-Billion/2025-ideabatic-3DPrint/blob/main/Images/Prototype%20V1%20reinforcing%20plate.png)

The reinforcing plate can be seen above, in our prototype it is laser cut out of 3 mm MDF and it is mainly designed to stiffen the structure. There are holes to rivet this plate onto the upper shell as seen, as well as additional holes designed to accept locating pins from the lower shell. The sketch for these locating pin holes can be seen.

![image](https://github.com/Technology-for-the-Poorest-Billion/2025-ideabatic-3DPrint/blob/main/Images/Prototype%20V1%20Locating%20pins.png)

And the locating pins on the lower shell

![image](https://github.com/Technology-for-the-Poorest-Billion/2025-ideabatic-3DPrint/blob/main/Images/Prototype%20V1%20thread%20pockets.png)

Finally the last features on the lower shell are pockets to accept thread inserts so we can bolt the upper shell and lower shell together. Note that the thread inserts stick up, this is to located into the reinforcing plate, there are also a few chamfer features and this is to ensure printability by avoiding overhangs. 

## Step 4: Splitting shell halves
Unlike the previous smile design, where each shell half could be made in one piece, the size limitation of 3d printers means that each half needs to be split into 4 to fit our size constraint of 175x175x175mm.

Here we are using the lap joint and rivet strategy decided on in [joining 3d prints](https://github.com/Technology-for-the-Poorest-Billion/2025-ideabatic-3DPrint/blob/main/Joining%203D%20prints%20-%20Iain.md).

![image](INSERT IMAGE)

Firstly by the center round section flanges are added by the split planes to help locate and seal these center sections. The part is then split into 4. The locations of the splits are designed to be on the flat faces of the hexagon, as this makes the lap joint more simple to design, as well as trying to maintain features like the vaccine door in once piece. 

### Lower shell lap joints
![image](INSERT IMAGE)

The laps for the lower shell are then created by offsetting the shell features and then extruding it in the direction of the shell face. This is then mirrored across.

![image](INSERT IMAGE)

Holes are then made for the rivets in the lap joints, 4 holes on each side, with another hole at the bottom.

![image](INSERT IMAGE)
A similar process is done for the inner lap joint, where the shell is offset and then revolved to form an overlap which we can rivet through to connect the four sections. Note that we cannot rivet the conical sections as this is a bearing surface for the carousel, so any rivets would disturb rotation

### Upper shell lap joints

![image](INSERT IMAGE)

The exact same process is used to make the lap joints for the upper shell so the four constitutent componenents can be combined together. The only differnece is that the central round feature is held together using the reinforcing plate

## Step 5: Rivet backing platees
The final step is extruding out the rivet backing plates which will be laser cut from MDF. The point of these plates is to spread the load as the rivet clinches down on the part preventing cracking. This is particularly an issue due to the anistropy of 3d prints, as they will tend to crack along their layer lines. 

![image](INSERT IMAGE)


