# Historical Timeseries backened processing of LIS ATLAS Output for Central Asia Region
# Input is NETCDF Format dataset from NCCS Portal
# This script is used to Flip the ESRI ASCII file generated from the Bash Script
# Input: Extracted ESRI ASCII file from the NETCDF file and date to define the file
# Scripts written by Nishan Kumar Biswas
# Phd Student and Graduate Research Assistant
# Dept of Civil and Environmental Engineering, University of washington
# email: nbiswas@uw.edu, nishan.wre.buet@gmail.com
## Special Note: During extracting the ESRI ASCII file, one option is turned of: GDAL_NETCDF_BOTTOMUP=NO and the result got flipped.
## This script again flip it to return the  ESRI File into original state

# Reading date.info to define the processing date
datefile=open('date.info', 'r')
date = datefile.read()[:-1]
# Reading the flipped ESRI ASCII file from the the bash script 
rasterfilepath=open('FLIP_'+ date + '.asc', 'r')
rasterfile = rasterfilepath.readlines()
rasterfile[2] = 'xllcorner    30.000\n'
rasterfile[3] = 'yllcorner    21.000\n'
rasterfile[4] = 'cellsize     0.01\n'
# Writing the corrected ASCII file
with open('Corr_' + date + '.asc', 'w') as txt:
	for i in xrange(6):
		txt.write(rasterfile[i])
	for j in xrange(len(rasterfile)-6):
		txt.write(rasterfile[len(rasterfile)-j-1])
