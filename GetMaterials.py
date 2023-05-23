import ifcopenshell
from ifcopenshell.util.element import get_elements_by_material as ele_by_materials

# Open the IFC file
ifc_file = ifcopenshell.open('test.ifc')
print(ifc_file.schema)

# Store unique material names and their instance counts
material_info = {}

direct_materials = ifc_file.by_type('IfcMaterialConstituent')

# Print the name of each direct material and its instance count
for material in direct_materials:
    if material.Name:
        material_name = material.Name
        if material_name not in material_info:
            material_info[material_name] = 1
        else:
            material_info[material_name] += 1
        print(material_name)

    for ele in ele_by_materials(ifc_file=ifc_file, material=material):
        print('|-->', ele.Name, '(', ele.is_a(), ')')

# Print the instance count for each material
print("\nMaterial Instance Counts:")
for material_name, count in material_info.items():
    print(material_name, ":", count)
