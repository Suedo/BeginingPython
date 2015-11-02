import traceback

try:
    with open('sketch.txt','r') as ipfile:
        with open('op_file.txt','w') as opfile:
            for line in ipfile:
                try:
                    (speaker, words) = line.split(':',1)
                    print(speaker + ' says : ' + words, end='',file=opfile)
                except ValueError:
                    pass
except IOError:
    print('>>traceback<<')
    traceback.print_exc()
    print('>>end<<')
