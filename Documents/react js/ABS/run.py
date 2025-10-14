from infection_model import InfectionModel

# Create model with 50 agents on a 10x10 grid
model = InfectionModel(N=50, width=10, height=10)

# Run 30 steps
for step in range(30):
    model.step()
    infected = sum(a.infected for a in model.schedule.agents)
    recovered = sum(a.recovered for a in model.schedule.agents)
    print(f"Step {step}: Infected={infected}, Recovered={recovered}")
