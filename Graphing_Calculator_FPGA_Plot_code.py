import matplotlib.pyplot as plt
import numpy as np
import serial

ser = serial.Serial("COM3", 115200)


def signed4(x):
    if x >= 8:
        return x - 16
    return x


while True:

    if ser.in_waiting >= 2:

        packet = ser.read(2)

        value = int.from_bytes(packet, byteorder='big')

        coord = (value >> 12) & 0b1

        A = (value >> 8) & 0b1111
        B = (value >> 4) & 0b1111
        C = value & 0b1111

        A = signed4(A)
        B = signed4(B)
        C = signed4(C)

        if coord == 0:

            x = np.linspace(-100, 100, 400)
            y = A * x**2 + B * x + C

            plt.plot(x, y)
            plt.xlabel("x")
            plt.ylabel("y")
            plt.grid(True)

        else:

            theta = np.linspace(0, 2 * np.pi, 400)
            r = A * theta**2 + B * theta + C

            ax = plt.subplot(111, projection="polar")
            ax.plot(theta, r)

        plt.show()
