import yaml
import os


def readyml(yamlPath):
    if not os.path.isfile(yamlPath):
        raise FileNotFoundError("文件路径不存在，请检查路径是否正确：%s" % yamlPath)
    f = open(yamlPath, 'r', encoding='utf-8')
    cfg = f.read()
    d = yaml.safe_load(cfg)
    return d


if __name__ == '__main__':
    b = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_path = os.path.join(b, "data", "data.yaml")
    print(data_path)
    r = readyml(yamlPath=data_path)
    print(r['login'])
