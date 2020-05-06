# photobot-v4

Install via a crontab at restart on root cause this is a low security use case.

```
crontab -u root -e
```

Needs too be hard path as cron is running in some other scope

```
@reboot /home/user-name/photo-bot-v4/photobot.py 
```