import pandas as pd
from fbutils import process


def aggregate_tile_movement(mob: pd.DataFrame, time_agg='daily') -> pd.DataFrame:

    if time_agg not in ['daily']:

        raise Exception('Unknown time_agg value {}'.fomat(time_agg))

    mob = mob.groupby(['date_time',
                       'journey',
                       'start_quadkey',
                       'end_quadkey']) \
            .agg({'n_crisis': 'sum', 'n_baseline': 'sum'}) \
            .reset_index()

    mob = process.process_tile_movement(mob)

    return mob
