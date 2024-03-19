from os import path

DP_WIDTH = 1600
DP_HEIGHT = 900
DP_DELTA = (DP_WIDTH - DP_HEIGHT) // 2
FPS = 30

MIN_BG_SPEED = 2
MAX_BG_SPEED = 20
DELTA_BG_SPEED = 2
TIME_TO_BG_SPEED_UP = 5

SCORE = 0
BEST_SCORE = 0
PREVIOUS_SCORE = 0

TIME_TO_GENERATE_ENEMIE = 3
TIME_TO_GENERATE_COIN = 5

K_HITBOX = 0.85

USER_CAR_HEALTH = 3
USER_CAR_INVULNERABLE_TIME = 3

BLACK = (0, 0, 0)
BLACKS_ALPHA = [(0, 0, 0, 10), (0, 0, 0, 30), (0, 0, 0, 50), (0, 0, 0, 70), (0, 0, 0, 90), (0, 0, 0, 100)]
WHITE = (255, 255, 255)
GRAY = (102, 102, 102)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

AUDI = path.abspath("image/cars/right_size/audi.png")
AMBULANCE = path.abspath("image/cars/right_size/ambulance.png")
VIPER = path.abspath("image/cars/right_size/black_viper.png")
CAR = path.abspath("image/cars/right_size/car.png")
MINI_TRUCK = path.abspath("image/cars/right_size/mini_truck.png")
MINI_VAN = path.abspath("image/cars/right_size/mini_van.png")
POLICE = path.abspath("image/cars/right_size/police.png")
TAXI = path.abspath("image/cars/right_size/taxi.png")
TRUCK = path.abspath("image/cars/right_size/truck.png")

AUDI_SPIRIT = path.abspath("image/cars/right_size/spirit/audi.png")
VIPER_SPIRIT = path.abspath("image/cars/right_size/Spirit/black_viper.png")
CAR_SPIRIT = path.abspath("image/cars/right_size/Spirit/car.png")
TAXI_SPIRIT = path.abspath("image/cars/right_size/Spirit/taxi.png")
POLICE_SPIRIT = path.abspath("image/cars/right_size/Spirit/police.png")

CAR_PATH = AUDI
CAR_SPIRIT_PATH = AUDI_SPIRIT
CARS_PATH = [AUDI, AMBULANCE, VIPER, CAR, MINI_TRUCK, MINI_VAN, POLICE, TAXI, TRUCK]

BG_PATH = path.abspath("image/background/background-1_0.png")
BUTTON_PATH = path.abspath("image/buttons/Button08.png")
COIN_PATH = path.abspath("image/coins/coin.png")


def cliargparse():
    import argparse
    global USER_CAR_HEALTH, CAR_PATH, CAR_SPIRIT_PATH

    parser = argparse.ArgumentParser()

    parser.add_argument("-m", "--model", help="set user car model", type=str,
                        choices=["viper", "taxi", "police", "corvette"])
    parser.add_argument("--health", help="set user car health", type=int)
    args = parser.parse_args()

    if args.health:
        USER_CAR_HEALTH = args.health

    if args.model:
        if args.model.upper() == "VIPER":
            CAR_PATH = VIPER
            CAR_SPIRIT_PATH = VIPER_SPIRIT
        elif args.model.upper() == "TAXI":
            CAR_PATH = TAXI
            CAR_SPIRIT_PATH = TAXI_SPIRIT
        elif args.model.upper() == "POLICE":
            CAR_PATH = POLICE
            CAR_SPIRIT_PATH = POLICE_SPIRIT
        elif args.model.upper() == "CORVETTE":
            CAR_PATH = CAR
            CAR_SPIRIT_PATH = CAR_SPIRIT

