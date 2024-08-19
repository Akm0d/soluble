CONFIG = {
    "roster_file": {
        "default": "/srv/salt/roster",
        "help": "Path to the roster file for salt-ssh",
    },
    "minion_config": {
        "default": "/etc/salt/minion",
        "help": "Path to the minion configuration template. Defaults to '/etc/salt/minion' or the master's default minion config",
    },
}

CLI_CONFIG = {
    "roster_file": {"options": ["-R"], "subcommands": ["_global_"]},
    "minion_config": {"subcommands": ["minion"]},
    "ssh-target": {
        "positional": True,
        "display_priority": 0,
        "subcommands": ["_global_"],
        "help": "Target for the salt-ssh command. This is typically a minion ID, wildcard, or grain.",
    },
    "salt_command": {
        "positional": True,
        "display_priority": 1,
        "subcommands": ["minion"],
        "help": "The salt command to run on the ephemeral nodes",
    },
    "salt_options": {
        "positional": True,
        "display_priority": 2,
        "nargs": "...",
        "subcommands": ["minion"],
        "help": "Additional options to be passed to the salt command",
    },
    "salt_ssh-options": {
        "positional": True,
        "nargs": "...",
        "help": "Additional options to be forwarded to salt-ssh",
    },
}

SUBCOMMANDS = {
    "minion": {
        "help": "",
        "desc": "",
    }
}


DYNE = {"soluble": ["soluble"]}
