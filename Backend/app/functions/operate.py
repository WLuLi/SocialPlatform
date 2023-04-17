from flask import Blueprint, request, jsonify
from app.functions.database import db_get_party_by_id, db_get_party_by_creater, db_add_party, delete_party, complete_party

operate_bp = Blueprint("operate", __name__)

@operate_bp.route("/getPartyById", methods=["GET"])
def getPartyById():
    party_id = request.json.get("party_id")
    status, party = db_get_party_by_id(party_id)
    if status:
        return jsonify({"party": party}), 200
    else:
        return status, 500

@operate_bp.route("/getPartyByCreater", methods=["GET"])
def getPartyByCreater():
    creater_id = request.json.get("creater_id")
    status, parties = db_get_party_by_creater(creater_id)
    if status:
        return jsonify({"parties": parties}), 200
    else:
        return status, 500

@operate_bp.route("/addParty", methods=["POST"])
def addParty():
    creater_id = request.json.get("creater_id")
    max_member_num = request.json.get("max_member_num")
    time = request.json.get("time")
    party_message = request.json.get("party_message")
    party_type = request.json.get("party_type")
    status = db_add_party(creater_id, max_member_num, time, party_message, party_type)
    if status:
        return status, 201
    else:
        return status, 500

@operate_bp.route("/deleteParty", methods=["POST"])
def deleteParty():
    party_id = request.json.get("party_id")
    status = delete_party(party_id)
    if status:
        return status, 200
    else:
        return status, 500

@operate_bp.route("/completeParty", methods=["POST"])
def completeParty():
    party_id = request.json.get("party_id")
    status = complete_party(party_id)
    if status:
        return status, 200
    else:
        return status, 500