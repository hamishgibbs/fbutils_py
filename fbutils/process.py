import pandas as pd


def process_tile_movement(mob: pd.DataFrame) -> pd.DataFrame:
    """Apply basic processing steps to Tile Movement dataset.

    1. Define a journey column.
    2. Define percent change from baseline.

    Args:
        mob (pd.DataFrame): Input movement data.

    Returns:
        pd.DataFrame: Processed movement data.

    """

    # Create journey column from start_quadkey and end_quadkey columns
    mob['journey'] = mob['start_quadkey'] + '_' + mob['end_quadkey']

    # Define percent change from baseline for each period
    mob['perc_change'] = ((mob['n_crisis'] - mob['n_baseline'])
                          / mob['n_baseline']) * 100

    return mob
