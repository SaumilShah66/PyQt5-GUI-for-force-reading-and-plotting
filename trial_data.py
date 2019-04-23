class all_test_data():
	def __init__(self):
		self.y_values = []
		self.displacement_values = []
		self.time_values = []
		self.checkboxes = []
		self.name = []
	
	def add_data(self, y_values, displacement_values, time_values, checkboxes, name):
		self.y_values.append(y_values)
		self.displacement_values.append(displacement_values)
		self.time_values.append(time_values)
		self.checkboxes.append(checkboxes)
		self.name.append(name)



class data_printer():
        def __init__(self, data):
                self.data = data

        def y_print(self):
                print(self.data.y_values)


t = all_test_data()
t.add_data(1,1,1,1,1)
dp = data_printer(t)
dp.y_print()
t.add_data(2,2,2,2,2)
t.add_data(3,3,3,3,3)
dp.y_print()