def run(background_points):

    import numpy as np
    
    x = [background_points[0][0], background_points[1][0]]
    y = [background_points[0][1], background_points[1][1]]

    line_fit = np.polyfit(x, y, 1)

    return line_fit
