from datetime import datetime
import pandas as pd


def pad_quadkey(data: pd.DataFrame, column: str, zoom_level: int):

    data[column] = [str(x).zfill(zoom_level) for x in data[column]]

    return(data)



def group_by_dict(data: pd.DataFrame, group_var: str) -> dict:
    """Return a dictionary of dataframes by grouping key.

    Args:
        data (pd.DataFrame): Input dataset.
        group_var (str): Grouping variable.

    Returns:
        dict: Dictionary of dataframes.

    """

    data = data.groupby(group_var)

    dict_keys = data.groups

    data = [data.get_group(x) for x in data.groups]

    return dict(zip(dict_keys, data))


def date_to_weekly(date: datetime) -> datetime:

    ref_week = date.strftime('%Y_%W') + '_1'

    ref_date = datetime.strptime(ref_week, "%Y_%W_%w")

    return(ref_date)


def date_to_daily(date: datetime):

    return date.replace(hour=0, minute=0)
