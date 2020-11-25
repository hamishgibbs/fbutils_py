from pyquadkey2 import quadkey
from shapely.geometry import Polygon


def tile_polygon(qk: str):
    '''Function to return a boundary polygon given a quadkey'''

    qk = quadkey.QuadKey(str(qk))

    a1 = qk.to_geo(anchor=1)
    a2 = qk.to_geo(anchor=2)
    a3 = qk.to_geo(anchor=3)
    a4 = qk.to_geo(anchor=5)

    bottom_l = [a1[1], a1[0]]
    bottom_r = [a4[1], a4[0]]
    top_l = [a3[1], a3[0]]
    top_r = [a2[1], a2[0]]

    return(Polygon([bottom_l, bottom_r, top_r, top_l]))


def tile_centroid(qk: str):
    '''Function to return a centroid given a quadkey'''

    p = tile_polygon(qk).centroid

    return(p)
