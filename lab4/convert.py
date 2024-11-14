import json
import xml.etree.ElementTree as ET


# Функция для конвертации JSON в XML
def json_to_xml(json_data):
    root = ET.Element("People")

    for person in json_data:
        person_element = ET.SubElement(root, "Person")

        for key, value in person.items():
            child = ET.SubElement(person_element, key)
            child.text = str(value)

    return ET.tostring(root, encoding='unicode')


# Чтение JSON файла
with open('data.json', 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)

# Конвертация в XML
xml_data = json_to_xml(data)

# Сохранение результата в файл
with open('data.xml', 'w', encoding='utf-8') as xml_file:
    xml_file.write(xml_data)

print("Конвертация завершена. Данные сохранены в data.xml.")