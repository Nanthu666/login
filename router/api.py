from fastapi import (
    APIRouter,
    status,
    Depends,
)
from fastapi.responses import JSONResponse, StreamingResponse
from sqlalchemy.orm import session, Session
from database import models, database,schemas
from authentication.username_authentication import (
    authenticate_user
)



router = APIRouter(
    prefix='/routers',
    tags=['API'],
)


@router.post("/signup")
async def signup(
    user: schemas.UserCreate,
    db: Session = Depends(database.get_db)
):
    """
    Endpoint to register a new user.

    Args:
    - user (schemas.UserCreate): User creation data.
    - db (Session): Database session.

    Returns:
    - JSONResponse: Response containing user details and status message.

    Raises:
    - HTTPException: If the email is already registered.

    Example:
    - To register a new user, send a POST request with user data to /signup.
        """
    existing_user = db.query(models.Users).filter(models.Users.email == user.email).first()
    if existing_user:

        return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={"user_details": user_details, "message": "Email already registered"},
    )

    new_user = database.create_user(db, user)

    user_details = {
        "email": new_user.email,
        "user_name": new_user.username,
        "first_name": new_user.first_name,
        "last_name": new_user.last_name,
    }

    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content={"user_details": user_details, "message": "User registered successfully"},
    )

@router.get("/login")
async def login(
    user=Depends(authenticate_user), db: session = Depends(database.get_db)
):
    """
    Authenticates the user with the provided credentials.

    Returns:
    - User: The authenticated user object.

    Raises:
    - HTTPException: If the authentication fails,
        either due to invalid password or email.
        - status_code (int): The HTTP status code (401 UNAUTHORIZED).
        - detail (str): The error message indicating
            the reason for the failed authentication.

    """
    user_details = {
        "email": user.email,
        "user_name": user.username,
        "first_name": user.first_name,
        "last_name": user.last_name,
    }
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={"user_details": user_details, "message": "Login successfully"},
    )