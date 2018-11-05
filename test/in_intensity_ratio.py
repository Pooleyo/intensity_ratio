import numpy as np

filename = 'integrated_intensity_vs_gsqr.dat'
x_col_index = 0
y_col_index = 1
skiprows = 1

background_points = [ [3.0, 1.5], [8.35, 6.25] ] # Define two points over which a line is defined, which is used to subtract background.

static_gaussian_ansatz = [[115, 6.0, 0.15], [74,3.99,0.062]] # [amplitude, x0, sigma]
driven_gaussian_ansatz = [[87, 7.02, 0.2], [30,4.6,0.12]]

limits = ((100, -np.inf, -np.inf, 70, -np.inf, -np.inf, 80, -np.inf, -np.inf, 28, -np.inf, -np.inf), (130, np.inf, np.inf, 80, np.inf, np.inf, 95, np.inf, np.inf, 35, np.inf, np.inf))
