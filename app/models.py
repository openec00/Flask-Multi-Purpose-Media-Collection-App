from app import db

class Entry(db.Model):
    id_no = db.Column(db.Integer, primary_key=True)
    asset_name = db.Column(db.String(64), index=True, nullable=False)
    format = db.Column(db.String(64), index=True, nullable=False)
    source = db.Column(db.String(64), index=True, nullable=False)
    full_description = db.Column(db.String(120), index=True, nullable=False)
    status = db.Column(db.Boolean, default=False)
