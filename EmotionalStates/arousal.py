import numpy

class MyOVBox(OVBox):
	def __init__(self):
		OVBox.__init__(self)
		self.signalHeader = None

    def initialize(self):
		# nop
		return
        
	def process(self):
		# self.input[0] is the alpha wave average
		# self.input[1] is the beta wave average
		self.output[0] = self.input[1] / self.input[0]

    def uninitialize(self):
		# nop
		return
        
box = MyOVBox()
