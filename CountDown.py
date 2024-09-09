#count down, take user input for number of minutes and number of seconds

import time
import os

def CountSecondsinFullMinutes():
    for seconds in range(59,-1,-1):
        if seconds <= 60:
            print("Counting down:","\n",minutes,':',seconds)
            time.sleep(1)
            seconds -= 1
            os.system('cls')


print("welcome to John's countdown app")
minutes = int(input("How many minutes?: ")) #input number of minutes, convert to int
seconds = int(input("And how many Seconds?: "))
print("Starting countdown: \n")
time.sleep(2)
os.system('cls')


for i in range(seconds,-1,-1): #count down the seconds specified
    if True:
        print("Counting down:","\n",minutes,':',i)
        time.sleep(1)
        os.system('cls')
        i = i - 1      

for m in range(minutes,-1,-1): #for each full minute, run the function
        if minutes > 0:
            minutes = minutes - 1  
            CountSecondsinFullMinutes()
        else:
            print("TIMER IS UP!")

  
 






