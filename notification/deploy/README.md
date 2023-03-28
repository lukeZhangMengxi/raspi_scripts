# Operation

## Deploy as systemd
```
sudo cp raspi_notification.sh /usr/bin/raspi_notification.sh
sudo chmod +x /usr/bin/raspi_notification.sh
sudo nano /usr/bin/raspi_notification.sh
--> Fill Password

sudo cp raspi_notification.service /etc/systemd/system/raspi_notification.service

sudo su
systemctl start raspi_notification
```

<br/>

## Check status
```
$ systemctl status raspi_notification.service
● raspi_notification.service - RaspberryPi Notification Service
   Loaded: loaded (/etc/systemd/system/raspi_notification.service; enabled; vendor preset: enabled)
   Active: active (running) since Mon 2023-03-27 22:09:58 PDT; 1min 45s ago
 Main PID: 1959 (bash)
    Tasks: 2 (limit: 2200)
   Memory: 7.9M
   CGroup: /system.slice/raspi_notification.service
           ├─1959 /bin/bash /usr/bin/raspi_notification.sh
           └─1967 python /home/pi/workspace/raspi_scripts/notification/main.py

Mar 27 22:09:58 raspberrypi systemd[1]: Started RaspberryPi Notification Service.


$ journalctl -u raspi_notification.service --since '2023-03-27 22:09:58 PDT'
-- Logs begin at Sun 2023-03-19 14:50:25 PDT, end at Mon 2023-03-27 22:10:31 PDT. --
Mar 27 22:09:58 raspberrypi systemd[1]: Stopping RaspberryPi Notification Service...
Mar 27 22:09:58 raspberrypi systemd[1]: raspi_notification.service: Main process exited, code=killed, status=15/TERM
Mar 27 22:09:58 raspberrypi systemd[1]: raspi_notification.service: Succeeded.
Mar 27 22:09:58 raspberrypi systemd[1]: Stopped RaspberryPi Notification Service.
Mar 27 22:09:58 raspberrypi systemd[1]: Started RaspberryPi Notification Service.
```

