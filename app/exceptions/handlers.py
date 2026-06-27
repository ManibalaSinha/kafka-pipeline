
@app.exception_handler(AppException)
async def app_exception_handler(request, exc):
    return JSONResponse(
        status_code=400,
        content={"success": False, "message": exc.message},
    )