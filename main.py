def main():
    import math
    import matplotlib.pyplot as plt
    import numpy as np
    z = 1 + 2j
    rotated = rotate(z, math.radians(45))

    fig, ax = plt.subplots()
    ax.set_xlabel("Real")
    ax.set_ylabel("Imaginary")
    limit = np.max(np.abs(rotated))
    plt.xlim(-limit, limit)
    plt.ylim(-limit, limit)
    ax.plot([0, np.real(z)], [0, np.imag(z)], 'ro-', )
    ax.plot([0, np.real(rotated)], [0, np.imag(rotated)], 'go-')
    plt.show()




    print(f"Initial (red): {z}")
    print(f"Rotated (green): {rotated}")

def rotate(z, angle):
    import cmath
    return z * cmath.exp(1j * angle)

if __name__ == "__main__":
        main()