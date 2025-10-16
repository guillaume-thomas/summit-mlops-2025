import logging

import fire
import mlflow
from mlflow.entities import Run


def get_last_model_uri(experiment_name: str) -> str:
    logging.warning(f"experiment_name: {experiment_name}")
    current_experiment = dict(mlflow.get_experiment_by_name(experiment_name))
    experiment_id = current_experiment['experiment_id']
    runs: list[Run] = mlflow.search_runs([experiment_id],
                                         filter_string="attributes.status = 'FINISHED'",
                                         max_results=1,
                                         order_by=["attributes.end_time DESC"],
                                         output_format="list")
    run = mlflow.get_run(runs[0].info.run_id)
    logging.warning(f"Found model id: {run.outputs.model_outputs[0].model_id}")
    model_uri = f"models:/{run.outputs.model_outputs[0].model_id}"
    logging.warning(f"Returning: {model_uri}")
    return model_uri

if __name__ == "__main__":
    fire.Fire(get_last_model_uri)