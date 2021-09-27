from decouple import config

TOKEN = config("VK_API_TOKEN", default="VK_API_TOKEN")
GROUP_ID = config("GROUP_ID", default="GROUP_ID")
WEATHER = config("OPEN_WEATHER_API_TOKEN", default="OPEN_WEATHER_API_TOKEN")
