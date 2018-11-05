def run(x, y, line_coeff):

    def line(x, m, c):
    
        y = m * x + c
    
        return y

    background_intensity = []
    new_intensity = []

    for i in x:
        current_background_intensity = line(i, line_coeff[0], line_coeff[1])
        
        background_intensity.append(current_background_intensity)
    
    for i in range(len(y)):
    
        current_new_intensity = y[i] - background_intensity[i]
        
        new_intensity.append(current_new_intensity)

    return new_intensity
