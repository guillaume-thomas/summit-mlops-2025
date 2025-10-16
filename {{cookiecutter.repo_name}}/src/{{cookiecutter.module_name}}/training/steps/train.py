import logging
import os

import fire
import joblib
import mlflow.sklearn
import pandas
from sklearn import linear_model

client = mlflow.MlflowClient()

ARTIFACT_PATH = "model_trained"

def train(x_train_path: str, y_train_path: str) -> str:
    logging.warning(f"train {x_train_path} {y_train_path}")
    x_train = pandas.read_csv(client.download_artifacts(run_id=mlflow.active_run().info.run_id, path=x_train_path), index_col=False)
    y_train = pandas.read_csv(client.download_artifacts(run_id=mlflow.active_run().info.run_id, path=y_train_path), index_col=False)

    model = linear_model.LinearRegression()
    model.fit(x_train, y_train)

    model_filename = "model.joblib"
    model_path = "./" + model_filename

    joblib.dump(model, model_path)
    mlflow.log_artifact(model_path, ARTIFACT_PATH)

    os.remove(model_path)

    return f"{ARTIFACT_PATH}/{model_filename}"



if __name__ == "__main__":
    fire.Fire(train)