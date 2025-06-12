import xmltodict
import os
import re


class Proc43:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.data = None
        self.resources_reference_list = list()
        self.read_file()


    def read_file(self):
        """Read the XML file and convert it to a dictionary."""
        if not os.path.exists(self.file_path):
            raise FileNotFoundError(f"The file {self.file_path} does not exist.")

        with open(self.file_path, 'r', encoding='utf-8') as file:
            file_content = file.read()

        if not file_content.strip():
            raise ValueError(f"The file {self.file_path} is empty.")

        self.data = xmltodict.parse(file_content)

        """
        Extrae la seccion 'PartyList' del diccionario de datos y asocia los valores de 'PartyName' a sus respectivos
        'PartyReference'. Para los nodos Party que tengan mas de un PartyName, se toma el primero por defecto bajo
        la key default y los demas se ponen bajo la key que venga en LanguageAndScriptCode.
        para P_ARTIST_1327278 debe de ser asi {'default': 'Stevie Ray Vaughan (Primary)', 'zh-Hant': '史堤夫雷范'}
        """

    def get_part_list(self):
        if not self.data:
            raise ValueError("No data loaded from XML.")

        party_list = self.data.get('ernm:NewReleaseMessage', {}).get('PartyList', {}).get('Party', [])
        if not party_list:
            return {}

        if isinstance(party_list, dict):
            party_list = [party_list]

        party_map = {}
        for party in party_list:
            party_ref = party.get('PartyReference')
            party_names = party.get('PartyName', [])
            if not party_ref or not party_names:
                continue

            if isinstance(party_names, dict):
                party_names = [party_names]

            name_dict = {}
            for idx, pname in enumerate(party_names):
                full_name = pname.get('FullName') if isinstance(pname, dict) else pname
                lang_code = pname.get('LanguageAndScriptCode') if isinstance(pname, dict) else None
                if lang_code:
                    name_dict[lang_code] = full_name
                elif 'default' not in name_dict:
                    name_dict['default'] = full_name

            party_map[party_ref] = name_dict

        return party_map


    '''
    Crea un metodo para extraer las informacion del nodo MessageHeader
    '''

    def get_message_header(self):
        """
        Extracts the 'MessageHeader' node information from the XML data.
        :return: dict with MessageHeader data or empty dict if not found
        """
        if not self.data:
            raise ValueError("No data loaded from XML.")

        return self.data.get('ernm:NewReleaseMessage', {}).get('MessageHeader', {}) or {}

    def to_snake_case(self, name):
        s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
        return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

    def get_resource_list(self):
        """
        Processes ResourceList: key is ResourceReference,
        value is dict with Type and SoundRecordingEdition fields (excluding TechnicalDetails).
        Also stores the ResourceReference keys in self.resources_reference_list.
        """
        if not self.data:
            raise ValueError("No data loaded from XML.")

        self.resources_reference_list.clear()  # Clear previous values

        resources = self.data.get('ernm:NewReleaseMessage', {}).get('ResourceList', {})
        sound_recordings = resources.get('SoundRecording', [])
        if isinstance(sound_recordings, dict):
            sound_recordings = [sound_recordings]

        result = {}
        for rec in sound_recordings:
            ref = rec.get('ResourceReference')
            typ = rec.get('Type')
            edition = rec.get('SoundRecordingEdition', {})
            if isinstance(edition, list):
                edition = edition[0]
            edition_dict = {}
            if isinstance(edition, dict):
                for k, v in edition.items():
                    if k != 'TechnicalDetails':
                        edition_dict[k] = v
            result[ref] = {
                'Type': typ,
                'SoundRecordingEdition': edition_dict
            }
            if ref is not None:
                self.resources_reference_list.append(ref)
        return result





if __name__ == "__main__":
    # Adjust the path as needed
    example_file = os.path.join("../xml_files", "file_ejemplo_1.xml")
    proc = Proc43(example_file)
    party_map = proc.get_part_list()
    print("PartyID to Party mapping:")
    for party_id, party_data in party_map.items():
        print(f"{party_id}: {party_data}")


    # Show MessageHeader info
    message_header = proc.get_message_header()
    print("\nMessageHeader info:")
    print(message_header)

    resource_map_filtered = proc.get_resource_list()
    print("\nResourceList mapping (filtered, no TechnicalDetails):")
    for resource_id, resource_data in resource_map_filtered.items():
        print(f"{resource_id}:")
        print(f"  Type: {resource_data['Type']}")
        print(f"  SoundRecordingEdition: {resource_data['SoundRecordingEdition']}")