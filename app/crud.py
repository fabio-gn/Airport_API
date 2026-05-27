from .database import *
import logging

logger = logging.getLogger(__name__)

def get_airports(page:int, size:int):
    logger.info(f"Fetching airports page={page} size={size}")
    start = (page - 1) * size
    end = start + size
    return {
        "page": page,
        "size": size,
        "total": len(airports_db),
        "data": list(airports_db.values())[start:end]
    }
def get_airport(airport_id: int):
    logger.info(f"Fetching airport id={airport_id}")
    airport = airports_db.get(airport_id)
    if not airport:
        logger.warning(f"Airport id={airport_id} not found")
    return airport


def create_airport(data: dict):
    new_id = max(airports_db.keys()) + 1
    new_airport = {"id": new_id, **data}
    airports_db[new_id] = new_airport
    logger.info(f"Airport created id={new_id}")
    return new_airport


def delete_airport(airport_id: int):
    if airport_id not in airports_db:
        logger.warning(f"Airport id={airport_id} not found")
        return False
    del airports_db[airport_id]
    logger.info(f"Airport deleted id={airport_id}")
    return True