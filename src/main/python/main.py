import os
from extractor import asteroids_extractor
from transform import transforming_asteroids
from gcp_utils import (
    upload_file_to_bucket,
    load_to_bigquery_from_cloud_storage
)
from config import GCPConfig
from config import (
    schema_nasa_asteroid_data,
    nasa_csv_file_path,
    filename
)
from logging_utils import LoggingUtils

log = LoggingUtils.config_logger(__name__)


if __name__ == "__main__":
    conf = GCPConfig

    data = asteroids_extractor()
    transforming_asteroids(data)

    upload_file_to_bucket(conf.gcp_bucket_name, nasa_csv_file_path, filename)
    load_to_bigquery_from_cloud_storage(conf.gcp_bucket_name, filename, conf.gcp_bq_table_id, schema_nasa_asteroid_data)
    os.remove(f"{conf.gcp_dataset_path}/{filename}")

    log.info("done")
