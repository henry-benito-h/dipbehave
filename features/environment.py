import yaml
from utils.request_manager import Request


global config
config = yaml.load(open('configuration/config.yml'))


def before_all(context):
    context.config = config
    context.request = Request(config['root'])
    context.vars = {}


def before_scenario(context, scenario):
    for tag in scenario.tags:
        if 'create_instance_' in str(tag):
            endpoint = str(tag).replace('create_instance_', '')
            context.execute_steps(f'''
                Given I create a record for "{endpoint}" from template
            ''')


# def after_scenario(context, scenario):
#     context.request.reset_credentials()

def get_context(context):
    return context

