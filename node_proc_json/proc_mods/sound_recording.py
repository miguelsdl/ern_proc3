def sound_recording(
        self, sound_recording_list, technical_details=None, display_artist=None, contributors=None, **kwargs):

    sound_recording_map = {}
    technical_details_map = {}
    display_artist_map = {}
    contributor_processor_map = {}

    for data in sound_recording_list:
        edition = data["SoundRecordingEdition"]
        technical = edition.get("TechnicalDetails", {})

        sound_recording_result = {
            "ResourceReference": data.get("ResourceReference"),
            "Type": data.get("Type"),
            "ISRC": edition.get("ResourceId", {}).get("ISRC"),
            "PLineYear": edition.get("PLine", {}).get("Year"),
            "PLineText": edition.get("PLine", {}).get("PLineText"),
            "Title": data.get("DisplayTitle", {}).get("TitleText"),
            "TitleText": data.get("DisplayTitleText", {}).get("#text"),
            "DisplayArtistName": data.get("DisplayArtistName"),
            "Duration": data.get("Duration"),
            "ParentalWarningType": data.get("ParentalWarningType"),
            "LanguageOfPerformance": data.get("LanguageOfPerformance"),
            "IsClip": technical.get("IsClip"),
            "ClipDetails": technical.get("ClipDetails"),

        }
        sound_recording_map[data["ResourceReference"]] = sound_recording_result

        # Procesamiento externo por los calleables proporcionados
        if technical_details:
            technical_details_map[data["ResourceReference"]] = technical_details(data=technical, **kwargs)

        if display_artist:
            display_artist_map[data["ResourceReference"]] = display_artist(data=data.get("DisplayArtist", {}), **kwargs)

        if contributors:
            contributor_processor_map[data["ResourceReference"]] = \
                contributors(data=data.get("Contributor", []), **kwargs)

    # Agregar los resultados procesados al diccionario de retorno
    to_return = {
        'result': sound_recording_map,
        'add_as_instance_var': {
            'technical_details': technical_details_map,
            'display_artist': display_artist_map,
            'contributors': contributor_processor_map,
        }
    }

    return to_return