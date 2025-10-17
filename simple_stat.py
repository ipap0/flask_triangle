from statistics import mean

from triangle_dba import get_triangles


def get_stat():
    triangles =[t[0] for t in get_triangles()]
    avg_p = mean([t.perimeter() for t in triangles])
    avg_s = mean([t.area() for t in triangles])
    stat = {'avg_p':avg_p, 'avg_s':avg_s}
    return stat