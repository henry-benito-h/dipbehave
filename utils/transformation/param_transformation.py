import re

# from utils.random_resources import *
import transformation.random_resources
start_char = "*"
end_char = "*"

# def replace_parameters(context, text):
#     parameters = {
#         ":my_account_id": "100",
#         ":randomName": random_string(20)
#     }
#     for key in parameters.keys():
#         text = text.replace(key, str(parameters[key]))
#     return text


def replace_parameters(text):
    parameters_on_text = re.findall(f"{replace_special_char(start_char)}.*?{replace_special_char(end_char)}", text)
    for param in parameters_on_text:
        function_name = get_function_name(param)
        if not hasattr(transformation.random_resources, function_name):
            return None
        param_value = get_parameter_value(param)
        new_value = getattr(transformation.random_resources, function_name)(param_value) if param_value else getattr(
            transformation.random_resources, function_name)()
        text = text.replace(param, str(new_value))

    return text


def get_function_name(input_parameter):
    input_parameter = remove_containers(input_parameter)
    if "(" in input_parameter:
        index_of_parenthesis = input_parameter.index("(")
        function_name = input_parameter[0:index_of_parenthesis]
    else:
        function_name = input_parameter
    return function_name.lower().replace(" ", "_")


def remove_containers(input_parameter):
    return input_parameter.replace(start_char, "").replace(end_char, "")


def get_parameter_value(input_parameter):
    if "(" and ")" in input_parameter:
        start = input_parameter.index("(") + 1
        end = input_parameter.index(")")
        return input_parameter[start: end].split(',')
    return None


def replace_special_char(input_char):
    if input_char in "[|\^&+\-%*/=!>]":
        return "\\" + input_char
