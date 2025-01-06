# Helper class for building URLs


class UrlHelper:
    def __init__(self, weather_config):
        self.weather_config = weather_config

    def get_ambient_weather_url(self):
        #  "https://rt.ambientweather.net/v1/devices/AW_STATION?applicationKey=APPLICATION_KEY&apiKey=API_KEY&limit=1"
        aw_url = self.weather_config.aw_url
        aw_url = aw_url.replace("API_KEY", self.weather_config.aw_api_key)
        aw_url = aw_url.replace(
            "APPLICATION_KEY", self.weather_config.aw_application_key
        )
        aw_url = aw_url.replace("AW_STATION", self.weather_config.aw_station)
        return aw_url

    def get_weather_gov_url(self):
        # "https://api.weather.gov/gridpoints/STATION/GRID_XY/forecast"
        # Docs/info at https://www.weather.gov/documentation/services-web-api
        wg_url = self.weather_config.wg_url
        wg_url = wg_url.replace("STATION", self.weather_config.wg_station)
        wg_url = wg_url.replace("GRID_XY", self.weather_config.wg_grid_x_y)
        return wg_url

    def get_vc_url(self):
        # "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/LOCATION/
        # today?unitGroup=us&elements=sunrise,sunset,moonphase,moonrise,moonset&include=days&key=APIKEY&contentType=json"
        vc_url = self.weather_config.vc_api_url
        vc_url = vc_url.replace("LOCATION", self.weather_config.vc_location)
        vc_url = vc_url.replace("APIKEY", self.weather_config.vc_api_key)
        return vc_url
