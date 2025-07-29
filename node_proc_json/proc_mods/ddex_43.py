def message_header(self, message_header_node, **kwargs):
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

def party(self, party_list, **kwargs):
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

    return {'result': result}

def sound_recording(self, sound_recording_list, **kwargs):

    sound_recording_map = {}
    technical_details_map = {}
    display_artist_map = {}
    contributor_processor_map = {}

    def technical_details(data, **kwargs):
        """Procesa el nodo TechnicalDetails, devolviendo un dict por TechnicalResourceDetailsReference."""
        items = data if isinstance(data, list) else [data]
        result = {}

        for entry in items:
            ref = entry.get("TechnicalResourceDetailsReference")
            if ref:
                result[ref] = entry

        return result

    def display_artist(data, party_value, **kwargs):
        """Procesa DisplayArtist devolviendo dict con referencia de artista como clave y detalles como valor."""
        raw_artists = data if isinstance(data, list) else [data]
        result = {}

        for artist in raw_artists:
            ref = artist.get("ArtistPartyReference")
            if not ref:
                continue

            role = artist.get("DisplayArtistRole")
            raw_artistic = artist.get("ArtisticRole")
            artistic_roles = []

            if isinstance(raw_artistic, str):
                artistic_roles.append(raw_artistic)
            elif isinstance(raw_artistic, dict):
                if raw_artistic.get("#text") == "UserDefined" and "@UserDefinedValue" in raw_artistic:
                    artistic_roles.append(raw_artistic["@UserDefinedValue"])
                elif raw_artistic.get("#text"):
                    artistic_roles.append(raw_artistic["#text"])

            result[ref] = {
                "sequence_number": artist.get("@SequenceNumber"),
                "artist_party_reference": ref,
                "name": party_value.get(ref, {}),
                "display_role": role,
                "artistic_roles": artistic_roles,
            }

        return result

    def contributors(data=None, party_value=None, **kwargs):
        """Processes a list of contributors and extracts sequence number, party reference, and roles."""
        raw_contributors = data  # .get("Contributor", [])
        if isinstance(raw_contributors, dict):
            raw_contributors = [raw_contributors]

        result = {}

        for contributor in raw_contributors:
            raw_roles = contributor.get("Role", [])
            if isinstance(raw_roles, dict):
                raw_roles = [raw_roles]
            elif isinstance(raw_roles, str):
                raw_roles = [raw_roles]

            roles = []
            for role in raw_roles:
                if isinstance(role, str):
                    roles.append(role)
                elif isinstance(role, dict):
                    if role.get("#text") == "UserDefined" and "@UserDefinedValue" in role:
                        roles.append(role["@UserDefinedValue"])
                    elif role.get("#text") and role["#text"] != "UserDefined":
                        roles.append(role["#text"])
                    elif "@UserDefinedValue" in role:
                        roles.append(role["@UserDefinedValue"])

            result[contributor["ContributorPartyReference"]] = {
                "sequence_number": contributor.get("@SequenceNumber"),
                "party_reference": contributor.get("ContributorPartyReference"),
                "name": party_value.get(contributor["ContributorPartyReference"], {}),
                "roles": roles
            }

        return result

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

def release(self, data, **kwargs):
    releases_raw = data
    releases = releases_raw if isinstance(releases_raw, list) else [releases_raw]

    resultado = {}

    for r in releases:
        title_dict = (
            {
                entry.get("@LanguageAndScriptCode", "default"): entry.get("TitleText")
                for entry in r.get("DisplayTitle", [])
            } if isinstance(r.get("DisplayTitle"), list)
            else {
                r.get("DisplayTitle", {}).get("@LanguageAndScriptCode", "default"):
                    r.get("DisplayTitle", {}).get("TitleText")
            }
        )
        if "en" in title_dict:
            title_dict["default"] = title_dict["en"]

        resultado[r["ReleaseReference"]] = {
            "title": title_dict,
            "artist": r.get("DisplayArtistName"),
            "year": r.get("PLine", {}).get("Year"),
            "genre": r.get("Genre", {}).get("GenreText"),
            "duration": r.get("Duration"),
            "original_release_date": r.get("OriginalReleaseDate"),
            "track_references": []
        }

        resource_items = r.get("ResourceGroup", {}).get("ResourceGroupContentItem", [])
        for item in resource_items:
            ref_id = item.get("ReleaseResourceReference")
            if ref_id:
                resultado[r["ReleaseReference"]]["track_references"].append(ref_id)

    return {'result': resultado, }

def track_release(self, data, **kwargs):
    track_raw = data
    tracks = track_raw if isinstance(track_raw, list) else [track_raw]

    tracks_info = {}
    track_release_reference = {}

    for track in tracks:
        ref = track["ReleaseReference"]
        release_id = track.get("ReleaseId", {})
        proprietary_id = release_id.get("ProprietaryId", {})
        resource_ref = track.get("ReleaseResourceReference")

        # Info detallada del track
        tracks_info[ref] = {
            "resource_reference": resource_ref,
            "isrc": proprietary_id.get("#text"),
            "isrc_namespace": proprietary_id.get("@Namespace"),
            "grid": release_id.get("GRid"),
            "label": track.get("ReleaseLabelReference", {}).get("#text"),
            "genre": track.get("Genre", {}).get("GenreText"),
        }

        # Asociar release con resource_reference
        if ref not in track_release_reference:
            track_release_reference[ref] = []
        track_release_reference[ref].append(resource_ref)

    # Agregar los resultados procesados al diccionario de retorno
    to_return = {
        'result': tracks_info,
        'add_as_instance_var': {
            'track_release_reference': track_release_reference,
        }
    }

    return to_return

'''
            "Release": {
                "ReleaseReference": "R0",
                "ReleaseType": "Album",
                "ReleaseId": {
                    "GRid": "A10301A0000935334X",
                    "ICPN": "074645736228",
                    "CatalogNumber": {
                        "@Namespace": "DPID:PADPIDA2007040502I",
                        "#text": "G010000935334X"
                    }
                },
                "DisplayTitleText": {
                    "@LanguageAndScriptCode": "en",
                    "#text": "Toys In The Attic"
                },
                "DisplayTitle": [
                    {
                        "@LanguageAndScriptCode": "en",
                        "TitleText": "Toys In The Attic"
                    },
                    {
                        "@LanguageAndScriptCode": "zh-Hant",
                        "TitleText": "閣樓裡的玩具"
                    }
                ],
                "DisplayArtistName": "Aerosmith",
                "DisplayArtist": {
                    "@SequenceNumber": "1",
                    "ArtistPartyReference": "P_ARTIST_2990300",
                    "DisplayArtistRole": "MainArtist"
                },
                "ReleaseLabelReference": {
                    "@LabelType": "DisplayLabel",
                    "#text": "P_LABEL_COLUMBIA"
                },
                "PLine": {
                    "Year": "1975",
                    "PLineText": "(P) 1975 Columbia Records, a division of Sony Music Entertainment"
                },
                "Duration": "PT0H37M8S",
                "Genre": {
                    "@ApplicableTerritoryCode": "Worldwide",
                    "GenreText": "Pop"
                },
                "OriginalReleaseDate": "2011-08-26",
                "ParentalWarningType": "NotExplicit",
                "ResourceGroup": {
                    "AdditionalTitle": {
                        "@TitleType": "GroupingTitle",
                        "TitleText": "Disc 1"
                    },
                    "SequenceNumber": "1",
                    "ResourceGroupContentItem": [
                        {
                            "SequenceNumber": "1",
                            "ReleaseResourceReference": "A1"
                        },
                        {
                            "SequenceNumber": "2",
                            "ReleaseResourceReference": "A2"
                        },
                        {
                            "SequenceNumber": "3",
                            "ReleaseResourceReference": "A3"
                        },
                        {
                            "SequenceNumber": "4",
                            "ReleaseResourceReference": "A4"
                        },
                        {
                            "SequenceNumber": "5",
                            "ReleaseResourceReference": "A5"
                        },
                        {
                            "SequenceNumber": "6",
                            "ReleaseResourceReference": "A6"
                        },
                        {
                            "SequenceNumber": "7",
                            "ReleaseResourceReference": "A7"
                        },
                        {
                            "SequenceNumber": "8",
                            "ReleaseResourceReference": "A8"
                        },
                        {
                            "SequenceNumber": "9",
                            "ReleaseResourceReference": "A9"
                        }
                    ],
                    "LinkedReleaseResourceReference": {
                        "@LinkDescription": "CoverArt",
                        "#text": "A10"
                    }
                }
            },

'''