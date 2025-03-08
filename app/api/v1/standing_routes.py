from fastapi import APIRouter
from app.services.standing_service import *
from app.models.standing import *

router = APIRouter()

@router.get("/", response_model=List[Standing])
def get_standings_endpoint():
    """
    Endpoint to retrieve NBA standings from the external NBA API.

    Returns:
        List[Standing]: A list of Standing objects representing NBA team standings.
    """
    return get_standings_from_nba_api()
