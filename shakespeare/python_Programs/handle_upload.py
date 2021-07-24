# FILE_PATH = './target'
FILE_PATH = '/tmp/shakespeare/target'

def handle_uploaded_file(f):
    with open(FILE_PATH, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    return FILE_PATH