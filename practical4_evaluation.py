features = {
    "X": {"margin": 8, "reliability": 7, "capacity": 2},
    "Y": {"margin": 5, "reliability": 5, "capacity": 8}
}
 
 
def evaluate(state, weights):
    f = features[state]
    return (weights[0] * f["margin"]
            + weights[1] * f["reliability"]
            + weights[2] * f["capacity"])
 
 
def main():
    experiments = {
        "Initial": (0.5, 0.3, 0.2),
        "Capacity increased": (0.3125, 0.1875, 0.5)
    }
    for name, weights in experiments.items():
        assert abs(sum(weights) - 1.0) < 1e-9
        scores = {state: evaluate(state, weights)
                  for state in features}
        preferred = max(scores, key=scores.get)
        print(name, "weights:", weights)
        print("Eval(X):", scores["X"])
        print("Eval(Y):", scores["Y"])
        print("MAX prefers:", preferred, "\n")
 
 
if __name__ == "__main__":
    main()
