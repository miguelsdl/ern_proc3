def releases_43(self, data, **kwargs):
    releases_raw = data
    releases = releases_raw if isinstance(releases_raw, list) else [releases_raw]

    resultado = {}

    for r in releases:
        ref = r["ReleaseReference"]
        resultado[ref] = {
            "title": r["DisplayTitle"]["TitleText"],
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
                resultado[ref]["track_references"].append(ref_id)

    return {'result': resultado, }