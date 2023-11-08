import arcpy
f_path = r'C:\Users\Dominic Ayon\Desktop\GEOG392Lab\GISProgramming'
db_name = 'GEOG392_LAB4.gdb'
db_path = f_path + '\\' + db_name
arcpy.CreateFileGDB_management(f_path, db_name)
excel_path = r'C:\Users\Dominic Ayon\Desktop\GEOG392Lab\GISProgramming\Lab_4\Lab04_Data\garages.csv'
garage_layer = 'Garage_Points'
garage = arcpy.MakeXYEventLayer_management(excel_path, 'X', 'Y', garage_layer)
arcpy.FeatureClassToGeodatabase_conversion(garage, db_path)
garage_points = db_path + '\\' + garage_layer
campus = r'C:\Users\Dominic Ayon\Desktop\GEOG392Lab\GISProgramming\Lab_4\Lab04_Data\Campus.gdb'
structs = campus + '\\' + 'Structures'
builds = campus + '\\' + 'Buildings'
arcpy.Copy_management(structs, builds)
spatial = arcpy.Describe(builds).spatialReference
arcpy.Project_management(garage_points, db_path + '\\' + 'garage_points_redone', spatial)
garagebuff = arcpy.Buffer_analysis(db_path + '\\' + 'garage_points_redone', db_path + '\\' + 'garage_points_buffed',
                                   150)
arcpy.Intersect_analysis([garagebuff, builds], db_path + '\\' + 'garage_intersects_all', 'ALL')
arcpy.TableToTable_conversion(db_path + '\\' +'garage_intersects_all.dbf', r'C:\Users\Dominic Ayon\Desktop\GEOG392Lab\
GISProgramming\Lab_4\Lab04_Data', 'nearbuildings.csv')
