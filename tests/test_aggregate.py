import pytest
import pandas as pd

from fbutils import aggregate


@pytest.fixture
def default_time_movement():

    mob = pd.DataFrame({
        'date_time': ['1', '1', '3'],
        'start_quadkey': ['1', '1', '3'],
        'end_quadkey': ['1', '1', '3'],
        'journey': ['1_1', '1_1', '3_3'],
        'n_crisis': [1, 2, 3],
        'n_baseline': [2, 2, 3]
    })

    return mob


def test_aggregate_tile_movement_columns(default_time_movement):

    res = aggregate.aggregate_tile_movement(default_time_movement)

    assert 'perc_change' in res.columns


def test_aggregate_tile_movement_records(default_time_movement):

    res = aggregate.aggregate_tile_movement(default_time_movement)

    assert len(res.index) == 2


def test_aggregate_tile_movement_errors(default_time_movement):

    with pytest.raises(Exception):
        aggregate.aggregate_tile_movement(default_time_movement, 'anything')
