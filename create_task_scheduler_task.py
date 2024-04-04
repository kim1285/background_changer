import subprocess
import os
import sys

# create the task scheduler task using command modified with elevated privileges
print("create_taskscheduler_task.exe successfully opened.")
print("now creating task scheduler task")

path = sys.executable
dir_tmp = os.path.dirname(path)
print(dir_tmp)

with open(os.path.join(dir_tmp, "command.txt"), 'r') as com:
    command = com.read()
subprocess.run(command, shell=True)
a = input("Enter any key to exit")
