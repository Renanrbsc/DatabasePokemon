from typing import List, Dict
import copy


def convert_txt_for_json(data: str, model_dict: Dict) -> List[dict]:
    list_of_processed_data: List[dict] = list()
    data_list: List[str] = data.strip().split("\r\n")

    for index_row, field_str in enumerate(data_list):
        processed_row: List[str, str] = field_str.split(';')
        processed_row.insert(0, str(index_row + 1))

        for index_field, key in enumerate(model_dict):
            model_dict[key]: str = processed_row[index_field]

        dict_save: Dict[str: str] = copy.deepcopy(model_dict)
        list_of_processed_data.append(dict_save)

    return list_of_processed_data
