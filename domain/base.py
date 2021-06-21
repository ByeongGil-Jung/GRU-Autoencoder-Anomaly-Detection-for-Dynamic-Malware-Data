import copy
from collections.abc import MutableMapping

import yaml


class AttributeDict(dict):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __repr__(self):
        if not len(self):
            return ""
        max_key_length = max([len(str(k)) for k in self])
        tmp_name = '{:' + str(max_key_length + 3) + 's} {}'
        rows = [tmp_name.format(f'"{n}":', self[n]) for n in sorted(self.keys())]
        out = '\n'.join(rows)
        return out

    def __getattr__(self, name):
        if name in self:
            return self[name]
        else:
            raise AttributeError("No such attribute: " + name)

    def __setattr__(self, name, value):
        self[name] = value

    def __delattr__(self, name):
        if name in self:
            del self[name]
        else:
            raise AttributeError("No such attribute: " + name)


class Domain(object):

    def __init__(self, *args, **kwargs):
        pass

    def copy(self):
        return copy.deepcopy(self)


class Factory(Domain):

    def __init__(self, *args, **kwargs):
        super(Factory, self).__init__(*args, **kwargs)

    @classmethod
    def create(cls, *args, **kwargs):
        pass


class Hyperparameters(AttributeDict, Domain):

    def __init__(self, *args, **kwargs):
        super(Hyperparameters, self).__init__(*args, **kwargs)

        self._allocate_recursive()

    def _allocate_recursive(self):
        for k in self.keys():
            if isinstance(self[k], dict):
                self[k] = Hyperparameters(self[k])

    def copy(self):
        return copy.deepcopy(self)


class Yaml(Domain):

    def __init__(self, path, *args, **kwargs):
        super(Yaml, self).__init__(*args, **kwargs)
        self.__dict__ = self._read_yaml(path)

    def __repr__(self):
        return self.__dict__.__repr__()

    def to_hyperparameters(self):
        return Hyperparameters(**self.__dict__)

    def _read_yaml(self, path):
        with open(path, "rb") as f:
            yaml_dict = yaml.load(f, Loader=yaml.FullLoader)

        return yaml_dict
