def set_identifier(df):
    df = df.reset_index().rename({"index": "asset_id"}, axis=1)
    return df
