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
from url_helper import UrlHelper


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

    def fetch_sun_moon_data(self):
        """Retrieves sunrise, sunset, moon phase, etc from the Visual Crossing
        API and updates self.astronomical_data"""
        self.astronomical_data_last_checked = datetime.now()
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

    def update_display(self):
        print(f"Moon phase: {self.astronomical_data["moonphase"]}")
        print(f"NWS forecast: {self.forecast[1]["name"]}")
        print(f"Ambient - current temp: {self.current_conditions["tempf"]}")

    def run(self):
        """Loop logic:
        Once every N mins retrieve current conditions
        Once every M hours retrieve astronomical data
        Once every O hours retrieve forecast data
        """
        self.fetch_current_conditions_data()
        self.fetch_sun_moon_data()
        self.fetch_forecast_data()
        while True:
            should_update_display = False
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
            time.sleep(1)


if __name__ == "__main__":
    iw = InkyWeather()
    iw.run()
