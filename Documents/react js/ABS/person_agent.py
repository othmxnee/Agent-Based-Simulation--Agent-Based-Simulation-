from mesa import Agent
import random

class PersonAgent(Agent):
    def __init__(self, unique_id, model, infected=False):
        super().__init__(unique_id, model)
        self.infected = infected
        self.recovered = False

    def move(self):
        """Agent moves to a random nearby cell"""
        possible_steps = self.model.grid.get_neighborhood(
            self.pos,
            moore=True,
            include_center=False
        )
        new_position = random.choice(possible_steps)
        self.model.grid.move_agent(self, new_position)

    def infect_others(self):
        """If agent is infected, everyone in the same cell gets infected"""
        if not self.infected:
            return
        cellmates = self.model.grid.get_cell_list_contents([self.pos])
        for other in cellmates:
            if not other.infected and not other.recovered:
                other.infected = True  # infection is instant (no probability)

    def step(self):
        self.move()
        self.infect_others()
        # Optional: agents recover after some time
        if self.infected and random.random() < 0.1:  # simple recovery rule
            self.infected = False
            self.recovered = True
