HEIGHT: int = 100
WIDTH: int = 100

SIZE: int = 100
NUM_BLOCK: int = 5
NUM_TRIAL: int = 15
NUM_SESSION: int = 3
EPOCH_DURATION: float = 3
ITI_DURATION: float = 0.1
CUE_DURATION: float = 1
NO_SUBSPELLER: int = 6
# FREQS: list = [12.4, 12.4, 12.4, 12.6, 12.6, 12.6, 12.8, 12.8, 12.8,
#                12.4, 12.4, 12.4, 12.6, 12.6, 12.6, 12.8, 12.8, 12.8,
#                12.4, 12.4, 12.4, 12.6, 12.6, 12.6, 12.8, 12.8, 12.8,
#                13.0, 13.0, 13.0, 13.2, 13.2, 13.2, 13.4, 13.4,  13.4,
#                13.0, 13.0, 13.0, 13.2, 13.2, 13.2, 13.4, 13.4,  13.4]

FREQS: list = [6 , 10 , 15]
# FREQS: list = [8 , 8, 10 , 10, 13, 13]
FREQS: list = [8, 8.2, 8.4, 8.6, 8.8, 9, 9.2, 9.4, 9.6]
# FREQS: list = [8, 9, 10, 11, 12, 13, 14, 15, 16, 8.2, 9.2, 10.2, 11.2, 12.2, 13.2, 14.2, 15.2, 16.2, 8.4, 9.4, 10.4, 11.4, 12.4, 13.4, 14.4, 15.4, 16.4, 8.6, 9.6, 10.6, 11.6, 12.6, 13.6, 14.6, 15.6, 16.6, 8.8, 9.8, 10.8, 11.8, 12.8, 13.8, 14.8, 15.8, 16.8]

# POSITIONS: list = [[-800, 300], [-600, 300], [-400, 300], [-200, 300], [0, 300], [200, 300], [400, 300], [600, 300], [800, 300],
#                    [-800, 150], [-600, 150], [-400, 150], [-200, 150], [0,150], [200, 150], [400, 150], [600, 150], [800, 150],
#                    [-800, 0], [-600, 0], [-400, 0], [-200, 0], [0,0], [200, 0], [400, 0], [600, 0], [800, 0],
#                    [-800, -150], [-600, -150], [-400, -150], [-200, -150], [0, -150], [200, -150], [400, -150], [600, -150], [800, -150],
#                    [-800, -300], [-600, -300], [-400, -300], [-200, -300], [0, -300], [200, -300], [400, -300], [600, -300], [800, -300]]


# POSITIONS: list = [(-800, 300), (-600, 300), (-400, 300), (-200, 300), (0, 300), (200, 300), (400, 300), (600, 300), (800, 300),             (-800, 150), (-600, 150), (-400, 150), (-200, 150), (0, 150), (200, 150), (400, 150), (600, 150), (800, 150),             (-800, 0), (-600, 0), (-400, 0), (-200, 0), (0, 0), (200, 0), (400, 0), (600, 0), (800, 0),             (-800, -150), (-600, -150), (-400, -150), (-200, -150), (0, -150), (200, -150), (400, -150), (600, -150), (800, -150),             (-800, -300), (-600, -300), (-400, -300), (-200, -300), (0, -300), (200, -300), (400, -300), (600, -300), (800, -300)]

POSITIONS: list = [(-800, 300), (0, 300), (800, 300), (-800, 0), (0,0), (800, 0), (-800, -300), (0, -300), (800, -300)]
# POSITIONS: list = [(0,300), (-600, -150), (600, -150)]
# POSITIONS: list = [(-600,300), (0,300), (600, 300), (-600, -150), (0, -150), (600, -150) ]
AMPLITUDE: float = 1.0
PHASES: list = [0, 1.75, 1.50, 1.25, 1.0, 0.75, 0.50, 0.25, 2.0, 0.35, 0.10, 1.85, 1.60, 1.35, 1.10, 0.85, 0.60, 2.35, 0.70, 0.45, 0.20, 1.95, 1.70, 1.45, 1.20, 0.95, 2.70, 1.05, 0.80, 0.55, 0.30, 0.05, 1.80, 1.55, 1.30, 3.05, 1.40, 1.15, 0.90, 0.65, 0.40, 0.15, 1.90, 1.65, 3.40]
# PHASES:list = [0, 0, 0, 0.35, 0.35, 0.35, 0.70, 0.70,  0.70,
#                0, 0, 0, 0.35, 0.35, 0.35, 0.70, 0.70,  0.70,
#                0, 0, 0, 0.35, 0.35, 0.35, 0.70, 0.70,  0.70,
#                1.05, 1.05, 1.05, 1.40, 1.40, 1.40, 1.75, 1.75, 1.75,
#                1.05, 1.05, 1.05, 1.40, 1.40, 1.40, 1.75, 1.75, 1.75]

# PHASES: list = [0 , 0 , 0]
# PHASES: list = [0 , 0 , 0, 0, 0, 0]
# PHASES: list = [0 , 0.35 , 0 , 0.35 , 0 , 0.35]
PHASES: list = [0 , 0.35 , 0.70 , 1.05 , 1.40 , 1.75, 0.10, 0.45, 0.80 ]
# TARGET_CHARACTERS:list = ["A", "B", "C", "J", "K", "L", "S", "T", "U",
#                       "D", "E", "F", "M", "N", "O", "V", "W", "X",
#                       "G", "H", "I", "P", "Q", "R", "Y", "Z", "0",
#                       "1", "2", "3", "7", "8", "9", "(", "Space",")",
#                       "4", "5", "6", ".", "?", ",", "!", "-", "<<"]
TARGET_CHARACTERS:list = ["A", "B", "C", "J", "K", "L", "S", "T", "U"]

# TARGET_CHARACTERS:list = ["A", "B", "C"]
# TARGET_CHARACTERS:list = ["A", "B", "C", "D", "E", "F"]
SUBSPELLERS:dict = {"1": ["A", "B", "C", "D", "E", "F", "G", "H", "I"],
                    "2": ["J", "K", "L", "M", "N", "O", "P", "Q", "R"],
                    "3": ["S", "T", "U", "V", "W", "X", "Y", "Z", "0"],
                    "4": ["1", "2", "3", "4", "5", "6"],
                    "5": ["7", "8", "9", ".", "?", ","],
                    "6": ["(", "Space", ")", "!", "-", "<<"]}
SERIAL_PORT:str = "COM3"
BOARD_ID:int = 8
PARTICIPANT_ID:str = "sunsun"
RECORDING_DIR:str = "simple_ssvep_v2/record"
TYPE_OF_FILE:str = ".fif"
CSV_DIR:str = "csv/"
BLOCK_BREAK:int = 1
MARKERS:dict = {"A": 1.0, "B": 2.0, "C": 3.0, "D": 4.0, "E": 5.0, "F": 6.0, "G": 7.0, "H": 8.0, "I": 9.0, "J": 10.0, "K": 11.0, "L": 12.0, "M": 13.0, "N": 14.0, "O": 15.0, "P": 16.0, "Q": 17.0, "R": 18.0, "S": 19.0, "T": 20.0, "U": 21.0, "V": 22.0, "W": 23.0, "X": 24.0, "Y": 25.0, "Z": 26.0, "0": 27.0, "1": 28.0, "2": 29.0, "3": 30.0, "4": 31.0, "5": 32.0, "6": 33.0, "7": 34.0, "8": 35.0, "9": 36.0, ".": 37.0, "?": 38.0, ",": 39.0, "(": 40.0, "Space": 41.0, ")": 42.0, "!": 43.0, "-": 44.0, "<<":45.0, "trial_start":99.0}