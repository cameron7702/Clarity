

Shashank Ojha, Andreas Joannou, Abdellah Ghassel, Cameron Smith  

# <img src = "https://drive.google.com/uc?export=view&id=1uSO3lyjBBNwF7WbjJNcRnYrchpkJCQGR" width="220" height="80">   
  
 <p align="center">  
<img src = "https://drive.google.com/uc?export=view&id=1griTlDOUhpmhqq7CLNtwrQnRGaBXGn72" width="170" height="160">   
 </p>

Clarity is an interactive smart glass that uses an Artificial Intelligence emotion detection system, to notify the user of the emotion that the users in front of them are feeling. This wearable gadget is also having regular smart glass abilities like; seeing the time, sending reminders, open schedules, and see the weather, to insure that all users get the best experience. 


## Problem:
As mental health continues make it a challenge for individuals to be integrated into the community, it is important that up and coming technologies also work to accommodate everyone. Specifically, studies have found the individuals with developmental disorders such as Autism and Asperger’s have trouble recognizing emotions, and fitting in. For this reason, we would like to introduce Clarity. Clarity is a smart glass allows for the user to detect the emotion that the individuals in their proximity are feeling, while still having the unique and powerful features of smart glasses including weather and showing daily routines and schedules. With more funding and development, the glasses can have so many more features to take accessibility away from your fingertips and into your eyes. 

<p align="center">  
<img src = "https://drive.google.com/uc?export=view&id=1eVZFYgQIm7vu5UOjp5tvgFOxvf3kv4Oj" width="300" height="300">   
<img src = "https://drive.google.com/uc?export=view&id=1L-5w9jzwKG0dLdwe-OCMUa6S2HnZeaFo" width="300" height="300">
<img src = "https://drive.google.com/uc?export=view&id=1LP7bI9jAupQDQcfbQIszs9igVEFSuqDb" width="300" height="300">
 
 </p>

## Misson Statment: 
We at clarity are determined to make everyone’s lives easier, specifically to help even the playing field for individuals with developmental disorders in recognizing how the society around them is interacting with one another.  


<p align="center">  
<img src = "https://drive.google.com/uc?export=view&id=1qJgJIAwDI0jxhs1Q59WyaGAvFg5fysTt" width="300" height="300"> 
<img src = "https://drive.google.com/uc?export=view&id=1AY5zbgfUB4c_4feWVVrQcuOGtn_yGc99" width="400" height="300"> 
 </p>

We are first time Makaton participants are determined to learn what it takes and make this project come in order to life and make an impact in as many lives as possible.  Throughout this Makathon, we have challenged our selves to deliver a well polished quality product that, we feel when brought to the market can really impact people’s lives. We are second year students from Queen's University who are very passionate about designing of innovative solutions to better the lives of everyone. We all have the mindset to give any task our all and obtain the best results. We have a diverse skillset in the team and throughout the hackathon we utlized it to work efficienty. We are first time Mackathoners, so even though we all had respective expierence in our own fields, this whole expierence was very new and educationally rewarding for us. 

## About: 

### Market Scope: 
<p align="center">
<img src = "https://drive.google.com/uc?export=view&id=10LWCDhgfDPp1scpVI1GSAGIWrjprQtOY" width="400" height="400"> 
  </p>
As the main point of this device is to help individuals with mental health disorders. However, the application on this device is limitless. Other integral market audiences to our device include:


  •	Educational Institutions can use clarity to help train children to learn about emotions and feelings at a young age. By being exposed to such a powerful technology to learn, students can be taught to share, and care by really being able to look at it from another person’s lenses. 
  
  •	Social Workers Interview Process can use our device to create a more dynamic and through process when it comes to determining the ideal person for a task. It can also be used by social workers and emotional intelligence researchers to have better studies and results. 
  
  •	With further development, this device can be used as a quick tool for     psychiatrists to analyse and understand their patients to a deeper level. By accessing individuals that need help at a faster level, more lives and be saved and improved.  
  
### Whats in it for you:
<p align="center">
<img src = "https://drive.google.com/uc?export=view&id=1XbrcnIEc3eAYDmkopmwGbSew11GQv91v" width="500" height="400"> 
  </p>
 
The first stakeholder to benefit from Clarity is users. This product provides accessibility right to the eye of almost 75 million users: approx. number of individuals in the world with developmental disorders.  The emotion detection system, that the user’s disposable will make it easy to recognize the emotion that anyone, is feeling. Whether ones watching a Netflix show, or having a live casual conversation, Clarity has got you covered. 

Next, Qualcomm could have a significant partnership in the forthcoming of Clarity, as they would be an excellent distributor and partner. With professional machining and the Qualcomm Snapdragon Processor technology, the AI model is guaranteed to have high performance in a small package. 

Due to the various applications mentioned of this product, this product has exponential growth potential in the educational, research, and counselling industry, thus being able to offer significant potential in profit/possibilities for investors and researchers. 

## Technological Specifications

## Hardware:
At first, the body of the device was a simple prism with an angled triangle to reflect the light 90 degrees from the user. The initial intention was to glue the glass reflector to the outer edge of the triangle to complete the 180-degree reflection. This plan was then scrapped in favour of a more robust mounting system, including a frontal clip for the reflector and a modular cage for the LCD screen. After feeling confident in the primary design, a prototype was 3D printed. During the construction of the initial prototype, a number of challenges surfaced including dealing with printer errors, component measurement, and manufacturing mistakes. One problem with the first prototype was lack of adhesion to the printing bed. This resulted in raised corners which negatively affected component cooperation. The issue was overcome by introducing a ring of material around the main body. Component measurement and manufacturing mistakes further led to improper fitting between pieces. This was ultimately solved by simplifying the initial design, which had fewer points of failure. The evolution of the CAD files can be seen below.
 
<p align="center">
<img src = "https://drive.google.com/uc?export=view&id=1vDT1gGyfM7FgioSRr71yBSysGntOfiFC" width="400" height="400"> 
  </p>
  
The material chosen for the prototypes was PLA plastic for its strength to weight ratio, and its price. This material is very lightweight and strong, allowing for a more comfortable experience for the user. Furthermore, the inexpensive plastic allows for inexpensive manufacturing.

Clarity runs on a Raspberry Pi Model 4b. The RPi communicates with the OLED screen using the I2C protocol. It additionally powers and communicates with the camera module and outputs a signal to a button to control the glasses. The RPi handles all the image processing, to prepare the image for emotion recognition and creating images to be output to the OLED screen.


### Optics: 
Clarity uses two reflections to project the image from the screen to the eye of the wearer. The process can be seen in the figure below.  First, the light from the lcd screen bounces off the mirror which has a normal line oriented at 45 degrees relative to the viewer. Due to the law of reflection, which states that the angle of incidence is equal to the angle of reflection relative to the normal line, the light rays first make a 90-degree turn. This results in a horizontal flip in the projected image. Then, in a similar fashion, this ray is reflected another 90 degrees against a transparent piece of polycarbonate plexiglass with anti reflective coating. This flips the image horizontally once again, resulting in a correctly oriented image. The total length that the light waves must travel should be equivalent to the straight-line distance required for an image to be discernible. This minimum distance is roughly 25cm for the average person. This led to shifting the screen back within the shell to create a clearer image in the final product.

<p align="center">
<img src = "https://drive.google.com/uc?export=view&id=1dOHIXN2L045LHh7rCoD0iTrW_IVKf7dz" width="200" height="200"> 
  </p>
  

## Software: 
<p align="center">
<img src = "https://drive.google.com/uc?export=view&id=1DzqhM4p5y729deKQQkTw5isccUeZRCP8" width="600" height="400"> 
  </p>
  
The emotion detection capabilities of the Clarity smart glasses are powered by Google Cloud Vision API. The glasses capture a photo of the people in front of the user, runs the photo through the Cloud Vision model using an API key, and outputs a discrete probability distribution of the emotions. This probability distribution is analyzed by Clarity’s code to determine the emotion of the people in the image. The output of the model is sent to the user through the OLED screen using the Pillow library.

The additional features of the smart glasses include displaying the current time, weather, and the user’s schedule for the day. These features are implemented using various Python libraries and a text file-based storage system. Clarity allows all the features of the smart glasses to be run concurrently through the implementation of asynchronous programming. Using the asyncio library, the user can iterate through the various functionalities seamlessly.
The glasses are interfaced through a button and the use of Siri. Using an iPhone, Siri can remotely power on the glasses and start the software. From there, users can switch between the various features of Clarity by pressing the button on the side of the glasses.

The software is implemented using a multi-file program that calls functions based on the current state of the glasses, acting as a finite state machine. The program looks for the rising edge of a button impulse to receive inputs from the user, resulting in a change of state and calling the respective function.

## Next Steps: 
The text steps include integrating a processor/computer inside the glasses, rather than using a raspberry pi. This would allow for the device to take the next step from a prototype stage to a mock mode. The model would also need to have bluetooth and wifi, so that the glasses are modular and easily customizable. We would also use magnifying lenses to make the images on the display bigger, so that a more dynamic UI is created. 

## Timelines:
As we believe that our device can really make an impact in people’s lives, the following diagram is used to show how we will pursue Clarity after this Makathon:

<p align="center">
<img src = "https://drive.google.com/uc?export=view&id=1m85rTMVAqIIK5VRbjqESn1Df-H0Pilx8" width="500" height="700"> 
</p>

## Refrences: 

### Hardware: 
All CADs were fully created from scratch. However, inspiration was taken from conventional DIY smartglasses out there.

### Software: 

### Research:
•	https://www.vectorstock.com/royalty-free-vector/smart-glasses-vector-3794640

•	https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2781897/

•	https://www.google.com/search?q=how+many+people+have+autism&rlz=1C1CHZN_enCA993CA993&oq=how+many+people+have+autism+&aqs=chrome..69i57j0i512l2j0i390l5.8901j0j9&sourceid=chrome&ie=UTF-8

•	(http://labman.phys.utk.edu/phys222core/modules/m8/human_eye.html)

•	https://mammothmemory.net/physics/mirrors/flat-mirrors/normal-line-and-two-flat-mirrors-at-right-angles.html



