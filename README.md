# pushbullet-notify 

Send notifications from the terminal to pushbullet devices.


### Requirements

- Python 3
- urllib
- Pushbullet-Account


### Installation

1.) Copy the config to `~/.pushbullet-notify.conf`.
2.) Get the application-token from your pushbullet-settings(https://www.pushbullet.com/#settings)
    and insert it into the config.
3.) Run `./pushbullet-notify.py -d` to list all devices and add the identifiers
    of the wanted devices to the array in your config.


### Usage

If you followed the installation steps and set up everything correctly, you are
able to send push messages with:


```
./pushbullet-notify.py -t "title" -m "message"
```

*Hint: The message parameter is optional.*


### License

(c) 2016 Daniel Jankowski


This project is licensed under the MIT License.
Check out [LICENSE](./LICENSE) for more information.
