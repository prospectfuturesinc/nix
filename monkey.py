import random

def main():
    # Simple birthday-simulation demo. This version fixes several bugs
    # from the original:
    # - correct __name__ guard so main() isn't called during import/evaluation
    # - avoid printing inside the inner loop (which flooded the terminal)
    # - iterate values correctly when checking for duplicates
    print('monkey')
    trials = 10           # how many trials to run (keeps output small)
    people_per_trial = 100
    days_in_year = 365

    for t in range(trials):
        # reset counts for each trial
        day_counts = [0] * days_in_year

        # simulate people picking birthdays
        for _ in range(people_per_trial):
            idx = int(random.random() * days_in_year)
            day_counts[idx] += 1

        # find days with 2 or more people
        duplicates = [c for c in day_counts if c >= 2]

        if duplicates:
            # report that at least one shared birthday occurred
            print(f"Trial {t}: shared birthday detected (examples: {duplicates[:8]})")
        else:
            print(f"Trial {t}: no shared birthdays")


if __name__ == "__main__":
    main()