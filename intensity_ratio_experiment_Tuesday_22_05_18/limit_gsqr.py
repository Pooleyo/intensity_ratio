def run(gsqr, intensity, limit):

    new_gsqr = []
    new_intensity = []
    
    for i in range(len(intensity)):
        if gsqr[i] >= limit[0] and gsqr[i] <= limit[1]:
            new_gsqr.append(gsqr[i])
            new_intensity.append(intensity[i])
            
        else:
            continue
            
    return new_gsqr, new_intensity
