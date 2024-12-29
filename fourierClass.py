"""DFT Class File. By Connor Fleser

This file contains a simple implementation of the Discrete Fourier Transform. It is neither optimized nor perfectly accurate.
Is is intended for educational purposes only.

"""

import numpy as np
from typing import Any


class Fourier():
    """Class for my own implementations of fourier transforms
    """

    def _defineDomain(t0: float, t1: float, size: int) -> tuple[float, float]:
        """Defines the domain of the fourier transform
        """
        return (t0, size/(2*(t1-t0))) #The maximum frequency a fourier transform can resolve is half the sampling frequency

    def _calculateFourier(t0: float, t1: float, inputVals: np.ndarray[float], resolution: int):
        """Calculates the fourier transform of the input values
        """

        yFourier = np.array([0 for i in range(int(Fourier._defineDomain(t0, t1, np.size(inputVals))[1]*resolution))],dtype = complex)
        
        for k in range(np.size(yFourier)):
            temp = 0
            for i in range(np.size(inputVals)):
                temp += inputVals[i] * np.exp((complex(0,-1)*2*np.pi*k*i*(t1-t0))/(resolution * np.size(inputVals)))
            yFourier[k] = temp
        return yFourier


    def __init__(self, t0: float, t1: float, inputVals: np.array, resolution: int):
        """Creates a Fourier Object

        Args:
            t0 (float): _description_
            t1 (float): _description_
            inputVals (np.array): _description_
            resolution (int): _description_
        """

        self._t0 = t0
        self._t1 = t1
        self._inputVals: np.array = inputVals
        self._fDomain: tuple[float, float] = Fourier._defineDomain(t0, t1, np.size(inputVals))
        self._yVals: np.array[complex] = Fourier._calculateFourier(t0, t1, inputVals, resolution)
        
    def getFourierInfo(self) -> dict[str: Any]:
        """Returns the fourier and info related to it

        Returns:
            Dict[
                'fDomain': (minFrequency (float), maxFrequecy (float)),
                'size': int,
                'yVals': np.array[complex]
            ]
        """
        fourierInfo: dict[str: Any] = dict()

        fourierInfo['fDomain'] = self._fDomain
        fourierInfo['size'] = np.size(self._yVals)
        fourierInfo['yVals'] = self._yVals

        return fourierInfo
    