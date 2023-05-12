import sys
import imageio
import matplotlib.pyplot as plt
import matplotlib.image as image
import numpy as np

class ImageProcessor:
    def __init__(self) -> None:
        pass
    def load(self, path):
        try:
            img = plt.imread(path)

        except Exception as error_msg:
            print("wshh Exception: FileNotFoundError -- strerror: No such file",file=sys.stderr)
            return None
        else:
            print(img)
            print(f"{img.shape[0]} x {img.shape[1]}")
            return img

    def display(self, array):
        if not isinstance(array, np.ndarray):
            print("ImgProcessor.display: Parameter is not a numpy array", file=sys.stderr)
            return
        plt.axis("off")
        plt.imshow(array)
        plt.show()

if __name__ == "__main__":
    imp = ImageProcessor()
    arr = imp.load("42AI.png")
    imp.display(arr)