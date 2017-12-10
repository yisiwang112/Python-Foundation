import time
import webbrowser
num = 0

print("This program started on "+time.ctime())
while num < 3:
    time.sleep(10)
    webbrowser.open("https://www.youtube.com/watch?v=-HjpL-Ns6_A")
    num = num + 1
