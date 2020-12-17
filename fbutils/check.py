import sys
import pandas as pd


def check_date_sequence(obs_dates: list, freq: str = '8H') -> None:
    """Check for missing dates given a certain frequency.

    If check fails - prompts user to exit.

    Args:
        obs_dates (list): Observed dates.
        freq (str): Expected frequency. Passed to pandas.date_range.

    Returns:
        None

    """

    exp_dates = pd.date_range(min(obs_dates), max(obs_dates), freq=freq) \
                  .tolist()

    missing_dates = set(exp_dates).difference(set(obs_dates))

    n_missing = len(missing_dates)

    if n_missing > 0:

        print('Missing {} dates in the data collection.'.format(n_missing))
        resp = input('Do you want to proceed? (y/n)')

        if resp != 'y':

            print('Aborting!')
            sys.exit()

    return None
