import matplotlib.path as mpath

cycles = [[(5, 3), (6, 4), (7, 4), (8, 5), (9, 4), (10, 3), (9, 2), (8, 1), (7, 2), (6, 2)], [(15, 5), (16, 4), (17, 3), (16, 2), (15, 1), (14, 2), (14, 3), (14, 4)]]
def find_bounding_box(polygon):
    x_coords = [point[0] for point in polygon]
    y_coords = [point[1] for point in polygon]
    
    min_x = min(x_coords)
    max_x = max(x_coords)
    min_y = min(y_coords)
    max_y = max(y_coords)

    bounding_box = [(min_x, min_y), (max_x, max_y)]
    return bounding_box

for i in cycles:
    polygon = mpath.Path(i)
    bounding_box = find_bounding_box(i)
    x1 = bounding_box[0][0]
    x2 = bounding_box[1][0]
    y1 = bounding_box[0][1]
    y2 = bounding_box[1][1]

    for x in range(x1, x2):
        for y in range(y1, y2):
            point = (x, y)
            if polygon.contains_point(point) and point not in i:
                print(point)
