#rodar os imports
import arcpy
import os
from arcpy import env
import csv
#juliana
#0º
#Adicione todos os shps no arcgis


#1º
# aqui vc precisa colocar onde esta entre aspas o caminho de onde
# estao os pontos, essa  pasta que vc me passou, mas só pode ter os shp quequer 
#fazer a operaca dentro dessa pasta
env.workspace=r'F:\data\Dani_ramos\join_tabel\shapes_pontos'


#2º
# vc precisa criar uma pasta para colca suas tabelas de saida 
#pra nao confundi, e onde esta xxx vc cola o caminho, vai fica +/- assim c:\xxxx\saidas, tambem entre as aspas
os.chdir(r'xxx')


fc=arcpy.ListFeatureClasses()

#3º 
# cola o mesmo caminhho do passp 2
env.workspace=r'F:\data\Dani_ramos\join_tabel\shapes_pontos\temp'

#daqui pra baixo nao precisa mudar nada
for i in fc:
    inps=i.replace('.shp','')
    out=inps+'_eucdist.txt'
    
    out_final=inps+'_eucdist_joinFinal.txt'
    arcpy.PointDistance_analysis(inps,inps,out,"")
    out_inp=out.replace('.txt','')
    arcpy.JoinField_management(out_inp,"INPUT_FID",inps,"FID")
    
    out_final_inp=out.replace('.txt','')
    fields = arcpy.ListFields(out_final_inp)
    field_names = [field.name for field in fields]
    with open(out_final,'w') as f:  
        w = csv.writer(f)  
        #--write all field names to the output file  
        w.writerow(field_names) 
        
        for row in arcpy.SearchCursor(out_final_inp):  
            field_vals = [row.getValue(field.name) for field in fields]  
            w.writerow(field_vals)  
        del row          
        f.close()
    