from app.src.controllers.apiRouter import router


@router.get('/health-check', status_code=200, tags=["Health Check"])
def health_check():
    return {'status_code':200}