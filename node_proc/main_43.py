import json

import xmltodict
from node_proc.proc import ProcDDEXRec
from node_proc.proc_mods.party_list import party_43
from node_proc.proc_mods.track_release import track_release_43
from node_proc.proc_mods.release import release_43
from node_proc.proc_mods.release_deal import release_deal_43
from node_proc.proc_mods.sound_recording import sound_recording_43
from node_proc.proc_mods.message_header import (
    message_thread_id_43, message_id_43, message_created_datetime_43, control_type_43
)


# Las keys del diccionario son los nombres de los nodos que se procesan y
# los valores son las funciones que procesan esos nodos KEYNAME_VERSION.

processor_methods = {
    'party': party_43,

}



def xml_to_json(file_path: str) -> dict:
    """
    Convierte un archivo XML a un diccionario JSON.

    :param file_path: Ruta del archivo XML
    :return: Diccionario representando el JSON
    """
    with open(file_path, 'r', encoding='utf-8') as xml_file:
        xml_content = xml_file.read()
        data_dict = xmltodict.parse(xml_content)
        return data_dict


with ProcDDEXRec() as o:
    # Convertir el XML a JSON
    # json_data = xml_to_json('./xml_files/ddex43.xml')
    # print(json.dumps(json_data))
    o.set_instance_methods(processor_methods)
    o.proc_ddex('./xml_files/ddex43.xml')
    print('------------------------------------------------')
    # print(o.merge_party_and_contributors())
