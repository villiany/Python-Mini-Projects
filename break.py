#program to pop up a youtube video every 10s, telling the user to take a break
import webbrowser
import time
breakcount=3
print("This program started on " + time.ctime())
while(breakcount>0):
    time.sleep(10)
    webbrowser.open("https://www.youtube.com/watch?v=1u_K_Jm8BWw")
    breakcount-=1

