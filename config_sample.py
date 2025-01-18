class WeatherConfig:
    def __init__(self):
        # Weather.gov API config values
        # Retrieve the following needed values for your location by hitting
        #   https://api.weather.gov/points/LAT,LONG
        #   For example https://api.weather.gov/points/43.3259722,-77.29205599
        self.wg_frequency_seconds = 600  # fetch new data every 10 mins (600 seconds)
        self.wg_url = "https://api.weather.gov/gridpoints/STATION/GRID_XY/forecast"  # don't change this
        self.wg_station = ""  # change this instead, e.g. BUF
        self.wg_grid_x_y = ""  # in form 88,65
        self.wg_email = ""  # your email address
        self.wg_app_name = "My weather app"  # your application name

        #  Visual Crossing Astronomical Data API config values
        self.vc_frequency_seconds = 7200  # fetch new data every 2 hours (7200 seconds)
        self.vc_api_url = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/LOCATION/today?unitGroup=us&elements=sunrise,sunset,moonphase,moonrise,moonset&include=days&key=APIKEY&contentType=json"  # don't change this
        self.vc_location = "City, ST"  # change this
        self.vc_api_key = "API_KEY"  # and this

        # Ambient Weather API config values
        self.aw_frequency_seconds = 60  # fetch new data every minute (60 seconds)
        self.aw_url = "https://rt.ambientweather.net/v1/devices/AW_STATION?applicationKey=APPLICATION_KEY&apiKey=API_KEY&limit=1"  # don't change this
        self.aw_station = "YOUR_STATIONS_MAC_ADDRESS"  # change this
        self.aw_api_key = "API_KEY"  # and this
        self.aw_application_key = "APPLICTION_KEY"  # and this
