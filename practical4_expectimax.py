payoffs = {
    "A": [8, 6, 4],
    "B": [3, 7, 5],
    "C": [2, 9, 1]
}
probabilities = {
    "A": [0.2, 0.3, 0.5],
    "B": [0.2, 0.5, 0.3],
    "C": [0.7, 0.2, 0.1]
}
 
 
def chance_value(strategy):
    p = probabilities[strategy]
    values = payoffs[strategy]
    assert abs(sum(p) - 1.0) < 1e-9
    return sum(prob * payoff for prob, payoff in zip(p, values))
 
 
def main():
    expected = {strategy: chance_value(strategy)
                for strategy in payoffs}
    worst_case = {strategy: min(values)
                  for strategy, values in payoffs.items()}
    for strategy in payoffs:
        print(strategy, "expected payoff:", round(expected[strategy], 2),
              "million KZT")
    print("Expectimax chooses:", max(expected, key=expected.get))
    print("Minimax chooses:", max(worst_case, key=worst_case.get))
 
 
if __name__ == "__main__":
    main()
