from enum import Enum

class SIDE_PHOTO_COLUMNS(Enum):
    ACCESS_ID = 0
    BACK_ARG = 1
    LEG_ARG = 2
    FILE_PATH = 3
    CREATED_AT = 4

def ave_for_side_photos(photos):
    back_arg_ave = sum([back_arg[SIDE_PHOTO_COLUMNS.BACK_ARG.value] for back_arg in photos]) / len(photos)
    leg_arg_ave = sum([leg_arg[SIDE_PHOTO_COLUMNS.LEG_ARG.value] for leg_arg in photos]) / len(photos)
    return back_arg_ave, leg_arg_ave

def getPhotosPathByClosest(data, num, key:SIDE_PHOTO_COLUMNS):
    # 最も近い値を見つける
    closest_value = None
    closest_difference = None

    for row in data:
        value = row[key.value]

        if type(value) is not float and type(value) is not int:
            return None
        difference = abs(value - num)

        if closest_value is None or difference < closest_difference:
            closest_value = value
            closest_row = row
            closest_difference = difference
            
    return closest_row[SIDE_PHOTO_COLUMNS.FILE_PATH.value]
    