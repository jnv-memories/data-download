from pathlib import Path
import xml.etree.ElementTree as ET

TEMP = Path("temp")
TEMP.mkdir(exist_ok=True)


def generate_xml(data):

    root = ET.Element("Users")

    for item in data:

        user = ET.SubElement(root, "User")

        for k, v in item.items():

            e = ET.SubElement(user, k)
            e.text = str(v)

    xml_file = TEMP / "generated.xml"

    ET.ElementTree(root).write(
        xml_file,
        encoding="utf-8",
        xml_declaration=True,
    )

    return str(xml_file)
