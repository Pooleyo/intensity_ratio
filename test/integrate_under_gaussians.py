def run(gsqr, gaussians):

    gsqr_width = (gsqr[-1] - gsqr[0])/(len(gsqr) - 1)
    
    integrated_intensities = []
    
    for i in gaussians:
    
        current_integrated_intensity = sum(i) * gsqr_width
        integrated_intensities.append(current_integrated_intensity)
        
    return integrated_intensities
