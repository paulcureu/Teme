import json


def update_data_base(data):
    with open('data-base.json', 'w') as file_update:
        json.dump(data, file_update, indent=4, separators=(',', ': '))

if __name__ == '__main__':
    with open('data-base.json', 'r') as file:
        data_base = json.load(file)
    print(data_base['bancnote'][0]['stoc'])
    # aici modifici datele dacă vrei
    data_base['bancnote'][0]['stoc'] -= 1  # exemplu: scazi 1 din stocul primei bancnote

    update_data_base(data_base)
    print(data_base['bancnote'][0]['stoc'])
