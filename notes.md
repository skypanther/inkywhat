# API sample payloads

## Visual Crossing API sample response

```
{
  "queryCost": 1,
  "latitude": 43.1558,
  "longitude": -77.6163,
  "resolvedAddress": "Rochester, NY, United States",
  "address": "Rochester, NY",
  "timezone": "America/New_York",
  "tzoffset": -5,
  "days": [
    {
      "sunrise": "07:42:10",
      "sunset": "16:43:43",
      "moonphase": 0.96,
      "moonrise": "06:56:55",
      "moonset": "15:12:42"
    }
  ]
}
```

## Ambient Weather API sample response

```
[
  {
    "dateutc": 1735682100000,
    "tempf": 46.8,
    "humidity": 69,
    "windspeedmph": 1.57,
    "windgustmph": 2.24,
    "maxdailygust": 11.41,
    "winddir": 82,
    "uv": 0,
    "solarradiation": 0.13,
    "hourlyrainin": 0,
    "eventrainin": 0,
    "dailyrainin": 0,
    "weeklyrainin": 0.051,
    "monthlyrainin": 1.803,
    "totalrainin": 57.902,
    "battout": 1,
    "tempinf": 68.4,
    "humidityin": 40,
    "baromrelin": 29.737,
    "baromabsin": 29.17,
    "feelsLike": 46.8,
    "dewPoint": 37.17,
    "feelsLikein": 66.8,
    "dewPointin": 43.1,
    "lastRain": "2024-12-30T16:40:00.000Z",
    "date": "2024-12-31T21:55:00.000Z"
  }
]
```

## NWS Forecast API sample response

```
{
  "@context": [
    "https://geojson.org/geojson-ld/geojson-context.jsonld",
    {
      "@version": "1.1",
      "wx": "https://api.weather.gov/ontology#",
      "geo": "http://www.opengis.net/ont/geosparql#",
      "unit": "http://codes.wmo.int/common/unit/",
      "@vocab": "https://api.weather.gov/ontology#"
    }
  ],
  "type": "Feature",
  "geometry": {
    "type": "Polygon",
    "coordinates": [
      [
        [
          -77.2626,
          43.1214
        ],
        [
          -77.2587999,
          43.1428
        ],
        [
          -77.2882,
          43.1457
        ],
        [
          -77.292,
          43.124199999999995
        ],
        [
          -77.2626,
          43.1214
        ]
      ]
    ]
  },
  "properties": {
    "units": "us",
    "forecastGenerator": "BaselineForecastGenerator",
    "generatedAt": "2025-01-05T23:02:33+00:00",
    "updateTime": "2025-01-05T20:40:16+00:00",
    "validTimes": "2025-01-05T14:00:00+00:00/P7DT14H",
    "elevation": {
      "unitCode": "wmoUnit:m",
      "value": 152.0952
    },
    "periods": [
      {
        "number": 1,
        "name": "Tonight",
        "startTime": "2025-01-05T18:00:00-05:00",
        "endTime": "2025-01-06T06:00:00-05:00",
        "isDaytime": false,
        "temperature": 19,
        "temperatureUnit": "F",
        "temperatureTrend": "",
        "probabilityOfPrecipitation": {
          "unitCode": "wmoUnit:percent",
          "value": 60
        },
        "windSpeed": "7 to 13 mph",
        "windDirection": "NW",
        "icon": "https://api.weather.gov/icons/land/night/snow,60/snow,50?size=medium",
        "shortForecast": "Snow Showers Likely",
        "detailedForecast": "Snow showers likely. Cloudy, with a low around 19. Northwest wind 7 to 13 mph. Chance of precipitation is 60%. New snow accumulation of 2 to 4 inches possible."
      },
      {
        "number": 2,
        "name": "Monday",
        "startTime": "2025-01-06T06:00:00-05:00",
        "endTime": "2025-01-06T18:00:00-05:00",
        "isDaytime": true,
        "temperature": 23,
        "temperatureUnit": "F",
        "temperatureTrend": "",
        "probabilityOfPrecipitation": {
          "unitCode": "wmoUnit:percent",
          "value": 50
        },
        "windSpeed": "8 to 12 mph",
        "windDirection": "NE",
        "icon": "https://api.weather.gov/icons/land/day/snow,50/snow,40?size=medium",
        "shortForecast": "Chance Snow Showers",
        "detailedForecast": "A chance of snow showers. Cloudy, with a high near 23. Northeast wind 8 to 12 mph. Chance of precipitation is 50%. New snow accumulation of 1 to 3 inches possible."
      },
      {
        "number": 3,
        "name": "Monday Night",
        "startTime": "2025-01-06T18:00:00-05:00",
        "endTime": "2025-01-07T06:00:00-05:00",
        "isDaytime": false,
        "temperature": 18,
        "temperatureUnit": "F",
        "temperatureTrend": "",
        "probabilityOfPrecipitation": {
          "unitCode": "wmoUnit:percent",
          "value": 50
        },
        "windSpeed": "12 to 16 mph",
        "windDirection": "NW",
        "icon": "https://api.weather.gov/icons/land/night/snow,40/snow,50?size=medium",
        "shortForecast": "Chance Snow Showers",
        "detailedForecast": "A chance of snow showers. Cloudy, with a low around 18. Northwest wind 12 to 16 mph. Chance of precipitation is 50%. New snow accumulation of 1 to 2 inches possible."
      },
      {
        "number": 4,
        "name": "Tuesday",
        "startTime": "2025-01-07T06:00:00-05:00",
        "endTime": "2025-01-07T18:00:00-05:00",
        "isDaytime": true,
        "temperature": 23,
        "temperatureUnit": "F",
        "temperatureTrend": "",
        "probabilityOfPrecipitation": {
          "unitCode": "wmoUnit:percent",
          "value": 60
        },
        "windSpeed": "16 to 20 mph",
        "windDirection": "NW",
        "icon": "https://api.weather.gov/icons/land/day/snow,60?size=medium",
        "shortForecast": "Snow Showers Likely",
        "detailedForecast": "Snow showers likely. Cloudy, with a high near 23. Northwest wind 16 to 20 mph, with gusts as high as 31 mph. Chance of precipitation is 60%. New snow accumulation of 1 to 2 inches possible."
      },
      {
        "number": 5,
        "name": "Tuesday Night",
        "startTime": "2025-01-07T18:00:00-05:00",
        "endTime": "2025-01-08T06:00:00-05:00",
        "isDaytime": false,
        "temperature": 15,
        "temperatureUnit": "F",
        "temperatureTrend": "",
        "probabilityOfPrecipitation": {
          "unitCode": "wmoUnit:percent",
          "value": 40
        },
        "windSpeed": "17 mph",
        "windDirection": "NW",
        "icon": "https://api.weather.gov/icons/land/night/snow,40?size=medium",
        "shortForecast": "Scattered Snow Showers",
        "detailedForecast": "Scattered snow showers. Cloudy, with a low around 15. Northwest wind around 17 mph, with gusts as high as 28 mph. Chance of precipitation is 40%. New snow accumulation of around one inch possible."
      },
      {
        "number": 6,
        "name": "Wednesday",
        "startTime": "2025-01-08T06:00:00-05:00",
        "endTime": "2025-01-08T18:00:00-05:00",
        "isDaytime": true,
        "temperature": 18,
        "temperatureUnit": "F",
        "temperatureTrend": "",
        "probabilityOfPrecipitation": {
          "unitCode": "wmoUnit:percent",
          "value": 40
        },
        "windSpeed": "15 mph",
        "windDirection": "NW",
        "icon": "https://api.weather.gov/icons/land/day/snow,40/snow,30?size=medium",
        "shortForecast": "Chance Snow Showers",
        "detailedForecast": "A chance of snow showers. Mostly cloudy, with a high near 18. Northwest wind around 15 mph, with gusts as high as 25 mph. Chance of precipitation is 40%. New snow accumulation of less than one inch possible."
      },
      {
        "number": 7,
        "name": "Wednesday Night",
        "startTime": "2025-01-08T18:00:00-05:00",
        "endTime": "2025-01-09T06:00:00-05:00",
        "isDaytime": false,
        "temperature": 12,
        "temperatureUnit": "F",
        "temperatureTrend": "",
        "probabilityOfPrecipitation": {
          "unitCode": "wmoUnit:percent",
          "value": 70
        },
        "windSpeed": "14 mph",
        "windDirection": "NW",
        "icon": "https://api.weather.gov/icons/land/night/snow,70?size=medium",
        "shortForecast": "Snow Showers Likely",
        "detailedForecast": "Snow showers likely. Mostly cloudy, with a low around 12. Northwest wind around 14 mph, with gusts as high as 25 mph. Chance of precipitation is 70%. New snow accumulation of around one inch possible."
      },
      {
        "number": 8,
        "name": "Thursday",
        "startTime": "2025-01-09T06:00:00-05:00",
        "endTime": "2025-01-09T18:00:00-05:00",
        "isDaytime": true,
        "temperature": 23,
        "temperatureUnit": "F",
        "temperatureTrend": "",
        "probabilityOfPrecipitation": {
          "unitCode": "wmoUnit:percent",
          "value": 60
        },
        "windSpeed": "16 mph",
        "windDirection": "NW",
        "icon": "https://api.weather.gov/icons/land/day/snow,60/snow,50?size=medium",
        "shortForecast": "Snow Showers Likely",
        "detailedForecast": "Snow showers likely. Mostly cloudy, with a high near 23. Northwest wind around 16 mph, with gusts as high as 28 mph. Chance of precipitation is 60%. New snow accumulation of less than half an inch possible."
      },
      {
        "number": 9,
        "name": "Thursday Night",
        "startTime": "2025-01-09T18:00:00-05:00",
        "endTime": "2025-01-10T06:00:00-05:00",
        "isDaytime": false,
        "temperature": 18,
        "temperatureUnit": "F",
        "temperatureTrend": "",
        "probabilityOfPrecipitation": {
          "unitCode": "wmoUnit:percent",
          "value": 40
        },
        "windSpeed": "9 to 13 mph",
        "windDirection": "NW",
        "icon": "https://api.weather.gov/icons/land/night/snow,40/bkn?size=medium",
        "shortForecast": "Chance Snow Showers then Mostly Cloudy",
        "detailedForecast": "A chance of snow showers before 7pm. Mostly cloudy, with a low around 18. Chance of precipitation is 40%."
      },
      {
        "number": 10,
        "name": "Friday",
        "startTime": "2025-01-10T06:00:00-05:00",
        "endTime": "2025-01-10T18:00:00-05:00",
        "isDaytime": true,
        "temperature": 27,
        "temperatureUnit": "F",
        "temperatureTrend": "",
        "probabilityOfPrecipitation": {
          "unitCode": "wmoUnit:percent",
          "value": null
        },
        "windSpeed": "6 to 9 mph",
        "windDirection": "W",
        "icon": "https://api.weather.gov/icons/land/day/bkn?size=medium",
        "shortForecast": "Partly Sunny",
        "detailedForecast": "Partly sunny, with a high near 27."
      },
      {
        "number": 11,
        "name": "Friday Night",
        "startTime": "2025-01-10T18:00:00-05:00",
        "endTime": "2025-01-11T06:00:00-05:00",
        "isDaytime": false,
        "temperature": 18,
        "temperatureUnit": "F",
        "temperatureTrend": "",
        "probabilityOfPrecipitation": {
          "unitCode": "wmoUnit:percent",
          "value": 40
        },
        "windSpeed": "6 mph",
        "windDirection": "SW",
        "icon": "https://api.weather.gov/icons/land/night/snow/snow,40?size=medium",
        "shortForecast": "Chance Light Snow",
        "detailedForecast": "A chance of snow after 7pm. Mostly cloudy, with a low around 18. Chance of precipitation is 40%."
      },
      {
        "number": 12,
        "name": "Saturday",
        "startTime": "2025-01-11T06:00:00-05:00",
        "endTime": "2025-01-11T18:00:00-05:00",
        "isDaytime": true,
        "temperature": 29,
        "temperatureUnit": "F",
        "temperatureTrend": "",
        "probabilityOfPrecipitation": {
          "unitCode": "wmoUnit:percent",
          "value": 60
        },
        "windSpeed": "7 mph",
        "windDirection": "SW",
        "icon": "https://api.weather.gov/icons/land/day/snow,60?size=medium",
        "shortForecast": "Light Snow Likely",
        "detailedForecast": "Snow likely. Mostly cloudy, with a high near 29. Chance of precipitation is 60%."
      },
      {
        "number": 13,
        "name": "Saturday Night",
        "startTime": "2025-01-11T18:00:00-05:00",
        "endTime": "2025-01-12T06:00:00-05:00",
        "isDaytime": false,
        "temperature": 20,
        "temperatureUnit": "F",
        "temperatureTrend": "",
        "probabilityOfPrecipitation": {
          "unitCode": "wmoUnit:percent",
          "value": 60
        },
        "windSpeed": "6 mph",
        "windDirection": "W",
        "icon": "https://api.weather.gov/icons/land/night/snow,60/snow,30?size=medium",
        "shortForecast": "Light Snow Likely",
        "detailedForecast": "Snow likely before 1am, then a slight chance of snow showers. Mostly cloudy, with a low around 20. Chance of precipitation is 60%."
      },
      {
        "number": 14,
        "name": "Sunday",
        "startTime": "2025-01-12T06:00:00-05:00",
        "endTime": "2025-01-12T18:00:00-05:00",
        "isDaytime": true,
        "temperature": 29,
        "temperatureUnit": "F",
        "temperatureTrend": "",
        "probabilityOfPrecipitation": {
          "unitCode": "wmoUnit:percent",
          "value": null
        },
        "windSpeed": "8 mph",
        "windDirection": "W",
        "icon": "https://api.weather.gov/icons/land/day/snow/bkn?size=medium",
        "shortForecast": "Slight Chance Snow Showers then Mostly Cloudy",
        "detailedForecast": "A slight chance of snow showers before 7am. Mostly cloudy, with a high near 29."
      }
    ]
  }
}
```
