def party_43_json(party_list):
    result = {}
    for party in party_list:
        party_ref = party.get("PartyReference")
        name_data = party.get("PartyName")

        name_dict = {}

        if isinstance(name_data, dict):  # Caso único
            lang = name_data.get("@LanguageAndScriptCode", "default")
            name_dict[lang] = name_data.get("FullName")

        elif isinstance(name_data, list):  # Caso multilingüe
            for name_entry in name_data:
                lang = name_entry.get("@LanguageAndScriptCode", "default")
                name_dict[lang] = name_entry.get("FullName")

        result[party_ref] = name_dict

    return result


def party_43(self, party_node):
    self.party_list = {}
    key = party_node.find("PartyReference").text.strip()
    val = party_node.find("PartyName").find("FullName").text.strip()
    return {'result': {key: val}}
