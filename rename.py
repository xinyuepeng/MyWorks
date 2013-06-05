#!/usr/bin/env python

import os
import shutil
import subprocess
import StringIO

#subprocess.call(["ls", "-l"])
p = subprocess.Popen('ls *.mobi', shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
out, err = p.communicate()
print out, ""
print type(out)

file_like_string = StringIO.StringIO(out)
print file_like_string.readline()
print type(file_like_string)

counter = 1
while True:
    line = file_like_string.readline()
    if not line:
        break
    line = line.strip('\n')
    items = line.split('\\')
    #print "%s: %s" % (counter, line)
    target = items[5].strip();
    target = target.strip('\n')
    print line ," --> ", target
    shutil.copy(line, target)
    counter += 1
