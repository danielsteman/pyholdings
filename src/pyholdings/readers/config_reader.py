import yaml

def config_reader(path):
    with open('sources.yaml', 'r') as f:
        doc = yaml.load(f, Loader=yaml.SafeLoader)
        return doc