import datetime

from app.models.models import Party
from app.extensions.extensions import db

def db_add_party(creater_id, max_member_num, time, party_message, party_type):
    try:
        party = Party(creater_id=creater_id,    
            max_member_num=max_member_num, 
            time=time,
            party_message=party_message,
            party_type=party_type,
            create_time=datetime.datetime.now())
        db.session.add(party)
        db.session.commit()
        return True
    except Exception as e:
        print(str(e))
        return False

def db_get_party_by_id(party_id):
    try:
        party = Party.query.filter_by(id=party_id).first()
        return True, party
    except Exception as e:
        print(str(e))
        return False, None

def db_get_party_by_creater(creater_id):
    try:
        parties = []
        cursor = db.session.execute("SELECT * FROM party WHERE id = %s" % creater_id)
        for row in cursor:
            party = {'id': str(row[0]), 'creater_id': row[1], 'max_member_num': str(row[2]), 'time': row[3][:-7], 'create_time': row[4][:-7], 'party_message': row[5], 'party_type': row[6]}
            parties.append(party)
        return True, parties
    except Exception as e:
        print(str(e))
        return False, None

def delete_party(party_id):
    try:
        party = Party.query.filter_by(id=party_id).first()
        db.session.delete(party)
        db.session.commit()
        return True
    except Exception as e:
        print(str(e))
        return False

def complete_party(party_id):
    try:
        party = Party.query.filter_by(id=party_id).first()
        party.is_complete = True
        db.session.commit()
        return True
    except Exception as e:
        print(str(e))
        return False