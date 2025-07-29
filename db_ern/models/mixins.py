from sqlalchemy.exc import NoResultFound
from sqlalchemy import and_

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