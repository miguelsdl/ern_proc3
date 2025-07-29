from db.models.track import Track
from db.models.albums_tracks import AlbumTrack
from .ddex_common import iso8601_to_mysql_time
from db.models.mixins import SaveByFieldsMixin as m

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
    resource_group_result = {}

    def parse_resource_group(data):
        items = data.get("ResourceGroupContentItem", [])
        volume_number = int(data.get("SequenceNumber", 1))  # por defecto 1
        res = {}

        for item in items:
            ref = item.get("ReleaseResourceReference")
            seq = item.get("SequenceNumber")
            if ref is not None:
                res[ref] = {
                    "volume": volume_number,
                    "sequence": int(seq) if seq is not None else None
                }

        return res

    for r in releases:
        release_ref = r.get("ReleaseReference")

        # Títulos multilingües
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

        # Duración como string ISO y MySQL TIME
        iso_duration = r.get("Duration")
        mysql_duration = self.iso8601_to_mysql_time(iso_duration) if iso_duration else None

        # Track references y resource group
        track_refs = []
        rg = r.get("ResourceGroup", {})
        resource_items = rg.get("ResourceGroupContentItem", [])
        for item in resource_items:
            ref_id = item.get("ReleaseResourceReference")
            if ref_id:
                track_refs.append(ref_id)

        resource_group_result = parse_resource_group(rg)

        resultado[release_ref] = {
            "title": title_dict,
            "artist": r.get("DisplayArtistName"),
            "year": r.get("PLine", {}).get("Year"),
            "genre": r.get("Genre", {}).get("GenreText"),
            "duration": iso_duration,
            "duration_time": mysql_duration,
            "original_release_date": r.get("OriginalReleaseDate"),
            "release_type": r.get("ReleaseType"),
            "grid": r.get("ReleaseId", {}).get("GRid"),
            "icpn": r.get("ReleaseId", {}).get("ICPN"),
            "subtitle": r.get("Subtitle"),  # puede no estar
            "track_references": track_refs,
            "resource_group": rg,
        }

        # Solo usar el primero
        break

    return {
        'result': resultado,
        'add_as_instance_var': {
            'resource_group': resource_group_result
        }
    }
def track_release_dep(self, data, **kwargs):
    track_raw = data
    tracks = track_raw if isinstance(track_raw, list) else [track_raw]
    tracks_info = {}
    track_release_reference = {}

    for track in tracks:
        ref = track["ReleaseReference"]
        release_id = track.get("ReleaseId", {})
        proprietary_id = release_id.get("ProprietaryId", {})
        resource_ref = track.get("ReleaseResourceReference")

        # 🛠 Crear objeto Track
        t = Track()
        t.isrc_track = proprietary_id.get("#text")
        t.grid_track = release_id.get("GRid")
        t.name_track = self.sound_recording_value.get(resource_ref, {}).get('Title')
        t.version_track = track.get("Version")
        t.length_track = iso8601_to_mysql_time(self.sound_recording_value.get(resource_ref, {}).get('Duration'))
        t.explicit_track = bool(self.sound_recording_value.get(resource_ref, {}).get('ParentalWarningType'))
        t.active_track = True  # o podés decidirlo según algún campo
        self.album.tracks_list.append(t)
        m.bulk_upsert(objects=self.album.tracks_list, session=self.session)

        # 🧱 Asignar valores a self acá ceo las relaciones entre álbum y track, no las guardo
        # hasta más adelante, el id todavía no existe
        at = AlbumTrack()
        at.id_album = self.album.id_album
        at.id_track = t.id_track
        at.volume_album_track = self.resource_group_value.get(resource_ref, []).get('volume')
        at.number_album_track = self.resource_group_value.get(resource_ref, []).get('sequence')
        self.album.album_track_relation.append(at)

        # Datos extras para otros propósitos
        tracks_info[ref] = {
            "resource_reference": resource_ref,
            "isrc": t.isrc_track,
            "isrc_namespace": proprietary_id.get("@Namespace"),
            "grid": t.grid_track,
            "label": track.get("ReleaseLabelReference", {}).get("#text"),
            "genre": track.get("Genre", {}).get("GenreText"),
        }

        if ref not in track_release_reference:
            track_release_reference[ref] = []
        track_release_reference[ref].append(resource_ref)

    return {
        'result': tracks_info,
        'add_as_instance_var': {
            'track_release_reference': track_release_reference,
        }
    }
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

        tracks_info[resource_ref] = {
            "release_reference": ref,
            "resource_reference": resource_ref,
            "isrc": proprietary_id.get("#text"),
            "isrc_namespace": proprietary_id.get("@Namespace"),
            "grid": release_id.get("GRid"),
            "version": track.get("Version"),
            "label": track.get("ReleaseLabelReference", {}).get("#text"),
            "genre": track.get("Genre", {}).get("GenreText"),
        }

        if ref not in track_release_reference:
            track_release_reference[ref] = []
        track_release_reference[ref].append(resource_ref)

    return {
        'result': tracks_info,
        'add_as_instance_var': {
            'track_release_reference': track_release_reference
        }
    }
# Acá pongo los métodos que uso para asignar los valores a los modelos

def release_assign_fields(self) -> None:
    release_ref, release_data = next(iter(self.release_value.items()))
    self.album.upc_album = release_data.get("icpn")
    self.album.grid_album = release_data.get("grid")
    self.album.name_album = release_data.get("title", {}).get("default")
    self.album.subtitle_album = release_data.get("subtitle")
    self.album.release_type_album = release_data.get("release_type")
    self.album.length_album = release_data.get("duration_time")
    self.album.tracks_qty_album = len(release_data.get("track_references", []))
    self.album.release_date_album = release_data.get("original_release_date")

def track_release_assign(self) -> list:
    """
    Crea instancias Track desde self.track_release_value, usando datos adicionales
    desde self.sound_recording_value y self.resource_group_value.
    Las instancias se agregan a self.album.tracks_list.
    """
    tracks = []

    for resource_ref, data in self.track_release_value.items():
        sr = self.sound_recording_value.get(resource_ref, {})
        rg = self.resource_group_value.get(resource_ref, {})

        t = Track()
        t.isrc_track = data.get("isrc")
        t.grid_track = data.get("grid")
        t.name_track = sr.get("Title")  # desde self
        t.version_track = data.get("version")
        t.length_track = self.iso8601_to_mysql_time(sr.get("Duration")) if sr.get("Duration") else None
        t.explicit_track = bool(sr.get("ParentalWarningType"))
        t.active_track = True

        tracks.append(t)
        self.album.tracks_list.append(t)

    return tracks