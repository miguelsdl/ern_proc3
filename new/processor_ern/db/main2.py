from db.session import SessionLocal, engine
from models import Base
from models.album import Album
from models.track import Track
from models.album_track import AlbumTrack
from models.contributor import Contributor
from models.album_contributor import AlbumContributor
from models.track_contributor import TrackContributor
from descriptors.album_descriptor import AlbumDescriptor

# 🛠 Crear las tablas
Base.metadata.create_all(bind=engine)
session = SessionLocal()

# 🎧 Crear el álbum
album = Album(name="Nuevo Álbum 3", description="Álbum completo de prueba. XXXXXXXXXXX")

# 🎵 Crear tracks
tracks = [
    Track(name="Track1", description="primer track"),
    Track(name="Track2", description="segundo track, XXXXXXX"),
]

# 👤 Contributors
contributors = [
    Contributor(name="Juan", active=True),
    Contributor(name="Ana", active=True),
]

# 🔗 Relaciones Album ↔ Track
at1 = AlbumTrack(description="versión principal")
at1.track_name = "Track1"

at2 = AlbumTrack(description="remix")
at2.track_name = "Track2"

album_track_links = [at1, at2]


# Album cintributor no va, es solo para los trakcs
# 🔗 Relaciones Album ↔ Contributor
album_contributor_links = [
    AlbumContributor(id_contributor=None, rol="Productor"),
    AlbumContributor(id_contributor=None, rol="Compositor2"),
]

# 🔗 Relaciones Track ↔ Contributor (usando track_name)
tc1 = TrackContributor(id_contributor=None, rol="Voz")
tc1.track_name = "Track1"

tc2 = TrackContributor(id_contributor=None, rol="Guitarra")
tc2.track_name = "Track2"

track_contributor_links = [tc1, tc2]

# 🔀 Asignar ids de contributor a relaciones
# (después del save se resolverán bien)
for i, ac in enumerate(album_contributor_links):
    ac.id_contributor = i + 1  # simplificado

for i, tc in enumerate(track_contributor_links):
    tc.id_contributor = i + 1

# 📦 Crear descriptor
descriptor = AlbumDescriptor(
    album=album,
    tracks=tracks,
    contributors=contributors,
    album_track_links=album_track_links,
    album_contributor_links=album_contributor_links,
    track_contributor_links=track_contributor_links,
)

# 💾 Guardar todo
descriptor.save_all(session)

# ✅ Mostrar resultado
print("\n✅ Objeto final guardado:")
print(descriptor)

session.close()