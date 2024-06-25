from fastapi import APIRouter
from services.questionnaire import create_Questionnaire

questionnaire_router = APIRouter(prefix='/questionnaire', tags=['questionnaire'])

@questionnaire_router.post('/add')
def add_questionnaire_controller():
    
    return create_Questionnaire()