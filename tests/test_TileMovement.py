import pandas as pd
from fbutils import TileMovement
import pytest

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
