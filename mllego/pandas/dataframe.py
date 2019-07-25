def crossjoin(df1, df2):
    df1["_tmpcol"] = 1
    df2["_tmpcol"] = 1
    result_df = df1.merge(df2, on="_tmpcol")
    result_df.drop(columns=["_tmpcol"])
    return result_df
