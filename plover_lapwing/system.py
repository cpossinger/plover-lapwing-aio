from plover.system.english_stenotype import *

KEYS = (
    "#",
    "^-",
    "+-",
    "S-",
    "T-",
    "K-",
    "P-",
    "W-",
    "H-",
    "R-",
    "A-",
    "O-",
    "@",
    "*",
    "-E",
    "-U",
    "-F",
    "-R",
    "-P",
    "-B",
    "-L",
    "-G",
    "-T",
    "-S",
    "-D",
    "-Z",
)

IMPLICIT_HYPHEN_KEYS = ("A-", "O-", "-E", "-U", "@", "*")

NUMBER_KEY = None

NUMBERS = {}

FERAL_NUMBER_KEY = False

KEYMAPS = {
    "Gemini PR": {
        "#": (
            "S1-",
            "#1",
            "#2",
            "#3",
            "#4",
            "#5",
            "#6",
            "#7",
            "#8",
            "#9",
            "#A",
            "#B",
            "#C",
        ),
        "S-": "S2-",
        "T-": "T-",
        "K-": "K-",
        "P-": "P-",
        "W-": "W-",
        "H-": "H-",
        "R-": "R-",
        "A-": "A-",
        "O-": "O-",
        "*": ("*1", "*2", "*3", "*4"),
        "-E": "-E",
        "-U": "-U",
        "-F": "-F",
        "-R": "-R",
        "-P": "-P",
        "-B": "-B",
        "-L": "-L",
        "-G": "-G",
        "-T": "-T",
        "-S": "-S",
        "-D": "-D",
        "-Z": "-Z",
        "no-op": ("Fn", "pwr", "res1", "res2"),
    },
    "Keyboard": {
        "#": ("q", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "-", "="),
        "S-": "a",
        "T-": "w",
        "K-": "s",
        "P-": "e",
        "W-": "d",
        "H-": "r",
        "R-": "f",
        "A-": "c",
        "O-": "v",
        "*": ("t", "g", "y", "h"),
        "-E": "n",
        "-U": "m",
        "-F": "u",
        "-R": "j",
        "-P": "i",
        "-B": "k",
        "-L": "o",
        "-G": "l",
        "-T": "p",
        "-S": ";",
        "-D": "[",
        "-Z": "'",
        "arpeggiate": "space",
        # Suppress adjacent keys to prevent miss-strokes.
        "no-op": ("z", "x", "b", ",", ".", "/", "]", "\\"),
    },
    "Passport": {
        "#": ("C", "#"),
        "S-": "S",
        "T-": "T",
        "K-": "K",
        "P-": "P",
        "W-": "W",
        "H-": "H",
        "R-": "R",
        "A-": "A",
        "O-": "O",
        "*": ("~", "*"),
        "-E": "E",
        "-U": "U",
        "-F": "F",
        "-R": "Q",
        "-P": "N",
        "-B": "B",
        "-L": "L",
        "-G": "G",
        "-T": "Y",
        "-S": "X",
        "-D": "D",
        "-Z": "Z",
        "no-op": ("!", "^", "+"),
    },
    "Stentura": {
        "#": "#",
        "S-": "S-",
        "T-": "T-",
        "K-": "K-",
        "P-": "P-",
        "W-": "W-",
        "H-": "H-",
        "R-": "R-",
        "A-": "A-",
        "O-": "O-",
        "*": "*",
        "-E": "-E",
        "-U": "-U",
        "-F": "-F",
        "-R": "-R",
        "-P": "-P",
        "-B": "-B",
        "-L": "-L",
        "-G": "-G",
        "-T": "-T",
        "-S": "-S",
        "-D": "-D",
        "-Z": "-Z",
        "no-op": "^",
    },
    "TX Bolt": {
        "#": "#",
        "S-": "S-",
        "T-": "T-",
        "K-": "K-",
        "P-": "P-",
        "W-": "W-",
        "H-": "H-",
        "R-": "R-",
        "A-": "A-",
        "O-": "O-",
        "*": "*",
        "-E": "-E",
        "-U": "-U",
        "-F": "-F",
        "-R": "-R",
        "-P": "-P",
        "-B": "-B",
        "-L": "-L",
        "-G": "-G",
        "-T": "-T",
        "-S": "-S",
        "-D": "-D",
        "-Z": "-Z",
    },
    "Treal": {
        "#": ("S1-", "#1", "#2", "#3", "#4", "#5", "#6", "#7", "#8", "#9", "#A", "#B"),
        "S-": "S2-",
        "T-": "T-",
        "K-": "K-",
        "P-": "P-",
        "W-": "W-",
        "H-": "H-",
        "R-": "R-",
        "A-": "A-",
        "O-": "O-",
        "*": ("*1", "*2"),
        "-E": "-E",
        "-U": "-U",
        "-F": "-F",
        "-R": "-R",
        "-P": "-P",
        "-B": "-B",
        "-L": "-L",
        "-G": "-G",
        "-T": "-T",
        "-S": "-S",
        "-D": "-D",
        "-Z": "-Z",
        "no-op": ("X1-", "X2-", "X3"),
    },
}

DICTIONARIES_ROOT = "asset:plover_lapwing:dictionaries"
DEFAULT_DICTIONARIES = (
    "user.json",
    "jeff-phrasing.py",
    "abby-left-hand-modifiers.py",
    "emily-modifiers.py",
    "emily-symbols.py",
    "lapwing-movement.modal",
    "lapwing-commands.json",
    "lapwing-numbers.json",
    "lapwing-uk-additions.json",
    "lapwing-proper-nouns.json",
    "lapwing-base.json",
)
