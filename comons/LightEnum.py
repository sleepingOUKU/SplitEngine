from enum import Enum

class LightEnum(Enum):
    DIRECTIONAL_LIGHT = 0;
    POINT_LIGHT = 1;
    SPOT_LIGHT = 2;
    AREA_LIGHT = 3;
    pass