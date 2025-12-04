# Background Changer – Quick Guide
A simple Windows app that automatically changes your desktop wallpaper every 2 hours using beautiful nature photos, gently reminding you of the passing day.

## Files included
```
installation.exe
background_changer.exe
configuration.exe
```
## Installation (Windows Pro / Enterprise)

Double-click installation.exe (no need to run as admin).
Enter your Windows password when prompted (only to create a scheduled task).
If the password is rejected, grant yourself “Log on as a batch job” right via secpol.msc → Local Policies → User Rights Assignment, then retry.

## Installation (Windows Home)

Run installation.exe anyway (ignore wrong-password error).
Open Task Scheduler → Action → Import Task… → select background_changer.xml (found in %LocalAppData%\Background_changer).
Check “Run with highest privileges” → OK.

Run manually anytime
In Task Scheduler, right-click the “background_changer” task → Run.

### Images
Default photos are royalty-free from Unsplash. Photographer credits are in each filename.
Privacy & Security

### No data collection
Your password never touches the app; it’s handled directly by Windows Task Scheduler

### Configuration
Run configuration.exe anytime to change picture folders or intervals.
Source & Contact

GitHub: https://github.com/kim1285
Email: rlarkdtks8713@gmail.com
LinkedIn: https://www.linkedin.com/in/kangsan-kim-02a85023a/

License
GNU GPL (see LICENSE file)

Enjoy a prettier desktop!
