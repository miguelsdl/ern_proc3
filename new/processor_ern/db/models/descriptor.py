class Descriptor:
    def __init__(self, album=None, tracks=None, album_track_links=None, contributors=None, album_contributor_links=None,
            track_contributor_links=None, ):
        self.album = album
        self.tracks_list = tracks or []
        self.album_track_relation = album_track_links or []

        self.contributors_list = contributors or []
        self.album_contributor_links = album_contributor_links or []
        self.track_contributor_links = track_contributor_links or []

    def save_all(self, session):
        pass
        # # 1. Guardar el álbum
        # self.album.save(session)

        # 2. Guardar contributors
        # for contributor in self.contributors_list:
        #     contributor.save(session)

        # 3. Guardar tracks
        # for track in self.tracks_list:
        #     track.save(session)

        # # 4. Resolver nombres de tracks para relaciones AlbumTrack
        # track_name_to_id = {t.name: t.id_album for t in self.tracks_list}
        # for link in self.album_track_relation:
        #     link.id_album = self.album.id_album
        #     if getattr(link, "id_track", None) is None and hasattr(link, "track_name"):
        #         link.id_track = track_name_to_id.get(link.track_name)
        #     if link.id_track is None:
        #         raise ValueError(f"❌ No se pudo resolver id_track para AlbumTrack: {link}")
        #     link.save(session)
        #
        # # 5. Guardar relaciones álbum-contributor
        # for acl in self.album_contributor_links:
        #     acl.id_album = self.album.id_album
        #     acl.save(session)
        #
        # # 6. Guardar relaciones track-contributor
        # for tcl in self.track_contributor_links:
        #     if tcl.id_track is None and hasattr(tcl, 'track_name'):
        #         tcl.id_track = track_name_to_id.get(tcl.track_name)
        #     if tcl.id_track is None:
        #         raise ValueError(f"❌ No se pudo resolver id_track para TrackContributor: {tcl}")
        #     tcl.save(session)
    def __repr__(self):
        return (
            f"AlbumDescriptor(\n"
            f"  album={self.album},\n"
            f"  tracks_list={[str(t) for t in self.tracks_list]},\n"
            f"  album_track_relation={[str(r) for r in self.album_track_relation]},\n"
            f"  contributors_list={[str(c) for c in self.contributors_list]},\n"
            f"  album_contributor_links={[str(a) for a in self.album_contributor_links]},\n"
            f"  track_contributor_links={[str(t) for t in self.track_contributor_links]}\n"
            f")"
        )