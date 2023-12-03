import arcpy
import arcpy.ddd
source = r"C:\Users\Dominic Ayon\Desktop\GEOG392Lab\GISProgramming\Lab_7\Lab07_Data\\"
results = r"C:\Users\Dominic Ayon\Desktop\GEOG392Lab\GISProgramming\Lab_7\Lab07_Results\\"
b1 = arcpy.sa.Raster(source + "LT05_L2SP_026039_20110803_20200820_02_T1_SR_B1.TIF")
b2 = arcpy.sa.Raster(source + "LT05_L2SP_026039_20110803_20200820_02_T1_SR_B2.TIF")
b3 = arcpy.sa.Raster(source + "LT05_L2SP_026039_20110803_20200820_02_T1_SR_B3.TIF")
b4 = arcpy.sa.Raster(source + "LT05_L2SP_026039_20110803_20200820_02_T1_SR_B4.TIF")
comp = arcpy.CompositeBands_management([b1, b2, b3, b4], results + "combined.tif")

az = 315
alt = 45
shadows = "NO_SHADOWS"
z_fac = 1
arcpy.ddd.HillShade(r"C:\Users\Dominic Ayon\Desktop\GEOG392Lab\GISProgramming\Lab_7\Lab07_Data\n30_w097_1arc_v3.tif",
                    r"C:\Users\Dominic Ayon\Desktop\GEOG392Lab\GISProgramming\Lab_7\Lab07_Results\hill_shade.tif",
                    az, alt, shadows, z_fac)

output_mes = "DEGREE"
arcpy.ddd.Slope(r"C:\Users\Dominic Ayon\Desktop\GEOG392Lab\GISProgramming\Lab_7\Lab07_Data\n30_w097_1arc_v3.tif",
                r"C:\Users\Dominic Ayon\Desktop\GEOG392Lab\GISProgramming\Lab_7\Lab07_Results\slopes.tif",
                output_mes, z_fac)
