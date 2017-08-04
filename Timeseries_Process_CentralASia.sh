# Historical Timeseries SWE Processing SCripts for Central Asia Region
# Scripts written by Nishan Kumar Biswas
# PhD Student and Graduate Research Assistant 
# Dept. of CEE, University of Washington
# email: nbiswas@uw.edu, nishan.wre.buet@gmail.com

# Provide input date here
input_start=2001-10-01
# Provide end date in here
input_end=2017-01-02

# Converting input date in  DAtetime format
startdate=$(date -I -d "$input_start")
# Conevrting end date into date time format
enddate=$(date -I -d "$input_end")
# Assigning date variable to a temporary variable
d="$startdate"
# Starting while loop to go from start date to end date
while [ "$d" != "$enddate" ]; do 
# Taking processing date from the temporary variable
curDate=$(date -d "$d" +"%Y%m%d")
# Saving date into a file so that python script can use it
echo ${curDate} > date.info
# extracting year variable from the date variable
curYear=$(date -d "$d" +"%Y")
# Region name of Central Asia (specified in file name)
region=('CA')
# ID used in LIS Visualization Framework (to connect with the raster visualization)
regionID=('centralasia')
# Models used in Central Asia Region (Specified in LIS Output filename)
model=('NOAH36')
# Model IDs used in LIS Visualization (in LIS Atlas, folder name is provided as this)
modelID=('noah')
# Parameter Accummulation Type (daily accummulation for Central Asia region, no monthly)
parAcc=('daily')
# Parameters used in LIS Visualization(Currently only SWE timeseries will be calculated)
paramID=('swe')
# Parameter IDs used in LIS Visualization Framework (Actual Parameter name provided in output file to define those parameters)
param=('SWE_mm')
# Loop over the regions of Central Asia
for((k=0; k<${#region[*]}; k++))
do
#Loop over the models of Central Asia
for((i=0; i<${#model[*]}; i++))
do
# Saving Region name into a temporary text file so that Python scripts can use it 
echo ${regionID[k]} > region.info
# Downloading the output file from Portal.nccs.gov website
wget --no-check-certificate https://portal.nccs.nasa.gov/lisdata_pub/FEWSNET/AFRICA_GESDISC/${model[i]}_RG_${region[k]}/$curYear/FLDAS_${model[i]}_A_${region[k]}_D.A$curDate.001.nc
#Loop over the parameters specified in param variable 
for((j=0; j<${#param[*]}; j++))
do
#For NETCDF File, needed to turn off this option to extract necessary parameters from the netcdf file
export GDAL_NETCDF_BOTTOMUP=NO
# Translating parameter into ESRI ASCII file from the NETCDF File
gdal_translate -of AAIGrid NETCDF:"FLDAS_${model[i]}_A_${region[k]}_D.A$curDate.001.nc":${param[j]} ${regionID[k]}_${paramID[j]}_$curDate.asc
done
#rm *.nc
rm *.xml
# Python script to modify the AAI Grid file (need to specify the resolution and also need to flip the Raster as the option GDAL_NETCDF_BOTTOMUP is set up as NO)
python correctasiaraster.py
# Python Script to calculate Timeseries average using the selected basin file, basin index raster and the ESRI ASCII file of the parameter of that particular date
python swe_timeseries.py
#rm *.asc
done
done
# Assigning new date to the temporary variable, more specifically adding 1 day to the date variable
d=$(date -I -d "$d + 1 day")
done

