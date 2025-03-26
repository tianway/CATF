import yaml


class ReadYaml:

    @classmethod
    def read_yaml(cls, filepath='../config/base.yaml'):
        with open(filepath, encoding='utf8') as f:
            content = f.read()
        return yaml.full_load(content)


if __name__ == '__main__':
    print(ReadYaml.read_yaml())
