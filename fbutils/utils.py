import pandas as pd


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
