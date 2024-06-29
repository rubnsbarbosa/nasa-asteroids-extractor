import os
import datetime

from google.cloud import bigquery

today = datetime.date.today()
filename = f"asteroids-{today}.csv"

nasa_csv_file_path = "nasa_asteroids_data"
if not os.path.exists(nasa_csv_file_path):
    os.makedirs(nasa_csv_file_path)


schema_nasa_asteroid_data = [
    bigquery.SchemaField(name="id", field_type="STRING", mode="REQUIRED"),
    bigquery.SchemaField(name="name", field_type="STRING", mode="REQUIRED"),
    bigquery.SchemaField(name="magnitude", field_type="STRING", mode="REQUIRED"),
    bigquery.SchemaField(name="min_diameter_estimated", field_type="FLOAT", mode="REQUIRED"),
    bigquery.SchemaField(name="max_diameter_estimated", field_type="FLOAT", mode="REQUIRED"),
    bigquery.SchemaField(name="is_hazardous", field_type="BOOLEAN", mode="REQUIRED"),
]


class GCPConfig:
    gcp_dataset_path = os.getenv("NASA_DATASET_PATH")
    gcp_project_id = "de-ru-data-engineering"
    gcp_secret_id = "nasa-api-key"
    gcp_bucket_name = "de-bu-nasa-asteroids"
    gcp_bq_table_id = "de-ru-data-engineering.asteroids.near_asteroids"
