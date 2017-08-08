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

#print(len(basinid))
#Reading Precipitation ASCII File
rainfilepath= region + '_noah_precipitation_' + seldate +'.asc'
rainfile = open(rainfilepath, 'r')
lines = rainfile.readlines()
rainf = []
for x in range(0, nrows):
        line = lines[x+6].split()
        for y in range(0, ncols):
                rainf.append(float(line[y]))
                

strContent = ""
basinIDs = []
meanbasins = []
for i in xrange(len(selbasins)):
    #print(selbasins[i])
    sumparam = 0
    cntparam = 0
    avgparam = 0
    for j in xrange(len(basinid)):
        if selbasins[i]==basinid[j] and rainf[j]!=-9999.0:
            sumparam = sumparam + rainf[j]
            cntparam = cntparam + 1
    avgparam = sumparam/float(cntparam)
    basinIDs.append(selbasins[i])
    meanbasins.append(avgparam*86400)
for j in xrange(len(meanbasins)):
    with open('Timeseries/' + region + '/noah_precipitation_' + str(selbasins[j]) +'.txt', 'a') as text:
        text.write(seldate + ',' + str(meanbasins[j]) + '\n')

#return basinIDs
#return meanbasins
    #strContent = strContent + "{}\n".format(str(selbasins[i]) + "    " + str(avgparam))
#with open(region + '_stat_' + seldate +'.txt', 'w') as txt:
    #txt.write(strContent)
