# Implementasi Integrasi Numerik untuk Menghitung Estimasi Nilai Pi

Repositori ini mengimplementasikan metode integral Riemann untuk menghitung nilai pi secara numerik. Metode ini menggunakan integral dari fungsi `f(x) = 4 / (1 + x^2)` dari 0 sampai 1.

## Struktur Repositori

- `src/riemann_integral.py`: Kode sumber untuk menghitung integral menggunakan metode Riemann.
- `tests/test_riemann_integral.py`: Kode pengujian untuk menguji berbagai nilai N.
- `data/results.csv`: Hasil pengujian dengan berbagai nilai N.
- `README.md`: Penjelasan isi repositori ini.

## Hasil Pengujian

Hasil pengujian dengan berbagai nilai N adalah sebagai berikut:

| N      | Approximation       | RMS Error           | Execution Time (s)   |
|--------|----------------------|---------------------|----------------------|
| 10     | 3.0418396189294032   | 0.09975303466038997 | 2.17e-05             |
| 100    | 3.1315929035585537   | 0.010000249968760815| 0.000124216079711914 |
| 1000   | 3.140592653839794    | 0.001000000250000642| 0.001101016998291015 |
| 10000  | 3.1414926535900345   | 0.000099999975976695| 0.012491941452026367 |

## Cara Menggunakan

Untuk menjalankan kalkulasi integral Riemann:
```bash
python src/riemann_integral.py
