datefile=open('date.info', 'r')
date = datefile.read()[:-1]
rasterfilepath=open('FLIP_'+ date + '.asc', 'r')
rasterfile = rasterfilepath.readlines()
with open('Corr_' + date + '.asc', 'w') as txt:
	for i in xrange(6):
		txt.write(rasterfile[i])
	for j in xrange(len(rasterfile)-6):
		txt.write(rasterfile[len(rasterfile)-j-1])
