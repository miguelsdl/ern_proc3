import xml.etree.ElementTree as ET

def track_release_43(self, track):
    release_reference = track.findtext('ReleaseReference')
    track_data = {
        'GRid': track.findtext('ReleaseId/GRid'),
        'ProprietaryId': track.find('ReleaseId/ProprietaryId').text,
        'ProprietaryIdNamespace': track.find('ReleaseId/ProprietaryId').attrib.get('Namespace'),
        'ReleaseResourceReference': track.findtext('ReleaseResourceReference'),
        'ReleaseLabelReference': track.findtext('ReleaseLabelReference'),
        'LabelType': track.find('ReleaseLabelReference').attrib.get('LabelType'),
        'Genre': track.findtext('Genre/GenreText'),
        'TerritoryCode': track.find('Genre').attrib.get('ApplicableTerritoryCode'),
    }
    return {'result':{release_reference: track_data}}