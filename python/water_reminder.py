import os
import time 

command = "osascript -e \'say \"Hey Harry drink water\"\'; osascript -e \'display alert \"Hey Harry, Drink water\"\'"
os.system(command)