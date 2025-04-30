import matplotlib.pyplot as plt
import numpy as np


f, U_out, delta_t = np.genfromtxt("data.txt", unpack=True)
delta_t *=1e-6

U_in = 10

L_U=20 * np.log10(U_out/U_in)

delta_phi=2*np.pi*f*delta_t

#plot
fig, ax1 = plt.subplots(layout="constrained")

ax1.plot(f,L_U, color="blue", label="Spannungspegel")
ax2=ax1.twinx()
ax2.plot(f, delta_phi,color="green" , label="Phasenverschiebung")

ax2.legend()
ax1.grid()
ax1.set(
    xscale="log",
    xlabel="Frequenz / Hz",
    ylabel=r"$L_U$ /dB",
)
ax2.set(
    ylabel="Phasenverschiebung / rad",
)
ax1.legend()



fig.savefig("build/Bode.pdf")
