import pandas as pd
from fbutils import quadkey


def read_tile_movement(fn: str, zoom_level: int = 12) -> pd.DataFrame:
    """Read tile movement dataset.

    Will attempt to parse dates in the ['date', 'date_time'] columns.

    Args:
        fn (str): Filename.
        zoom_level (int): Intended zoom_level.

    Returns:
        pd.DataFrame: Formatted movement data.

    """
    try:

        mob = pd.read_csv(fn, parse_dates=['date'])

    except Exception:

        pass

    try:

        mob = pd.read_csv(fn, parse_dates=['date_time'])

    except Exception:

        pass

    # Pad start and end quadkeys at the intended zoom level
    mob['start_quadkey'] = [quadkey.pad_quadkey(x, zoom_level) for x in
                            mob['start_quadkey']]

    mob['end_quadkey'] = [quadkey.pad_quadkey(x, zoom_level) for x in
                          mob['end_quadkey']]

    return(mob)
