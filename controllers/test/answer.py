from fastapi import APIRouter
from services.test.answer import list_all_answers, get_answer

answer_router = APIRouter(prefix='/answer', tags=['answer'])

@answer_router.get('/')
def list_all_answers_controller():
    
    return list_all_answers()

@answer_router.get('/{answer_id}')
def get_answer_controller(answer_id):
    return get_answer(answer_id)