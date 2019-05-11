from transformation.param_transformation import *


def test_replace_special_char():
    new_string = replace_special_char('*')
    assert new_string == '\\*'


def test_get_wrong_parameter_value():
    assert get_parameter_value("something") is None


def test_get_parameter_value():
    assert get_parameter_value("something(20,43)") == ['20', '43']


def test_get_function_name_with_parameters():
    assert get_function_name('function name(test)') == 'function_name'


def test_get_function_name():
    assert get_function_name('function name') == 'function_name'


def test_replace_parameters():
    assert len(replace_parameters('*random_string(15)*')) == 15


def test_replace_parameters_non_existent_method():
    assert replace_parameters('*random_something(15)*') is None
