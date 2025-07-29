import xml.etree.ElementTree as ET
from email.headerregistry import MessageIDHeader


def message_header_43(self, message_header_node):
    """
    MessageHeader = {
        "MessageThreadId": "G0100006698146_KUC",
        "MessageId": "332932439",
        "MessageSender": {
            "PartyId": "PADPIDA2007040502I",
            "PartyName": {
                "FullName": "Sony Music Entertainment"
            }
        },
        "MessageRecipient": {
            "PartyId": "PADPIDA2012073006T",
            "PartyName": {
                "FullName": "KuackMedia 4.3 SD"
            }
        },
        "MessageCreatedDateTime": "2024-10-23T08:55:26.447Z",
        "MessageControlType": "TestMessage"
    }
    """

    party_id = message_header_node.get('MessageSender', {}).get('PartyId', None)
    party_full_name = message_header_node.get('MessageSender', {}).get('PartyName', {}).get('FullName', None)
    party = {party_id: party_full_name}
    return {'result': message_header_node.get('MessageHeader', dict())}


def message_header_43_dep(self, xml_str):
    header = ET.fromstring(xml_str).find('MessageHeader')

    if header is None:
        message_header = {}
    else:
        message_header = {
            'MessageThreadId': header.findtext('MessageThreadId'),
            'MessageId': header.findtext('MessageId'),
            'MessageSenderId': header.findtext('MessageSender/PartyId'),
            'MessageSenderName': header.findtext('MessageSender/PartyName/FullName'),
            'MessageRecipientId': header.findtext('MessageRecipient/PartyId'),
            'MessageRecipientName': header.findtext('MessageRecipient/PartyName/FullName'),
            'MessageCreatedDateTime': header.findtext('MessageCreatedDateTime'),
            'MessageControlType': header.findtext('MessageControlType')
        }

    return {'result': message_header}

def message_header_42(self, xml_str):
    root = ET.fromstring(xml_str)
    header = root.find('MessageHeader')

    if header is None:
        message_header = {}
    else:
        message_header = {
            'MessageThreadId': header.findtext('MessageThreadId'),
            'MessageId': header.findtext('MessageId'),
            'MessageSenderId': header.find('MessageSender/PartyId').text,
            'MessageSenderName': header.find('MessageSender/PartyName/FullName').text,
            'MessageRecipientId': header.find('MessageRecipient/PartyId').text,
            'MessageRecipientName': header.find('MessageRecipient/PartyName/FullName').text,
            'MessageCreatedDateTime': header.findtext('MessageCreatedDateTime'),
            'MessageControlType': header.findtext('MessageControlType')
        }

    return {'result': message_header}

def message_header_38(self, header):

    return {
        'result': {
            "MessageThreadId": header.findtext("MessageThreadId"),
            "MessageId": header.findtext("MessageId"),
            "SenderPartyId": header.find("MessageSender/PartyId").text,
            "SenderFullName": header.find("MessageSender/PartyName/FullName").text,
            "RecipientPartyId": header.find("MessageRecipient/PartyId").text,
            "RecipientFullName": header.find("MessageRecipient/PartyName/FullName").text,
            "CreatedDateTime": header.findtext("MessageCreatedDateTime"),
            "ControlType": header.findtext("MessageControlType")
        }
    }


# Version 4.2 of the DDEX standard processing functions for MessageHeader

def message_thread_id_42(self, xml_str):
    return xml_str.text

def message_id_42(self, xml_str):
    return xml_str.text

def sender_id_42(self, xml_str):
    return xml_str.text

def sender_name_42(self, xml_str):
    return xml_str.text

def recipient_id_42(self, xml_str):
    return xml_str.text

def recipient_name_42(self, xml_str):
    return xml_str.text

def created_datetime_42(self, xml_str):
    return xml_str.text

def control_type_42(self, xml_str):
    return xml_str.text


# Version 4.3 of the DDEX standard processing functions for MessageHeader

def message_thread_id_43(self, xml_str):
    return xml_str.text

def message_id_43(self, xml_str):
    return xml_str.text

def sender_id_43(self, xml_str):
    return xml_str.text

def sender_name_43(self, xml_str):
    return xml_str.text

def recipient_id_43(self, xml_str):
    return xml_str.text

def recipient_name_43(self, xml_str):
    return xml_str.text

def message_created_datetime_43(self, xml_str):
    return xml_str.text

def control_type_43(self, xml_str):
    return xml_str.text
