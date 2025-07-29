def release_43(self, node):
    release_data = {
        "ReleaseReference": node.findtext("ReleaseReference"),
        "ReleaseType": node.findtext("ReleaseType"),
        "GRid": node.find("ReleaseId/GRid").text,
        "ICPN": node.find("ReleaseId/ICPN").text,
        "CatalogNumber": node.find("ReleaseId/CatalogNumber").text,
        "DisplayTitleText": node.find("DisplayTitleText").text,
        "TitleText": node.find("DisplayTitle/TitleText").text,
        "DisplayArtistName": node.find("DisplayArtistName").text,
        "DisplayArtistReference": node.find("DisplayArtist/ArtistPartyReference").text,
        "DisplayArtistRole": node.find("DisplayArtist/DisplayArtistRole").text,
        "LabelReference": node.find("ReleaseLabelReference").text,
        "PLineYear": node.find("PLine/Year").text,
        "PLineText": node.find("PLine/PLineText").text,
        "Duration": node.find("Duration").text,
        "GenreText": node.find("Genre/GenreText").text,
        "OriginalReleaseDate": node.find("OriginalReleaseDate").text,
        "ParentalWarningType": node.find("ParentalWarningType").text,
        "AdditionalTitleText": node.find("ResourceGroup/AdditionalTitle/TitleText").text,
        "LinkedReleaseResourceReference": node.find("ResourceGroup/LinkedReleaseResourceReference").text,
        "ReleaseResourceReferences": [
            item.find("ReleaseResourceReference").text
            for item in node.findall("ResourceGroup/ResourceGroupContentItem")
        ]
    }
    return {'result':release_data }