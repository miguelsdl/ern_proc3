# -*- coding: utf-8 -*-
def message_header_43(self, message_header_node, **kwargs):
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

    ms_sender_party_id = message_header_node.get('MessageSender', {}).get('PartyId', None)
    ms_ender_full_name = message_header_node.get('MessageSender', {}).get('PartyName', {}).get('FullName', None)

    ms_recipient_party_id = message_header_node.get('MessageRecipient', {}).get('PartyId', None)
    ms_recipient_full_name = message_header_node.get('MessageRecipient', {}).get('PartyName', {}).get('FullName', None)

    party = {
        ms_sender_party_id: {'default': ms_ender_full_name},
        ms_recipient_party_id: {'default': ms_recipient_full_name}
    }

    # Pongo party en add_as_instance_var para que se agregue al party_value en self el método
    # que llama a este se encarga de agregar el valor al party_vale que ya tiene el party list.
    to_return = {
        'result': message_header_node,
        'add_as_instance_var': {
            'party': party
        }
    }

    return to_return
