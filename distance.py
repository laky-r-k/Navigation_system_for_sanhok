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
calculate_polyline_distance( [{ "lat": 514.8062496185303, "lng": 454 },
        { "lat": 516.0562496185303, "lng": 444.25 },
        { "lat": 510.5562496185303, "lng": 443.75 },
        { "lat": 505.5562496185303, "lng": 444 },
        { "lat": 500.8062496185303, "lng": 445.5 },
        { "lat": 497.0562496185303, "lng": 448 },
        { "lat": 492.8062496185303, "lng": 451.5 },
        { "lat": 490.8062496185303, "lng": 457 },
        { "lat": 490.8062496185303, "lng": 464.5 },
        { "lat": 491.0562496185303, "lng": 501.75 },
        { "lat": 494.8062496185303, "lng": 510.5 },
        { "lat": 489.5562496185303, "lng": 514.25 },
        { "lat": 483.0562496185303, "lng": 515.75 },
        { "lat": 470.11249923706055, "lng": 518 },
        { "lat": 448.11249923706055, "lng": 519.5 },
        { "lat": 434.11249923706055, "lng": 523.5 },
        { "lat": 420.11249923706055, "lng": 531.5 },
        { "lat": 408.61249923706055, "lng": 547.5 },
        { "lat": 406.61249923706055, "lng": 560 },
        { "lat": 408.11249923706055, "lng": 611.5 },
        { "lat": 405.11249923706055, "lng": 636 },
        { "lat": 399.11249923706055, "lng": 657.5 },
        { "lat": 393.61249923706055, "lng": 675.5 },
        { "lat": 388.11249923706055, "lng": 685.5 }
      ])