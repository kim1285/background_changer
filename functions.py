import os
import time
import datetime
import random
import ctypes
import sys
import shutil
import win32security
import subprocess
import xml.etree.ElementTree as ET
from database import time_names


def get_username():  # get username
    local_username = os.getenv('USERNAME')
    return local_username


def get_user_sid(local_username):  # gets user's SID to use in task manager xml
    username = local_username
    try:
        sid_info, _, _ = win32security.LookupAccountName(None, username)
        return win32security.ConvertSidToStringSid(sid_info)
    except Exception as e:
        print(f"Error getting SID for {username}: {e}")
        return None


def get_program_data_path():  # get the data path in user's appdata dir
    appdata_dir_wo_username = 'C:\\Users\\'
    username = get_username()
    appdata_dir_w_username = os.path.join(appdata_dir_wo_username, username)
    appdata_dir_w_username = os.path.join(appdata_dir_w_username, "AppData\\Local")
    program_data_path_local = os.path.join(appdata_dir_w_username, "Background_changer")
    return program_data_path_local


def create_data_path():  # Create program_data_path
    appdata_dir_wo_username = 'C:\\Users\\'
    username = get_username()
    appdata_dir_w_username = os.path.join(appdata_dir_wo_username, username)
    appdata_dir_w_username = os.path.join(appdata_dir_w_username, "AppData\\Local")
    program_data_path_local = os.path.join(appdata_dir_w_username, "Background_changer")
    try:
        os.makedirs(program_data_path_local)
    except OSError as program_data_path_error:
        error_time_log = time.strftime("%b %d, %y, %H:%M:%S")
        error_time_log = f"{error_time_log} - {program_data_path_error}"
        print(error_time_log)
    return program_data_path_local


def update_pictures():  # Update directories of existing pictures in the folders and make them into dictionaries
    program_data_path = get_program_data_path()
    picture_paths_dict = {}
    time_names_local = time_names
    for i in range(len(time_names_local)):
        time_folder_dir_i = str(os.path.join(program_data_path, "background_pictures", time_names_local[i]))
        picture_paths_dict[time_names_local[i]] = (os.listdir(time_folder_dir_i))
    return picture_paths_dict


def initial_installation():  # locate the directories of default picture folders
    script_dir = os.path.dirname(sys.executable)
    source_pics_path = os.path.join(script_dir, "background_pictures")

    # locate the directories of target picture folders to deploy
    destination_pics_path = create_data_path()
    print(source_pics_path)
    print(destination_pics_path)

    # move the default pictures with nested folder structures into user's background_changer/background_pictures.
    try:
        shutil.move(source_pics_path, destination_pics_path)
    except shutil.Error as e1:
        print(e1)

    # log changes
    program_data_path = create_data_path()
    with open(os.path.join(program_data_path, "log.txt"), "a") as log_file:
        log_file.write(f"{datetime.datetime.now()} - default pictures have been "
                       f"deployed to user's directories in structured folders.\n")

    # move the background_changer.exe to appdata path. important for task scheduler task.
    background_changer_path = os.path.join(script_dir, "background_changer.exe")
    try:
        shutil.move(background_changer_path, create_data_path())
    except shutil.Error as e2:
        print(e2)


def create_task_scheduler_task():  # creates a windows task scheduler task to start main script every 2h
    # locate the directory of bundled task scheduler xml
    tmp_path = os.path.dirname(sys.executable)
    sample_task_scheduler_xml_path = os.path.join(tmp_path, "background_changer.xml")
    source_file_path = sample_task_scheduler_xml_path

    # move the sample_task_scheduler_xml to user's background_changer folder in appdata dir
    # change later to `move` from `copy`
    user_data_path = create_data_path()
    target_file_path = os.path.join(user_data_path, "background_changer.xml")
    try:
        shutil.copy(source_file_path, target_file_path)
    except shutil.Error as e:
        print(f'Error: {e}')

    # get the user's SID
    username = get_username()
    user_sid = get_user_sid(username)

    # parse the XML file
    tree = ET.parse(target_file_path)
    root = tree.getroot()

    # Register the namespace with an empty prefix
    ET.register_namespace('', 'http://schemas.microsoft.com/windows/2004/02/mit/task')

    # find the <UserId> element and modify its text
    for user_id in root.iter('{http://schemas.microsoft.com/windows/2004/02/mit/task}UserId'):
        print("Found UserId element:", user_id.text)
        user_id.text = user_sid  # replace with the new SID
        print("Modified UserId to:", user_id.text)

    # find the <Command> element and modify its text
    program_exe_path = os.path.join(get_program_data_path(), "background_changer.exe")
    for program_path in root.iter('{http://schemas.microsoft.com/windows/2004/02/mit/task}Command'):
        print("Found CommandPath element:", program_path.text)
        program_path.text = program_exe_path
        print("Modified CommandPath to: program_exe_path")

    # find the <LogonType> element and modify its text so that the task only starts when the user is logged on.
    # This is an anecdotal bugfix.
    logon_type = str("InteractiveToken")
    for logon_type_tmp in root.iter('{http://schemas.microsoft.com/windows/2004/02/mit/task}LogonType'):
        print("Found LogonType element:", logon_type_tmp.text)
        logon_type_tmp.text = logon_type
        print("Modified LogonType to: InteractiveToken")

    # write the modified XML back to the file
    tree.write(target_file_path, encoding="utf-16", xml_declaration=True)

    # command to create a new task using schtasks with the XML file.
    command = f"schtasks /Create /XML {target_file_path} /TN background_changer /RU {username}"
    return command


# opens create_task_scheduler_task.exe with elevated privileges.
def run_with_elevated_privileges(target_exe_local):
    try:
        ctypes.windll.shell32.ShellExecuteW(
            None,
            "runas",
            target_exe_local,
            None,
            None,
            1  # SW_SHOW
        )
    except Exception as e:
        print(f'Error: {e}')
        sys.exit(1)


def change_background():  # randomly choose a picture in the time appropriate folder, and set it to current background.
    now = int(time.strftime('%H'))
    picture_paths_dict = update_pictures()
    program_data_path = get_program_data_path()

    for i in range(len(time_names)):
        if 2 * i <= now < 2 * (i + 1):
            selected_picture = random.choice(picture_paths_dict[time_names[i]])

            # Set the background into a randomly-selected-time-appropriate-picture.
            ctypes.windll.user32.SystemParametersInfoW(20, 0, os.path.join(program_data_path, "background_pictures",
                                                                           time_names[i], selected_picture))
            temp_dir = os.path.join(program_data_path, "background_pictures", time_names[i], selected_picture)

            print(f"{time.strftime("%b %d, %Y %H:%M:%S")} - successfully set the background to "
                  f"a time appropriate picture: {temp_dir}")

            # logging the change of background to log.txt
            log(f"successfully set the background to a time appropriate picture: {temp_dir}")


def log(text_to_log):
    data_path = get_program_data_path()
    with open(os.path.join(data_path, "log.txt"), "a") as local_log:
        local_log.write(f"{time.strftime("%b %d, %Y %H:%M:%S")} - {text_to_log}")

