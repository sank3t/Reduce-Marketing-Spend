def missing_value_stats(df):
    num_rows = df.shape[0]
    # Missing value count by columns
    df_missing = df.isna().sum().reset_index()
    # Renaming columns
    df_missing.columns = ['column', 'missing_values']
    # Getting only those columns having missing values > 0
    df_missing = df_missing[df_missing['missing_values'] > 0]
    df_missing.reset_index(drop=True, inplace=True)
    # Calculating percentage of missing
    df_missing['missing_percentage'] = df_missing['missing_values'].apply(
        lambda missing_value: round((missing_value / num_rows) * 100, 2)
    )
    return df_missing


def unique_value_stats(df):
    df_unique = df.agg(['nunique']).transpose().reset_index()
    df_unique.columns = ['column', 'unique_value_count']
    return df_unique


def discard_columns(df, df_nunique):
    discard_filter = df_nunique['unique_value_count'] == df.shape[0]
    discard_cols = df_nunique.loc[discard_filter, 'column'].tolist()
    return discard_cols
