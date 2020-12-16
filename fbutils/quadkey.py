from pyquadkey2 import quadkey
from shapely.geometry import Point, Polygon


def tile_polygon(qk: str) -> Polygon:
    """Return a bounding polygon given a quadkey.

    Args:
        qk (str): Quadkey.

    Returns:
        Polygon: Bounding polygon.

    """

    # Convert quadkey str to quadkey object
    qk = quadkey.QuadKey(str(qk))

    # Extract corners of bounding polygon
    a1 = qk.to_geo(anchor=1)
    a2 = qk.to_geo(anchor=2)
    a3 = qk.to_geo(anchor=3)
    a4 = qk.to_geo(anchor=5)

    # Define conrner coordinates of bounding polygon
    bottom_l = [a1[1], a1[0]]
    bottom_r = [a4[1], a4[0]]
    top_l = [a3[1], a3[0]]
    top_r = [a2[1], a2[0]]

    # Return polygon of coordinates
    return Polygon([bottom_l, bottom_r, top_r, top_l])


def tile_centroid(qk: str) -> Point:
    """Return a centroid given a quadkey.

    Args:
        qk (str): Quadkey.

    Returns:
        Point: Polygon centroid.

    """

    # Extract centroid from polygon
    return tile_polygon(qk).centroid
