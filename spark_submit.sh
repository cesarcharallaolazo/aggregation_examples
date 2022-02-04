make build &&\
cd target &&\

spark_submit_cmd="spark-submit --master local[*] --deploy-mode client --py-files spark.zip run.py --root_path /home/jovyan/SparkProjects/Project1/data/ --checkpoint_path /home/jovyan/SparkProjects/Project1/data/checkpoints/"
eval $spark_submit_cmd
