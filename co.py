
import numpy as np
import matplotlib.pyplot as plt
 
def simulate_mc_coin_toss(num_tosses=100):
    tosses = []
    p_estimates = []
    variances = []
 
    for i in range(1, num_tosses + 1):
        toss = np.random.choice([0, 1])
        tosses.append(toss)
 
        p_estimate = np.mean(tosses)
        p_tail = 1 - p_estimate
        var_p = p_estimate * p_tail / i
 
        p_estimates.append(p_estimate)
        variances.append(var_p)
 
        print(f"Toss {i}: {'Heads' if toss else 'Tails'} | p_estimate = {p_estimate:.3f} | Var(p_estimate) = {var_p:.6f}")
 
    x = np.arange(1, num_tosses + 1)
 
    plt.figure(figsize=(10, 5))
 
    plt.subplot(2, 1, 1)
    plt.bar(['Tails', 'Heads'], [1 - p_estimate, p_estimate], color=['gray', 'skyblue'])
    plt.ylim(0, 1)
    plt.ylabel('Estimated Probability')
    plt.title('Final Estimated Probability of Tails and Heads')
 
    plt.subplot(2, 1, 2)
    plt.plot(x, variances, color='orange', label=f'Var(p_estimate) after {len(tosses)} tosses : {variances[-1]:0.3f}')
    plt.title(f'Variance of p_estimate Over {len(tosses)} Tosses')
    plt.xlabel('Number of Tosses')
    plt.ylabel('Variance')
    plt.legend()
 
    plt.tight_layout()
    plt.show()
 
n = int(input("Enter the number of tosses you want to simulate: "))
simulate_mc_coin_toss(num_tosses=n)
