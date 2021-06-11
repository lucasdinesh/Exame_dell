from math import radians, sin, cos, sqrt, asin


def haversine(lat1, lon1, HashTable):
    aux_table = []
    for i in range(len(HashTable)):
        if(HashTable[i] == ''):
            pass
        else:
            lat2=HashTable[i][0]
            lon2=HashTable[i][1]
            R = 6372.8  # Earth radius in kilometers

            dLat = radians(lat2 - lat1)
            dLon = radians(lon2 - lon1)
            lat1 = radians(lat1)
            lat2 = radians(lat2)

            a = sin(dLat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dLon / 2) ** 2
            c = 2 * asin(sqrt(a))
            aux_tuple= (i, R*c)
            aux_table.append(aux_tuple)


    return aux_table