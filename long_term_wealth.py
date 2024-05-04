from core.people import People
from core.person import Person
import random


def calculate_long_term_wealth(days=1000, experiments=1000000, setback_rate=0.2):
    """
    Calculate and print the wealth comparison between Alice and Bob over a set number of days and experiments.

    Parameters:
    days (int): Number of days to simulate.
    experiments (int): Number of experimental runs.
    setback_rate (float): Probability rate at which a setback (wealth decrease) occurs.

    Returns:
    None: Outputs to console the day-by-day results of the experiments.
    """
    alice_wealthier_days = [0] * days
    total_alice_wealth = [0.0] * days
    total_bob_wealth = [0.0] * days

    for _ in range(experiments):
        participants = People([Person("Alice"), Person("Bob")])
        simulate_days(participants, days, setback_rate, alice_wealthier_days, total_alice_wealth, total_bob_wealth)

    print_simulation_results(days, experiments, alice_wealthier_days, total_alice_wealth, total_bob_wealth)


def simulate_days(participants, days, setback_rate, alice_wealthier_days, total_alice_wealth, total_bob_wealth):
    for day in range(days):
        for participant in participants:
            update_wealth(participant, setback_rate)

        update_counts(participants, alice_wealthier_days, total_alice_wealth, total_bob_wealth, day)


def update_wealth(participant, setback_rate):
    if random.random() < participant.lie_discovered_rate:
        participant.cash *= (1 - setback_rate)
    else:
        participant.cash += participant.subs_growth


def update_counts(participants, alice_wealthier_days, total_alice_wealth, total_bob_wealth, day):
    if participants[0].cash > participants[1].cash:
        alice_wealthier_days[day] += 1

    total_alice_wealth[day] += participants[0].cash
    total_bob_wealth[day] += participants[1].cash

def print_simulation_results(days, experiments, alice_wealthier_days, total_alice_wealth, total_bob_wealth):
    for day in range(days):
        if (day + 1) % 100 == 0:  # Check if it's a multiple of 100
            alice_average_wealth = total_alice_wealth[day] / experiments
            bob_average_wealth = total_bob_wealth[day] / experiments
            percentage_alice_wealthier = alice_wealthier_days[day] / experiments * 100
            print(f"Day {day + 1}: % of experiments where Alice is the top earner: {percentage_alice_wealthier:.2f}%")
            print(f"Alice's average wealth: {alice_average_wealth:.2f}, Bob's average wealth: {bob_average_wealth:.2f}")
