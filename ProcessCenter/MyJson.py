import json

class MyEncoder(json.JSONEncoder):
	def default(self, obj):
		dictObject = {}
		dictObject['__class__'] = obj.__class__.__name__
		dictObject['__module__'] = obj.__module__
		dictObject.update(obj.__dict__)

		return dictObject

class MyDecoder(json.JSONDecoder):
	def __init__(self):
		json.JSONDecoder.__init__(self, object_hook = self.dict2object)

	def dict2object(self, dictObject):
		#convert dict to object

		if'__class__' in dictObject:
			class_name = dictObject.pop('__class__')
			#print(class_name)
			module_name = dictObject.pop('__module__')
			#print(module_name)
			module = __import__(module_name, globals(), locals(), ['Token', 'Datagram'], 0)
			#print(module)
			class_ = getattr(module, class_name)
			args = dict((key, value) for key, value in dictObject.items()) #get args
			newInstance = class_(**args) #create new instance
			print("convert dict to object3")
		else:
			newInstance = dictObject
		return newInstance