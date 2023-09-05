import matplotlib.pyplot as plt
import numpy as np

def gaussian(x: np.array, 
             mu: float = 0.0,
             sigma: float = 1.0,
             save: bool = True):
    """
    Plots Gaussian function

    Args:
        x (np.array):
        mu (float): Expectation value of Gaussian. Defaults to 0.0. 
        sigma (float): Width of Gaussian. Defaults to 1.0. Must be greater than 0.
        save (bool): Save a figure of the Gaussian. Default to True.
    
    Returns:
        y (np.array)
    """

    y = 1 / (sigma * np.sqrt(2 * np.pi)) * np.exp(-0.5  * ((x-mu)**2 / (sigma**2)))

    if save:
        plt.plot(x, y)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title(f'Gaussian $(\sigma = {sigma}, \mu = {mu})$')

        plt.savefig("gaussian.png")

    return y

if (__name__ == "__main__"):
    x = np.linspace(-10, 10, 1000)
    mu = 0
    sigma = 2

    gaussian(x, mu, sigma)

