#time = '07:05:45PM'

def am(time):
        return (time[-2:] == 'AM')

def convert(time):
        
        hh,mm,ss = [int(entry) for entry in time[:-2].split(':')]
        
        if(am(time)):
                print('{:02d}:{:02d}:{:02d}'.format(hh%12,mm,ss))
        else:
                print('{:02d}:{:02d}:{:02d}'.format(12+(hh%12),mm,ss))
                

convert('07:05:45PM')
