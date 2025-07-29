# -*- coding: utf-8 -*-
import json
import re
from xml.etree import ElementTree as ET


class ProcDDEXRec:

    def __init__(self):
        self.ddex_version = None

    def set_instance_methods(self, methods):
        for method_name, method_definition in methods.items():
            self.__setattr__(method_name, method_definition)

    # def proc_ddex(self, xml_file) -> bool:
    #     def recurse(element, path):
    #         current_path = path + [element.tag.split('}')[-1]]  # Remove namespace
    #         # print(' > '.join(current_path))
    #         try:
    #             # esto es para que no falle la recusión
    #             self.case_filter(node=element, xml_current_path=current_path)
    #         except Exception as e:
    #             raise e
    #
    #         for child in element:
    #             recurse(child, current_path)
    #
    #     tree = ET.parse(xml_file)
    #     root = tree.getroot()
    #     recurse(root, [])
    #     return True

    def proc_ddex(self, xml_file) -> bool:
        """Procesa el archivo XML recorriendo recursivamente los nodos."""
        tree = self._parse_tree(xml_file)
        self._recurse(tree.getroot(), [])
        return True

    def _parse_tree(self, xml_file):
        """Parsea el archivo XML y devuelve el árbol."""
        try:
            return ET.parse(xml_file)
        except ET.ParseError as e:
            raise ValueError(f"Error al parsear el XML: {e}")

    def _recurse(self, element, path):
        """Recorre recursivamente el árbol XML aplicando la lógica del filtro."""
        current_path = path + [element.tag.split('}')[-1]]  # Remueve namespace

        try:
            self.case_filter(node=element, xml_current_path=current_path)
        except Exception as e:
            raise RuntimeError(f"Error procesando nodo {' > '.join(current_path)}: {e}") from e

        for child in element:
            self._recurse(child, current_path)

    def case_filter(self, node, xml_current_path=None):
        """Este método es un case que según el tag del nodo llama a un método especifico."""
        tag_name = node.tag.split('}')[-1]

        method_name = ProcDDEXRec.pascal_to_snake_case(tag_name)
        if hasattr(self, method_name):
            value = self.__getattribute__(method_name)(self, node)
            var_name = "{}_value".format(method_name)
            if isinstance(value, str) or isinstance(value, int) or isinstance(value, float):
                # Si es str, int o float, lo reemplazo.
                self.__setattr__("{}_value".format(method_name), value)
            elif isinstance(value, dict):
                # si es dict, lo actualizo.
                new_value = self.__getattribute__(var_name) if hasattr(self, var_name) else {}
                if 'add_as_instance_var' in value:
                    # Si el diccionario tiene la clave 'add_as_instance_var', lo agrego como variable de instancia,
                    # esto es para los nodos que tienen mucha información anidada.
                    for key, val in value['add_as_instance_var'].items():
                        self.__setattr__(f"{key}_value", val)
                        # print(f"{key}: {val}")
                # Actualizo el valor del lo que viene en la key result.
                new_value.update(value.get('result', {}))
                self.__setattr__("{}_value".format(method_name), new_value)
            elif isinstance(value, list):
                # Si es lista, lo extiendo.
                new_value = self.__getattribute__(var_name) if hasattr(self, var_name) else []
                new_value.extend(value)
                self.__setattr__("{}_value".format(method_name), new_value)
            else:
                # Si no es ninguno de los anteriores, lanzo un error.
                raise TypeError(
                    "{} tipo no reconocido en el else del método proc.ProcDDEXRec.case_filter()".format(value)
                )

            # print(var_name, ':', self.__getattribute__("{}_value".format(method_name)))

    @staticmethod
    def pascal_to_snake_case(s: str) -> str:
        """Pasa de CamelCase o PascalCase a snake_case."""
        return re.sub(r'(?<!^)(?=[A-Z])', '_', s).lower()

    def clean_values(self):
        for attr in list(self.__dict__):
            if attr.endswith('_value'):
                print(attr, ':', json.dumps(self.__getattribute__(attr)))
                # print(f"Limpiando {attr}")
                # delattr(self, attr)

    def __enter__(self):
        print("Iniciando parseo XML")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("🚪 Terminando y limpiando")
        self.clean_values()

    def merge_party_and_contributors(self) -> dict:
        merged_data = {}
        for resource, contributors in self.contributors_value.items():
            merged_data[resource] = {}
            for artist_key, roles in contributors.items():
                artist_name = self.party_value.get(artist_key, artist_key)
                merged_data[resource][artist_name] = roles
        return merged_data


# Acá importo los módulos necesarios para procesar los nodos específicos,
# cada módulo tiene métodos para procesar nodos específicos del XML.

# from node_proc.proc_mods.party_list import party_43
# from node_proc.proc_mods.message_header import (
#     message_thread_id_43, message_id_43, sender_id_43, sender_name_43, recipient_id_43, recipient_name_43,
#     message_created_datetime_43, control_type_43
# )
# from node_proc.proc_mods.track_release import (
#     track_release_43
# )
# from node_proc.proc_mods.release import (
#     release_43
# )
# from node_proc.proc_mods.release_deal import (
#     release_deal_43
# )
# from node_proc.proc_mods.sound_recording import (
# sound_recording_43
# )
#
#
# # Las keys del diccionario son los nombres de los nodos que se procesan y
# # los valores son las funciones que procesan esos nodos KEYNAME_VERSION.
#
# processor_methods = {
#     # Valores escalares.
#     "message_thread_id": message_thread_id_43,
#     "message_id": message_id_43,
#     "message_created_date_time": message_created_datetime_43,
#     "message_control_type": control_type_43,
#
#     'party': party_43,
#     "track_release": track_release_43,
#     "release": release_43,
#     "release_deal": release_deal_43,
#     "sound_recording": sound_recording_43,
# }
#
#
# # Example usage:
# with ProcDDEXRec() as o:
#     o.set_instance_methods(processor_methods)
#     o.proc_ddex('./xml_files/ddex43.xml')

# processor_methods = {
#     "message_thread_id": message_thread_id_42,
#     "message_id": message_id_42,
#     "message_sender_id": sender_id_42,
#     "message_sender_name": sender_name_42,
#     "message_recipient_id": recipient_id_42,
#     "message_recipient_name": recipient_name_42,
#     "message_created_datetime": created_datetime_42,
#     "message_control_type": control_type_42,
# }