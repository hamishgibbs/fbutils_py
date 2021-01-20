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
