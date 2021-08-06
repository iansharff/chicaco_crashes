import pickle
"""
This script is for determining the aggregated target values in 'PRIM_CONTRIBUTORY_CAUSE' and saving them as
a PKL file to be used for the modeling notebooks. It can be run in the terminal from the root directory.
"""

def main():
    driving = [
        'FAILING TO YIELD RIGHT-OF-WAY',
        'FOLLOWING TOO CLOSELY',
        'IMPROPER OVERTAKING/PASSING',
        'FAILING TO REDUCE SPEED TO AVOID CRASH',
        'IMPROPER BACKING',
        'IMPROPER LANE USAGE',
        'IMPROPER TURNING/NO SIGNAL',
        'DRIVING SKILLS/KNOWLEDGE/EXPERIENCE',
        'OPERATING VEHICLE IN ERRATIC, RECKLESS, CARELESS, NEGLIGENT OR AGGRESSIVE MANNER',
        'PHYSICAL CONDITION OF DRIVER',
        'UNDER THE INFLUENCE OF ALCOHOL/DRUGS (USE WHEN ARREST IS EFFECTED)',
        'DRIVING ON WRONG SIDE/WRONG WAY',
        'EXCEEDING AUTHORIZED SPEED LIMIT',
        'EXCEEDING SAFE SPEED FOR CONDITIONS',
        'CELL PHONE USE OTHER THAN TEXTING',
        'HAD BEEN DRINKING (USE WHEN ARREST IS NOT MADE)',
        'TURNING RIGHT ON RED',
        'DISTRACTION - OTHER ELECTRONIC DEVICE (NAVIGATION DEVICE, DVD PLAYER, ETC.)',
        'TEXTING',
    ]

    disregarding_signs = [
        'DISREGARDING TRAFFIC SIGNALS',
        'DISREGARDING STOP SIGN',
        'DISREGARDING OTHER TRAFFIC SIGNS',
        'DISREGARDING ROAD MARKINGS',
        'DISREGARDING YIELD SIGN',
        'PASSING STOPPED SCHOOL BUS'
    ]

    environment = [
        'WEATHER',
        'VISION OBSCURED (SIGNS, TREE LIMBS, BUILDINGS, ETC.)',
        'DISTRACTION - FROM INSIDE VEHICLE',
        'DISTRACTION - FROM OUTSIDE VEHICLE',
        'ROAD ENGINEERING/SURFACE/MARKING DEFECTS',
        'ROAD CONSTRUCTION/MAINTENANCE',
        'EVASIVE ACTION DUE TO ANIMAL, OBJECT, NONMOTORIST',
        'RELATED TO BUS STOP',
        'BICYCLE ADVANCING LEGALLY ON RED LIGHT',
        'MOTORCYCLE ADVANCING LEGALLY ON RED LIGHT',
        'ANIMAL',
        'OBSTRUCTED CROSSWALKS',
        'EQUIPMENT - VEHICLE CONDITION'
    ]

    driving_dict = dict.fromkeys(driving, "DRIVER")
    disregarding_signs_dict = dict.fromkeys(disregarding_signs, "DISREGARDING_SIGNS")
    environment_dict = dict.fromkeys(environment, "ENVIRONMENT")
    binned_causes = {**driving_dict, **disregarding_signs_dict, **environment_dict}
    with open('data/binned_causes.pkl', 'wb') as f:
        pickle.dump(binned_causes, f)


if __name__ == '__main__':
    main()
