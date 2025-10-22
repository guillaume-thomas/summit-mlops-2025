echo Uninstall summit-mlflow
oc delete -f k8s/mlflow/minio.yml
oc delete -f k8s/mlflow/mysql.yml
oc delete -f k8s/mlflow/mlflow.yml
oc delete -f k8s/mlflow/dailyclean.yml
oc delete -f k8s/api/api.yaml