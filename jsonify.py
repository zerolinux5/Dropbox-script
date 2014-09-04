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
			name = "{\"name\": \"" + filestrip + "\" , "
			output.write(name)

			body = ""
			inText = open(file, 'r')
			while 1:	
				lines = inText.readline(100000)
				if not lines:
					break;
				for line in lines:
					body += line
			bodyText = "\"body\": \"" + body + "\" , "
			output.write(bodyText)		

			image = filestrip + ".txt"
			
			filename = "hello" + str(count) + ".txt"
			p = subprocess.Popen("cp " + image + " ~/Dropbox/public", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
			p.wait()
			output.write("}")
	output.write("]}")
