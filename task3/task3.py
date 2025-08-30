import sys
import json


def load_json(path):
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)


def save_json(data, path):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


def build_value_map(values_data):
    return {item['id']: item['value'] for item in values_data['values']}


def fill_values(test_node, value_map):
    if 'id' in test_node and test_node['id'] in value_map:
        test_node['value'] = value_map[test_node['id']]

    if 'values' in test_node:
        for child in test_node['values']:
            fill_values(child, value_map)


def main():
    if len(sys.argv) != 4:
        print('Указаны неверные параметры при запуске!', file=sys.stderr)
        sys.exit(1)
    values_data = load_json(sys.argv[1])
    tests_data = load_json(sys.argv[2])

    value_map = build_value_map(values_data)

    for test in tests_data['tests']:
        fill_values(test, value_map)

    save_json(tests_data, sys.argv[3])


if __name__ == '__main__':    
    main()
