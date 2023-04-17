from app.extensions.extensions import db

class Party(db.Model):
    __tablename__ = 'party'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, doc='Party ID')

    creater_id = db.Column(db.String(20), unique=True, doc='Party Creater ID')
    
    max_member_num = db.Column(db.Integer, unique=True, doc='Party Max Member Number')

    time = db.Column(db.DateTime, unique=True, doc='Party Time')

    create_time = db.Column(db.DateTime, unique=True, doc='Party Create Time')

    party_message = db.Column(db.String(100), unique=True, doc='Party Message')

    party_type = db.Column(db.String(20), unique=True, doc='Party Type')

    is_complete = db.Column(db.Boolean, unique=True, doc='Party Is Complete')

    attenders = db.relationship('Attender', backref='party', lazy='dynamic')

class Attender(db.Model):
    __tablename__ = 'attender'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, doc='Attender ID')

    party_id = db.Column(db.Integer, db.ForeignKey('party.id'), doc='Party ID')
    