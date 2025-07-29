def message_header(self, message_header, **kwargs):

    # Agregar los resultados procesados al diccionario de retorno
    to_return = {
        'result': {
            "MessageThreadId": message_header.get("MessageThreadId"),
            "MessageId": message_header.get("MessageId"),
            "SenderPartyId": message_header.get("MessageSender", {}).get("PartyId"),
            "SenderFullName": message_header.get("MessageSender", {}).get("PartyName", {}).get("FullName"),
            "RecipientPartyId": message_header.get("MessageRecipient", {}).get("PartyId"),
            "RecipientFullName": message_header.get("MessageRecipient", {}).get("PartyName", {}).get("FullName"),
            "MessageCreatedDateTime": message_header.get("MessageCreatedDateTime"),
            "MessageControlType": message_header.get("MessageControlType")
        },
    }

    return to_return

def resource_list(self, resource_list, **kwargs):
    extracted = {
        "SoundRecording": {},
        "Image": {}
    }

    # SoundRecording puede ser lista o un solo dict
    sound_recordings = resource_list.get("SoundRecording", [])
    if isinstance(sound_recordings, dict):
        sound_recordings = [sound_recordings]

    for sound in sound_recordings:
        ref = sound.get("ResourceReference")
        if ref:
            extracted["SoundRecording"][ref] = sound

    # Image es único
    image = resource_list.get("Image")
    if image and isinstance(image, dict):
        ref = image.get("ResourceReference")
        if ref:
            extracted["Image"][ref] = image

    to_return = {
        'result': extracted.get('SoundRecording'),
        'add_as_instance_var': {
            'image': extracted.get('Image'),
        }
    }

    return to_return