#!/usr/bin/env python
from boomslang import StackedBars, Bar, Plot
from ImageComparisonTestCase import ImageComparisonTestCase
import unittest

class StackedBarTest(ImageComparisonTestCase, unittest.TestCase):
    def __init__(self, testCaseName):
        super(StackedBarTest,self).__init__(testCaseName)
        self.imageName = "stackedbar.png"

    def constructImage(self):
        bar1 = Bar()
        bar1.xValues = range(5)
        bar1.yValues = [1, 2, 1, 2, 3]
        bar1.color = "red"
        bar1.label = "Red Cluster"

        bar2 = Bar()
        bar2.xValues = range(5)
        bar2.yValues = [2, 2, 3, 3, 4]
        bar2.color = "blue"
        bar2.label = "Blue Cluster"

        bar3 = Bar()
        bar3.xValues = range(5)
        bar3.yValues = [3, 5, 4, 5, 3]
        bar3.color = "green"
        bar3.label = "Green Cluster"

        stackedBars = StackedBars()
        stackedBars.add(bar1)
        stackedBars.add(bar2)
        stackedBars.add(bar3)

        stackedBars.xTickLabels = ["A", "B", "C", "D", "E"]

        plot = Plot()
        plot.add(stackedBars)
        plot.yLimits = (0, 15)
        plot.hasLegend()
        plot.save(self.imageName)

ImageComparisonTestCase.register(StackedBarTest)

if __name__ == "__main__":
    test = StackedBarTest("testImageComparison")
    test.constructImage()
