import numpy

class MyOVBox(OVBox):
	def __init__(self):
		OVBox.__init__(self)
        
    def initialize(self):
		# nop
		return
        
	def process(self):
		# self.input[0] is the alpha wave
		# self.input[1] is the beta wave
        total = 0
        for chunkIndex in range(len(self.input[0])):
            total += self.input[0][chunkIndex]
        average = total/len(self.input[0])
        self.output[0].append(average)
        
    def uninitialize(self):
		# nop
		return

box = MyOVBox()
