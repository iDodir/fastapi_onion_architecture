from src.api.tasks import router as router_tasks
from src.api.users import router as router_users

all_routers = [
    router_tasks,
    router_users,
]
