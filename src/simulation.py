import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Slider
from tank import Tank

class TankSimulation:
    def __init__(self):
        self.fig, self.ax = plt.subplots()
        plt.subplots_adjust(left=0.1, right=0.9, top=0.85, bottom=0.25)
        self.ax.set_xlim(0, 10)
        self.ax.set_ylim(0, 12)
        self.ax.set_aspect('equal')
        self.ax.set_title("Tank Simulation with Controls")

        self.tank = Tank(x=2, y=1, width=5, height=10, initial_level=2, fluid_color="red")
        self.tank.add_to_axes(self.ax)

        ax_inflow = plt.axes([0.15, 0.15, 0.7, 0.03])
        ax_outflow = plt.axes([0.15, 0.1, 0.7, 0.03])
        self.slider_inflow = Slider(ax_inflow, 'Inflow', 0, 0.5, valinit=self.tank.inflow_rate, valstep=0.01)
        self.slider_outflow = Slider(ax_outflow, 'Outflow', 0, 0.5, valinit=self.tank.outflow_rate, valstep=0.01)

        self.slider_inflow.on_changed(self.update_inflow)
        self.slider_outflow.on_changed(self.update_outflow)

        self.level_text = self.ax.text(4.75, 11.25, f"{self.tank.fluid_level:.2f}",
                                       ha='center', fontsize=10, color='black')

    def update_inflow(self, val):
        self.tank.inflow_rate = self.slider_inflow.val

    def update_outflow(self, val):
        self.tank.outflow_rate = self.slider_outflow.val

    def animate(self, frame):
        self.tank.update()
        self.level_text.set_text(f"{self.tank.fluid_level:.2f}")
        return self.tank.fluid_patch, self.level_text

    def run(self):
        ani = FuncAnimation(self.fig, self.animate, frames=500, interval=50, blit=True)
        plt.show()


if __name__ == "__main__":
    sim = TankSimulation()
    sim.run()
