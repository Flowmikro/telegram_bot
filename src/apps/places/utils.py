import random

from src.apps.places.texts import locations, poses


async def random_generate_pose_and_location() -> tuple[str, str, str]:
    location: str = random.choice(locations)
    random_pose: list[str, str] = random.choice(list(poses.items()))
    pose_key: str = random_pose[0]
    pose_item: str = random_pose[1]

    return location, pose_key, pose_item
