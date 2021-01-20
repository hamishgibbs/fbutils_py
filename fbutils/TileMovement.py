import pandas as pd
from fbutils.utils import pad_quadkey, date_to_daily, date_to_weekly

def read(fn, zoom_level=12):

    data = pd.read_csv(fn)

    data = pad_quadkey(data, 'start_quadkey', zoom_level)
    data = pad_quadkey(data, 'end_quadkey', zoom_level)

    return data


def define_journey(data: pd.DataFrame):

    data["journey"] = data["start_quadkey"] + "_" + data["end_quadkey"]

    return data


def define_perc_change(data: pd.DataFrame):

    data["perc_change"] = (
        (data["n_crisis"] - data["n_baseline"]) / data["n_baseline"]
    ) * 100

    return data

def filter_country(data: pd.DataFrame, country: str):

    return data[data['country'] == country]


def aggregate_time(data: pd.DataFrame, type: str):

    try:

        assert type in ['daily', 'weekly']

    except AssertionError:

        raise ValueError('Unknown aggregation type %s'.format(type))

    if type == 'daily':

        data['date_time'] = [date_to_daily(x) for x in data['date_time']]

    if type == 'weekly':

        data['date_time'] = [date_to_weekly(x) for x in data['date_time']]

    data = (
        data.groupby(["date_time", "journey", "start_quadkey", "end_quadkey"])
        .agg({"n_crisis": "sum", "n_baseline": "sum"})
        .reset_index()
    )

    return data
