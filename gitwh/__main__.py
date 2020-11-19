from typing import List

def _init(args: List[str] = []): ...

def _add(args: List[str] = []): ...

def _list(args: List[str] = []): ...

def _rem(args: List[str] = []): ...

def _run(args: List[str] = []): ...

commands = {
    "help": {
        "alias": ["h", "help"],                  # Help
        "func": lambda args: 
            print(commands["help"]["help"]) if len(args) == 0 else\
            print(commands[args[0]]["help"]) if len(args) == 1 else\
            print("Help only accept one arguments !"),
        "help": "\n".join([
            "Git Webhook Helper",
            "Help you make automize webhook for your repository collection",
            "Usage:",
            "    gitwh [command] [args]",
            "",
            "Commands:",
            "    h, help            Show this Help message",
            "    i, init,           initialize repositories collection",
            "    initialize         folders",
            "    add                add new repository to collection",
            "    l, ls, list        list of added repositories",
            "    rm, rem, remove    remove repository from collection",
        ])
    },
    "init": {
        "alias": ["i", "init", "initialize"],    # Initialize
        "func": lambda args: _init(args) if len(args) > 1 else commands["help"]["func"](["init"]),
        "help": "\n".join([
            "Git Webhook Helper > Init",
            "Initialize repository collection",
            "",
            "Usage:",
            "   gitwh i <args>          OR",
            "   gitwh init <args>       OR",
            "   gitwh initialize <args>",
            "",
            "Arguments:",
            "   here                Initialize repository collection in",
            "                       Current working directories",
            "   at <where>          Initialize repository collection at",
            "                       a specific location spesified",
            "                       with <where> subarguments",
        ])
    },
    "add" : {
        "alias": ["add"],                           # Add Repo
        "func": _add,
        "help": "\n".join([
            "Git Webhook Helper > Add",
            "Add repository to your location",
            "",
            "Usage:",
            "   gitwh i <args>          OR",
            "   gitwh init <args>       OR",
            "   gitwh initialize <args>",
            "",
            "Arguments:",
            "   here                Initialize repository collection in",
            "                       Current working directories",
            "   at <where>          Initialize repository collection at",
            "                       a specific location spesified",
            "                       with <where> subarguments",
        ])
    },
    "list": {
        "alias": ["l", "ls", "list"],               # List repos
        "func": _list,
        "help": "\n".join([
            "Git Webhook Helper > Add",
            "Add repository to your location",
            "",
            "Usage:",
            "   gitwh i <args>          OR",
            "   gitwh init <args>       OR",
            "   gitwh initialize <args>",
            "",
            "Arguments:",
            "   here                Initialize repository collection in",
            "                       Current working directories",
            "   at <where>          Initialize repository collection at",
            "                       a specific location spesified",
            "                       with <where> subarguments",
        ])
    },
    "rem" : {
        "alias": ["rm", "rem", "remove"],           # Remove Repo
        "func": _rem,
        "help": """
        """
    },
    "run" : {
        "alias": ["run"],                           # Run Server
        "func": _run,
        "help": """
        """
    },
}

avail_commands = []
[(avail_commands:=avail_commands + commands[i]["alias"]) for i in commands]

def parse_args(args: List[str]):
    if len(args[1::]) <= 0:
        print(f"gitwh: command not provided !")
        print(f"  please refer to 'gitwh help'")
        exit(250)
    args = args[1::]
    arguments = args[1::]
    if not args[0] in avail_commands:
        print(f"gitwh: {args} is not a valid command")
        exit(251)
    for i in commands:
        if args[0] in commands[i]["alias"]:
            print(commands[i]["func"], arguments)
            commands[i]["func"](arguments)
    
if __name__ == "__main__":
    import sys
    parse_args(sys.argv)