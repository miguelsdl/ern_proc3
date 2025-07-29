import xml.etree.ElementTree as ET
from typing import Dict, Any

def image_43(nodo_image: ET.Element) -> Dict[str, Any]:
    def get_text(path):
        el = nodo_image.find(path)
        return el.text if el is not None else None

    def get_nested_text(parent, path):
        el = parent.find(path)
        return el.text if el is not None else None

    resource_reference = get_text('ResourceReference')
    image_type = get_text('Type')

    proprietary_id_node = nodo_image.find('ResourceId/ProprietaryId')
    resource_id = {
        "namespace": proprietary_id_node.attrib.get("Namespace") if proprietary_id_node is not None else None,
        "value": proprietary_id_node.text if proprietary_id_node is not None else None
    }

    publication_date = get_text('FirstPublicationDate/FulfillmentDate')

    technical = nodo_image.find('TechnicalDetails')
    file_node = technical.find('File') if technical is not None else None

    image_data = {
        "resource_reference": resource_reference,
        "type": image_type,
        "resource_id": resource_id,
        "publication_date": publication_date,
        "technical_details": {
            "reference": get_nested_text(technical, 'TechnicalResourceDetailsReference'),
            "codec": get_nested_text(technical, 'ImageCodecType'),
            "height": int(get_nested_text(technical, 'ImageHeight') or 0),
            "width": int(get_nested_text(technical, 'ImageWidth') or 0),
            "resolution": int(get_nested_text(technical, 'ImageResolution') or 0),
            "file": {
                "uri": get_nested_text(file_node, 'URI'),
                "hash": {
                    "algorithm": get_nested_text(file_node.find('HashSum'), 'Algorithm'),
                    "value": get_nested_text(file_node.find('HashSum'), 'HashSumValue')
                },
                "size": int(get_nested_text(file_node, 'FileSize') or 0)
            } if file_node is not None else None,
            "is_provided_in_delivery": get_nested_text(technical, 'IsProvidedInDelivery') == "true"
        } if technical is not None else None
    }

    return {'result': {image_data.get('resource_reference'): image_data }}
