import os
import subprocess

files = [f for f in os.listdir('.') if os.path.isfile(f)]
count = 0;

with open('output.json', 'w') as output:
	for file in files:
		if(file != "jsonify.py" and file != "output.json"):
			output.write(file)
			output.write('\n')
			filename = "hello" + str(count) + ".txt"
			p = subprocess.Popen("mkdir hello2.txt", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
			p.wait()
