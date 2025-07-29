def release_deal_43(self, release_deal_node):
    extracted_data = {}
    deal_references = [ref.text for ref in release_deal_node.findall('DealReleaseReference')]
    deal_terms = release_deal_node.findall('.//DealTerms')

    for deal_reference in deal_references:
        extracted_data[deal_reference] = []
        for terms in deal_terms:
            data = {
                'TerritoryCodes': [code.text for code in terms.findall('TerritoryCode')],
                'ValidityPeriod': {
                    'StartDateTime': terms.find('.//ValidityPeriod/StartDateTime').text,
                    'EndDateTime': terms.find('.//ValidityPeriod/EndDateTime').text
                },
                'CommercialModelType': terms.find('CommercialModelType').text,
                'UseTypes': [use.text for use in terms.findall('UseType')]
            }
            extracted_data[deal_reference].append(data)

    return {'result': extracted_data}
