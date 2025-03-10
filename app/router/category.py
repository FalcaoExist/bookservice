from fastapi import APIRouter
from schema import category
from services.file_services import FileService

router1 = APIRouter()

@router1.get('/')
def list_categories():
    file_services_instance = FileService()
    read_file = file_services_instance.read()
    return read_file

@router1.post('/create-category', name="rota criação")
def create(param: category.RequestCreateCategory):
    text_file = FileService()
    write_file = text_file.write(param.name)
    print(param)
    return True

