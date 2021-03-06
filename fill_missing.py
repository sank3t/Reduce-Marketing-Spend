import re


def check_case(name):
    chars_hindi = [chr(c) for c in range(0x0900, 0x097f)]
    hindi_regex = '|'.join(chars_hindi)

    try:
        if (len(re.findall(hindi_regex, name)) > 0) or (name.islower()):
            return True
        else:
            return False
    except TypeError:
        pass


def fill_geography(flag):
    if flag:
        return 'India'
    else:
        return 'USA'


def fill_deal_value(df, df_proba):
    imputed_values = []

    for index, row in df.iterrows():
        proba_filter = (df_proba['industry'] == row['industry']) & (df_proba['pitch'] == row['pitch'])
        probability = df_proba.loc[proba_filter, 'median'].values[0]
        imputed_values.append(row['weighted_amount'] / probability)

    return imputed_values

