from shapely.geometry import Point, Polygon

from fbutils import quadkey


def test_pad_quadkey():
    """Test that pad_quadkey returns an appropriate length string"""

    qk = "123"

    zoom_level = 12

    res = quadkey.pad_quadkey(qk, zoom_level)

    assert len(res) == zoom_level


def test_tile_polygon():
    """Test that tile_polygon returns a shapely Polygon"""

    qk = "0333311100101"

    res = quadkey.tile_polygon(qk)

    assert type(res) is Polygon


def test_tile_point():
    """Test that tile_centroid returns a shapely Point"""

    qk = "0333311100101"

    res = quadkey.tile_centroid(qk)

    assert type(res) is Point
