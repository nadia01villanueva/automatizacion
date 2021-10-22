import xml.etree.cElementTree as et
from xml.etree.ElementTree import SubElement, parse

xml_file= parse('registro.xml')
root = et.Element("Edificio2_De_La_Universidad_Tecnologica_De_Coahuila")
xmlRoot = xml_file.getroot()

se = et.SubElement(root,"Mecatronica")
et.SubElement(se, "Nombre").text = "Rodrigo Alvarez Reyes"
et.SubElement(se, "Matricula").text = "18047277"

xmlRoot.append(se)
xml_file.write("registro.xml",xml_declaration=True)
