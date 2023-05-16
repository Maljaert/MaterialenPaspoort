import ifcopenshell
from ifcopenshell.util.element import get_elements_by_material as ele_by_materials

# Open the IFC file
ifc_file = ifcopenshell.open('test.ifc')
print(ifc_file.schema)

direct_materials = ifc_file.by_type('IfcMaterial')
# Print the name of each direct material
for material in direct_materials:
    if material.Name:
        print(material.Name)

    for ele in ele_by_materials(ifc_file=ifc_file, material=material):
        print('|-->',ele.Name, '(', ele.is_a(), ')')

