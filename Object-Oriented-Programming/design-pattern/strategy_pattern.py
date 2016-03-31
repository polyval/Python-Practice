# -*- coding: utf-8 -*-

"""
	The pattern implements different solutions to
	a single problem, each in a different object.
	The client code can then choose the most
	appropriate implementation dynamically at
	runtime.
"""

# User - - - - Abstration
# 			+someAction()         
# 			-				-	
# 		  -						-
# 	Implementation1			Implementation2
# 	+someAction()			+someAction()

# The User code connection to the strategy pattern
# simply needs to konw that it is dealing with the
# Abstration inteface


class ImageFinder:
    """ 
    In this example the base object ImageFinder keeps a copy
    of the concrete class (strategy).  You may also set
    a default strategy to use which might be convienient.
    In this case it is set to None which forces the caller
    to supply a concrete class.
        
    The concrete find method is supplied with an instance of
    this object so its state can be tracked.
    """
    
    def __init__(self, strategy=None):
        self.action = None
        self.count = 0
        if strategy:
            #get a handle to the object
            self.action = strategy()
    
    def find(self, image):
        if(self.action):
            self.count += 1
            return self.action.find(image, self)
        else: 
            raise UnboundLocalError('Exception raised, no strategyClass supplied to ImageFinder!')

class ImageFinderFlickr:
    ''' Locates images in Flickr. '''

    def find(self, image, instance):
        # in reality, query Flickr API for image path
        return "Found image in Flickr: " + image + ", search #" + str(instance.count)


class ImageFinderDatabase:
    ''' Locates images in database. '''
    def find(self, image, instance):
        #in reality, query database for image path
        return "Found image in database: " + image + ", search #" + str(instance.count)
    
    
if __name__ == "__main__" :

    finderBase = ImageFinder()
    finderFlickr = ImageFinder(strategy=ImageFinderFlickr)
    finderDatabase = ImageFinder(strategy=ImageFinderDatabase)

    try:
        #this is going to blow up!
        print finderBase.find('chickens')
    except Exception as e:
        print "The following exception was expected:"
        print e
        

    print finderFlickr.find('chickens')
    print finderFlickr.find('bugs bunny')
    print finderFlickr.find('tweety')
    print finderDatabase.find('dogs')
    print finderDatabase.find('cats')
    print finderDatabase.find('rabbits')