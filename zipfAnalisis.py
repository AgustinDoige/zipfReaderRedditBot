import os
import io

Mdictionary = {}


for it in os.listdir():
	if "thread_" in it:

		with open(it,"r") as f:
			while True:
				try:
					character = f.read(1)
				except UnicodeDecodeError:
					character = "Error"

				if (character == ''):
					break

				print(character)

				try:
					Mdictionary[character] = Mdictionary[character] + 1
				except KeyError:
					Mdictionary[character] = 1


with open("results.txt","w") as g:
	for keys,values in Mdictionary.items():
		g.write(str(keys)+" : "+str(values)+"\n")

print("Completed")

