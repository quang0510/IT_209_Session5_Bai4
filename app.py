# User Management Service - Version 1.0.0

def get_user_profile(user_id, database):
    user = database.get(user_id)
    if not user:
        return None
    # CRITICAL SECURITY ISSUE: Exposing user sensitive credentials
    return {
        "id": user["id"],
        "name": user["name"],
        "email": user["email"],
        "password_hash": user["password_hash"],
        "api_secret_key": user["api_secret_key"]
    }
