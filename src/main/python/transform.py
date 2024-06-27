import csv
import datetime
from logging_utils import LoggingUtils

log = LoggingUtils.config_logger(__name__)


def transforming_asteroids(data):
    log.info("transforming asteroids json data near earth...")
    today = datetime.date.today()

    near_objects = {}
    if isinstance(data, dict):
        for key, value in data.items():
            if key == "near_earth_objects":
                near_objects = value

    near_objects_content = {}
    if isinstance(near_objects, dict):
        for value in near_objects.values():
            # example of keys: 2024-06-23, 2024-06-22
            near_objects_content = value

    with open(f"nasa_asteroids_data/asteroids-{today}.csv", mode="w", newline="") as file:
        writer = csv.writer(file)

        for asteroid in near_objects_content:
            writer.writerow([asteroid["id"], asteroid["name"], asteroid["absolute_magnitude_h"],
                             asteroid["estimated_diameter"]["meters"]["estimated_diameter_min"],
                             asteroid["estimated_diameter"]["meters"]["estimated_diameter_max"],
                             asteroid["is_potentially_hazardous_asteroid"]
                             ])
