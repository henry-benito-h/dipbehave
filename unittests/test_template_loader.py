from utils.templates.template_loader import TemplateLoader

template_loader = TemplateLoader("templates")


def test_read_template():
    new_string = template_loader.get_template("projects")
    assert type(new_string) == str


def test_read_non_existent_template():
    new_string = template_loader.get_template("projectX")
    assert new_string is None
