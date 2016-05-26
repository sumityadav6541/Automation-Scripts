from shutil import copyfile
import os

os.system("mvn clean install")
print "build complete"

source = ""
destination = ""

try:
    os.remove(destination)
except:
    pass

copyfile(source, destination)
print "copied the new deployble files !"
