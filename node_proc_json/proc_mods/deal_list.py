def deal_list_43(self, data, **kwargs):
    release_deal = data.get("ReleaseDeal", {})

    release_refs = release_deal.get("DealReleaseReference", [])
    release_refs = release_refs if isinstance(release_refs, list) else [release_refs]

    deals = release_deal.get("Deal", [])
    deals = deals if isinstance(deals, list) else [deals]

    resultado = {}
    use_types = set()
    commercials_models = set()

    for ref in release_refs:
        resultado[ref] = []
        for d in deals:
            terms = d.get("DealTerms", {})
            periodo = terms.get("ValidityPeriod", {})

            ut = terms.get("UseType", [])
            ut = ut if isinstance(ut, list) else [ut]

            resultado[ref].append({
                "start_date": periodo.get("StartDateTime"),
                "end_date": periodo.get("EndDateTime"),
                "commercial_model": terms.get("CommercialModelType"),
                "use_types": ut,
                "territories": terms.get("TerritoryCode", [])
            })

            use_types.update(ut)
            commercials_models.add(terms.get("CommercialModelType"))

    return {
        'result': resultado,
        'add_as_instance_var': {
            'use_types': list(use_types),
            'commercials_models': list(commercials_models),
        }
    }


"""
{'ReleaseDeal': {'Deal': [{'DealTerms': {'CommercialModelType': 'SubscriptionModel', 'TerritoryCode': ['AG', 'AI', 'AW', 'BB', 'BM', 'BO', 'BQ', 'BR', 'BZ', 'CL', 'CO', 'CR', 'CW', 'DM', 'DO', 'EC', 'ES', 'GD', 'GF', 'GP', 'GY', 'HT', 'JM', 'KN', 'KY', 'LC', 'MQ', 'MS', 'PA', 'PE', 'SR', 'SV', 'TC', 'TT', 'VC', 'VG', 'VU', 'ZM'], 'UseType': ['ConditionalDownload', 'NonInteractiveStream', 'OnDemandStream'], 'ValidityPeriod': {'StartDateTime': '2016-05-06T00:00:00'}}}, {'DealTerms': {'CommercialModelType': 'AdvertisementSupportedModel', 'TerritoryCode': ['AG', 'AI', 'AW', 'BB', 'BM', 'BO', 'BQ', 'BR', 'BZ', 'CL', 'CO', 'CR', 'CW', 'DM', 'DO', 'EC', 'ES', 'GD', 'GF', 'GP', 'GY', 'HT', 'JM', 'KN', 'KY', 'LC', 'MQ', 'MS', 'PA', 'PE', 'SR', 'SV', 'TC', 'TT', 'VC', 'VG', 'VU', 'ZM'], 'UseType': ['NonInteractiveStream', 'OnDemandStream'], 'ValidityPeriod': {'StartDateTime': '2016-05-06T00:00:00'}}}], 'DealReleaseReference': ['R1', 'R2', 'R3', 'R4', 'R5', 'R6', 'R7', 'R8', 'R9', 'R10', 'R11', 'R12', 'R13', 'R14', 'R15', 'R16', 'R17', 'R18', 'R19', 'R20']}}
"""