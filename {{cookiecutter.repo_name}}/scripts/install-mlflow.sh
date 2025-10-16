echo Install summit-mlflow
oc apply -f k8s/mlflow/minio.yml
oc apply -f k8s/mlflow/mysql.yml
oc apply -f k8s/mlflow/mlflow.yml
oc apply -f k8s/mlflow/dailyclean.yml
oc label deployment dailyclean-api axa.com/dailyclean=false
oc label statefulset mysql axa.com/dailyclean=true