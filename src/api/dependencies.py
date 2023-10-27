from src.repositories.tasks import TasksRepository
from src.repositories.users import UsersRepository
from src.services.tasks import TasksService
from src.services.users import UsersService


def tasks_service():
    return TasksService(TasksRepository)


def users_service():
    return UsersService(UsersRepository)
