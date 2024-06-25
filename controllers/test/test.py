from fastapi import APIRouter
from services.test.test import list_all_tests, get_test

test_router = APIRouter(prefix='/test', tags=['test'])

@test_router.get('/')
def list_all_tests_controller():
    
    return list_all_tests()

@test_router.get('/<test_id>')
def get_test_controller(test_id):
    return get_test(test_id)