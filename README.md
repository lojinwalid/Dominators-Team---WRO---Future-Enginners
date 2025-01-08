# WRO FUTURE ENGINEERS Dominators Team
This documentation previews our project in WRO FUTURE ENGINEERS our team consists of 3 members:
* Rodina Ahmed - responsible for Mechanical  design -
* Lojin walid - responsible for electrical system design -
* Yassin Mohamed Abdelhamid - responsible for Software system -
  
<b> Our coach : Omar Khaled El-Sayed </b>

## Vehicle’s Electromechanical Components

* Openmv H7: for detecting blocks and their color
  <p align="center">
  
<img src="https://github.com/lojinwalid/Dominators-Team---WRO---Future-Enginners/assets/141444821/e29d6f8d-df7b-4d4f-9931-5a66845fbe4a" width="200"> 
</p>

* Arduino Nano: for communicating with the camera and giving signals to the motor driver accordingly

  
<img src="https://github.com/lojinwalid/Dominators-Team---WRO---Future-Enginners/assets/141444821/bd7bc5f2-0eef-4d78-bda0-f4d41e5e175c" width="200"> 


*A DC Motor with Gear Box JGA25-370-12V-250RPM 8.8Kg.cm

<img src="https://github.com/lojinwalid/Dominators-Team---WRO---Future-Enginners/assets/102741393/e1ea36af-f705-4714-b7a9-7fc6d847756c" width="200"> 


</p>

*L298 motor driver: to drive the DC motor

<img src="https://github.com/lojinwalid/Dominators-Team---WRO---Future-Enginners/assets/141444821/f2024799-376b-4e8a-83b7-62600243081e" width="200"> 



*Servo motor : to control the angle of steering 

<img src="https://github.com/lojinwalid/Dominators-Team---WRO---Future-Enginners/assets/141444821/3b6664e2-9cb1-49a6-aa03-4dcb656a0642" width="200"> 


*Buck converter DC to DC : 12 volts input to get 6 volts output for servo motor

<img src="https://github.com/lojinwalid/Dominators-Team---WRO---Future-Enginners/assets/141444821/e137dce7-e05c-4c1f-979f-5b75382d2b44" width="200"> 


*12V 3S-2P 3600mAh Rechargeable 18650 Li-ion Battery Pack with battery management system (BMS) 

<img src="https://github.com/lojinwalid/Dominators-Team---WRO---Future-Enginners/assets/102741393/d489b517-8898-4295-8f5f-665a395b457f" width="200"> 

## links 
* Buck converter: https://makerselectronics.com/product/lm2596s-dc-dc-converter-3a-step-down
* Servo motor: https://makerselectronics.com/product/micro-servo-sg90-0180-degree
* Openmv H7:  https://openmv.io/products/openmv-cam-h7
* Arduino nano: https://makerselectronics.com/product/arduino-nano-with-usb-type-c

## Electrical schematic of our robot

![Screenshot 2023-08-04 233702](https://github.com/lojinwalid/Dominators-Team---WRO---Future-Enginners/assets/141444821/b910dcf0-357d-4ce3-b3f0-d050e43fe766)

## code
* Code is divided into steps:
     * blocks
     * Lines
     * Walls
Ordered according to priority from top to bottom

### Blocks:

We used a simple searching algorithm where the camera searches in a specified ROI (region of interest) which detects the red and green blocks and orders the servo motor to rotate depending on the block's color

### Lines :

In the lines, it was a little different from the blocks. We made a function on the first color the robot detects whether it's orange or blue, and the robot turns and cancels the second line. If the first line the robot sees is orange it turns right and when it sees blue it turns left

### Walls:

the walls it was pretty simple as the camera sees the walls on both sides with no problem in their color values as they have high contrast black color. the robot finds the two walls and calculates their area and then finds the biggest area then goes to the opposite side according to the closer wall then makes the decision to go left or right or forward 

  

## Left Side of robot

<img src="https://github.com/lojinwalid/Dominators-Team---WRO---Future-Enginners/assets/141444821/46688d15-5be3-47cb-9f35-35996fe2f02f" width="500"> 


## Right side of robot

<img src="https://github.com/lojinwalid/Dominators-Team---WRO---Future-Enginners/assets/141444821/6e53a4e9-7d5e-4d15-9a47-ba5de19ed0d3" width="500"> 


##  Top view of robot

<img src="https://github.com/lojinwalid/Dominators-Team---WRO---Future-Enginners/assets/141444821/084e8022-f2a4-48d3-bbb6-ab1733a10a0a" width="350"> 


##  Bottom view of robot

<img src="https://github.com/lojinwalid/Dominators-Team---WRO---Future-Enginners/assets/141444821/43fe51b3-be49-419b-af9a-b4aa75429e01" width="350"> 


## bottom view on SOLIDWORKS

<img src="https://github.com/lojinwalid/Dominators-Team---WRO---Future-Enginners/assets/141444821/98fe4d7c-1c39-4170-b241-4eee49522783" width="350"> 


## Isometric view on SOLIDWORKS

<img src="https://github.com/lojinwalid/Dominators-Team---WRO---Future-Enginners/assets/141444821/56ebcb6f-d8a5-4488-b915-9b3748e37b8a" width="500"> 

<img src="https://github.com/lojinwalid/Dominators-Team---WRO---Future-Enginners/assets/141444821/c3a3dcd8-f346-4d83-98bd-d5d33f4cd4aa" width="500"> 

<img src="https://github.com/lojinwalid/Dominators-Team---WRO---Future-Enginners/assets/141444821/05d7be9a-d718-4ffa-80e6-8dd8849f5314" width="500"> 

