from sqlalchemy.exc import NoResultFound
from sqlalchemy import and_, or_

class SaveByFieldsMixin:
    __unique_fields__ = ('name',)  # Valor por defecto

    def save(self, session):
        model_cls = type(self)
        filters = [getattr(model_cls, field) == getattr(self, field) for field in self.__unique_fields__]
        try:
            existing = session.query(model_cls).filter(and_(*filters)).one()
            for attr in self.__table__.columns.keys():
                if attr not in self.__mapper__.primary_key[0].name:
                    setattr(existing, attr, getattr(self, attr))
            session.commit()
            pk_field = self.__mapper__.primary_key[0].name
            setattr(self, pk_field, getattr(existing, pk_field))
            print(f"✔️ Actualizado: {existing}")
        except NoResultFound:
            session.add(self)
            session.commit()
            print(f"🆕 Insertado: {self}")

    @classmethod
    def bulk_upsert(cls, objects: list, session):
        unique_fields = cls.__unique_fields__
        if not unique_fields:
            raise ValueError(f"{cls.__name__} must define __unique_fields__ for bulk_upsert")

        # Armar conjunto de filtros únicos
        filters = [
            tuple(getattr(obj, field) for field in unique_fields)
            for obj in objects
        ]

        # Armar consulta para encontrar existentes
        filters_clause = [and_(*[getattr(cls, f) == val for f, val in zip(unique_fields, key)])
                          for key in filters]

        existing_objs = (
            session.query(cls)
            .filter(or_(*filters_clause))
            .all()
        )

        # Indexar por valores únicos
        existing_map = {
            tuple(getattr(e, field) for field in unique_fields): e
            for e in existing_objs
        }

        for obj in objects:
            key = tuple(getattr(obj, field) for field in unique_fields)
            if key in existing_map:
                existing = existing_map[key]
                for attr in obj.__table__.columns.keys():
                    if attr != obj.__mapper__.primary_key[0].name:
                        setattr(existing, attr, getattr(obj, attr))
                session.add(existing)
                setattr(obj, obj.__mapper__.primary_key[0].name, getattr(existing, obj.__mapper__.primary_key[0].name))
            else:
                session.add(obj)

        session.flush()