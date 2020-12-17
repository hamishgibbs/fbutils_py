import pytest
import pandas as pd
from fbutils import utils


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


def test_group_by_dict_type(default_time_movement):

    res = utils.group_by_dict(default_time_movement, 'date_time')

    assert type(res) is dict


def test_group_by_dict_len(default_time_movement):

    res = utils.group_by_dict(default_time_movement, 'date_time')

    assert len(res) == 2
