# photobot-v4

# deps
https://ubuntu-mate.org/download/arm64/ 
Setup to not need to login with checkbox.
Enable SSH - 
    sudo apt-get remove openssh-server
    sudo apt-get install openssh-server
    # I rebooted system after install
    sudo systemctl enable ssh
Update power management settings.
If using a screen with a height of 600px, rotate the screen.
Activate screen saver when idle
Lock screen when screen saver is active.
If screen was rotated before (due to a height of 600px), then rotate the screen back.
Remember the password!

sudo apt-get -y install python3-tk python3-pil python3-pil.imagetk gphoto2 curl python-xlib python3-pip
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py

Then run the following command in the folder where you have downloaded get-pip.py:

python get-pip.py

pip install keyboard pyserial

sudo usermod -a -G dialout $USER
Logout/login required.


Install via a crontab at restart on ???root???? cause this is a low security use case.
```
sudo crontab -u root -e
```

Needs too be hard path as cron is running in some other scope. Also while we are at it schedule auto reboots.

```
@reboot /home/atm-machine/photobot-v4/photobot.py 
0 4   *   *   *    /sbin/shutdown -r +5
```