import pandas as pd
from fbutils import TileMovement
import pytest
from datetime import datetime

@pytest.fixture
def default_time_movement():

    mob = pd.DataFrame(
        {
            "date_time": [datetime(2020, 1, 1, 0),
                          datetime(2020, 1, 1, 8),
                          datetime(2020, 1, 1, 16)],
            "start_quadkey": ["1", "1", "1"],
            "end_quadkey": ["1", "1", "1"],
            "journey": ["1_1", "1_1", "1_1"],
            "n_crisis": [1, 2, 3],
            "n_baseline": [2, 2, 3],
        }
    )

    return mob


@pytest.fixture(scope="session")
def tmp_dir(tmpdir_factory):

    path = tmpdir_factory.mktemp("tmp")

    return str(path)

def test_read(tmp_dir):

    data = pd.DataFrame({'start_quadkey': ['1', '2', '3'],
                         'end_quadkey': ['1', '2', '3']})

    fn = 'test.csv'

    data.to_csv(fn)

    res = TileMovement.read(fn, zoom_level = 5)

    assert type(res) is pd.DataFrame
    assert res.loc[0, 'start_quadkey'] == '00001'

def test_define_journey():

    data = pd.DataFrame({'start_quadkey': ['1', '2', '3'],
                         'end_quadkey': ['1', '2', '3']})

    res = TileMovement.define_journey(data)

    assert 'journey' in res.columns
    assert res.loc[0, 'journey'] == '1_1'


def test_define_perc_change():

    data = pd.DataFrame({'n_crisis': [1],
                        'n_baseline': [2]})

    res = TileMovement.define_perc_change(data)

    assert 'perc_change' in res.columns
    assert res.loc[0, 'perc_change'] == -50


def test_filter_country():

    data = pd.DataFrame({'country': ['GB', 'GB', 'USA']})

    res = TileMovement.filter_country(data, 'GB')

    assert len(res.index) == 2
    assert res['country'].unique() == 'GB'


def test_aggregate_raises(default_time_movement):

    with pytest.raises(ValueError):
        TileMovement.aggregate_time(default_time_movement, 'other')


def test_aggregate(default_time_movement):

    res = TileMovement.aggregate_time(default_time_movement, 'daily')

    assert len(res.index) == 1
