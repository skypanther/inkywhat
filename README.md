# Inky wHAT weather display

A weather data display for the Inky wHAT e-paper display.

- Pulls live weather data from the Ambient Weather API
- Pulls moon phase and sunrise/sunset from the Visual Crossing API
- Pulls forecast data from the National Weather Service API

![Example image](images/live_example.jpeg "Example image")

## How To

You'll need API keys and such from the API providers.

Get the NWS API URL by sending a GET request to https://api.weather.gov/points/LAT,LONG where LAT and LONG are your latitude and longitude separated by a comma. In the resulting payload, you'll find the station ID (3 letter code) and the grid x/y to use.

You'll need an Ambient Weather weather station or info about a friend's so that you can pull data from the station. You can get the required info from your A-W web site account.

Information on setting up and testing your Inky wHAT is at https://learn.pimoroni.com/article/getting-started-with-inky-what

On the Raspberry Pi on which the Inky wHAT is installed, in your home directory:

1. `git clone https://github.com/pimoroni/inky`
2. `git clone https://github.com/skypanther/inkywhat.git`
3. `cd ./inkywhat`
4. Create a virtual environment with `python3 -m venv venv`
5. Activate it with `source venv/bin/activate`
6. `sudo apt-get install python3-dev libopenjp2-7 libopenblas-dev`
7. Depending on your version of Raspbian and PIL, you might need to install additional libraries for PIL/Pillow, which is installed by the install.sh script. Run `sudo apt-get install libjpeg-dev zlib1g-dev libfreetype6-dev pybind11-dev`
8. `cd ../inky`
9. Run `./install.sh` and when prompted, do not create a virtual environment; do install the example files.
10. Reboot when done
11. Use `sudo raspi-config` to enable both SPI and I2C. The installer is supposed to do this but didn't on my system. If you made changes, you'll need to reboot here.
12. `source inkywhat/venv/bin/activate`
13. `cd inky`
14. `pip install -r requirements-examples.txt` (if you did this as part of the install.sh step, you can skip it here)
15. Run an Inky wHAT sample to be sure your display is working as you expect.
16. `cd ~/inkywhat`
17. Install the required Python dependencies with `pip install -r requirements.txt`
18. Rename config_sample.py to config.py then open it in your favorite code editor
19. In the Weather.gov section, enter your station ID, grid x/y, your email address, and your application's name.
20. In the Visual Crossing section, enter your city name and two-letter state, and your API key.
21. In the Ambient Weather section, enter your station's MAC address, your API key, and your application key.
22. Save the file.
23. Run `python main.py`

I needed to manually install an older version of PIL/Pillow to get the script to work: `pip install pillow==11.3.0` I was getting import errors (`cannot import name '_imagingft' from 'PIL'`) with the 12.x version. Do this _before_ running the Inky install.sh script.

If you get "⚠️ Chip Select: (line 8, GPIO8) currently claimed by spi0 CS0" error, check for dtoverlay=spi0-0cs in your /boot/firmware/config.txt file (if not there, add it, reboot, and try again). If it's already there, then try `sudo rpi-update oldstable` (reboot and try again).

### Config notes

The frequency of API requests is also configurable. However, the default values are chosen a) to reflect that the Inky wHAT display takes many seconds to refresh and has a limited lifespan of refreshes, b) to be nice to the API providers, and c) to pull data at a rate reasonable to how often it changes. For example, the moon phase will not change significantly over short periods of time. So, the default Visual Crossing API calls are every 2 hours. Likewise, forecast data doesn't change too frequently, so that's fetched every 10 mins. Current conditions change by the second. However, remember the e-ink display can't refresh quickly. So, the default is every 2 minutes.

## Weather icons

This project uses the weather icons from https://erikflowers.github.io/weather-icons/

## License

- This repo's code is licensed under the MIT license
- The Weather Icons and the IniSans fonts are licensed under the SIL OFL 1.1
