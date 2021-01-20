import pandas as pd
from fbutils.utils import pad_quadkey

def read(fn, zoom_level=12):

    data = pd.read_csv(fn)

    data = pad_quadkey(data, 'start_quadkey', zoom_level)
    data = pad_quadkey(data, 'end_quadkey', zoom_level)

    return data


def define_journey(data: pd.DataFrame):

    data["journey"] = data["start_quadkey"] + "_" + data["end_quadkey"]

    return data


def define_perc_change(data: pd.DataFrame):

    mob["perc_change"] = (
        (mob["n_crisis"] - mob["n_baseline"]) / mob["n_baseline"]
    ) * 100

    return data
