from fbutils import path
from datetime import datetime


def test_get_file_dates_dates():

    files = ['2020_01_02_0000.csv', '2020_01_02_0800.csv']

    res = path.get_file_dates(files)

    assert type(res[0]) is datetime
