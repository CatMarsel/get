import numpy as np
import time

def get_sin_wave_amplitude(freq, time_point):
    """
    Вычисляет амплитуду сдвинутого и нормализованного синусоидального сигнала
    Args:
        freq: частота сигнала (Гц)
        time_point: момент времени для расчета амплитуды
    Returns:
        Нормализованная амплитуда в диапазоне [0, 1]
    """
    raw_sin = np.sin(2 * np.pi * freq * time_point)
    shifted = raw_sin + 1   # Сдвиг из [-1, 1] в [0, 2]
    normalized = shifted / 2  # Нормализация в [0, 1]
    return normalized

def wait_for_sampling_period(sampling_frequency):
    """
    Ожидает один период дискретизации
    Args:
        sampling_frequency: частота дискретизации (Гц)
    """
    period = 1.0 / sampling_frequency
    time.sleep(period)