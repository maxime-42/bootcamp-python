import matplotlib.pyplot as plt
import numpy as np
from matplotlib.image import imread
import copy

class ColorFilter:
    def __init__(self) -> None:
        pass

    def invert(self, array):
        """
        Applies a blue filter to the image received as a numpy array.
        Args:
        -----
        array: numpy.ndarray corresponding to the image.
        Return:
        -------
        array: numpy.ndarray corresponding to the transformed image.
        None: otherwise.
        Raises:
        -------
        This function should not raise any Exception.
        """
        res = 1 - array
        res[..., 3:] = array[..., 3:]
        return res

    def  to_blue(self, array):
        """
        Applies a blue filter to the image received as a numpy array.
        Args:
        -----
        array: numpy.ndarray corresponding to the image.
        Return:
        -------
        array: numpy.ndarray corresponding to the transformed image.
        None: otherwise.
        Raises:
        -------
        This function should not raise any Exception.
        """
        res = np.zeros(array.shape)
        res[..., 2:] = array[..., 2:]
        return array

    def to_green(self, array):
        """
        Applies a green filter to the image received as a numpy array.
        Args:
        -----
        array: numpy.ndarray corresponding to the image.
        Return:
        -------
        array: numpy.ndarray corresponding to the transformed image.
        None: otherwise.
        Raises:
        -------
        This function should not raise any Exception.
        """

        res = copy.deepcopy(array)
        res[..., :3:2] = res[..., :3:2] * 0
        return res

    def to_red(self, array):
        """
        Applies a red filter to the image received as a numpy array.
        Args:
        -----
        array: numpy.ndarray corresponding to the image.
        Return:
        -------
        array: numpy.ndarray corresponding to the transformed image.
        None: otherwise.
        Raises:
        -------
        This function should not raise any Exception.
        """
        array = array[:]
        array[:,:,1] = 0
        array[:,:,2] = 0
        return (array)

    def to_celluloid(self, array):
        """
        Applies a celluloid filter to the image received as a numpy array.
        Celluloid filter must display at least four thresholds of shades.
        Be careful! You are not asked to apply black contour on the object,
        you only have to work on the shades of your images.
        Remarks:
        celluloid filter is also known as cel-shading or toon-shading.
        Args:
        -----
        array: numpy.ndarray corresponding to the image.
        Return:
        -------
        array: numpy.ndarray corresponding to the transformed image.
        None: otherwise.
        Raises:
        -------
        This function should not raise any Exception.
        """
        shades = 4
            
        # Create the threshold values for the shades
        thresholds = np.linspace(0, 1, num=4)
        print(f"{thresholds=}")
        # Iterate through the color channels
        for i in range(3):
            # Create a copy of the channel
            channel = array[..., i].copy()
            # Iterate through the thresholds and apply the shades
            for t in thresholds:
                channel[array[..., i] >= t] = t
                # Replace the channel in the original array
                array[..., i] = channel
            # Return the modified array
            return array
        

if __name__ == "__main__":

    img = imread('elon.png')
    cf = ColorFilter() 
    array = cf.to_celluloid(img)
    plt.imshow(array)
    plt.show()
