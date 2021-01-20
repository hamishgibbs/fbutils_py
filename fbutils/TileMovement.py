import pandas as pd
from fbutils.utils import pad_quadkey

def read(fn, zoom_level=12):

    data = pd.read_csv(fn)

    data = pad_quadkey(data, 'start_quadkey', zoom_level)
    data = pad_quadkey(data, 'end_quadkey', zoom_level)

    return data
