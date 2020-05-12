from enum import Enum

class LightEnum(Enum):
    # 直线光源
    DIRECTIONAL_LIGHT = 0
    # 点光源
    POINT_LIGHT = 1
    # 散射光源
    SPOT_LIGHT = 2
    # 环境光
    AREA_LIGHT = 3

    # 光源是否启用
    LIGHT_STATUS_ON = True
    LIGHT_STATUS_OFF = False
    pass