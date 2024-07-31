import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, Polygon
from ipywidgets import interact, widgets

class BlockBasedInterface:
    def __init__(self):
        self.fig, self.ax = plt.subplots(figsize=(6, 4))
        self.ax.set_xlim(0, 10)
        self.ax.set_ylim(0, 10)
        self.ax.axis('off')

    def draw_shape(self, shape, color):
        self.ax.clear()
        self.ax.set_xlim(0, 10)
        self.ax.set_ylim(0, 10)
        self.ax.axis('off')
        
        if shape == 'circle':
            shape = Circle((5, 5), 2, fill=True, color=color)
        elif shape == 'square':
            shape = Rectangle((3, 3), 4, 4, fill=True, color=color)
        elif shape == 'triangle':
            shape = Polygon([(5, 8), (3, 3), (7, 3)], fill=True, color=color)
        
        self.ax.add_patch(shape)
        plt.show()

interface = BlockBasedInterface()

interact(
    interface.draw_shape,
    shape=widgets.Dropdown(options=['circle', 'square', 'triangle'], value='circle', description='Shape:'),
    color=widgets.Dropdown(options=['red', 'green', 'blue'], value='blue', description='Color:')
)
