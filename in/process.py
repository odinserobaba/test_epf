import json


def process_licenses(json_file_path, numbers_file_path, output_file_path):
    with open(json_file_path, 'r', encoding='utf-8') as file:
        json_lines = file.readlines()
    print(f'json_file_path')
    with open(numbers_file_path, 'r', encoding='utf-8') as file:
        numbers = file.read().splitlines()
    print(f'numbers_file_path')
    results = []
    for line in json_lines:
        try:
            data = json.loads(line)
            order_id = data.get('epgu', {}).get('orderID')
            if order_id in numbers:
                license_number = data.get('renewal', {}).get(
                    'license', {}).get('licenseNumber', 'N/A')
                if license_number == 'N/A':
                    license_number = data.get('grant', {}).get(
                        'license', {}).get('licenseNumber', 'N/A')
                if license_number == 'N/A':
                    license_number = data.get('termination', {}).get(
                        'license', {}).get('licenseNumber', 'N/A')
                if license_number == 'N/A':
                    license_number = data.get('prolongation', {}).get(
                        'license', {}).get('licenseNumber', 'N/A')
                if license_number != 'N/A':
                    results.append((order_id, license_number))
                print(f'{order_id}  {license_number}')
        except json.JSONDecodeError:
            print(f'ERROR {data}')
            continue

    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        for order_id, license_number in results:
            output_file.write(f"{order_id}, {license_number}\n")


json_file_path = 'license1.txt'
numbers_file_path = 'license_te1.txt'
output_file_path = 'license_results1.txt'

process_licenses(json_file_path, numbers_file_path, output_file_path)
