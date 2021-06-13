from math import radians, sin, cos, sqrt, asin

def haversine(lat1, lon1, lat2, lon2, codigo):
    dLat = radians(lat2 - lat1)
    dLon = radians(lon2 - lon1)
    lat2 = radians(lat2)
    lat1 = radians(lat1)
    
    R = 6372.8  # Earth radius in kilometers
    
    a = sin(dLat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dLon / 2) ** 2
    c = 2 * asin(sqrt(a))
    
    aux_tuple= (codigo, R*c)
    
    return aux_tuple
