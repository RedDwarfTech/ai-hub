from fastapi import HTTPException, Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

security = HTTPBearer()

async def has_access(credentials: HTTPAuthorizationCredentials= Depends(security)):
    """
        Function that is used to validate the token in the case that it requires it
    """
    token = credentials.credentials
    if token is None:
        raise HTTPException(status_code=401, detail="Invalid authorization token")
