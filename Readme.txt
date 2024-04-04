Dear user,

Thank you for downloading the background changer. Background changer program is a windows program to automatically change your background into pre-selected, groups of random pictures every two hours a day. The program is designed to give you a sense of passage of time throughout the day, by subtly reminding you of the visual changes of nature.



[[Installation Instructions]]
The background changer program is divided into three parts - "installation.exe", "background_changer.exe", "configuration.exe"



[If you have a non-windows home edition, such as pro]
1. To install the program, you should locate the "installation.exe" and then double click to open it (manually opening it using elevated privilege is not recommanded). 

2.A command prompt will show up. You will be prompted to enter your pc's password(if you have one.) This is required to create windows task scheduler task initially.

3. If it says wrong password even if your password is correct, you need to add batch logon right to your windows account. 

1. Press Win + R to open the "Run" dialog. Type secpol.msc and press Enter.

2. Navigate to Local Policies: In the left pane of the Local Security Policy window, expand the following: Local Policies -> User Rights Assignment -> Add Batch Logon Rights:

3. In the right pane, locate and double-click on the policy named Log on as a batch job.

4. Add User or Group: Click the "Add User or Group" button.

5. Type your username to add batch logon rights to.

6. Click "Check Names" to validate the entry.

7. Click "OK" when done.

8. Apply Changes: Click "Apply" and then "OK" to close the policy window.

9. Now try click installation.exe and try again. If it still doesn't work, follow the windows home edition installation guide.

10. To immediately run the program once to change background, open task scheduler.

11. find background_changer task.

12. Click 'Run' on 'Selected Item' selction while your background_changer task routine is highlighted to change background manaually.


- note: The program does not store the password. The windows task scheduler directly handle your password. Background changer does not have access to your password at any point by design, it just calls the windows task scheduler program you already have and then let them handle your pw. 



[If you have a windows home edition]
Do everything same as the above. However, you may encounter in a prompt that says the password is incorrect. This is because of user's permission difference in home edition. To work around this issue, please follow the steps:

1. Mannually exit the promt that says your pw is wrong. You will still have created necessary files ready to run the program. 

2. Press windows key and type '%appdata%' and press enter to open a path to "C:\Users\'your_username'\AppData\Roaming". now go navigate to "C:\Users\'your_username'\AppData\Local\Background_changer". 'your_username' is your username.

3. You will see background_pictures folder, background_changer.exe, log.txt, and background_changer.xml. you will manually create a windows task scheduler task using this background_changer.xml file.

4. Press windows key and type 'task scheduler' and press enter to open windows task schedueler program.

5. Inside the progarm, on the right top side, you will see 'Import Task...' on Actions section.

6. Once a popup window opens up, navigate to the background_changer.xml file and click, press open.

7. Create task popup window will show up. Check if the 'Run with highest privileges' check box is checked. If it isn't check it. Other than that, you do not need to make any changes unless you desire. Press okay and You are good to go. 

8. To immediately run the program once to change background, click 'Run' on 'Selected Item' selction while your background_changer task routine is highlighted.



[About the images included]
The default pictures for each 2 hour frame of the day are gathered from unsplash.com. They are created by many talented individuals. You could find the name of the original authors of the pictures in each picture's name. I have not made any modifications of the pictures gathered from there.



[Security and Privacy]
Rest assured, the Background Changer does not collect or store any personal information from users. Your privacy and security are paramount. 



[Contact]
For further security concerns and or suggestions of improvements, you are welcome to check out the code of the program, available on Github for potential contributions. or contact me directly.
- GitHub: https://github.com/kim1285
- Linkedin: https://www.linkedin.com/in/kangsan-kim-02a85023a/
- Email: rlarkdtks8713@gmail.com



[License]
This program is released under GNU, allowing users to modify and distribute it with certain conditions. Please refer to the LICENSE file for details.




Thank you again, for downloading the background changer and I hope it adds a touch of beauty to your day.


Best regards,
Kangsan Kim



