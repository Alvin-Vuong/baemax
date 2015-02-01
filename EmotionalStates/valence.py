import numpy

class MyOVBox(OVBox):
	def __init__(self):
		OVBox.__init__(self)
        
    def initialize(self):
		# nop
		return
        
	def process(self):
		# self.input[0] is the F3 alpha wave
		# self.input[1] is the F4 alpha wave
		# self.input[2] is the F3 beta wave
		# self.input[3] is the F4 beta wave
		self.output[0].append((self.input[1] / self.input[3]) - (self.input[0] / self.input[2]))
    
    def uninitialize(self):
		# nop
		return

box = MyOVBox()
