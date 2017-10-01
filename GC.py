with open('data.txt', 'r') as data_file:
    m = ('', 0)
    label, data = '', ''
    for line in data_file:
        if line[0] == '>':
            if data:
                gc_content = (data.count('G')+data.count('C')) / len(data)
                if gc_content > m[1]:
                    m = (label, gc_content)
                data = ''
            label = line[1:]
        else:
            data += line.strip()
    gc_content = (data.count('G') + data.count('C')) / len(data)
    if gc_content > m[1]:
        m = (label, gc_content)
print('%s%f' % (m[0], m[1]*100))
