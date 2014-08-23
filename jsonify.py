import os
files = [f for f in os.listdir('.') if os.path.isfile(f)]
for file in files:
	if(file != "jsonify.py"):
		print(file)
