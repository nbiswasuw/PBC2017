datefile=open('date.info', 'r')
seldate = datefile.read()[:-1]
metadata=open('region.info', 'r')
region = metadata.read()[:-1]

#Reading Selected Basin File
selbasinpath='metadata/'+ region + 'basin.txt'
basinfile = open(selbasinpath, 'r')
lines = basinfile.readlines()
selbasins=[]
for x in xrange(len(lines)):
        line = lines[x].split()
        selbasins.append(int(line[0]))


#Reading Basin Extent File
basingridpath= 'metadata/'+ region + 'basinindex.asc'
basinfile = open(basingridpath, 'r')
lines = basinfile.readlines()
line = lines[0].split()
ncols = int(line[1])
line = lines[1].split()
nrows = int(line[1])
basinid = []
for x in range(0, nrows):
        line = lines[x+6].split()
        for y in range(0, ncols):
                basinid.append(int(line[y]))

#Reading Qs_tAvg File
qsfilepath= region + '_noah_qstavg_' + seldate +'.asc'
qsfile = open(qsfilepath, 'r')
lines = qsfile.readlines()
qstavg = []
for x in range(0, nrows):
        line = lines[x+6].split()
        for y in range(0, ncols):
                qstavg.append(float(line[y]))
                
#Reading QsbTavg File 
qsbfilepath= region + '_noah_qsbtavg_' + seldate +'.asc'
qsbfile = open(qsbfilepath, 'r')
lines = qsbfile.readlines()
qsbtavg = []
for x in range(0, nrows):
        line = lines[x+6].split()
        for y in range(0, ncols):
                qsbtavg.append(float(line[y]))

strContent = ""
basinIDs = []
meanbasins = []
for i in xrange(len(selbasins)):
    #print(selbasins[i])
    sumparam = 0
    cntparam = 0
    avgparam = 0
    for j in xrange(len(basinid)):
        if selbasins[i]==basinid[j] and qstavg[j]!=-9999.0 and qsbtavg[j]!=-9999.0:
            sumparam = sumparam + qstavg[j] + qsbtavg[j]
            cntparam = cntparam + 1
    avgparam = sumparam/float(cntparam)
    basinIDs.append(selbasins[i])
    meanbasins.append(avgparam*86400)

for j in xrange(len(meanbasins)):
    with open('Timeseries/' + region + '/noah_runoff_' + str(selbasins[j]) +'.txt', 'a') as text:
        text.write(seldate + ',' + str(meanbasins[j]) + '\n')

