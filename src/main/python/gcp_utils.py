from google.cloud import storage, bigquery, secretmanager
from logging_utils import LoggingUtils

log = LoggingUtils.config_logger(__name__)


def upload_file_to_bucket(bucket_name, source_file_path, filename):
    """
    Uploads a csv file to the bucket.

    :param bucket_name: The id of your GCS bucket
    :param source_file_path: The path to your file to upload
    :param filename: The filename to upload
    """

    log.info("uploading a file to the bucket")
    client = storage.Client()
    log.info("get the bucket")
    bucket = client.bucket(bucket_name)
    log.info("create a new blob and upload the files content")
    blob = bucket.blob(filename)
    with open(f"{source_file_path}/{filename}", "rb") as file:
        blob.upload_from_file(file)

    log.info(f"{filename} successfully uploaded to {bucket_name}")


def access_secret(project_id, secret_id, version_id="latest"):
    """
    Access a secret NASA API token stored in Secret Manager

    :param project_id: The unique identifier of Google Cloud project
    :param secret_id: The secret id created in Google Cloud Secret Manager
    :param version_id: The unique identifier for a specific version of a secret
    """

    client = secretmanager.SecretManagerServiceClient()
    name = f"projects/{project_id}/secrets/{secret_id}/versions/{version_id}"
    response = client.access_secret_version(request={"name": name})
    return response.payload.data.decode("UTF-8")


def load_to_bigquery_from_cloud_storage(bucket_name, filename, table_id, schema_nasa_bigquery):
    log.info(f"loading {filename} from {bucket_name} to bigquery")

    client = bigquery.Client()

    job_config = bigquery.LoadJobConfig(
        source_format=bigquery.SourceFormat.CSV,
        schema=schema_nasa_bigquery,
        skip_leading_rows=1,
        autodetect=True,
        ignore_unknown_values=True,
    )

    gcs_uri = f"gs://{bucket_name}/{filename}"

    load_job = client.load_table_from_uri(
        gcs_uri, table_id, job_config=job_config
    )

    load_job.result()  # waits for the load job to finish
    destination_table = client.get_table(table_id)
    log.info(f"asteroids data uploaded to bigquery {destination_table}")
