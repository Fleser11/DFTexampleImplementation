"""This program plots a cosine function and its fourier transform.

By Connor Fleser
"""


import matplotlib.pyplot as plt
import numpy as np

import fourierClass as f


    

def main():
    """Main function that runs the program
    """

def plot_cosine():
    # Generate x values from 0 to 2π
    x = np.linspace(0, 8, 1000)

    # Calculate cosine for each x value
    y = np.cos(2*np.pi*x) + np.cos(4*np.pi*x) + np.sin(6*np.pi*x)

    fourier = f.Fourier(0, 8, y, 50).getFourierInfo()

    # Create a new figure
    plt.figure()

    # Plot the cosine function
    plt.plot(x, y, label='cos(x)', color='blue')
    # plt.plot(np.linspace(fourier['fDomain'][0], fourier['fDomain'][1], fourier['size']), np.real(fourier['yVals']), label='Fourier Real', color='red')
    # plt.plot(np.linspace(fourier['fDomain'][0], fourier['fDomain'][1], fourier['size']), np.imag(fourier['yVals']), label='Fourier Imaginary', color='green')
    plt.plot(np.linspace(fourier['fDomain'][0], fourier['fDomain'][1], fourier['size']), np.abs(fourier['yVals']), label='Fourier Magnitude', color='purple')
    plt.plot(np.linspace(fourier['fDomain'][0], fourier['fDomain'][1], fourier['size']), 180/np.pi*np.arctan(np.imag(fourier['yVals'])/np.real(fourier['yVals'])), label='Fourier Angle', color='orange')


    # Add a title and labels
    plt.title('Cosine functions and their fourier transforms')
    plt.xlabel('x')
    plt.ylabel('y')

    # Add a grid
    plt.grid(True)

    # Add a legend
    plt.legend()

    # Show the plot
    plt.show()

if __name__ == "__main__":
    plot_cosine()
