import numpy as np
from numpy.linalg import eig

# 1. Buat matriks contoh (simetris)
A = np.array([[4, 1], [1, 3]])  # Matriks 2x2

# 2. Hitung nilai eigen dan vektor eigen
eigenvalues, eigenvectors = eig(A)
print("Nilai Eigen:", eigenvalues)
print("Vektor Eigen:\n", eigenvectors)

# 3. Analisis sensitivitas: Ubah satu elemen matriks
A_perturbed = A.copy()
A_perturbed[0, 0] += 0.1  # Tambahkan 0.1 ke elemen (0,0)

eigenvalues_perturbed, _ = eig(A_perturbed)
print("Nilai Eigen setelah perturbasi:", eigenvalues_perturbed)

# 4. Hitung perbedaan nilai eigen
delta_eigenvalues = np.abs(eigenvalues - eigenvalues_perturbed)
print("Perubahan Nilai Eigen:", delta_eigenvalues)