import xmltodict
import os

class ERNExtractor:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None
        self.message_header = {}
        self.party_map = {}
        self.resource_map = {}
        self.contributors_by_artist = {}
        self._parse()

    def _parse(self):
        with open(self.file_path, 'r', encoding='utf-8') as f:
            self.data = xmltodict.parse(f.read())

        root = self.data.get('ernm:NewReleaseMessage', {})

        # 1. MessageHeader
        self.message_header = root.get('MessageHeader', {})

        # 2. PartyList
        party_list = root.get('PartyList', {}).get('Party', [])
        if isinstance(party_list, dict):
            party_list = [party_list]
        for party in party_list:
            ref = party.get('PartyReference')
            if ref:
                self.party_map[ref] = party

        # 3. ResourceList
        resources = root.get('ResourceList', {})
        sound_recordings = resources.get('SoundRecording', [])
        if isinstance(sound_recordings, dict):
            sound_recordings = [sound_recordings]
        for rec in sound_recordings:
            ref = rec.get('ResourceReference')
            if not ref:
                continue
            # Remove TechnicalDetails from SoundRecordingEdition
            edition = rec.get('SoundRecordingEdition', {})
            if isinstance(edition, list):
                edition = edition[0]
            if isinstance(edition, dict):
                edition = {k: v for k, v in edition.items() if k != 'TechnicalDetails'}
            rec_copy = dict(rec)
            rec_copy['SoundRecordingEdition'] = edition
            self.resource_map[ref] = rec_copy

            # 3c. Contributors by ArtistPartyReference
            # DisplayArtist
            display_artists = rec.get('DisplayArtist', [])
            if isinstance(display_artists, dict):
                display_artists = [display_artists]
            for da in display_artists:
                artist_ref = da.get('ArtistPartyReference')
                if artist_ref:
                    self.contributors_by_artist.setdefault(artist_ref, []).append({'type': 'DisplayArtist', **da})

            # Contributor
            contributors = rec.get('Contributor', [])
            if isinstance(contributors, dict):
                contributors = [contributors]
            for c in contributors:
                party_ref = c.get('ContributorPartyReference')
                if party_ref:
                    self.contributors_by_artist.setdefault(party_ref, []).append({'type': 'Contributor', **c})

# Example usage
if __name__ == "__main__":
    xml_path = os.path.join("../xml_files", "file_ejemplo_1.xml")
    ern = ERNExtractor(xml_path)
    print("MessageHeader:")
    print(ern.message_header)
    print("\nParty Map:")
    for k, v in ern.party_map.items():
        print(f"{k}: {v}")
    print("\nResource Map:")
    for k, v in ern.resource_map.items():
        print(f"{k}: {v}")
    print("\nContributors by ArtistPartyReference:")
    for k, v in ern.contributors_by_artist.items():
        print(f"{k}: {v}")