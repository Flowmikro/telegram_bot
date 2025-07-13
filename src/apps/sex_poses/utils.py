import os
import json
import random

# Получаем путь до текущего файла (utils.py)
CURRENT_DIR = os.path.dirname(__file__)  # → src/apps/sex_poses
SRC_DIR = os.path.dirname(os.path.dirname(CURRENT_DIR))  # → src
JSON_PATH = os.path.join(SRC_DIR, "common", "poses.json")  # → src/common/poses.json

with open(JSON_PATH, "r", encoding="utf-8") as f:
    poses = json.load(f)


async def get_random_pose() -> tuple[str, ...]:
    json_result: dict = random.choice(poses)
    name = json_result.get("name")
    image = json_result.get("image")
    dignity = json_result.get("dignity")
    tip = json_result.get("tip")
    return name, image, dignity, tip
