import matplotlib.pyplot as plt
import matplotlib.animation as animation
import itertools
import numpy as np
import random

line_position = float(input("Where would you like the partition to be? please enter a value between 0 and 1   "))

#creating the canvas class
class Canvas():
    """This class creates the canvas object."""

    def __init__(self):
        """With self you can access private attributes of the object."""
        self.size = 2
        self.blocks = []
        self.fig, self.ax = plt.subplots(2, 1, figsize=(7, 7))
        self.avg_pos = []

    def add_block(self, block):
        """Every time a block is created it gets put into the array."""
        self.blocks.append(block)

    def update_blocks(self):
        """This method moves and draws all blocks."""
        self.ax[0].clear()
        for i, block in enumerate(self.blocks):
            block.move()
            block.draw()

        #appending the mean value of the positions of the particles to a list 
        self.ax[1].clear()
        self.avg_pos.append(np.mean([block.position[0] for block in self.blocks]))
        self.ax[1].plot(self.avg_pos)
        self.ax[0].set_title('Simulation of elastically colliding particles in a box')
        self.ax[1].set_title('Plot of average x position of particles in box over time')
        plt.show()

    def fix_axes(self):
        """The axes would change with each iteration otherwise."""
        self.ax[0].set_xlim((-self.size / 2, self.size / 2))
        self.ax[0].set_ylim((-self.size / 2, self.size / 2))
        self.ax[1].set_xlim((0, 500))
        self.ax[1].set_ylim((-canvas.size/2, canvas.size/2))

    def check_collision(self):
        """This method checks if blocks are colliding."""
        combinations = list(itertools.combinations(range(len(self.blocks)), 2))
        for pair in combinations:
            self.blocks[pair[0]].collide(self.blocks[pair[1]])

class Block():
    """This class creates the block object."""

    def __init__(self, canvas, mass, position=[0,0], velocity=[0,0]):
        self.canvas = canvas
        self.mass = mass
        self.position = position
        self.velocity = velocity
        self.canvas.add_block(self)
        self.bsize = 7

    def move(self):
        """The block is moved based on the velocity."""
        self.position = (
            self.position[0] + self.velocity[0],
            self.position[1] + self.velocity[1],
        )

        #new conditions for exchanging the velocities of the particles elastically
        if self.position[0] >= canvas.size/2:
            self.velocity[0] = -abs(self.velocity[0])
        if self.position[0] <= -canvas.size/2:
            self.velocity[0] = abs(self.velocity[0])

        if self.position[1] >= canvas.size/2:
            self.velocity[1] = -abs(self.velocity[1])
        if self.position[1] <= -canvas.size/2:
            self.velocity[1] = abs(self.velocity[1])

    def draw(self):
        """The method to draw the block."""
        canvas.ax[0].plot(self.position[0], self.position[1], "o", markersize=self.bsize)
        canvas.ax[0].plot((-line_position,-line_position), (-canvas.size / 2, canvas.size / 2), linestyle='dotted', color='blue')

    def collide(self, other):
        if np.sqrt(sum((np.array(self.position) - np.array(other.position)) ** 2)) <= 0.06:
            u, v = self.velocity, other.velocity
            self.velocity, other.velocity = v, u


#creating the canvas and block and giving them the required attributes
canvas = Canvas()
block1 = Block(canvas, mass=1, position=[random.uniform(-canvas.size/2,-line_position), \
                                random.uniform(-canvas.size/2,canvas.size/2)], velocity=[random.uniform(-0.03,0.03), random.uniform(-0.03,0.03)])
block2 = Block(canvas, mass=1, position=[random.uniform(-canvas.size/2,-line_position), \
                                random.uniform(-canvas.size/2,canvas.size/2)], velocity=[random.uniform(-0.03,0.03), random.uniform(-0.03,0.03)])
block3 = Block(canvas, mass=1, position=[random.uniform(-canvas.size/2,-line_position), \
                                random.uniform(-canvas.size/2,canvas.size/2)], velocity=[random.uniform(-0.03,0.03), random.uniform(-0.03,0.03)])
block4 = Block(canvas, mass=1, position=[random.uniform(-canvas.size/2,-line_position), \
                                random.uniform(-canvas.size/2,canvas.size/2)], velocity=[random.uniform(-0.03,0.03), random.uniform(-0.03,0.03)])
block5 = Block(canvas, mass=1, position=[random.uniform(-canvas.size/2,-line_position), \
                                random.uniform(-canvas.size/2,canvas.size/2)], velocity=[random.uniform(-0.03,0.03), random.uniform(-0.03,0.03)])
block6 = Block(canvas, mass=1, position=[random.uniform(-canvas.size/2,-line_position), \
                                random.uniform(-canvas.size/2,canvas.size/2)], velocity=[random.uniform(-0.03,0.03), random.uniform(-0.03,0.03)])
block7 = Block(canvas, mass=1, position=[random.uniform(-canvas.size/2,-line_position), \
                                random.uniform(-canvas.size/2,canvas.size/2)], velocity=[random.uniform(-0.03,0.03), random.uniform(-0.03,0.03)])
block8 = Block(canvas, mass=1, position=[random.uniform(-canvas.size/2,-line_position), \
                                random.uniform(-canvas.size/2,canvas.size/2)], velocity=[random.uniform(-0.03,0.03), random.uniform(-0.03,0.03)])
block9 = Block(canvas, mass=1, position=[random.uniform(-canvas.size/2,-line_position), \
                                random.uniform(-canvas.size/2,canvas.size/2)], velocity=[random.uniform(-0.03,0.03), random.uniform(-0.03,0.03)])
block10 = Block(canvas, mass=1, position=[random.uniform(-canvas.size/2,-line_position), \
                                random.uniform(-canvas.size/2,canvas.size/2)], velocity=[random.uniform(-0.03,0.03), random.uniform(-0.03,0.03)])
block11 = Block(canvas, mass=1, position=[random.uniform(-canvas.size/2,-line_position), \
                                random.uniform(-canvas.size/2,canvas.size/2)], velocity=[random.uniform(-0.03,0.03), random.uniform(-0.03,0.03)])
block12 = Block(canvas, mass=1, position=[random.uniform(-canvas.size/2,-line_position), \
                                random.uniform(-canvas.size/2,canvas.size/2)], velocity=[random.uniform(-0.03,0.03), random.uniform(-0.03,0.03)])
block13 = Block(canvas, mass=1, position=[random.uniform(-canvas.size/2,-line_position), \
                                random.uniform(-canvas.size/2,canvas.size/2)], velocity=[random.uniform(-0.03,0.03), random.uniform(-0.03,0.03)])
block14 = Block(canvas, mass=1, position=[random.uniform(-canvas.size/2,-line_position), \
                                random.uniform(-canvas.size/2,canvas.size/2)], velocity=[random.uniform(-0.03,0.03), random.uniform(-0.03,0.03)])
block15 = Block(canvas, mass=1, position=[random.uniform(-canvas.size/2,-line_position), \
                                random.uniform(-canvas.size/2,canvas.size/2)], velocity=[random.uniform(-0.03,0.03), random.uniform(-0.03,0.03)])
block16 = Block(canvas, mass=1, position=[random.uniform(-canvas.size/2,-line_position), \
                                random.uniform(-canvas.size/2,canvas.size/2)], velocity=[random.uniform(-0.03,0.03), random.uniform(-0.03,0.03)])
block17 = Block(canvas, mass=1, position=[random.uniform(-canvas.size/2,-line_position), \
                                random.uniform(-canvas.size/2,canvas.size/2)], velocity=[random.uniform(-0.03,0.03), random.uniform(-0.03,0.03)])
block18 = Block(canvas, mass=1, position=[random.uniform(-canvas.size/2,-line_position), \
                                random.uniform(-canvas.size/2,canvas.size/2)], velocity=[random.uniform(-0.03,0.03), random.uniform(-0.03,0.03)])
block19 = Block(canvas, mass=1, position=[random.uniform(-canvas.size/2,-line_position), \
                                random.uniform(-canvas.size/2,canvas.size/2)], velocity=[random.uniform(-0.03,0.03), random.uniform(-0.03,0.03)])
block20 = Block(canvas, mass=1, position=[random.uniform(-canvas.size/2,-line_position), \
                                random.uniform(-canvas.size/2,canvas.size/2)], velocity=[random.uniform(-0.03,0.03), random.uniform(-0.03,0.03)])



def animate(i):
    canvas.update_blocks()
    canvas.check_collision()
    canvas.fix_axes()

anim = animation.FuncAnimation(canvas.fig, animate, frames=500, interval=10)
writervideo = animation.FFMpegWriter(fps=60)
#anim.save("blocks_animation.mp4", writer=writervideo, dpi=200)
plt.show()
