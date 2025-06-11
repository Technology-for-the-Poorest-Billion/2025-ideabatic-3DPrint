# Prototype V1 CAD + Design
This page outlines the developement of the first prototype icebox, the design decisions made and how the CAD is developed if further work is to be done.

Onshape is used as the CAD software of choice mainly due to the fact that is it free, making it widely accessible even in the developing world. 

The aim of this prototype is to explore possible issues with the overall concept of a multi segment 3d printed shell filled with expanding foam. Precise features such as gaskets are not included. 


# Constraints and overall concept
The icebox is based off the overall concept of 


Things to be aware off is how foam is trimmed off

How everything needs to be at at least a 30 degree angle to prevent overhang


# CAD

## Step 1 Manufacturing carousel
The first step in the cad is producing the carousel that houses the vaccines. The dimensions of this is enforced by the size of our icepack, and we are trying to keep the slots where the vaccines sit the same as the existing model.

This is made with a revolve pattern with care made to include chamfers to avoid the need for supports

[INSERT IMAGE]

Unfortunately due to our 175x175x175 part size limit, we are unable to manufacture the carousel in one piece. This means a separate cap is needed. 

[INSERT IMAGE]

This cap is designed to be filled with foam, trimmed flush and then threaded onto the carousel body. It is also designed to provide somehwat of a seal with the icebox with the two conical features.

The idea with the thread is that the spacing between the conical features can be adjusted to provide the best seal without restricting rotation.

[INSERT IMAGE]

Finally bolt features are produced in the cap so to prevent the cap from rotating once threaded in

## Shell features
The general shape of the main shell is then produced as a revolve and the same hexagonal shape is used as in the existing SMILE icebox. 

Note that instead of fillets, chamfers are used, this is to enable printability, as fillets will result in steep overhangs which are difficult to print. The thickness of this shell is enforced by the insulation thickness which was chosen to be 34mm after modelling by Hussain. 

[INSERT IMAGE]

Additional features are then added to this solid shell body, first including the icepack door. This part is hollow to be filled with foam, with a small hole at the top to allow for this. It seals against the main shell using taper feature with attention paid for printability