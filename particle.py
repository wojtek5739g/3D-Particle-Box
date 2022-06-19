import numpy as np
import mayavi.mlab as mlab

def main():
    # x, y, z, value = np.random.random((4, 40))
    # mlab.points3d(x, y, z, value)
    # mlab.show()

    a, b, c = 5, 5, 5
    p, q, r = 2, 3, 1
    x, y, z = np.ogrid[-5:5:64j, -5:5:64j, -5:5:64j]
    scalars = abs((np.sin((p*np.pi*x)/a))*(np.sin((q*np.pi*y)/b))*(np.sin((r*np.pi*z)/c)))**2
    mlab.contour3d(scalars, contours=4, transparent=True)
    mlab.show()

if __name__ == "__main__":
    main()