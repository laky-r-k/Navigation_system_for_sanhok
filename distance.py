def calculate_polyline_distance(polyline):
    """
    Calculates total Euclidean distance of a polyline in flat CRS coordinates.
    Input: List of dicts like [{'lat': ..., 'lng': ...}, ...]
    Output: Total distance (same unit as coordinate system, e.g. pixels)
    """
    from math import sqrt

    total = 0
    for i in range(1, len(polyline)):
        x1, y1 = polyline[i - 1]['lng'], polyline[i - 1]['lat']
        x2, y2 = polyline[i]['lng'], polyline[i]['lat']
        dist = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        total += dist
    print( total)
calculate_polyline_distance( [
    {"lat": 587.31, "lng": 219.75},
    {"lat": 599.31, "lng": 223.25},
    {"lat": 617.06, "lng": 221.75},
    {"lat": 632.81, "lng": 216.5},
    {"lat": 642.06, "lng": 211.75},
    {"lat": 663.06, "lng": 211.5},
    {"lat": 673.06, "lng": 213.5},
    {"lat": 681.06, "lng": 222.5},
    {"lat": 684.81, "lng": 233.5},
    {"lat": 684.56, "lng": 258.75},
    {"lat": 685.81, "lng": 278.5},
    {"lat": 691.31, "lng": 302.0},
    {"lat": 699.06, "lng": 332.5},
    {"lat": 698.81, "lng": 351.75},
    {"lat": 692.81, "lng": 372.5},
    {"lat": 687.31, "lng": 429.75},
    {"lat": 690.81, "lng": 451.0},
    {"lat": 689.81, "lng": 473.25},
    {"lat": 691.31, "lng": 486.25},
    {"lat": 698.31, "lng": 498.75},
    {"lat": 682.06, "lng": 499.5},
    {"lat": 665.06, "lng": 501.5},
    {"lat": 651.06, "lng": 509.5},
    {"lat": 638.06, "lng": 524.25},
    {"lat": 629.81, "lng": 537.0},
    {"lat": 621.06, "lng": 546.25},
    {"lat": 609.81, "lng": 549.25},
    {"lat": 597.56, "lng": 552.25},
    {"lat": 582.81, "lng": 554.25},
    {"lat": 570.81, "lng": 559.75},
    {"lat": 559.31, "lng": 566.25},
    {"lat": 554.56, "lng": 571.5},
    {"lat": 552.31, "lng": 559.75},
    {"lat": 551.31, "lng": 538.25},
    {"lat": 552.81, "lng": 514.25},
    {"lat": 551.56, "lng": 465.25},
    {"lat": 546.06, "lng": 454.5},
    {"lat": 537.31, "lng": 446.75},
    {"lat": 526.31, "lng": 443.5},
    {"lat": 515.56, "lng": 444.25}
])