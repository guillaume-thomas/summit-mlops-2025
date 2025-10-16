import logging

import fire
import joblib
import pandas as pd
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score, median_absolute_error
import mlflow
from mlflow.models import infer_signature

client = mlflow.MlflowClient()

def validate(model_path: str, x_test_path: str, y_test_path: str) -> None:
    logging.warning(f"validate {model_path}")
    model = joblib.load(client.download_artifacts(run_id=mlflow.active_run().info.run_id, path=model_path))

    x_test = pd.read_csv(client.download_artifacts(run_id=mlflow.active_run().info.run_id, path=x_test_path), index_col=False)
    y_test = pd.read_csv(client.download_artifacts(run_id=mlflow.active_run().info.run_id, path=y_test_path), index_col=False)

    if y_test.shape[1] == 1:
        y_test = y_test.iloc[:, 0]

    y_pred = model.predict(x_test)

    mse = mean_squared_error(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    medae = median_absolute_error(y_test, y_pred)

    # feature importance
    feature_names = x_test.columns.tolist()
    coefs = model.coef_

    if hasattr(coefs, 'shape') and len(coefs.shape) > 1:
        coefs = coefs[0]
    feature_importance = {name: float(coef) for name, coef in zip(feature_names, coefs)}

    mlflow.log_metric("mse", mse)
    mlflow.log_metric("mae", mae)
    mlflow.log_metric("r2", r2)
    mlflow.log_metric("medae", medae)
    mlflow.log_dict(feature_importance, "feature_importance.json")

    model_info = mlflow.sklearn.log_model(model,
                                          name="model_final",
                                          signature=infer_signature(x_test, y_pred),
                                          input_example=x_test.head(10))
    logging.warning(f"artifact path {model_info.artifact_path}")
    logging.warning(f"model uri {model_info.model_uri}")
    logging.warning(f"model uuid {model_info.model_uuid}")
    logging.warning(f"model metadata {model_info.metadata}")

    try:
        mlflow.register_model(model_info.model_uri, "model_registered")
    except Exception as e:
        logging.error(f"Erreur registry: {e}")



if __name__ == "__main__":
    fire.Fire(validate)