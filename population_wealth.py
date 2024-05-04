from core.cycle import simulate
from core.people import People
from core.person import Person

def calculate_population_wealth(iterations=30, setback_percent=1.0, population_size=200000):
    """
    Simulates wealth changes in a large population of "Alice" and "Bob" over multiple iterations.

    Args:
    iterations (int): Number of times to simulate the wealth changes.
    setback_percent (float): The percentage by which a person's wealth is reduced during a setback.
    population_size (int): Total number of people in the simulation, must be even for equal numbers of Alice and Bob.

    Returns:
    None
    """
    # Validate population size
    if population_size % 2 != 0:
        raise ValueError("Population size must be even to ensure equal numbers of Alice and Bob.")

    # Initialize population
    people = People([Person("Alice") if i % 2 == 0 else Person("Bob") for i in range(population_size)])

    # Perform simulations
    for iteration in range(iterations):
        simulate(setback_percent, people)
        if (iteration + 1) % 5 == 0:  # Print results every 5 iterations
            print(f"Iteration {iteration + 1}:")
            people.print_stats()

if __name__ == "__main__":
    calculate_population_wealth()
