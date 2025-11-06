import numpy as np
def read_values_from_file(filename):
    with open(filename, 'r') as file:
        values = [float(line.strip()) for line in file]
    return np.array(values)
print(read_values_from_file(r"C:\Users\6298664\Desktop\values.txt"))


def read_oscillatory_wave_data(filename):
    data = np.loadtxt(filename, delimiter= ',') 
    lengths = data[:, 0]
    amplitudes = data[:, 1]
    mean_amplitude = np.mean(amplitudes)
    max_amplitude = np.max(amplitudes)
    return data, mean_amplitude, max_amplitude
print(read_oscillatory_wave_data(r"C:\Users\6298664\Desktop\wave_data.csv"))


def read_standing_wave_data(filename):
    data = np.loadtxt(filename, delimiter=',')

    lengths = data[:, 0]
    
    tensions = data[:, 1]

    wave_speed = np.sqrt(tensions)

    return data, wave_speed

print(read_standing_wave_data(r"C:\Users\6298664\Desktop\standing_wave.csv"))

