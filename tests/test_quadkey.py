import quadkey
import shapely

class Test_tile_polygon:

    def test_tile_polygon(self):
        '''Test that tile_polygon returns a shapely polygon'''

        qk = "0333311100101"

        res = quadkey.tile_polygon(qk)

        assert type(res) is shapely.geometry.polygon.Polygon

class Test_tile_centroid:

    def test_tile_polygon(self):
        '''Test that tile_centroid returns a shapely point'''

        qk = "0333311100101"

        res = quadkey.tile_centroid(qk)

        assert type(res) is shapely.geometry.point.Point
