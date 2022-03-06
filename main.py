import matplotlib.pyplot as plt
from random import *
import math, numpy, os

class Percent:
    def __init__(self):
        while True:
            try:
                self.TRY = float(input("Write Value\n--> "))
                self.TRY / 1
                break
            except:
                print("##################"+
                      "\n#Write Int Please#\n"+
                      "##################")

        self.InCircle, self.Rectangle = 0, 0
        self._x, self._y = list(), list()
        self.figure, self.axes = plt.subplots()
        plt.title('Let\'s Find π\'s Secret')
    """
    Vector2 Size
    """
    def distance(self, x, y):
        try:
            if (x-1.)**2+(y-1.)**2 <= 1.:
                return True
            else:
                return False
        except:
            print("Distance Calculate Error")
    """
    Show Result
    """
    def pi(self, incircle, rect):
        result = float((incircle/rect)*4)
        print(f"Σ--> {result}"+
            f"\nπ--> {math.pi}"+
            f"\nΔ==> {abs(math.pi-result)}")


    def draw(self):
        """
        Random dots
        """
        for i in range(int(self.TRY)):
            r_x = uniform(0, 2)
            r_y = uniform(0, 2)
            self._x.append(r_x)
            self._y.append(r_y)
            self.Rectangle += 1
            if self.distance(r_x, r_y): # judge in circler
                self.InCircle += 1
        numpy.unique(self._x)
        numpy.unique(self._y)
        plt.plot(self._x, self._y,
                color="blue",
                marker=".",
                linestyle="",
                label="Random Dot")
        
        """
        Draw Circle Radius --> 1.
        """
        circle = plt.Circle((1., 1.), 1.,fill=True)
        self.axes.set_aspect(1)
        self.axes.add_patch(circle)
        # show result
        self.pi(self.InCircle, self.Rectangle)
        plt.legend()
        plt.show()


if __name__=="__main__":
    while input("-r to start\n--> ") == "r":
        os.system('clear')
        percent = Percent()
        percent.draw()
