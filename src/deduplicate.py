import logging
import pandas as pd

from pandas.errors import EmptyDataError
from utils import set_identifier

if __name__ == "__main__":
    try:
        # read csv
        df = pd.read_csv("./data/query_result_2021-11-25T16_27_02.44381Z.csv")

        # aggregate by asset identifier columns
        df_agg = df.groupby(["latitude", "longitude", "superficie_total_m2",
                             "superficie_util_m2", "price_uf",
                             "parking", "origin"]).size().reset_index().rename(columns={0: "count"})

        # pivot by origin column (web portal)
        df_final = df_agg.pivot_table(index=["latitude", "longitude", "superficie_total_m2",
                                             "superficie_util_m2", "price_uf", "parking"], columns='origin',
                                      values='count', aggfunc='first', fill_value=0).reset_index()

        # set an asset identifier
        df_final = set_identifier(df_final)

        print(df_final, flush=True)
    except FileNotFoundError:
        logging.warning("The is not present !")
    except KeyError as err:
        logging.warning(f"Key not encountered --> {err.args[0]}, verify !")
    except EmptyDataError:
        logging.warning("Empty Dataframe ! Verify the file")
