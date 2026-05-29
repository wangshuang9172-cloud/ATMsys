from typing import Any


def get_nested_value(obj:dict[str,Any], path:str,default:Any = None) -> Any:
    '''
    安全地获取嵌套对象中的深层次路径下的值
    :param obj: 目标嵌套字典对象
    :param path: 路径
    :param default: 路径不存在时的默认返回值，默认为None
    :return: 返回默认值或目标值
    '''
    if not path:
        return default
    keys = path.split('.')
    curent = obj
    for key in keys:
        if isinstance(curent, dict) and key in curent:
            curent = curent[key]
        else:
            return default
    return curent

