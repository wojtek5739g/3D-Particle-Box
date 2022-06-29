import numpy as np
import mayavi.mlab as mlab

from traits.api import HasTraits, Range, Instance, \
        on_trait_change
from traitsui.api import View, Item, Group

from mayavi.core.api import PipelineBase
from mayavi.core.ui.api import MayaviScene, SceneEditor, \
                MlabSceneModel

a, b, c = 100, 100, 100
x = np.arange(a)
y = np.arange(b)
z = np.arange(c)
xx, yy, zz = np.meshgrid(x, y, z)

def cube_faces(xmin, xmax, ymin, ymax, zmin, zmax):
    faces = []

    x,y = np.mgrid[xmin:xmax:a,ymin:ymax:a]
    z = np.ones(y.shape)*zmin
    faces.append((x,y,z))

    x,y = np.mgrid[xmin:xmax:a,ymin:ymax:a]
    z = np.ones(y.shape)*zmax
    faces.append((x,y,z))

    x,z = np.mgrid[xmin:xmax:a,zmin:zmax:a]
    y = np.ones(z.shape)*ymin
    faces.append((x,y,z))

    x,z = np.mgrid[xmin:xmax:a,zmin:zmax:a]
    y = np.ones(z.shape)*ymax
    faces.append((x,y,z))

    y,z = np.mgrid[ymin:ymax:a,zmin:zmax:a]
    x = np.ones(z.shape)*xmin
    faces.append((x,y,z))

    y,z = np.mgrid[ymin:ymax:a,zmin:zmax:a]
    x = np.ones(z.shape)*xmax
    faces.append((x,y,z))

    return faces

def mlab_plt_cube(xmin,xmax,ymin,ymax,zmin,zmax):
    faces = cube_faces(xmin,xmax,ymin,ymax,zmin,zmax)
    for grid in faces:
        x,y,z = grid
        mlab.mesh(x,y,z,opacity=0.4)

class MyModel(HasTraits):

    nx = Range(1, 10, 1)
    ny = Range(1, 10, 1)
    nz = Range(1, 10, 1)
    scene = Instance(MlabSceneModel, ())
    plot = Instance(PipelineBase)

    @on_trait_change('nx,ny,nz,scene.activated')
    def update_plot(self):
        mlab.clf()
        p, q, r = (self.nx, self.ny, self.nz)
        self.plot = mlab.contour3d(abs((np.sin((p*np.pi*xx)/a))*(np.sin((q*np.pi*yy)/b))*(np.sin((r*np.pi*zz)/c)))**2, contours=6, transparent=True, name = 'Particle in 3D box')
        mlab_plt_cube(0,a,0,a,0,a)

    view = View(Item('scene', editor=SceneEditor(scene_class=MayaviScene),
                     height=250, width=300, show_label=False),
                Group(
                        'nx', 'ny','nz',
                     ),
                resizable=True,
                )

def main():
    my_model = MyModel()
    my_model.configure_traits()

if __name__ == "__main__":
    main()