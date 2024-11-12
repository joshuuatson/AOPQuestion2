import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D

class SolarSystem():   #defines the class of solar system and gives attributes
    def __init__(self):
        self.size = 1000
        self.planets = []
        #initializes the 3D figure
        self.fig = plt.figure()
        self.ax = Axes3D(self.fig, auto_add_to_figure=False)
        self.fig.add_axes(self.ax)
        self.dT = 1

    #adds new planet to the array
    def add_planet(self, planet):
        self.planets.append(planet)
    
    def update_planets(self):
        """ This method moves and draws all of the planets. """
        self.ax.clear()
        for planet in self.planets:
            planet.move()
            planet.draw()
    
    def fix_axes(self):
        """ The axes would change with each iteration
        otherwise.
        """
        self.ax.set_xlim((-self.size/2, self.size/2))
        self.ax.set_ylim((-self.size/2, self.size/2))
        self.ax.set_zlim((-self.size/2, self.size/2))
    
    def gravity_planets(self):
        """ This method calculated gravity interaction for
        every planet.
        """
        for i, first in enumerate(self.planets):
            for second in self.planets[i+1:]:
                first.gravity(second)


                
class Planet():
    """ This class creates the Planet object. """
    def __init__(
            self,
            SolarSys,
            mass,
            position=(0, 0, 0),
            velocity=(0, 0, 0)
    ):
        self.SolarSys = SolarSys
        self.mass = mass
        self.position = position
        self.velocity = velocity
        # The planet is automatically added to the SolarSys.
        self.SolarSys.add_planet(self)
        self.color = "black"
    
    def move(self):
        """ The planet is moved based on the velocity. """
        self.position = (
            self.position[0]+self.velocity[0]*SolarSys.dT,
            self.position[1]+self.velocity[1]*SolarSys.dT,
            self.position[2]+self.velocity[2]*SolarSys.dT
        )
    
    def draw(self):
        """ The method to draw the planet. """
        if not hasattr(self, 'trajectory'):
            self.trajectory = []
        self.trajectory.append(self.position)
        if len(self.trajectory) > 1:
            xs, ys, zs = zip(*self.trajectory)
            self.SolarSys.ax.plot(xs, ys, zs, color=self.color)
        self.SolarSys.ax.plot(
            *self.position,
            marker="o",
            markersize=10,
            color=self.color
        )

    
    def gravity(self, other):
        """ The method to compute gravitational force for two
        planets. numpy module is used to handle vectors.
        """
        distance = np.subtract(other.position, self.position)
        distanceMag = np.linalg.norm(distance)
        distanceUnit = np.divide(distance, distanceMag)
        forceMag = self.mass*other.mass/(distanceMag**2)
        force = np.multiply(distanceUnit, forceMag)
        # Switch makes force on self opossite to other
        switch = 1
        for body in self, other:
            acceleration = np.divide(force, body.mass)
            acceleration = np.multiply(force, SolarSys \
                                      .dT*switch)
            body.velocity = np.add(body.velocity,
                                   acceleration)
            switch *= -1




class Sun(Planet):
    def __init__(self, SolarSys, mass=1000, position=(0, 0, 0), velocity=(0, 0, 0)):
        super(Sun, self).__init__(SolarSys, mass, position, velocity)
        self.color = "yellow"

    def move(self):
        self.position = self.position


# Instantiating of the solar system.
SolarSys = SolarSystem()

# Instantiating of planets.
planet1 = Planet(SolarSys, mass=10, position=(150, 50, 0), velocity=(0, 5, 5))
planet2 = Planet(SolarSys, mass=10, position=(100, -50, 150), velocity=(5, 0, 0))
planet3 = Planet(SolarSys, mass=10, position=(-100, -50, 150), velocity=(-4, 0, 0))

# Instantiating of the sun.
sun = Sun(SolarSys)


def animate(i):
    """This controls the animation."""
    print("The frame is:", i)
    SolarSys.gravity_planets()
    SolarSys.update_planets()
    SolarSys.fix_axes()


# This calls the animate function and creates animation.
anim = animation.FuncAnimation(SolarSys.fig, animate, frames=100, interval=100)

# This prepares the writer for the animation.
writervideo = animation.FFMpegWriter(fps=60)
plt.show()

# This saves the animation.
anim.save("planets_animation.mp4", writer=writervideo , dpi =200)


    
