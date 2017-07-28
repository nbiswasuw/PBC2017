import datetime
import os
dirpath = 'rainfall/'
startdatestr='20170101'
startdate = datetime.datetime.strptime(startdatestr, '%Y%m%d')
for fn in os.listdir(dirpath):
    timeseriesfilepath = os.path.join(dirpath, fn)
    timeseriesfile = open(timeseriesfilepath, 'r')
    timeseriesdata = timeseriesfile.readlines()
    tmseriesdate = []
    tmseriesdata = []
    for i in xrange(len(timeseriesdata)):
        data = timeseriesdata[i].split(',')
        tmseriesdate.append(datetime.datetime.strptime(data[0], '%Y%m%d'))
        tmseriesdata.append(float(data[1]))
    csvcontent = []                     
    for i in xrange(366):
        time = datetime.timedelta(days=i)
        data = []
        for j in xrange(len(tmseriesdate)):
            if int(tmseriesdate[j].strftime('%j')) == (i+1):
                data.append(tmseriesdata[j])
        maxval = max(data)
        minval = min(data)
        meanval = sum(data)/len(data)
        csvcontent.append((startdate+time).strftime('%Y-%m-%d') + "," + "{0:.3f}".format(meanval) + "," + "{0:.3f}".format(maxval) + "," + "{0:.3f}".format(minval))
        
    refyears = [2004, 2006, 2008]
    for i in xrange(len(refyears)):
        refdatasets = []
        for j in xrange(len(tmseriesdata)):
            if int(tmseriesdate[j].strftime('%Y')) == refyears[i]:
                refdatasets.append(tmseriesdata[j])
        for k in xrange(len(refdatasets)):
            csvcontent[k] = csvcontent[k] + ',' + "{0:.3f}".format(refdatasets[k])
    with open(dirpath + fn[:-4] + ".csv", 'w') as txt:
        txt.write('date,average,maximum,minimum,ref2010,ref2015,current')
        for i in xrange(len(csvcontent)):
            txt.write('\n' + csvcontent[i])
