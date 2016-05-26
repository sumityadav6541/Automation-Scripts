## Import Libraries
import os
from shutil import copyfile
from shutil import rmtree
import psutil


## execute build
print "-"*50
print "executing the gradle clean build..."
print "-"*50
returnVal = os.system("gradle clean build")


if not returnVal:
	print "-"*50
	print "build complete"
	print "-"*50
else:
	print "-"*50
	print "Build Failed !"
	print "-"*50
	sys.exit()


## kill existing tomcat instances
for proc in psutil.process_iter():
    if proc.name()=='java.exe':
        proc.kill()



sourceDir = ''
genFile = ''
destDir = ''

## copy war
try:
    os.remove(genFile)
except:
    pass

try:
    rmtree(destDir)
except:
    pass
print "removed the old deployed file"

copyfile(sourceDir,destDir)
print "copied the new generated file"

## start tomcat again in debug mode
print ""
os.chdir("C:\\apache-tomcat-7.0.69\\bin")
os.system("catalina jpda start")
