# WRO FUTURE ENGINNERS Dominators Team
This documentation previews our project in WRO FUTURE ENIGNNERS our team consists of 3 members:
* Rodina Ahmed - responsible for Mechanical  design -
* Lojin walid - responsible for electrical system design -
* Yassin Mohamed Abdelhamid - responsible Software system -
  
<b> Our coach : Omar Khaled El-Sayed </b>

## Vehicle’s Electromechanical Components

* Openmv H7: for detecting blocks and their colour
  <p align="center">
 ![R](https://github.com/lojinwalid/Dominators-Team---WRO---Future-Enginners/assets/141444821/e29d6f8d-df7b-4d4f-9931-5a66845fbe4a) 
</p>
* Arduino Nano: for communicating with camera and giving signals to the motor driver accordingly

<p align="center">
  
![OIP](https://github.com/lojinwalid/Dominators-Team---WRO---Future-Enginners/assets/141444821/bd7bc5f2-0eef-4d78-bda0-f4d41e5e175c)
</p>
*A DC Motor with Gear Box JGA25-370-12V-250RPM 8.8Kg.cm
<p align="center">
![OIP](https://github.com/lojinwalid/Dominators-Team---WRO---Future-Enginners/assets/102741393/e1ea36af-f705-4714-b7a9-7fc6d847756c)
</p>
*L298 motor driver: to drive the DC motor

<p align="center">
  
![OIP](https://github.com/lojinwalid/Dominators-Team---WRO---Future-Enginners/assets/141444821/f2024799-376b-4e8a-83b7-62600243081e)

</p>

*Servo motor : to control the angle of steering 
<p align="center">
  
![Servo-Motor](https://github.com/lojinwalid/Dominators-Team---WRO---Future-Enginners/assets/141444821/3b6664e2-9cb1-49a6-aa03-4dcb656a0642)

</p>

*Buck converter DC to DC : 12 volts input to get 6 volts output for servo motor
<p align="center">
  
![OIP](https://github.com/lojinwalid/Dominators-Team---WRO---Future-Enginners/assets/141444821/e137dce7-e05c-4c1f-979f-5b75382d2b44)

</p>
</p>
*12V 3S-2P 3600mAh Rechargeable 18650 Li-ion Battery Pack with battery management system (BMS) 
![OIP](https://github.com/lojinwalid/Dominators-Team---WRO---Future-Enginners/assets/102741393/d489b517-8898-4295-8f5f-665a395b457f)

</p>


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

We used a simple searching algorithm where camera search in a specified ROI (region of interest) which detects the red and green blocks and orders the srvo motor to rotate depending on the block's colour

### Lines :

In the lines, it was a little different from the blocks. We made a function on the first colour the robots detects whether it's orange or blue the robot turns and cancel the second line. If the first line the robot sees is orange it turns right and when seeing blue it turns left

### Walls:

the walls it was pretty simple as the camera sees the walls on both sides with no problem in their colour values as they have high contrast black colour. the robot finds the two walls and calculates their area and then finds the biggest area  then go to the opposite side according to the closer wall then make the decision to go left or right or forward 

  

## Left Side of robot


![WhatsApp Image 2023-07-31 at 11 43 14 PM](https://github.com/lojinwalid/Dominators-Team---WRO---Future-Enginners/assets/141444821/46688d15-5be3-47cb-9f35-35996fe2f02f)


## Right side of robot


![WhatsApp Image 2023-07-31 at 11 43 15 PM](https://github.com/lojinwalid/Dominators-Team---WRO---Future-Enginners/assets/141444821/6e53a4e9-7d5e-4d15-9a47-ba5de19ed0d3)


##  Top view of robot


![WhatsApp Image 2023-08-01 at 2 38 37 PM](https://github.com/lojinwalid/Dominators-Team---WRO---Future-Enginners/assets/141444821/084e8022-f2a4-48d3-bbb6-ab1733a10a0a)


##  Bottom view of robot

![WhatsApp Image 2023-08-01 at 2 39 46 PM](https://github.com/lojinwalid/Dominators-Team---WRO---Future-Enginners/assets/141444821/43fe51b3-be49-419b-af9a-b4aa75429e01)


## bottom view on SOLIDWORKS

![543](https://github.com/lojinwalid/Dominators-Team---WRO---Future-Enginners/assets/141444821/98fe4d7c-1c39-4170-b241-4eee49522783)


## Isometric view on SOLIDWORKS

![123](https://github.com/lojinwalid/Dominators-Team---WRO---Future-Enginners/assets/141444821/56ebcb6f-d8a5-4488-b915-9b3748e37b8a)

![Capture](https://github.com/lojinwalid/Dominators-Team---WRO---Future-Enginners/assets/141444821/c3a3dcd8-f346-4d83-98bd-d5d33f4cd4aa)

![713](https://github.com/lojinwalid/Dominators-Team---WRO---Future-Enginners/assets/141444821/05d7be9a-d718-4ffa-80e6-8dd8849f5314)

