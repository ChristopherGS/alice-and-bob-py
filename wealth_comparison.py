from core.cycle import simulate
from core.people import People
from core.person import Person

def calculate_wealth_comparison(trials=1000000, trial_length=2, setback_percent=1.0):
    """
    Simulates a series of trials to determine how often Alice is wealthier than Bob
    after a given number of simulation cycles.

    Args:
    trials (int): Number of trials to run.
    trial_length (int): Number of simulation cycles in each trial.
    setback_percent (float): The percentage by which a person's wealth is reduced during a setback.

    Returns:
    None: Prints the percentage of times Alice is wealthier.
    """
    alice_richer_count = 0
    for _ in range(trials):
        people = People([Person("Alice"), Person("Bob")])
        for _ in range(trial_length):
            simulate(setback_percent, people)
        # Direct comparison to determine if Alice is wealthier
        if people[0].cash > people[1].cash:
            alice_richer_count += 1

    percentage_alice_richer = (alice_richer_count / trials) * 100
    print(f"Alice is wealthier {percentage_alice_richer:.2f}% of times.")

if __name__ == "__main__":
    calculate_wealth_comparison()
