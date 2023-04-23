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
![schematic](https://github.com/carolynjhsu/Carol_Spr23/blob/main/03_Final_RaceStrip/Photos/schematic.heic)



### Software

```if(program_state=="start"): 
        if(start_pin.value()==0): #push button to start racing 
            countdown(3) #call function countdown to start the countdown before race starts
            start_time_1 = ticks_ms()
            start_time_2 = ticks_ms() #after countdown is initialized, start storing time elapsed in 2 variables for 2 separate lanes
```


        ```lane_val1 = sensor1.read() #start reading values for sensor to prepare for race end
        lane_val2 = sensor2.read()
```

```if(lane_val1<1500): #find proper threshold to activate sensor when dark. 
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
                

### Enclosure

Basic Wiring details for enclosure. Used tabs and push pins in cardboard to easily take out atom matrix and rewire as necessary. 

![wiring](https://github.com/carolynjhsu/Carol_Spr23/blob/main/03_Final_RaceStrip/Photos/wire_placement.HEIC)

Attached hinge plate to blocks of cardboard, attached metal dowels sandwiched inbetween to hold up cars. The dowels were a bit too short so I removed some layers of cardboard and added some hot glue gun dots on top to add height. 
![hinge](https://github.com/carolynjhsu/Carol_Spr23/blob/main/03_Final_RaceStrip/Photos/hinge_plate.HEIC)

Sensors fit snugly in predrilled holes in the tracks. Fit them through the slots to lay flat enough for cars to roll over/against. 

![sensors](https://github.com/carolynjhsu/Carol_Spr23/blob/main/03_Final_RaceStrip/Photos/sensors.HEIC)

### Integrations

Use a web serial port to connect to a styled local page displaying countdown markers. In order to connect to the port, I have to first connect it via Pymakr in VS Code and then kill both the terminal and the connection to the atom matrix, and then pair the atom matrix to age via the port. 

### Project Demo


![demo](https://github.com/carolynjhsu/Carol_Spr23/blob/main/03_Final_RaceStrip/Photos/prototype_simulation.MOV)


### References

Countdown Timer Reference
![Countdown Timer Ref](https://www.geeksforgeeks.org/how-to-create-a-countdown-timer-using-python/)