from mesa import Model
from mesa.space import MultiGrid
from mesa.time import RandomActivation
import random
from person_agent import PersonAgent

class InfectionModel(Model):
    def __init__(self, N, width, height):
        self.num_agents = N
        self.grid = MultiGrid(width, height, True)
        self.schedule = RandomActivation(self)
        self.running = True

        # Create agents
        for i in range(self.num_agents):
            infected = (i == 0)  # only first agent starts infected
            agent = PersonAgent(i, self, infected)
            self.schedule.add(agent)

            # Place agent randomly on the grid
            x = random.randrange(self.grid.width)
            y = random.randrange(self.grid.height)
            self.grid.place_agent(agent, (x, y))

    def step(self):
        self.schedule.step()
