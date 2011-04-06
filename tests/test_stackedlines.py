#!/usr/bin/env python

from boomslang import Line, StackedLines, Plot

from ImageComparisonTestCase import ImageComparisonTestCase

class StackedLinesTest(ImageComparisonTestCase):
    def __init__(self, testCaseName):
        super(StackedLinesTest,self).__init__("stackedlines.png")

    def constructImage(self):
        line1 = Line()
        line2 = Line()
        line3 = Line()

        line1.xValues = range(0,10)
        line1.yValues = [2,5,2,3,2,2,1,0,1,0]
        line2.xValues = range(0,10)
        line2.yValues = [3,1,2,3,2,1,5,3,1,7]
        line3.xValues = range(0,10)
        line3.yValues = [2,1,3,1,3,4,1,4,5,0]

        stack = StackedLines()
        stack.addLine(line1, "red")
        stack.addLine(line2, "green")
        stack.addLine(line3, "blue")

        plot = Plot()
        plot.setYLimits(0, 7)
        plot.add(stack)
        plot.save(self.imageName)

ImageComparisonTestCase.register(StackedLinesTest)

if __name__ == "__main__":
    test = StackedLinesTest()

    test.constructImage()