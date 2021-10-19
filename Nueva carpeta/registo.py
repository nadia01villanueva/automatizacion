import xml.etree.cElementTree as et 

 

root = et.Element("Edificio2_De_La_Universidad_Tecnologica_De_Coahuila") 

 

se = et.SubElement(root,"Desarollo_Y_Gestion_De_Software") 

et.SubElement(se, "Nombre").text =  "Luicia_Guadalupe_Rodriguez_Mata" 

et.SubElement(se, "Matricula").text =  "18030206" 

et.SubElement(se, "Nombre").text =  "Gerardo_Daniel_Ortiz_Hernandez" 

et.SubElement(se, "Matricula").text =  "18347285" 

et.SubElement(se, "Nombre").text =  "Gabriela_Gonazlez_Gaona" 

et.SubElement(se, "Matricula").text =  "18928277" 

et.SubElement(se, "Nombre").text =  "Luis_Angel_Mendez_Garcia" 

et.SubElement(se, "Matricula").text =  "18772375" 

et.SubElement(se, "Nombre").text =  "Santiago_Aleanrdro_Sanchez_Reyes" 

et.SubElement(se, "Matricula").text =  "18995254" 

 

se = et.SubElement(root,"Entornos_Virtuales_Y_Negocios_Digitales") 

et.SubElement(se, "Nombre").text =  "Maria_Laura_Vielma_Luna" 

et.SubElement(se, "Matricula").text =  "18007600" 

et.SubElement(se, "Nombre").text =  "Mario_Ivan_Fuentes_Contreras " 

et.SubElement(se, "Matricula").text =  "18347285" 

et.SubElement(se, "Nombre").text =  "Angel_Manuel_Lopez_Ochoa" 

et.SubElement(se, "Matricula").text =  "18030066" 

et.SubElement(se, "Nombre").text =  "Rubi_Sarahi_Alvarado_Perez" 

et.SubElement(se, "Matricula").text =  "18654783" 

et.SubElement(se, "Nombre").text =  "Eva_Daniela_Alarcon_Franco" 

et.SubElement(se, "Matricula").text =  "18000568" 

 

se = et.SubElement(root, "Redes_Inteligentes_Y_Cibersegurida") 

et.SubElement(se, "Nombre").text =  "Octavio_Maldonado_Morales" 

et.SubElement(se, "Matricula").text =  "18055500" 

et.SubElement(se, "Nombre").text =  "Ruben_Mendez_Gomez" 

et.SubElement(se, "Matricula").text =  "18441212" 

et.SubElement(se, "Nombre").text =  "Karla_Vanessa_Reyna_Reyes" 

et.SubElement(se, "Matricula").text =  "18558274" 

et.SubElement(se, "Nombre").text =  "Gloria_Guadalupe_Salas_Garcia" 

et.SubElement(se, "Matricula").text =  "18288340" 

et.SubElement(se, "Nombre").text =  "Nadia_Itzel_Villanueva_Cortes" 

et.SubElement(se, "Matricula").text =  "18040109" 

 

tree = et.ElementTree(root) 

tree.write("registro.xml", xml_declaration=True) 
