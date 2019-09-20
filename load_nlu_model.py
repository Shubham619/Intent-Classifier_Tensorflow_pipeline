from rasa_nlu.model import Metadata, Interpreter

def load_model():
	# where `model_directory points to the folder the model is persisted in`
	interpreter = Interpreter.load('models/current/nlu_model')
	print(interpreter.parse("Hello All,    After updating to android 9, the Portrait lock/Auto Rotate option is missing from my phone. I cant find it in settings or anywhere, I even tried a full settings reset but still unable to find it. I am attaching a screenshot of my notification pull down drawer. the option is no where to be seen. Please help been struggling with this for long.    I am posting 2 images for reference"))
	
if __name__ == '__main__':
	load_model()


