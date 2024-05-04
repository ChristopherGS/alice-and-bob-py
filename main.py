from long_term_wealth import calculate_long_term_wealth
from population_wealth import calculate_population_wealth
from wealth_comparison import calculate_wealth_comparison


def run_simulation():
    # sim 1: Long-Term wealth
    print(f'\nTest 1: Long-Term Wealth')
    calculate_long_term_wealth(days=1000, experiments=1000, setback_rate=0.2)

    # sim 2: Population wealth
    print(f'\nTest 2: Population Wealth')
    calculate_population_wealth(iterations=20, setback_percent=1.0, population_size=100000)

    # sim 3: Wealth comparison
    print(f'\nTest 3: Wealth Comparison')
    calculate_wealth_comparison(trials=1000000, trial_length=2, setback_percent=1.0)


if __name__ == "__main__":
    run_simulation()
