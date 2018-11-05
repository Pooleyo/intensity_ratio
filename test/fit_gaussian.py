def run(ansatz, x, y, limits):

    import numpy as np
    from scipy.optimize import curve_fit

    print limits

    def gaussian_sum(x, *ansatz):

        gaussian_sum = 0.0

        for i in range(len(ansatz)/3):

            gaussian_sum += ansatz[i + 0] * np.exp(-(x - ansatz[i + 1]) ** 2 / (2 * ansatz[i + 2] ** 2))
    
        return gaussian_sum

    gaussian_coeff = curve_fit(gaussian_sum, x, y, ansatz, bounds=limits)

    gaussian_list = []

    for i in range(len(gaussian_coeff[0])/3):

        gaussian_list.append([gaussian_coeff[0][i + 0], gaussian_coeff[0][i + 1], gaussian_coeff[0][i + 2]])

    return gaussian_list
