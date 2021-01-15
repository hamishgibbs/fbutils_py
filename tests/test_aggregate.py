import pandas as pd
import pytest
from datetime import datetime

from fbutils import aggregate


@pytest.fixture
def default_time_movement():

    mob = pd.DataFrame(
        {
            "date_time": ["1", "1", "3"],
            "start_quadkey": ["1", "1", "3"],
            "end_quadkey": ["1", "1", "3"],
            "journey": ["1_1", "1_1", "3_3"],
            "n_crisis": [1, 2, 3],
            "n_baseline": [2, 2, 3],
        }
    )

    return mob


@pytest.fixture
def default_daily_movement():

    mob = pd.DataFrame(
        {
            "date_time": [datetime(2020, 3, 10),
                          datetime(2020, 3, 11),
                          datetime(2020, 3, 12)],
            "start_quadkey": ["1", "1", "1"],
            "end_quadkey": ["1", "1", "1"],
            "journey": ["1_1", "1_1", "1_1"],
            "n_crisis": [1, 2, 3],
            "n_baseline": [2, 2, 3],
        }
    )

    return mob


def test_aggregate_tile_movement_columns(default_time_movement):

    res = aggregate.aggregate_tile_movement(default_time_movement, time_agg='daily')

    assert "perc_change" in res.columns


def test_aggregate_tile_movement_records(default_time_movement):

    res = aggregate.aggregate_tile_movement(default_time_movement, time_agg='daily')

    assert len(res.index) == 2


def test_aggregate_tile_movement_errors(default_time_movement):

    with pytest.raises(Exception):
        aggregate.aggregate_tile_movement(default_time_movement, "anything")


def test_aggregate_tile_movement_weekly(default_daily_movement):

    res = aggregate.aggregate_tile_movement(default_daily_movement, time_agg='weekly')

    print(res)

    assert len(res.index) == 1


def test_date_to_weekly():

    date = datetime(2020, 3, 10)

    res = aggregate.date_to_weekly(date)

    assert res == datetime(2020, 3, 9)
