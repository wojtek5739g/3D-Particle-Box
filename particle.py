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

    view = View(Item('scene', editor=SceneEditor(scene_class=MayaviScene),
                     height=250, width=300, show_label=False),
                Group(
                        'nx', 'ny','nz',
                     ),
                resizable=True,
                )

my_model = MyModel()
my_model.configure_traits()