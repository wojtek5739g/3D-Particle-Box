import numpy as np
import mayavi.mlab as mlab

def main():
    # x, y, z, value = np.random.random((4, 40))
    # mlab.points3d(x, y, z, value)
    # mlab.show()

    a, b, c = 10, 10, 10
    p, q, r = 2, 1, 1
    x = np.arange(a)
    y = np.arange(b)
    z = np.arange(c)
    # x, y, z = np.ogrid[-5:5:64j, -5:5:64j, -5:5:64j]
    xx, yy, zz = np.meshgrid(x, y, z)
    scalars = abs((np.sin((p*np.pi*xx)/a))*(np.sin((q*np.pi*yy)/b))*(np.sin((r*np.pi*zz)/c)))**2
    mlab.contour3d(scalars, contours=4, transparent=True)
    mlab.show()

if __name__ == "__main__":
    main()