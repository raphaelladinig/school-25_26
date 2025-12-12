import random


def draw_lottery(total_numbers=45, numbers_to_draw=6):
    number_pool = list(range(1, total_numbers + 1))

    drawn_numbers = random.sample(number_pool, numbers_to_draw)

    return drawn_numbers


print("-" * 50)
print(f"Drawn numbers: {draw_lottery(45, 6)}")
print("-" * 50)


def run_statistics(num_draws=1000, total_numbers=45, numbers_to_draw=6):
    stats_dict = {number: 0 for number in range(1, total_numbers + 1)}

    for _ in range(num_draws):
        drawn_numbers = draw_lottery(total_numbers, numbers_to_draw)

        for number in drawn_numbers:
            stats_dict[number] += 1

    return stats_dict


def main():
    statistics = run_statistics()

    print("Number | Count")
    print("------ | ------")

    for number, count in sorted(statistics.items()):
        print(f"{number: <6} | {count}")


if __name__ == main:
    main()
