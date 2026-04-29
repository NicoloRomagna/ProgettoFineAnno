from app.models import Lego
from app import db

class LegoRepository:

    def get_all(self):
        return Lego.query.all()

    def get_by_id(self, lego_id):
        return Lego.query.get(lego_id)

    def add(self, name, description, image=None):
        lego = Lego(
            name=name,
            description=description,
            image=image
        )
        db.session.add(lego)
        db.session.commit()
        return lego

    def delete(self, lego_id):
        lego = Lego.query.get(lego_id)
        if lego:
            db.session.delete(lego)
            db.session.commit()
        return lego