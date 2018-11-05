def run(ansatz, gsqr):

    import numpy as np

    def gaussian(x, a, x0, sigma):
    
        gaussian = a*np.exp(-(x-x0)**2/(2*sigma**2))
    
        return gaussian
        
    gaussian_intensities = []

    
    for j in range(len(ansatz)): 
        gaussian_intensities.append([])   
        for i in gsqr:
            current_gaussian_intensity = gaussian(i, ansatz[j][0], ansatz[j][1], ansatz[j][2])
            gaussian_intensities[j].append(current_gaussian_intensity)

    return gaussian_intensities 
