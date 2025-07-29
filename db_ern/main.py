from db.session import SessionLocal
from models import Base
from models.album import Album
from models.track import Track
from models.album_track import AlbumTrack
from db.session import engine
from models.contributor import Contributor
from models.album_contributor import AlbumContributor
from models.track_contributor import TrackContributor


# 🛠️ Crear todas las tablas (si no existen)
Base.metadata.create_all(bind=engine)
# Crear tablas
Base.metadata.create_all(bind=engine)
session = SessionLocal()

# Test Album
a = Album(name="alb1", description="desc1")
a.save(session)

a2 = Album(name="alb1", description="updated desc")
a2.save(session)

a3 = Album(name="alb2", description="new alb")
a3.save(session)

# Test Track
t = Track(name="track1", description="desc track")
t.save(session)

t2 = Track(name="track1", description="updated track")
t2.save(session)

t3 = Track(name="track2", description="nuevo")
t3.save(session)

a3 = Album(name="alb1", description="lalalalallalalalallala")
a3.save(session)

# Insertar o actualizar una relación
rel1 = AlbumTrack(id_album=1, id_track=1, description="relación 1")
rel1.save(session)

# Actualizar esa misma relación
rel2 = AlbumTrack(id_album=1, id_track=1, description="relación actualizada")
rel2.save(session)

# Insertar otra
rel3 = AlbumTrack(id_album=1, id_track=2, description="otra relación")
rel3.save(session)

# Crear o actualizar un contributor
c1 = Contributor(name="Jane Doe", active=True)
c1.save(session)

# Asociar contributor a un álbum
ac = AlbumContributor(id_album=a.id_album, id_contributor=c1.id_contributor, rol="productor")
ac.save(session)

# Asociar contributor a un track
tc = TrackContributor(id_track=t.id_album, id_contributor=c1.id_contributor, rol="guitarrista")
tc.save(session)

session.close()