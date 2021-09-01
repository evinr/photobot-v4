# photobot-v4

https://ubuntu-mate.org/download/arm64/ 
Setup to not need to login with checkbox.
Enable SSH - 
```
    sudo apt-get remove openssh-server
```
```
    sudo apt-get install openssh-server
```
Reboot system after install 
```
    sudo systemctl enable ssh
```
Update power management settings.
If using a screen with a height of 600px, the screen will need to be rotated to expose the button.
Uncheck the Activate Screen Saver when Idle.
Uncheck Lock Screen when Screen Saver is Active.
If screen was rotated before (due to a height of 600px), then rotate the screen back.
Remember the password!
```
sudo apt-get -y install gphoto2 curl python-xlib python3-pip eog python3-tk python3-pil python3-pil.imagetk
```
```
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
```
Then run the following command in the folder where you have downloaded get-pip.py:
```
python get-pip.py
```
```
pip install keyboard pyserial
```
Finally we need to set our environmental variables. Rather than doing it in the bash_config or bashrc we need them to be available to the root user as well since that is who will be running our script.
export $MACHINE_NAME=your-user-name

Alternatively, to create persistent variables that are truly system-wide, you should set them in /etc/environment
```
sudo usermod -a -G dialout $USER
```
Logout/login required for these changes to be made.


Install via a crontab at restart on root due to the way we are listing for keyboard presses
```
sudo crontab -u root -e
```

Needs too be hard path as cron is running in some other scope. Also while we are at it schedule auto reboots.

```
@reboot python3 /home/atm-machine/photobot-v4/photobot.py 
0 4   *   *   *    /sbin/shutdown -r +5
```


ENVIRONMENTAL VARIABLE ON ROOT IS MISSING!!!
DISPLAY=:0.0
/etc/environment
Add this command to the startup scripts application
feh latest.jpeg -F -R 3 --hide-pointer 

?? --auto-reload ??