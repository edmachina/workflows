from pydantic import BaseModel

from app.src.controllers import router
from workers.backend.worker import GreetingWorkflow


class NameRequest(BaseModel):
    name: str

@router.post('/name', status_code=201, response_model=dict)
async def say_hello(request: NameRequest):
    from app.src.main import app
    result = await app.state.temporal_client.execute_workflow(
        GreetingWorkflow.run, request.name, id=f"name-workflow-{request.name}", task_queue='name-task-queue'
    )
    return {
        "result": result
    }