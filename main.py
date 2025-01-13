"""
Weather app for the Inky wHAT e-ink display.

Rough plan:

* Once per day (1:00 am)
    * fetch sunrise,sunset,moonphase from Visual Crossing
    * save JSON / data
* Once per hour
    * fetch next N days forecast from Weather.gov
    * save JSON / data
* Every N minutes
    * Fetch current conditions from Ambient Weather
    * save JSON / data
* Every N minutes
    * read saved data
    * update display
"""

import time
import requests
from config import WeatherConfig
from datetime import datetime

# from inky.auto import auto
from PIL import Image, ImageFont, ImageDraw

from moonphases import get_moon_phase_image
from url_helper import UrlHelper

MOCK = True


class InkyWeather:
    def __init__(self):
        self.weather_config = WeatherConfig()
        self.url_helper = UrlHelper(self.weather_config)
        self.astronomical_data = {}
        self.forecast = {}
        self.current_conditions = {}
        self.ambient_weather_url = self.url_helper.get_ambient_weather_url()
        self.weather_gov_url = self.url_helper.get_weather_gov_url()
        self.visual_crossing_url = self.url_helper.get_vc_url()
        self.astronomical_data_last_checked = 0
        self.forecast_last_checked = 0
        self.current_conditions_last_fetched = 0
        # self.inky_display = auto()
        # self.inky_display.set_border(inky_display.WHITE)

    def fetch_sun_moon_data(self):
        """Retrieves sunrise, sunset, moon phase, etc from the Visual Crossing
        API and updates self.astronomical_data"""
        self.astronomical_data_last_checked = datetime.now()
        if MOCK is True:
            self.astronomical_data = {
                "sunrise": "07:42:10",
                "sunset": "16:43:43",
                "moonphase": 0.25,
            }
            return
        try:
            resp = requests.get(self.visual_crossing_url)
            resp.raise_for_status()
            data = resp.json()
            self.astronomical_data = data["days"][0]
            print("fetching astronomical data")
        except requests.HTTPError as exc:
            print(exc.response.status_code)

    def fetch_forecast_data(self):
        """Retrieves forecast from the NWS API and updates self.forecast"""
        self.forecast_last_checked = datetime.now()
        if MOCK is True:
            self.forecast = [
                {},
                {
                    "temperature": 84,
                    "probabilityOfPrecipitation": {"value": 50},
                    "windSpeed": "8 to 12 mph",
                },
            ]
            return
        # Add headers per NWS API instructions
        headers = {
            "User-Agent": f"({self.weather_config.wg_app_name}, {self.weather_config.wg_email})"
        }
        try:
            resp = requests.get(self.weather_gov_url, headers=headers)
            resp.raise_for_status()
            data = resp.json()
            self.forecast = data["properties"]["periods"]
            print("fetching NWS forecast data")
        except requests.HTTPError as exc:
            print(exc.response.status_code)
        except requests.JSONDecodeError:
            print("NWS API: Response not JSON")
        except KeyError:
            print("NWS API: Forecast data missing")

    def fetch_current_conditions_data(self):
        """Retrieves current weather conditions from Ambient Weather (my station)
        and updates self.current_conditions
        """
        self.current_conditions_last_fetched = datetime.now()
        if MOCK is True:
            self.current_conditions = {
                "tempf": 80,
                "windspeedmph": 10,
                "windgustmph": 15,
                "dailyrainin": 0.5,
            }
            return
        try:
            resp = requests.get(self.ambient_weather_url)
            resp.raise_for_status()
            data = resp.json()
            self.current_conditions = data[0]
            print("fetching current conditions")
        except requests.HTTPError as exc:
            print(exc.response.status_code)

    def should_get_current_conditions(self, last_fetched, freqency):
        """Determine whether to hit URL to retrieve conditions data"""
        now = datetime.now()
        diff = round((now - last_fetched).total_seconds())
        if diff != 0 and (diff == freqency or diff % freqency == 0):
            return True
        return False

    def parse_ambient_data(self, data):
        """Parse the API response and return select values"""
        return {
            "temp": (data["tempf"], 90, 50),
            "windspeed": (data["windspeedmph"], 90, 220),
            "gust": (data["windgustmph"], 90, 245),
            "rain": (data["dailyrainin"], 90, 145),
        }

    def parse_astronomical_data(self, data):
        """Parse the API response and return select values"""
        return {
            "sunrise": (data["sunrise"], 300, 30),
            "sunset": (data["sunset"], 300, 70),
            "moonphase": (data["moonphase"], 300, 100),
        }

    def parse_nws_data(self, data):
        """Parse the API response and return select values"""
        return {
            "high": (data["temperature"], 300, 212),
            "precip": (data["probabilityOfPrecipitation"]["value"], 300, 260),
            "wind": (data["windSpeed"], 300, 235),
        }

    def update_display(self):
        current_conditions = self.parse_ambient_data(self.current_conditions)
        # print(current_conditions["temp"][0])
        astro_data = self.parse_astronomical_data(self.astronomical_data)
        forecast_data = self.parse_nws_data(self.forecast[1])
        font16 = ImageFont.truetype("font/inisans.otf", 16)
        font32 = ImageFont.truetype("font/inisans.otf", 32)
        font48 = ImageFont.truetype("font/inisans.otf", 48)
        black = (0, 0, 0, 255)
        red = (255, 0, 0, 255)

        with Image.open("images/weather_background2.png") as im:
            im1 = im.convert("RGBA")
            txt = Image.new("RGBA", im.size, (255, 255, 255, 0))
            draw = ImageDraw.Draw(txt)
            temp_color = black
            if current_conditions["temp"][0] > 79:
                temp_color = red
            draw.text(
                (current_conditions["temp"][1], current_conditions["temp"][2]),
                f'{current_conditions["temp"][0]} F',
                font=font48,
                fill=temp_color,
            )
            draw.text(
                (current_conditions["rain"][1], current_conditions["rain"][2]),
                f'{current_conditions["rain"][0]} in',
                font=font32,
                fill=(0, 0, 0, 255),
            )
            draw.text(
                (
                    current_conditions["windspeed"][1],
                    current_conditions["windspeed"][2],
                ),
                f'{current_conditions["windspeed"][0]} mph',
                font=font16,
                fill=(0, 0, 0, 255),
            )
            draw.text(
                (
                    current_conditions["gust"][1],
                    current_conditions["gust"][2],
                ),
                f'{current_conditions["gust"][0]} mph gust',
                font=font16,
                fill=(0, 0, 0, 255),
            )
            draw.text(
                (
                    astro_data["sunrise"][1],
                    astro_data["sunrise"][2],
                ),
                f'{astro_data["sunrise"][0]}',
                font=font16,
                fill=(0, 0, 0, 255),
            )
            draw.text(
                (
                    astro_data["sunset"][1],
                    astro_data["sunset"][2],
                ),
                f'{astro_data["sunset"][0]}',
                font=font16,
                fill=(0, 0, 0, 255),
            )
            # moonphase is an image rather than text
            phase_img = get_moon_phase_image(astro_data["moonphase"][0])
            offset = (astro_data["moonphase"][1], astro_data["moonphase"][2])
            im1.paste(phase_img, offset)
            high_color = (0, 0, 0, 255)
            if forecast_data["high"][0] > 79:
                high_color = (255, 0, 0, 255)
            draw.text(
                (
                    forecast_data["high"][1],
                    forecast_data["high"][2],
                ),
                f'{forecast_data["high"][0]} F',
                font=font16,
                fill=high_color,
            )
            draw.text(
                (
                    forecast_data["wind"][1],
                    forecast_data["wind"][2],
                ),
                f'{forecast_data["wind"][0]}',
                font=font16,
                fill=(0, 0, 0, 255),
            )
            draw.text(
                (
                    forecast_data["precip"][1],
                    forecast_data["precip"][2],
                ),
                f'{forecast_data["precip"][0]}%',
                font=font16,
                fill=(0, 0, 0, 255),
            )

            out = Image.alpha_composite(im1, txt)
            out.show()
        # inky_display.set_image(img)
        # inky_display.show()

    def run(self):
        """Loop logic:
        Once every N mins retrieve current conditions
        Once every M hours retrieve astronomical data
        Once every O hours retrieve forecast data
        """
        self.fetch_current_conditions_data()
        self.fetch_sun_moon_data()
        self.fetch_forecast_data()
        is_first_run = True
        while True:
            should_update_display = is_first_run
            # Check to see if we should get new sun/moon data
            if self.should_get_current_conditions(
                self.astronomical_data_last_checked,
                self.weather_config.vc_frequency_seconds,
            ):
                self.fetch_sun_moon_data()
                should_update_display = True
            # Check to see if we should get new conditions data
            if self.should_get_current_conditions(
                self.current_conditions_last_fetched,
                self.weather_config.aw_frequency_seconds,
            ):
                self.fetch_current_conditions_data()
                should_update_display = True
            # Check to see if we should get new forecast data
            if self.should_get_current_conditions(
                self.forecast_last_checked,
                self.weather_config.wg_frequency_seconds,
            ):
                self.fetch_forecast_data()
                should_update_display = True

            # self.fetch_sun_moon_data()
            # self.fetch_forecast_data()
            if should_update_display:
                self.update_display()
            is_first_run = False
            time.sleep(1)
            if MOCK is True:
                exit()


if __name__ == "__main__":
    iw = InkyWeather()
    iw.run()
