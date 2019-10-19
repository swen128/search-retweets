deps:
	pip3 install -r requirements_to_freeze.txt
	pip3 freeze > requirements.txt
