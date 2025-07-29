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