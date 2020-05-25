import yaml


def test_yml():
    print(yaml.safe_load(open("data.yml")))