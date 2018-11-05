def run(gsqr, gaussian_intensity):

    gsqr_width = (gsqr[-1] - gsqr[0])/(len(gsqr) - 1)
    integrated_intensity = sum(gaussian_intensity) * gsqr_width

    return integrated_intensity
