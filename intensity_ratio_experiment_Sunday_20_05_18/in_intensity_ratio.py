filename = 'integrated_intensity_vs_gsqr.dat'
x_col_index = 0
y_col_index = 1
skiprows = 1

background_points = [ [5.0, 8.0], [8.0, 8.0] ] # Define two points over which a line is defined, which is used to subtract background.

gaussian_1_ansatz = [110, 6, 0.15] # [amplitude, x0, sigma]
gaussian_2_ansatz = [84, 7.02, 0.2]
