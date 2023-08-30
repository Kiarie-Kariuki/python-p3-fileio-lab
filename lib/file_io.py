def write_file(file_name, content):
    f = open(f'{file_name}.txt', 'w')
    f.write(content)
    f.close()

def append_file(file_name, content):
    f = open(f'{file_name}.txt', 'a')
    f.write(content)
    f.close()

def read_file(file_name):
    f = open(f'{file_name}.txt', 'r')
    content = f.read()
    f.close()
    return content
