import in_intensity_ratio as ip
import fit_line_to_background
import read_in_data
import subtract_background
import fit_gaussian
import limit_gsqr
import calc_gaussian
import make_plots
import integrate_under_gaussians
import print_output
import subtract_static_gaussians

#####################

background_line = fit_line_to_background.run(ip.background_points)

gsqr, intensity = read_in_data.run(ip.filename, ip.x_col_index, ip.y_col_index, ip.skiprows)

intensity = subtract_background.run(gsqr, intensity, background_line)

static_gaussians = calc_gaussian.run(ip.static_gaussian_ansatz, gsqr)

driven_gaussians = calc_gaussian.run(ip.driven_gaussian_ansatz, gsqr)

gaussians = static_gaussians + driven_gaussians

make_plots.run(gsqr, intensity, gaussians, 'static_and_driven_gaussian_fits.png')

intensity = subtract_static_gaussians.run(gsqr, intensity, static_gaussians)

all_ansatz = ip.static_gaussian_ansatz + ip.driven_gaussian_ansatz

integrated_intensities = integrate_under_gaussians.run(gsqr, gaussians)

print_output.run(integrated_intensities, all_ansatz)

make_plots.run(gsqr, intensity, gaussians, 'static_subtracted_gaussian_fits.png')
