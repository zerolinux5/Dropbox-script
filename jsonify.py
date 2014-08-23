import os
files = [f for f in os.listdir('.') if os.path.isfile(f)]
with open('output.json', 'w') as output:
	for file in files:
		if(file != "jsonify.py" and file != "output.json"):
			output.write(file)
			output.write('\n')
