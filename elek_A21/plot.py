import matplotlib.pyplot as plt
import numpy as np


U_in, U_diode, I_diode = np.genfromtxt("data.txt", unpack=True)


#plot
fig, ax1 = plt.subplots(layout="constrained")

ax1.plot(U_diode,I_diode, color="blue", label="Diodenkennlinie")

ax1.grid()
ax1.legend()
ax1.set(
    xlabel="Diodenspannung / ?",
    ylabel=r"$I$/?",
)

fig.savefig("build/Diodenkennlinie.pdf")