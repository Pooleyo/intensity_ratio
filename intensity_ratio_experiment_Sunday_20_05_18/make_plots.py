def run(gsqr, intensity, gaussians):

    import matplotlib.pyplot as plt
    
    plt.ylabel('Intensity integrated over phi (PSL)')
    plt.xlabel('$|G^2|$')
    plt.plot(gsqr, intensity)
    
    for i in gaussians:
        plt.plot(gsqr,i)
    
    plt.savefig('gaussian_estimates.png')
    plt.show()

    return
