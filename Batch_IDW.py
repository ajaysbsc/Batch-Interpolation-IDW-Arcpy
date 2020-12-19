import arcpy
from arcpy import env
from arcpy.sa import *

# Set environment settings
env.workspace = "/working directory/"

# Set local variables
input = "rh1.shp"
cellSize = 0.027078076
power = 2
searchRadius = RadiusVariable(12, 150000)
# getting the name of fields 
zfield = [f.name for f in arcpy.ListFields(input)]
#printing the zfield for selection of necessary fields 
zfield
# removing the latitude longitude field by defining size of field 
# here in this case i have removed first 4 field
zfield = zfield[4::]
loop for selecting the z value 
for f in zfield:
    outfile = outPath + f
    outIDW = Idw(input, f, cellSize, power, SearchRadius)
    outIDW.save("/path/" + f + ".tif")        # change the /path/ to the folder where output to be saved 
