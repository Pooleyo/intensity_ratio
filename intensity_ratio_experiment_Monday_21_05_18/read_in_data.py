def run(filename, x_col_index, y_col_index, skiprows):

    import numpy as np
    
    gsqr, intensity = np.loadtxt(filename, usecols=(x_col_index, y_col_index), skiprows=skiprows, unpack=True, delimiter=',')

    return gsqr, intensity
