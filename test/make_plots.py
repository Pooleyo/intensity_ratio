def run(gsqr, intensity, gaussians, plot_name):

    import matplotlib.pyplot as plt

    plt.figure(plot_name)
    plt.ylabel('Intensity integrated over phi (PSL)')
    plt.xlabel('$|G^2|$')
    plt.plot(gsqr, intensity)

    for i in gaussians:

        plt.plot(gsqr,i)
    
    envelope_of_gaussians = [0] * len(gsqr)

    for j in gaussians:
        for i in range(len(gsqr)):
            envelope_of_gaussians[i] += j[i]
    
    plt.plot(gsqr,envelope_of_gaussians)        
    
    plt.savefig(plot_name)
    plt.draw()

    return
