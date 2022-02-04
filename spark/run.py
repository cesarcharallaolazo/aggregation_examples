import argparse

from pyspark import SparkContext
from pyspark.sql import SparkSession
from pyspark.sql.types import *
from pyspark.sql.functions import *
from utils.constant import *


def parse_cli_args():
    """
    Parse cli arguments
    returns a dictionary of arguments
    """
    parser = argparse.ArgumentParser()

    parser.add_argument('--root_path', action='store', dest=root_path, type=str,
                        help='Store', default=None)

    parser.add_argument('--checkpoint_path', action='store', dest=checkpoint_path, type=str,
                        help='Store', default=None)

    known_args, unknown_args = parser.parse_known_args()
    known_args_dict = vars(known_args)
    return known_args_dict


if __name__ == '__main__':
    args = parse_cli_args()

    # Start Spark Environment
    spark = SparkSession.builder.getOrCreate()
    sc = SparkContext.getOrCreate()
    sc.setCheckpointDir(args[checkpoint_path])

    try:

        df = spark.read.option("sep", ",") \
            .csv(args[root_path] + 'query_result_2021-11-25T16_27_02.44381Z.csv',
                 header=True)

        df = df.groupBy("latitude", "longitude", "superficie_total_m2",
                        "superficie_util_m2", "price_uf",
                        "parking", "origin").count()

        pivotDF = df.groupBy("latitude", "longitude", "superficie_total_m2",
                             "superficie_util_m2", "price_uf", "parking") \
            .pivot("origin").agg(first("count")).fillna(0)

        pivotDF.show(100)

    except Exception as e:
        print("PYSPARK ERROR !")
        print(e.args)
