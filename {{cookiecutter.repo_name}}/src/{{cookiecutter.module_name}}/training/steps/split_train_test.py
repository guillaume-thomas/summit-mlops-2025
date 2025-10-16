import logging
import os
from typing import Tuple

import fire
import mlflow
import pandas as pd
import sklearn.model_selection

client = mlflow.MlflowClient()

def split_train_test(data_path: str) -> Tuple[str, str, str, str]:
    logging.warning(f"split on {data_path}")

    df = pd.read_csv(client.download_artifacts(run_id=mlflow.active_run().info.run_id, path=data_path), index_col=False)

    y = df["target"]
    x = df.drop(columns="target")
    x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size=0.3, random_state=42)

    datasets = [
        (x_train, "xtrain", "xtrain.csv"),
        (x_test, "xtest", "xtest.csv"),
        (y_train, "ytrain", "ytrain.csv"),
        (y_test, "ytest", "ytest.csv")
    ]

    artifact_paths = []
    for data, artifact_path, filename in datasets:
        data.to_csv(filename, index=False)
        mlflow.log_artifact(filename, artifact_path)
        os.remove(filename)
        artifact_paths.append(f"{artifact_path}/{filename}")

    return tuple(artifact_paths)

if __name__ == "__main__":
    fire.Fire(split_train_test)