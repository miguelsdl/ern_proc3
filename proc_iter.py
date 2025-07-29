from xml.etree import ElementTree as ET
from collections import deque


class XMLIterator:
    def __init__(self, xml_string):
        """
        Inicializa el iterador con una cadena XML.

        Args:
            xml_string (str): La cadena XML a procesar
        """
        self.root = ET.fromstring(xml_string)

    def iterate(self):
        """
        Recorre el XML de manera iterativa usando una cola.

        Yields:
            tuple: (elemento, nivel, ruta)
        """
        queue = deque([(self.root, 0, "/")])

        while queue:
            element, level, path = queue.popleft()

            # Construye la ruta completa del elemento
            current_path = f"{path}/{element.tag}" if path != "/" else f"/{element.tag}"

            # Procesa el elemento actual
            yield element, level, current_path

            # Agrega los hijos a la cola
            for child in element:
                queue.append((child, level + 1, current_path))


# Ejemplo de uso
xml_string = """<?xml version="1.0" encoding="UTF-8"?>
<ernm:NewReleaseMessage xmlns:ernm="http://ddex.net/xml/ern/383">
    <MessageHeader>
        <MessageThreadId>1</MessageThreadId>
        <MessageId>1</MessageId>
    </MessageHeader>
    <ResourceList>
        <SoundRecording>
            <SoundRecordingType>MusicalWorkSoundRecording</SoundRecordingType>
        </SoundRecording>
    </ResourceList>
</ernm:NewReleaseMessage>"""

# Crear instancia del iterador
iterator = XMLIterator(xml_string)

# Recorrer y mostrar los elementos
for element, level, path in iterator.iterate():
    print(f"Nivel {level}: {path}")
    if element.text and element.text.strip():
        print(f"  Texto: {element.text.strip()}")