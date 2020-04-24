import numpy as np

def haversine_distance(loc_ini, loc_end):
    lon1, lat1, lon2, lat2 = map(np.radians,
            [loc_ini[0], loc_ini[1],
            loc_end[0], loc_end[1]])

    delta_lon = lon2 - lon1
    delta_lat = lat2 - lat1

    a = np.square(np.sin(delta_lat / 2.0)) + \
        np.cos(lat1) * np.cos(lat2) * np.square(np.sin(delta_lon / 2.0))

    c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1.0 - a))
    meters = 6371000.0 * c
    return meters
