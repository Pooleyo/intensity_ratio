def run(ansatz, x, y):

    import numpy as np
    from scipy.optimize import curve_fit

    def gaussian(x, a, x0, sigma):
    
        gaussian = a*np.exp(-(x-x0)**2/(2*sigma**2))
    
        return gaussian

    gaussian_coeff = curve_fit(gaussian, x, y, ansatz) 

    return gaussian_coeff
