# [Time names]
# 00 ~ 02: mid_night
# 02 ~ 04: late_night
# 04 ~ 06: very_early_morning
# 06~ 08: early_morning
# 08 ~ 10: mid_morning
# 10 ~ 12: late_morning
# 12 ~ 14: early_afternoon
# 14 ~ 16: mid_afternoon
# 16 ~ 18: late_afternoon
# 18 ~ 20: evening
# 20 ~ 22: late_evening
# 22 ~ 24: night
from database import time_names
from functions import get_program_data_path
import os

title = "[Background Changer Configuration Menu]\n"

description = ("Welcome to background changer configuration menu,\n"
               "where you can directly open up a folder containing\n"
               "your pictures for a specific time throughout the day!\n"
               "You can put new pictures in the folders you have opened up\n"
               "by entering certain number from 1 to 12 so that\n"
               "you can expect to see them as your background picture in the future!\n")

time_names_table = ("[Time names]\n"
                    "1. 00 ~ 02: mid_night\n"
                    "2. 02 ~ 04: late_night\n"
                    "3. 04 ~ 06: very_early_morning\n"
                    "4. 06~ 08: early_morning\n"
                    "5. 08 ~ 10: mid_morning\n"
                    "6. 10 ~ 12: late_morning\n"
                    "7. 12 ~ 14: early_afternoon\n"
                    "8. 14 ~ 16: mid_afternoon\n"
                    "9. 16 ~ 18: late_afternoon\n"
                    "10. 18 ~ 20: evening\n"
                    "11. 20 ~ 22: late_evening\n"
                    "12. 22 ~ 24: night\n")

# create a list of time names directories.
time_name_dirs_list = []
data_path = get_program_data_path()
for i in range(len(time_names)):
    time_name_dirs_list.append(os.path.join(data_path, "background_pictures",
                                            time_names[i]))


# create a dictionary where keys are integers(user selection numbers)
# and values are paths
time_name_dirs_dict = {}
counter_list = []

for i in range(len(time_names)):
    counter_list.append(i+1)

for i in range(len(counter_list)):
    time_name_dirs_dict[counter_list[i]] = time_name_dirs_list[i]


# get the user_config_input
def get_user_config_input():
    local_user_config_input = int(input("Enter a number between 1 and 12 to choose"
                                        " and open that corresponding picture folder.\n"
                                        "(For example, entering 2 will open the "
                                        "late_night picture folder.)\n"
                                        "Enter your input here: "))
    return local_user_config_input


print(title)
print(description)
print(time_names_table)


while True:
    # get user config input
    user_config_input = get_user_config_input()

    # open the folder the user has chosen
    os.system(f'explorer "{time_name_dirs_dict[user_config_input]}"')

    # prompt to continue or exit
    exit_prompt = int(input("Enter 1 to continue or 2 to exit\n"))
    if exit_prompt == 2:
        break
    else:
        continue

