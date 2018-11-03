# Add your Python code here. E.g.
from microbit import *
import random


computer_choice = random.randint(0, 4)
rock = Image("00000:"
             "09990:"
             "09990:"
             "09990:"
             "00000:")

paper = Image("99999:"
              "90009:"
              "90009:"
              "90009:"
              "99999:")

scissors = Image("99009:"
                 "99090:"
                 "00900:"
                 "99090:"
                 "99009:")

spock = Image("90000:"
              "90900:"
              "99990:"
              "00900:"
              "09090:")

lizard = Image("99099:"
               "09990:"
               "09990:"
               "00900:"
               "99900:")

human_choice = [rock, paper, scissors, spock, lizard]



while True:
    if accelerometer.was_gesture("shake"):
        sleep(100)
        display.show(random.choice(human_choice))
        
        
        
        
        
        
        
        
        
           
                 
