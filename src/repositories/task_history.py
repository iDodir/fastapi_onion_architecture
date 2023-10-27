from src.models.tasks import TaskHistory
from src.utils.repository import SQLAlchemyRepository


class TaskHistoryRepository(SQLAlchemyRepository):
    model = TaskHistory
