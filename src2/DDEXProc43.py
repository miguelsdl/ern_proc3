import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Dict, Any

class ResultadoProcesamiento:
    def __init__(self, exitoso: bool, mensaje: str, datos: Dict[str, Any] = None):
        self.exitoso = exitoso
        self.mensaje = mensaje
        self.datos = datos or {}

class IDDEXProcessor:
    def procesar_archivo(self, archivo: Path) -> ResultadoProcesamiento:
        raise NotImplementedError

class DDEXProc43(IDDEXProcessor):
    def procesar_archivo(self, archivo: Path) -> ResultadoProcesamiento:
        try:
            tree = ET.parse(archivo)
            root = tree.getroot()

            if not self._validar_formato_v43(root):
                return ResultadoProcesamiento(
                    False,
                    "Error: Formato XML no válido para versión 4.3"
                )

            datos_procesados = self._procesar_datos_v43(root)

            return ResultadoProcesamiento(
                True,
                "Procesamiento exitoso",
                datos_procesados
            )
        except Exception as e:
            return ResultadoProcesamiento(
                False,
                f"Error en el procesamiento: {str(e)}"
            )

    def _validar_formato_v43(self, root: ET.Element) -> bool:
        # Validación básica: comprobar que la raíz es 'NewReleaseMessage'
        return root.tag.endswith('NewReleaseMessage')

    def _procesar_datos_v43(self, root: ET.Element) -> Dict[str, Any]:
        deals = []
        # Handle namespaces if present
        ns = {}
        if root.tag.startswith('{'):
            uri = root.tag.split('}')[0].strip('{')
            ns = {'ns': uri}

        # Build a map from ReleaseReference to Release element
        release_map = {}
        for release in root.findall('.//Release', ns):
            ref = release.findtext('ReleaseReference', namespaces=ns)
            if ref:
                release_map[ref] = release

        for deal in root.findall('.//Deal', ns):
            release_ref = deal.findtext('ReleaseReference', namespaces=ns)
            deal_info = {'ReleaseReference': release_ref}
            release = release_map.get(release_ref)
            if release is not None:
                release_id_node = release.find('ReleaseId', ns)
                if release_id_node is not None:
                    # Try to get child elements, handling namespaces
                    def get_text(tag):
                        node = release_id_node.find(tag, ns)
                        return node.text if node is not None else ''

                    deal_info['GRid'] = get_text('GRid')
                    deal_info['ICPN'] = get_text('ICPN')
                    deal_info['CatalogNumber'] = get_text('CatalogNumber')
            deals.append(deal_info)
        return {'deals': deals}

    def extraer_album_info(self, root: ET.Element) -> dict:
        # Handle namespaces
        ns = {}
        if root.tag.startswith('{'):
            uri = root.tag.split('}')[0].strip('{')
            ns = {'ns': uri}

        album_info = {}
        release = root.find('.//Release', ns)
        if release is not None:
            for child in release:
                tag = child.tag.split('}')[-1]
                # If the child has subelements, join their text
                if list(child):
                    sub_info = {}
                    for sub in child:
                        sub_tag = sub.tag.split('}')[-1]
                        sub_info[sub_tag] = sub.text if sub.text else ''
                    album_info[tag] = sub_info
                else:
                    album_info[tag] = child.text if child.text else ''
        return album_info


import xml.etree.ElementTree as ET

def procesar_archivos_xml(file_paths, processor):
    resultados = []
    for file_path in file_paths:
        tree = ET.parse(file_path)
        root = tree.getroot()
        resultado = processor(root)
        resultados.append({'file': file_path, 'resultado': resultado})
    return resultados

# Example usage:
file_paths = [
    'xml_files/file_ejemplo_1.xml',
    'xml_files/file_ejemplo_2.xml',
    'xml_files/file_ejemplo_3.xml'
]

ddex_proc = DDEXProc43()


# Replace `tu_metodo_de_procesamiento` with your actual processing method, e.g., ddex_proc.extraer_album_info
resultados = procesar_archivos_xml(file_paths, ddex_proc.extraer_album_info)
for r in resultados:
    print(f"File: {r['file']}")
    print(r['resultado'])