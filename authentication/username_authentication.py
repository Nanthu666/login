from database import models, database
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import session
from passlib.context import CryptContext
from fastapi.security import HTTPBasic, HTTPBasicCredentials, HTTPBearer


security = HTTPBasic()



def authenticate_user(
    credentials: HTTPBasicCredentials = Depends(security),
    db: session = Depends(database.get_db),
):
    email = credentials.username
    password = credentials.password

    user = (
        db.query(
            models.Users.email,
            models.Users.username,
            models.Users.first_name,
            models.Users.last_name,
            models.Users.password,
        )
        .filter(models.Users.email == email)
        .first()
    )
    print(user.password)

    if user:
        stored_password = user.password
        if password == stored_password:
            return user
        else:
            message = "Invalid password"
    else:
        message = "Invalid email"

    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=message)

