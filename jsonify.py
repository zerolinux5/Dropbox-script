import os
import subprocess

files = [f for f in os.listdir('.') if os.path.isfile(f)]
count = 0;

with open('output.json', 'w') as output:
	output.write("{\"all\":[");
	for file in files:
		if(file != "jsonify.py" and file != "output.json"):
			if(count != 0):
				output.write(",")
			filestrip = file[:-4]
			name = "{\"name\": \"" + filestrip + "\""
			output.write(name)
			filename = "hello" + str(count) + ".txt"
			p = subprocess.Popen("mkdir hello2.txt", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
			p.wait()
			output.write("}")
	output.write("]}")
