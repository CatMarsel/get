import r2r_dac as r2r
import signal_generator as sg
import time

amplitude = 3.2
signal_freq=80
sampling_freq=100

try:
    time=0
    dac=r2r.R2R_DAC([16, 20, 21, 25, 26, 17, 27, 22], 3.2, True)
    while True:
        v=sg.get_sin_wave_amplitude(signal_freq, time)
        dac.set_voltage(v)
        sg.wait_for_sampling_period(sampling_freq)
        time+=0.001
        print(time)
        print(v)
finally:
    dac.deinit()