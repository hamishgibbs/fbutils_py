import pandas as pd
from datetime import datetime

from fbutils import process


def aggregate_tile_movement(mob: pd.DataFrame, time_agg="daily") -> pd.DataFrame:

    if time_agg not in ["daily", "weekly"]:

        raise Exception("Unknown time_agg value {}".fomat(time_agg))

    if time_agg == 'weekly':

        mob['date_time'] = [date_to_weekly(x) for x in mob['date_time']]

    mob = (
        mob.groupby(["date_time", "journey", "start_quadkey", "end_quadkey"])
        .agg({"n_crisis": "sum", "n_baseline": "sum"})
        .reset_index()
    )

    mob = process.process_tile_movement(mob)

    return mob


def date_to_weekly(date: datetime) -> datetime:

    ref_week = date.strftime('%Y_%W') + '_1'

    ref_date = datetime.strptime(ref_week, "%Y_%W_%w")

    return(ref_date)
