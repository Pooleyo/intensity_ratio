filename = 'integrated_intensity_vs_gsqr.dat'
x_col_index = 0
y_col_index = 1
skiprows = 1

background_points = [ [0.0, 0.0], [1.0, 0.0] ] # Define two points over which a line is defined, which is used to subtract background.

static_gaussian_ansatz = [[411, 9.923, 0.17], [196.6,11.95,0.22], [457,13.97,0.2]] # [amplitude, x0, sigma]
driven_gaussian_ansatz = [[145.0, 10.5, 0.5], [100.0,13.0,0.8], [140.0,15.0,0.4]]
