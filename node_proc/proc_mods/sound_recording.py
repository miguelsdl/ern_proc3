def sound_recording_43(self, node):
    result = {}

    # Información básica
    result['ResourceReference'] = node.find('ResourceReference').text
    result['Type'] = node.find('Type').text

    # ISRC y PLine
    resource_id = node.find('.//ResourceId')
    result['ISRC'] = resource_id.find('ISRC').text if resource_id is not None else None

    pline = node.find('.//PLine')
    if pline is not None:
        result['Year'] = pline.find('Year').text
        result['PLineText'] = pline.find('PLineText').text

    # TechnicalResourceDetailsReference
    tech_details = node.find('.//TechnicalDetails')
    result['TechnicalResourceDetailsReference'] = tech_details.find(
        'TechnicalResourceDetailsReference').text if tech_details is not None else None

    # Contributors
    contributors = {}
    for contributor in node.findall('.//Contributor'):
        party_ref = contributor.find('ContributorPartyReference').text
        roles = []
        for role in contributor.findall('Role'):
            if role.text == 'UserDefined':
                roles.append(role.attrib.get('UserDefinedValue', 'UserDefined'))
            else:
                roles.append(role.text)
        if party_ref in contributors:
            contributors[party_ref].extend(roles)
        else:
            contributors[party_ref] = roles

    to_return = {result['ResourceReference']: result}

    # Este tag tiene mucha información, por eso devuelvo un diccionacion con add_as_instance_var
    # que son valores para poner en variables de instancia, el método que llama a este se encarga
    #  de poner el nombre de la variable como contributors_value.
    return {
        "result": to_return,
        'add_as_instance_var': {
            'contributors': {
                result['ResourceReference']: contributors
            }
        }
    }
