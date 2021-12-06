# very short script for copying file to another file


# importing the require module
from sys import argv    # for passing commandline argument and specify filename copy from to

from os.path import exists # to check if file to copy to exist

# specifying commandline args : filename to copy from and to

script, from_file, to_file = argv

# opening file in read mode and reading the content

indata = open(from_file, 'r').read()

# opening the new file in write mode and writting to it.
#out_file = open(to_file, 'w').write(indata)

with open(to_file, 'w') as file:
    file.write(indata)

print(f"{len(indata)} bytes of content copied")

