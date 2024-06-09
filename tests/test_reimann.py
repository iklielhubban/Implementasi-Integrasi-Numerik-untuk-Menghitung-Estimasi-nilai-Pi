from reimann_integral import reimann_integral, f  # Melakukan impor langsung dari modul

import time
import json
import numpy as np

def calculate_rms_error(estimated_pi, actual_pi=3.14159265358979323846):
    return np.sqrt((estimated_pi - actual_pi)**2)

def test_reimann():
    a = 0
    b = 1
    Ns = [10, 100, 1000, 10000]
    actual_pi = 3.14159265358979323846
    
    results = []
    for N in Ns:
        start_time = time.time()
        estimated_pi = reimann_integral(f, a, b, N)
        end_time = time.time()
        elapsed_time = end_time - start_time
        rms_error = calculate_rms_error(estimated_pi, actual_pi)
        
        result = {
            'N': N,
            'Estimated Pi': estimated_pi,
            'RMS Error': rms_error,
            'Execution Time (s)': elapsed_time
        }
        results.append(result)
        
        print(f"N={N}, Estimated Pi={estimated_pi}, RMS Error={rms_error}, Execution Time={elapsed_time}s")
    
    # Simpan hasil ke file JSON
    with open('data/results.json', 'w') as f:
        json.dump(results, f, indent=4)
    
    return results

if __name__ == "__main__":
    results = test_reimann()