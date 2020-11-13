""" Configuration Related Functions """
import json

from .models import Configuration, Repository


DEFAULT_CONFIG = """
{
    "host": "0.0.0.0",
    "port": 6569,
    "repositories": [
        {
            "url": "__YOUR_GITHUB_REPOSITORY__",
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


def parse_config():
    """ Parse Config to Dataclass Model """
    with open("config.json", "r") as file:
        data = json.loads(
            "".join(
                    [
                        "".join(i.split(" ")).replace(":", ": ").replace(",", ", ")
                        for i in [
                            i.replace("\n", "") for i in file.readlines()
                        ]
                    ]
                )
            )
    data["repositories"] = [Repository(**i) for i in data["repositories"]]
    data = Configuration(**data)
    print(data)
    return data
