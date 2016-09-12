def num_beers(n):
    if n <= 0:
        print 'bottles of beer on the wall'
    else:
        print n, 'bottles of beer on the wall'
        print n, 'bottles of beer'
        print 'if one of those beers should happen to fall'
        print n-1, 'bottles of beer on the wall\n'

        num_beers(n-1)

num_beers(99)

