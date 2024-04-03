from anyio import Path
from direct.showbase.ShowBase import ShowBase
from direct.gui.OnscreenText import OnscreenText
import sys

class MyApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        # Load the environment model.
        self.scene = self.loader.loadModel("models/environment")
        # Reparent the model to render.
        self.scene.reparentTo(self.render)
        # Apply scale and position transforms on the model.
        self.scene.setScale(0.25, 0.25, 0.25)
        self.scene.setPos(-8, 42, 0)

        # Add some basic text
        # self.text = OnscreenText(text="Panda3D: Hello World!", parent=base.a2dTopLeft,
        #                          pos=(0.08, -0.1), scale=0.05, fg=(1, 1, 1, 1),
        #                          shadow=(0, 0, 0, 0.5))

        # Disable the camera trackball controls.
        self.disableMouse()

        # Load and transform a model. Replace "models/panda-model" with your model path.
        path = "D:\\Cours\\3A_CI\\Group_Project\\code\\megapose6d\\local_data\\examples\\barbecue-sauce\\meshes\\barbecue-sauce\\hope_000002.ply"
        # path = Path("/d/Cours/3A_CI/Group_Project/code/megapose6d/local_data/examples/barbecue-sauce/meshes/barbecue-sauce/hope_000002.ply")
        # path = "/d/Cours/3A_CI/Group_Project/code/megapose6d/local_data/examples/barbecue-sauce/meshes/barbecue-sauce/hope_000002.ply"
        self.model = self.loader.loadModel(path)
        self.model.reparentTo(self.render)
        self.model.setScale(0.005, 0.005, 0.005)
        self.model.setPos(0, 30, -5)

app = MyApp()
app.run()