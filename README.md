# aggregation_examples

### 1. python + pandas
Python 3.8.3 was used

#### install virtual env
    pip install virtualenv
    virtualenv venv --python=python3.8

#### init virtual env & install requeriments
    source venv/bin/activate
    pip install -r requirements.txt

#### run script & tests
    python src/deduplicate.py
    pytest tests

### 2. great amount of data: pyspark

#### docker build
    docker build (https://github.com/cesarcharallaolazo/docker_spark_submit/blob/main/v23_Dockerfile_pyspark_py3_spk3) -t pyspark3_sub 

#### docker run
    docker run --name spark_submit_run_aggregation_examples -v /Users/user/Documents/docs_cesar/other_repos/aggregation_examples:/home/jovyan/SparkProjects/Project1/ pyspark3_sub