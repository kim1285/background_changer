from functions import (initial_installation, create_task_scheduler_task,
                       run_with_elevated_privileges)
import os
import sys

if __name__ == '__main__':
    # performs initial installation.
    initial_installation()

    # creates a windows task schedular task to run background_changer.exe every 2h.
    command = create_task_scheduler_task()

    # opens create_task_scheduler_task.exe with elevated privileges.
    print('opening create_task_scheduler_task.exe with elevated privileges.')
    script_path = sys.executable
    script_dir = os.path.dirname(script_path)
    target_exe_path = os.path.join(script_dir, 'create_task_scheduler_task.exe')
    print(f'target_exe path: {target_exe_path}')

    with open(os.path.join(script_dir, "command.txt"), 'w') as c:
        c.write(command)

    run_with_elevated_privileges(target_exe_path)



