build:
	cp ./spark/run.py ./target
	cd ./spark && zip -x run.py -r ../target/spark.zip .
