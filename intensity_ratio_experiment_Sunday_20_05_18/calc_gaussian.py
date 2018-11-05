def run(ansatz, gsqr):

    import numpy as np

    def gaussian(x, a, x0, sigma):
    
        gaussian = a*np.exp(-(x-x0)**2/(2*sigma**2))
    
        return gaussian
        
    gaussian_intensity = []
        
    for i in gsqr:
        current_gaussian_intensity = gaussian(i, ansatz[0], ansatz[1], ansatz[2])
        gaussian_intensity.append(current_gaussian_intensity)
        
    return gaussian_intensity
