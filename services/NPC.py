from flask import request, jsonify
import uuid

from models.NPC import NPC

def meet_NPC(exhibitID):
    response = NPC.query.get(exhibitID=exhibitID).toDict()
    
    return jsonify(response)

def interact_NPC():
    request_form = request.form.to_dict()

    return 