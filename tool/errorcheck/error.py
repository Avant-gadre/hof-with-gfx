import os.path

import core


docpath = core.getDocPath()
errorpath = os.path.join(docpath,'Paradox Interactive','Hearts of Iron IV','logs','error.log')

with open(errorpath,'r+',encoding='utf-8') as f:
    errorC = f.readlines()
print('error共有',str(len(errorC)),"个")
portraitError = []
gfxError = []
for line in errorC:
    line.lower()
    if 'gfx' in line and 'font' not in line:
        gfxError.append(line)
    if 'portrait' in line:
        portraitError.append(line)
    elif 'gfx/leader' in line:
        portraitError.append(line)
print(len(portraitError))
for error in portraitError:
    print(error)



# print(path1)