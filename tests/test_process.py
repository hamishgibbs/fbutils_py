import pytest
import pandas as pd
from fbutils import process


@pytest.fixture
def default_time_movement():

    mob = pd.DataFrame({
        'start_quadkey': ['1', '2', '3'],
        'end_quadkey': ['1', '2', '3'],
        'n_crisis': [1, 2, 3],
        'n_baseline': [2, 2, 3]
    })

    return mob


def test_process_tile_movement_journey(default_time_movement):

    res = process.process_tile_movement(default_time_movement)

    assert 'journey' in res.columns


def test_process_tile_movement_perc_change(default_time_movement):

    res = process.process_tile_movement(default_time_movement)

    assert 'perc_change' in res.columns


def test_process_tile_movement_perc_change_val(default_time_movement):

    res = process.process_tile_movement(default_time_movement)

    assert res['perc_change'][0] == -50
