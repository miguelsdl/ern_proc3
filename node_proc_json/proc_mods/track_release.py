def track_releases_43(self, data, **kwargs):
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