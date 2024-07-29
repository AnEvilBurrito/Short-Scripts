# binomial distribution can help find the odds of some events occurring X times
# in N number of trials. 
# However, it is only useful for binary outcomes.

from math import factorial

def binomial_distribution(n, x, p):
    # n = number of trials
    # x = number of event occurrences
    # p = probability of event occurring
    # f(x, n, p) = (n choose x) * p^x * (1-p)^(n-x)
    nCx = factorial(n) / (factorial(x) * factorial(n-x))
    return nCx * p**x * (1-p)**(n-x)


def compute_binomial_distribution_probability(n, x, p, mode: str):
    if mode == "==":
        return binomial_distribution(n, x, p)
    elif mode == ">":
        return sum([binomial_distribution(n, i, p) for i in range(x+1, n+1)])
    elif mode == "<":
        return sum([binomial_distribution(n, i, p) for i in range(x)])
    elif mode == ">=":
        return sum([binomial_distribution(n, i, p) for i in range(x, n+1)])
    elif mode == "<=":
        return sum([binomial_distribution(n, i, p) for i in range(x+1)])
    elif mode == "!=":
        return 1 - binomial_distribution(n, x, p)
    elif mode == "display":
        all_probabilities = [binomial_distribution(n, i, p) for i in range(n+1)]
        print(f'--- Probabilities for {n} trials and {p} probability of event occurring ---')
        for i, prob in enumerate(all_probabilities):
            print(f"Probability of {i} occurrences within {n} trials: {prob.__round__(4)}")
        print(f"Total probability: {sum(all_probabilities).__round__(4)}")
        return all_probabilities
    else:
        raise ValueError("Invalid mode, please use one of the following: '==', '>', '<', '>=', '<='")


print('--- Analysis of Catan Yields ---')
total_die_surface = 36 
n = 18
dot_probs = [i/total_die_surface for i in range(1, 6)]
robber_prob = 6/total_die_surface
for i, prob in enumerate(dot_probs):
    print('------ Dot:', i+1, '------')
    compute_binomial_distribution_probability(n, 1, prob, "display")
    print(f'Chance of at least 1 successful roll: {compute_binomial_distribution_probability(n, 0, prob, ">").__round__(4)}')
print('------ Robber ------')
compute_binomial_distribution_probability(n, 1, robber_prob, "display")
print(f'Chance of at least 1 successful roll: {compute_binomial_distribution_probability(n, 0, robber_prob, ">").__round__(4)}')



# if __name__ == "__main__":
#     n = int(input("Enter the number of trials: "))
#     x = int(input("Enter the number of event occurrences: "))
#     p = float(input("Enter the probability of event occurring: "))
#     mode = input("Enter the mode: ")
#     print(compute_binomial_distribution_probability(n, x, p, mode))


