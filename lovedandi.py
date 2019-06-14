
import requests
from requests import get


# api-endpoint
URL = "https://api.openaq.org/v1/cities"


r = requests.get(URL)

# r.status_code
# r.body
# r.json()

print(r.json())





# ----------------------------- # -----------------------------
# response = unirest.get("https://national-weather-service.p.rapidapi.com/alerts",
#                        headers={
#                            "X-RapidAPI-Host": "national-weather-service.p.rapidapi.com",
#                            "X-RapidAPI-Key": "3c35e517bemsh658fc591678c4bap1e0827jsn102fc3b149c4"
#                        }
#                        )

# ----------------------------- # -----------------------------
# PARAMS = {'address': location}
# ----------------------------- # -----------------------------
