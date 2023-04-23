## 03 Final RaceStrip

I wanted to make a hot wheels based derby racetrack. Includes a servo operated start gate and digital countdown, which releases cars after 3 seconds. Button at the finish line will detect which lanes finishes. External screen will display time elapsed and a winning message. 



### Sketch / Build
![sketch](https://github.com/carolynjhsu/Carol_Spr23/blob/main/03_Final_RaceStrip/Photos/Sketch.png)


### List of Hardware Components

-Atom Matrix + Prototyping Kit
-Angle Servo 
    -Control hinge plate that drops upon game start, moves back to start position after cars are deployed
-Light Dependent Resistor (LDR)
    -Used to sense when cars have moved past the sensor, signalling race end. 
![schematic](https://github.com/carolynjhsu/Carol_Spr23/blob/main/03_Final_RaceStrip/Photos/schematic.jpg)



### Software

Countdown details
```if(program_state=="start"): 
        if(start_pin.value()==0): #push button to start racing 
            countdown(3) #call function countdown to start the countdown before race starts
            start_time_1 = ticks_ms()
            start_time_2 = ticks_ms() #after countdown is initialized, start storing time elapsed in 2 variables for 2 separate lanes
```

Read values for sensor 1 and sensor 2

        ```lane_val1 = sensor1.read() #start reading values for sensor to prepare for race end
        lane_val2 = sensor2.read()
```
Then, find proper threshold to activate sensor when dark. 

```if(lane_val1<1500): #Figured out a good number by reading values of the sensor when obscured and unobscured.
            end_time_1 = ticks_ms()
            lane1_finished = True
```

        ``` if (lane1_finished and lane2_finished):
                    program_state="END GAME" 
                    #Use boolean values for both lane sensors to end game
            if(program_state=="END GAME"):
                time_lapsed_1 = end_time_1 - start_time_1
                time_lapsed_2 = end_time_2 - start_time_2
        ```
````
#web serial port connection to styled ID class
          if (value) {

            console.log('received.. ' + value);

            const textElement = document.getElementById("text");

            textElement.textContent = value;


          }
          ````
                

### Enclosure

Basic Wiring details for enclosure. Used tabs and push pins in cardboard to easily take out atom matrix and rewire as necessary. 

![placement_atom](https://github.com/carolynjhsu/Carol_Spr23/blob/main/03_Final_RaceStrip/Photos/placement.jpg)
![wiring](https://github.com/carolynjhsu/Carol_Spr23/blob/main/03_Final_RaceStrip/Photos/wires.jpg)

Attached hinge plate to blocks of cardboard, attached metal dowels sandwiched inbetween to hold up cars. The dowels were a bit too short so I removed some layers of cardboard and added some hot glue gun dots on top to add height. 
![hinge](https://github.com/carolynjhsu/Carol_Spr23/blob/main/03_Final_RaceStrip/Photos/hinge.jpg)

Sensors fit snugly in predrilled holes in the tracks. Fit them through the slots to lay flat enough for cars to roll over/against. 

![sensors](https://github.com/carolynjhsu/Carol_Spr23/blob/main/03_Final_RaceStrip/Photos/sensors.jpeg)

### Integrations

Use a web serial port to connect to a styled local page displaying countdown markers. In order to connect to the port, I have to first connect it via Pymakr in VS Code and then kill both the terminal and the connection to the port.

![Ready_Example](https://github.com/carolynjhsu/Carol_Spr23/blob/main/03_Final_RaceStrip/Photos/Ready.png)

### Project Demo

Unforunately I did not get to rerecord the demo as the laser cut arm on the servo broke off. I was not able to put it back together in such short notice, but I do have a recording of the in class demo. 

![demo](https://github.com/carolynjhsu/Carol_Spr23/blob/main/03_Final_RaceStrip/Photos/prototype_simulation.MOV)

### Final Thoughts

Overall, Though I had a few kinks with the prototyping process, I'm happy with how it turned out. Mechanical components were never something I was comfortable with, and though there is still a lot to learn, I've been able to gain a lot more confidence in this regard. I felt quite proud seeing my code work in real time, even if it did not perfectly execute during the final. 

Mechanical components are tricky in that there is no straightforward way to "debug" them–there were time when I had no idea how to move forward, since the issue at hand was not something I was ever familiar with (such as with the sensors and servo not working reliably. It's so easy to make a wrong connection and potentially ruin everything. It's a little more difficult to do that in code, so that was definitely a learning curve for me.)

Moving forward I would love to refine the actual prototype, utilizing cardboard laser cut outs once measurements are finalized and figuring out a more stable way to attach the servo in place (this is part of the "physical" prototyping process that I'm less privy to–making things work together in a mechanically elegant way as opposed to just tacking them onto a board. I'm not used to visualizing in that kind of environment, so that would be a good place to move forward with.)

With the skills and knowledge that I've accumulated in this class, I've been able to conquer something that I've been intimidated, but intrigued by, for years. 




### References
 

Countdown Timer Reference
[Countdown Timer Ref](https://www.geeksforgeeks.org/how-to-create-a-countdown-timer-using-python/)
Time Documentation for MicroPython
[Micropython_Time_Ref](https://docs.micropython.org/en/latest/library/time.html)
[Arduino_Hot_Wheels_Track](https://blog.arduino.cc/2016/12/20/dad-builds-an-arduino-hot-wheels-drag-strip-for-son/)

 I would have never thought to use a web serial port to connect my script to an externally styled page, simply because I did not come across that on the internet. Though there are a wealth of resources online, thank you to my advisor and to our TA for being a great source of help. 