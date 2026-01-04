items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}


def greedy_algorithm(items, budget):
    sorted_items = sorted(
        items.items(),
        key=lambda x: x[1]["calories"] / x[1]["cost"],
        reverse=True
    )

    total_cost = 0
    total_calories = 0
    result = []

    for name, data in sorted_items:
        if total_cost + data["cost"] <= budget:
            total_cost += data["cost"]
            total_calories += data["calories"]
            result.append(name)

    return result, total_cost, total_calories


def dynamic_programming(items, budget):
    names = list(items.keys())
    n = len(names)

    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        cost = items[names[i - 1]]["cost"]
        calories = items[names[i - 1]]["calories"]

        for w in range(budget + 1):
            if cost <= w:
                dp[i][w] = max(
                    dp[i - 1][w],
                    dp[i - 1][w - cost] + calories
                )
            else:
                dp[i][w] = dp[i - 1][w]

    result = []
    w = budget
    total_cost = 0

    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            item = names[i - 1]
            result.append(item)
            w -= items[item]["cost"]
            total_cost += items[item]["cost"]

    result.reverse()
    return result, total_cost, dp[n][budget]


if __name__ == "__main__":
    budget = 100

    greedy_res = greedy_algorithm(items, budget)
    dp_res = dynamic_programming(items, budget)

    print("Greedy:", greedy_res)
    print("Dynamic Programming:", dp_res)