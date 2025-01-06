class WeatherConfig:
    def __init__(self):
        # Weather.gov API config values
        # Retrieve the following needed values for your location by hitting
        #   https://api.weather.gov/points/LAT,LONG
        #   For example https://api.weather.gov/points/43.3259722,-77.29205599
        self.wg_frequency_seconds = 300  # fetch new data every 5 mins (300 seconds)
        self.wg_url = "https://api.weather.gov/gridpoints/STATION/GRID_XY/forecast"
        self.wg_station = ""  # e.g. BUF
        self.wg_grid_x_y = ""  # in form 88,65
        self.wg_email = ""  # your email address
        self.wg_app_name = "My weather app"  # your application name

        #  Visual Crossing Astronomical Data API config values
        self.vc_frequency_seconds = 3600  # fetch new data every hour (3600 seconds)
        self.vc_api_url = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/LOCATION/today?unitGroup=us&elements=sunrise,sunset,moonphase,moonrise,moonset&include=days&key=APIKEY&contentType=json"
        self.vc_location = "City, ST"
        self.vc_api_key = "API_KEY"

        # Ambient Weather API config values
        self.aw_frequency_seconds = 60  # fetch new data every minute (60 seconds)
        self.aw_url = "https://rt.ambientweather.net/v1/devices/AW_STATION?applicationKey=APPLICATION_KEY&apiKey=API_KEY&limit=1"
        self.aw_station = "YOUR_STATIONS_MAC_ADDRESS"
        self.aw_api_key = "API_KEY"
        self.aw_application_key = "APPLICTION_KEY"
