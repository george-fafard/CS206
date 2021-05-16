import numpy as np
import matplotlib.pyplot as plt
import constants as c

font = {'family' : 'normal',
        'size'   : 24}

plt.rc('font', **font)

def plot_progress(a_single, a_group, b_single, b_group):
    plt.title("Member Negative X Fitness over Generations")
    plt.xlabel("Generations")
    plt.ylabel("Negative X Fitness")
    for i in range(0, len(a_single)):
        plt.plot(a_single[i][0,:], 'b-')
        plt.plot(b_single[i][0,:], 'r-')
    plt.legend(['Individual Evaluated Fitness', 'Group Evaluated Fitness'])
    plt.show()
    plt.title("Collective Negative X Fitness over Generations")
    plt.xlabel("Generations")
    plt.ylabel("Negative X Fitness")
    for i in range(0, len(a_single)):
        plt.plot(a_group[i][0,:], 'b-')
        plt.plot(b_group[i][0,:], 'r-')
    plt.legend(['Individual Evaluated Fitness', 'Group Evaluated Fitness'])
    plt.show()

    # for i in range(0, len(b_group)):
    #     plt.plot(b_group[i][0,:])
    #     plt.show()

def plot_std_dev(a_s_plus, a_s_minus, a_g_plus, a_g_minus, b_s_plus, b_s_minus, b_g_plus, b_g_minus, a_avg_s, b_avg_s, a_avg_g, b_avg_g):
    plt.title("Member Average Negative X Fitness over Generation")
    plt.ylabel("Negative X Fitness")
    plt.xlabel("Generation")
    plt.plot(a_s_plus, 'c--')
    plt.plot(a_s_minus, 'g--')
    plt.plot(b_s_plus, 'm--')
    plt.plot(b_s_minus, 'y--')
    plt.plot(a_avg_s, 'b-')
    plt.plot(b_avg_s, 'r-')
    plt.legend(
        ['Individual Evaluated Fitness Positive Boundary', 'Individual Evaluated Negative Boundary',
         'Group Evaluated Positive Boundary', 'Group Evaluated Negative Boundary'
            , 'Individual Evaluated Fitness', 'Group Evaluated Fitness'])
    plt.show()

    plt.title("Collective Average Negative X Fitness over Generation")
    plt.ylabel("Negative X Fitness")
    plt.xlabel("Generation")
    plt.plot(a_g_plus, 'c--')
    plt.plot(a_g_minus, 'g--')
    plt.plot(b_g_plus, 'm--')
    plt.plot(b_g_minus, 'y--')
    plt.plot(a_avg_g, 'b-')
    plt.plot(b_avg_g, 'r-')
    plt.legend(
        ['Individual Evaluated Fitness Positive Boundary', 'Individual Evaluated Negative Boundary',
         'Group Evaluated Positive Boundary', 'Group Evaluated Negative Boundary'
            , 'Individual Evaluated Fitness', 'Group Evaluated Fitness'])
    plt.show()

def main():
    a_single = []
    a_group = []
    b_single = []
    b_group = []

    for i in range(0, c.A_B_TESTS):
        a_single.append(np.array((np.load("A_single_results_" + str(i) + ".npy"))))
        b_single.append(np.array((np.load("B_single_results_" + str(i) + ".npy"))))
        a_group.append(np.array((np.load("A_group_results_" + str(i) + ".npy"))))
        b_group.append(np.array((np.load("B_group_results_" + str(i) + ".npy"))))

    a_avg_g = []
    a_avg_s = []
    b_avg_g = []
    b_avg_s = []
    for i in range(0, c.A_B_TESTS):
        a_avg_g.append(np.mean(a_group[i]))
        a_avg_s.append(np.mean(a_single[i]))
        b_avg_g.append(np.mean(b_group[i]))
        b_avg_s.append(np.mean(b_single[i]))

    std_a_s = np.std(a_avg_s)
    std_b_s = np.std(b_avg_s)
    std_a_g = np.std(a_avg_g)
    std_b_g = np.std(b_avg_g)

    a_s_plus = []
    a_s_minus = []
    b_s_plus = []
    b_s_minus = []
    a_g_plus = []
    a_g_minus = []
    b_g_plus = []
    b_g_minus = []

    for i in range(0, len(a_avg_s)):
        a_s_plus.append(a_avg_s[i] + std_a_s)
        a_s_minus.append(a_avg_s[i] - std_a_s)
        a_g_plus.append(a_avg_g[i] + std_a_g)
        a_g_minus.append(a_avg_g[i] - std_a_g)
        b_s_plus.append(b_avg_s[i] + std_b_s)
        b_s_minus.append(b_avg_s[i] - std_b_s)
        b_g_plus.append(b_avg_g[i] + std_b_g)
        b_g_minus.append(b_avg_g[i] - std_b_g)

    plot_std_dev(a_s_plus, a_s_minus, a_g_plus, a_g_minus, b_s_plus, b_s_minus, b_g_plus, b_g_minus, a_avg_s, b_avg_s, a_avg_g, b_avg_g)
    plot_progress(a_single, a_group, b_single, b_group)

main()