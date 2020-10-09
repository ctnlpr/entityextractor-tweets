

def data_cleaning(term):
    if len(term) > 3:
        term = term.replace('.','')
        term = term.replace(',','')
        term = term.replace('-','')
        term = term.replace('?','')
        term = term.replace('_','')
        term = term.replace('#','')
    return term

read_file = open('/home/barathiganesh-hb/Desktop/ner_new_cen/ner_new/data/train.txt', 'r+')
write_file = open('../data/train.txt', 'w')
for line in read_file:
    line=line.strip()
    line = line.replace('\t', '')
    items = line.split()
    write_file.write(data_cleaning(items[1])+'\t'+items[2]+'\n')
read_file.close()
write_file.close()

