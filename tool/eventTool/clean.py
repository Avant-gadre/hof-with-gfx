import re
import os
import io
import os.path
import sys
import datetime
# sys.path.append('../')
import core

# 路径识别
# 根目录
time0 = datetime.datetime.now()
rootpath = os.path.abspath(os.path.join(os.getcwd(), "../.."))
# evenstpath = os.path.join(rootpath,'events','')
eventfiles = core.getTxtName(core.eventpath)
eventContxt = []
outpath = os.path.join(rootpath,'tool','out','')
if not os.path.exists(outpath):
    os.makedirs(outpath)
eventsCollection = []

evetcontext = []
num = 0

for eventfiletxt in eventfiles:
    counter_leave = 0
    eventfile = os.path.join(core.eventpath, eventfiletxt)
    with open(eventfile, "r", encoding= 'utf-8') as file:
        eventfull = file.readlines()
        evetcontext.extend(eventfull)
    # print(eventfull)
    # 分块
    for line in eventfull:
        if counter_leave == 0 and '=' in line and '{' in line :
            num += 1
            # 这里是起始位置
            eventContxt = [line]
        elif num > 0:
            eventContxt.append(line)
            if counter_leave == 1 and '}' in line:
                # 这里是结束位置
                eventsCollection.append(eventContxt)
        counter_leave += line.count('{')
        counter_leave -= line.count('}')
    # break
# print(eventfiles)
# a =len(eventsCollection)
print(len(eventsCollection))
time1 = datetime.datetime.now()
EMPlist = []
idlist = []
for event in eventsCollection:
    eventid = ''
    eventtrigger = 0
    counter_leave = 0
    for line in event:
        if 'id' in line and '=' in line and counter_leave == 1:
            eventid = line.strip()
            eventid = re.sub(r'id = ','',eventid).strip()
            # eventid = re.sub(r'=', '', eventid).strip()
            counter_leave = 0
            break
        counter_leave += line.count('{')
        counter_leave -= line.count('}')
    for line in event:
        if 'is_triggered_only' in line and 'yes' in line and '#' not in line:
            eventtrigger = 1
            break
    idlist.append(eventid)
    EMP = core.eventBlock(eventid,eventtrigger,event)
    EMPlist.append(EMP)
#在事件内部搜索
time2 = datetime.datetime.now()
overid = set()
i = 0
idset = set()
print(len(EMPlist))
for emp in EMPlist:
    if emp.trigger > 0:
      idset.add(emp.id)
    i += 1
    counter_leave = 0
    for line in emp.context:
        if counter_leave > 1 and re.search(r'[^0-9 ]+\.[0-9]+',line) :
            temp = re.search(r'[^0-9 ]+\.[0-9]+',line).group().strip()
            if temp == emp.id:
                continue
            else:
                overid.add(temp)
        counter_leave += line.count('{')
        counter_leave -= line.count('}')

print(datetime.datetime.now() - time2)
with open(outpath+'overlist.txt','w+',encoding='utf-8') as file22:
    file22.write('\n'.join(idset))

print(datetime.datetime.now() - time2)




# 读取国策 决议等等
focusfiles = core.getTxtName(core.focuspath)
on_actionsfiles = core.getTxtName(core.on_actionspath)
decisionsfiles = core.getTxtName(core.decisionspath)
scripted_effectsfiles = core.getTxtName(core.scripted_effects)

othercontext = []
for focus in focusfiles:
    file00 = os.path.join(core.focuspath, focus)
    with open(file00, "r", encoding= 'utf-8') as file01:
        conts = file01.readlines()
        othercontext.extend(conts)
for on_ac in on_actionsfiles:
    file00 = os.path.join(core.on_actionspath, on_ac)
    with open(file00, "r", encoding= 'utf-8') as file02:
        conts = file02.readlines()
        othercontext.extend(conts)
for deci in decisionsfiles:
    file00 = os.path.join(core.decisionspath, deci)
    with open(file00, "r", encoding= 'utf-8') as file03:
        conts = file03.readlines()
        othercontext.extend(conts)
for scrpit in scripted_effectsfiles:
    file00 = os.path.join(core.scripted_effects, scrpit)
    with open(file00, "r", encoding= 'utf-8') as file04:
        conts = file04.readlines()
        othercontext.extend(conts)


for line in othercontext:
    if  re.search(r'[^0-9 ]+\.[0-9]+',line) :
        temp = re.search(r'[^0-9 ]+\.[0-9]+',line).group().strip()
        overid.add(temp)
finalset = idset.difference(overid)
ss = list(finalset)
ss.sort()
print(ss)
with open(outpath+'savelist.txt','w+',encoding='utf-8') as file23:
    file23.write('\n'.join(ss))

print(datetime.datetime.now() - time2)