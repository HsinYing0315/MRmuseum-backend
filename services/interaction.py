from fastapi.responses import JSONResponse
import uuid

from database import session
from models.interaction import Interaction

def create_interaction(interaction):
    
    id = str(uuid.uuid4())
    new_interaction = Interaction(
                          id             = id,
                          type            = interaction['type'],
                          content        = interaction['content'],
                          visitorID       = interaction['visitorID'],
                          exhibitID       = interaction['exhibitID'],
                          )
    session.add(new_interaction)
    session.commit()

    return JSONResponse(content="interaction recorded")

def get_interaction_count(visitorID):
    interactions = session.query(Interaction).filter_by(visitorID=visitorID).all()
    return len(interactions)

def get_interaction_duration(visitorID):
    interactions = session.query(Interaction).filter_by(visitorID=visitorID, type='duration').all()
    
    if (len(interactions) == 0):
        return 0
    total = 0
    for interaction in interactions:
        interaction = interaction.toDict()
        total += interaction['content']
        
    return total / len(interactions)
