#!/usr/bin/env python2

import os, sys, re
from datetime import datetime

# getdatetime
now = datetime.now().strftime('%Y%m%d%H%M%S')
 
# settings
chapters_folder = "chapters"
result_folder = "result"
resultfile = "%s.pdf" %(now)

# keep number of older result files
keep_oldresult = 4

def getChapters():
    chapters = " "
    for filename in os.listdir(chapters_folder):
        if os.path.isfile(os.path.join(chapters_folder,filename)):
            print(filename)
            chapters += "%s/%s " % (chapters_folder, filename)
    return chapters
    
def getRemoveOldResults():
    fileData = {}
    for fname in os.listdir(result_folder):
        fileData[fname] = os.stat(os.path.join(result_folder,fname)).st_mtime
    sortedFiles = sorted(fileData.items())
    for file in range(0, len(sortedFiles) - keep_oldresult):
        os.remove(os.path.join(result_folder,sortedFiles[file][0]))
    
cmd_string ="pandoc -p -f markdown \
            --csl=resources/ieee.csl \
            --chapters \
            --number-sections \
            --include-before-body=resources/startthesis.tex \
            --include-after-body=resources/appendix.tex \
            --template=resources/ba_template.tex \
            -o %s/%s \
            --bibliography resources/thesis.bib \
            settings.yaml %s" % (result_folder, resultfile, getChapters())


getRemoveOldResults()
os.system(cmd_string)
if sys.platform.startswith("win"):
    os.startfile(os.path.join("result", resultfile))
