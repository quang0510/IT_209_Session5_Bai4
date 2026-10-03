# User Management Service - Version 1.0.1 (Hotfix)

def get_user_profile(user_id, database):
    user = database.get(user_id)
    if not user:
        return None
    # HOTFIX v1.0.1: Removed sensitive credentials leak (password_hash, api_secret_key)
    return {
        "id": user["id"],
        "name": user["name"],
        "email": user["email"]
    }
