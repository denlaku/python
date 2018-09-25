try:
    f = open('temp.txt1', 'r+')
except IOError, e:
    print 'error'
    print e
else:
    print 'right'
