from typing import Type

from src.db.db import async_session_maker
from src.repositories.task_history import TaskHistoryRepository
from src.repositories.tasks import TasksRepository
from src.repositories.users import UsersRepository


class IUnitOfWork:
    users: Type[UsersRepository]
    tasks: Type[TasksRepository]
    task_history: Type[TaskHistoryRepository]

    def __init__(self):
        ...

    async def __aenter__(self):
        ...

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        ...

    async def commit(self):
        ...

    async def rollback(self):
        ...


class UnitOfWork:
    def __init__(self):
        self.session_factory = async_session_maker

    async def __aenter__(self):
        self.session = self.session_factory()

        self.tasks = TasksRepository(self.session)
        self.task_history = TaskHistoryRepository(self.session)

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.rollback()
        await self.session.close()

    async def commit(self):
        await self.session.commit()

    async def rollback(self):
        await self.session.rollback()
