from fastapi import APIRouter, Response, BackgroundTasks
from fastapi.responses import JSONResponse
from services.questionnaire import create_Questionnaire, get_overall_score, get_average_score, QuestionnaireSchema

questionnaire_router = APIRouter(prefix='/questionnaire', tags=['questionnaire'])

@questionnaire_router.post('/add')
def add_questionnaire_controller(questionnaire: QuestionnaireSchema):
    
    return create_Questionnaire(questionnaire)

@questionnaire_router.get('/overall')
def get_overall_score_controller():
    
    return get_overall_score()

@questionnaire_router.get('/average')
def get_average_score_controller(background_tasks: BackgroundTasks):
    if (get_average_score() is None): return JSONResponse(status_code=404, content={"message": "No data found"})
    buffer = get_average_score()
    background_tasks.add_task(buffer.close)
    headers = {'Content-Disposition': 'inline; filename="plot.png"'}
    
    return Response(buffer.getvalue(), headers=headers, media_type='image/png')