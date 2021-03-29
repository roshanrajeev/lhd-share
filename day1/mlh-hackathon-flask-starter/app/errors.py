from app import app

@app.errorhandler(500)
def internal_error(error):
    return "internal server error", 500

@app.errorhandler(404)
def not_found(error):
    return "not found",404