import matplotlib.patches as patches

class Tank:
    def __init__(self, x=2, y=1, width=5, height=10, inflow_rate=0.1, outflow_rate=0.05, initial_level=0, fluid_color='blue'):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.inflow_rate = inflow_rate
        self.outflow_rate = outflow_rate
        self.fluid_level = initial_level
        self.fluid_color = fluid_color

        self.tank_patch = patches.Rectangle((x, y), width, height, fill=False, linewidth=2)
        self.fluid_patch = patches.Rectangle((x, y), width, self.fluid_level, color=fluid_color)

    def add_to_axes(self, ax):
        ax.add_patch(self.tank_patch)
        ax.add_patch(self.fluid_patch)

    def update(self):
        self.fluid_level += self.inflow_rate - self.outflow_rate
        self.fluid_level = max(0, min(self.fluid_level, self.height))
        self.fluid_patch.set_height(self.fluid_level)
        return self.fluid_patch
