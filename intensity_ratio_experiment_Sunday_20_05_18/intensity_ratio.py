import in_intensity_ratio as ip
import fit_line_to_background
import read_in_data
import subtract_background
import fit_gaussian
import limit_gsqr
import calc_gaussian
import make_plots
import integrate_under_gaussian
import calc_intensity_ratio

#####################

background_line = fit_line_to_background.run(ip.background_points)

gsqr, intensity = read_in_data.run(ip.filename, ip.x_col_index, ip.y_col_index, ip.skiprows)

intensity = subtract_background.run(gsqr, intensity, background_line)

gaussian_1 = calc_gaussian.run(ip.gaussian_1_ansatz, gsqr)

gaussian_2 = calc_gaussian.run(ip.gaussian_2_ansatz, gsqr)

gaussian_1_integrated_intensity = integrate_under_gaussian.run(gsqr, gaussian_1)

gaussian_2_integrated_intensity = integrate_under_gaussian.run(gsqr, gaussian_2)

intensity_ratio = calc_intensity_ratio.run(gaussian_1_integrated_intensity, gaussian_2_integrated_intensity)

gaussians = [gaussian_1, gaussian_2]

make_plots.run(gsqr, intensity, gaussians)
