def run(gsqr, intensity, static_gaussians):

    for j in static_gaussians:
        for i in range(len(gsqr)):
            intensity[i] = intensity[i] - j[i]

    return intensity
