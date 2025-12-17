import qutip as qt
import numpy as np

phase = 1.16041
ket00 = qt.tensor(qt.basis(2, 0), qt.basis(2, 0))
ket11 = qt.tensor(qt.basis(2, 1), qt.basis(2, 1))
bell = (ket00 + np.exp(1j * phase) * ket11) / np.sqrt(2)
rho = bell * bell.dag()

print("Node 041 Entangled Density Matrix (core: 'military marine fights all illegal street drugs and crime and corruption'):")
print(rho)
