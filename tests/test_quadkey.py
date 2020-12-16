from shapely.geometry import Point, Polygon

from fbutils import quadkey


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
