""" Configuration Related Functions """
import json

from .models import Configuration, Repository


DEFAULT_CONFIG = """
{
    "host": "0.0.0.0",
    "port": 6569,
    "repositories": [
        {
            "url": "https://github.com/_YOUR_ORGANIZATION/__YOUR_GITHUB_REPOSITORY__.git",
            "endpoint": "/your/desired/repository",
            "secret": null,
            "status_path": "./hellogitworld.status"
        }
    ]
}
"""


def write_default_config(config_path_name: str = "config.json"):
    """ Write Default Config if it doesn't exist """
    with open(config_path_name, "w") as file:
        file.write(DEFAULT_CONFIG)


def parse_config(config_path_name: str = "config.json"):
    """ Parse Config to Dataclass Model """
    with open(config_path_name, "r") as file:
        data = json.loads(
            "".join([
                    "".join(i.split(" ")).replace(":", ": ").replace(",", ", ")
                    for i in [
                        i.replace("\n", "") for i in file.readlines()
                    ]
                ]
            )
        )
    data["repositories"] = [Repository(**i) for i in data["repositories"]]
    data = Configuration(**data)
    return data


def init_config(config_path_name: str = "config.json"):
    print(f"Trying to load {config_path_name}")
    try: open(config_path_name, "r")
    except: write_default_config("config.json")
    finally:
        return parse_config()
