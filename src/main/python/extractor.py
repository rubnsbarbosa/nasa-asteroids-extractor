import datetime
import requests
from gcp_utils import access_secret
from config import GCPConfig
from logging_utils import LoggingUtils

log = LoggingUtils.config_logger(__name__)


def asteroids_extractor():
    """
    Extract JSON information about asteroids near earth from NASA data source API
    """
    conf = GCPConfig
    api_key = access_secret(conf.gcp_project_id, conf.gcp_secret_id)

    try:
        log.info("extracting asteroids data from NASA API")
        today = datetime.date.today()
        tomorrow = datetime.date.today() + datetime.timedelta(days=1)

        url = f"https://api.nasa.gov/neo/rest/v1/feed?start_date={today}&end_date={tomorrow}&api_key={api_key}"
        response = requests.get(url)
        data = response.json()

        return data

    except requests.JSONDecodeError as e:
        raise Exception(f"Extracting asteroids data failed due to: {e}")
