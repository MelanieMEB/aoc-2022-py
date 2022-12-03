def read_file(name):
    batch_file = open(name,'r')
    content = batch_file.read().split('\n')
    batch_file.close()
    return content
