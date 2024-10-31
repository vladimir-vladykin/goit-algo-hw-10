import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as spi


# function x^3
def f(x):
    return x ** 3

F_TEXT_REPRESENTATION = "f(x) = x^3"

# range of integration
START = 2
END = 6

# for Monte-Carlo randomization
SMALL_NUM_SAMPLES = 500
MEDIUM_NUM_SAMPLES = 5000
BIG_NUM_SAMPLES = 50000

# calculate x and y
x = np.linspace(-0.5, 7.0, 400)
y = f(x)


def main():
    # just for representation of our function and range of integration
    draw_chart(x, y, START, END)

    # run tests of Monte-Carlo implementation with different number of samples
    for num_sumples in [SMALL_NUM_SAMPLES, MEDIUM_NUM_SAMPLES, BIG_NUM_SAMPLES]:
        monte_carlo_result = calculate_integral_with_monte_carlo(f, START, END, BIG_NUM_SAMPLES)
        print(f"Integral for {F_TEXT_REPRESENTATION} via Monte-Carlo method is: {monte_carlo_result:.8f}, samples used for randomization: {num_sumples}")

    # compare with integral calculation via buit-in method
    spi_result, _ = spi.quad(f, START, END)
    print(f"Integral for {F_TEXT_REPRESENTATION} via scipy is: {spi_result:.8f}")


def calculate_integral_with_monte_carlo(f, start, end, num_samples):
    x_random = np.random.uniform(start, end, num_samples)
    y_random = np.random.uniform(0, f(end), num_samples)

    points_in = np.sum(y_random < f(x_random))
    
    # calculate area of figure via Monte-Carlo method
    area = (end - start) * f(end) * points_in / num_samples
    return area


def draw_chart(x, y, start, end):
    fig, ax = plt.subplots()

    ax.plot(x, y, 'r', linewidth=2)

    ix = np.linspace(start, end)
    iy = f(ix)
    ax.fill_between(ix, iy, color='gray', alpha=0.3)

    ax.set_xlim([x[0], x[-1]])
    ax.set_ylim([0, max(y) + 0.1])
    ax.set_xlabel('x')
    ax.set_ylabel('f(x)')

    ax.axvline(x=start, color='gray', linestyle='--')
    ax.axvline(x=end, color='gray', linestyle='--')
    ax.set_title(f'Графік інтегрування {F_TEXT_REPRESENTATION} від ' + str(start) + ' до ' + str(end))
    plt.grid()
    plt.show()


if __name__ == '__main__':
    main()