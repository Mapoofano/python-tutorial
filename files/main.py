def getter(path):
    data = {}
    with open(path) as file:
        list = file.readlines()
        for i in range(0, len(list), 2):
            key = list[i]
            value = list[i + 1]
            data[key] = value
        file.close()
        return data

def setter(path, data: dict):
    with open(path, 'w') as result:
        for key, value in data.items():
            print()
            result.write(f"Name: {key}Age: {value}")
        result.close()
    
try:

    file_path = input('Enter the path: ')
    data = getter(file_path)
    setter('result.txt', data)

except FileNotFoundError: 
    print('File not found')
except Exception as exc :
    print(f'Something went wrong:{exc}')