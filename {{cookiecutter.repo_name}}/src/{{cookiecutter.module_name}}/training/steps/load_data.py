import logging
import os
from pathlib import Path

import boto3
import fire
import mlflow

ARTIFACT_PATH = "path_output"
LOCAL_PATH = "./data.csv"

def load_data(path: str) -> str:
    logging.warning(f"load_data on path : {path}")

    s3_client = boto3.client(
        "s3",
        endpoint_url=os.environ.get("MLFLOW_S3_ENDPOINT_URL"),
        aws_access_key_id=os.environ.get("AWS_ACCESS_KEY_ID"),
        aws_secret_access_key=os.environ.get("AWS_SECRET_ACCESS_KEY")
    )

    s3_client.download_file("summit", path, LOCAL_PATH)
    p = Path(LOCAL_PATH)
    mlflow.log_artifact(p.name, ARTIFACT_PATH)

    os.remove(LOCAL_PATH)

    return f"{ARTIFACT_PATH}/{p.name}"


if __name__ == "__main__":
    fire.Fire(load_data)
