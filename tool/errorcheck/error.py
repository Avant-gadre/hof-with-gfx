import os.path

import core


docpath = core.getDocPath()
errorpath = os.path.join(docpath,'Paradox Interactive','Hearts of Iron IV','logs','error.log')

with open(errorpath,'r+',encoding='utf-8') as f:
    errorC = f.readlines()
portraitError = []
for line in errorC:
    line.lower()
    if 'portrait' in line:
        portraitError.append(line)
    elif 'gfx/leader' in line:
        portraitError.append(line)
print(len(portraitError))
for line in portraitError:
    print(line)



# print(path1)