from wxPython.wx import *

class Gradient:
	def __init__(self):
		self.spline = False
		self.numberOfColors = 0
		self.color = []
		self.colorPosition = []

	def loadGradient(self, spline, numberOfColors, color, colorPosition):
		self.spline = spline
		self.numberOfColors = numberOfColors
		self.color = color
		self.colorPosition = colorPosition
		
	def getColorAt(self, position):
		for i in range(0, self.numberOfColors):
			if position <= self.colorPosition[i+1]:
				break

		c1 = self.color[i]
		c2 = self.color[i+1]

		if self.colorPosition[i+1] > self.colorPosition[i]:
			delta = float(position - self.colorPosition[i]) / float(self.colorPosition[i+1] - self.colorPosition[i])
		else:
			delta = 0

		if self.spline:
			ar = 2*c1.Red() - 2*c2.Red()
			br = -3*c1.Red() + 3*c2.Red()
			dr = c1.Red()

			ag = 2*c1.Green() - 2*c2.Green()
			bg = -3*c1.Green() + 3*c2.Green()
			dg = c1.Green()

			ab = 2*c1.Blue() - 2*c2.Blue()
			bb = -3*c1.Blue() + 3*c2.Blue()
			db = c1.Blue()

			delta2 = delta*delta
			delta3 = delta2*delta

			c = wxColour(int(ar*delta3 + br*delta2 + dr),
				int(ag*delta3 + bg*delta2 + dg),
				int(ab*delta3 + bb*delta2 + db))
		else:
			c = wxColour(int(c1.Red()*(1-delta) + c2.Red()*delta),
				int(c1.Green()*(1-delta) + c2.Green()*delta),
				int(c1.Blue()*(1-delta) + c2.Blue()*delta))

		return c
