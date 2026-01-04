import random
from collections import Counter
import matplotlib.pyplot as plt

N = 1_000_000

sums = []
for _ in range(N):
    sums.append(random.randint(1, 6) + random.randint(1, 6))

counts = Counter(sums)

analytic_probabilities = {
    2: 1/36, 3: 2/36, 4: 3/36, 5: 4/36, 6: 5/36,
    7: 6/36, 8: 5/36, 9: 4/36, 10: 3/36, 11: 2/36, 12: 1/36
}

print(f"{'Сума':<5}{'Монте-Карло':<15}{'Аналітична':<15}")
for s in range(2, 13):
    print(f"{s:<5}{counts[s]/N:<15.5f}{analytic_probabilities[s]:<15.5f}")

x = list(range(2, 13))
monte_carlo_values = [counts[s] / N for s in x]
analytic_values = [analytic_probabilities[s] for s in x]

plt.figure(figsize=(10, 5))
plt.bar(x, monte_carlo_values, width=0.4, label="Метод Монте-Карло")
plt.plot(x, analytic_values, marker="o", label="Аналітичні значення")

plt.xlabel("Сума")
plt.ylabel("Ймовірність")
plt.title("Порівняння методу Монте-Карло з аналітичними ймовірностями")
plt.legend()
plt.grid(axis="y")
plt.show()