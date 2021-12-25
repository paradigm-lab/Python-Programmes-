# Fizz buzz is a group word game for children to teach them about division.

# Player take turns to count increamentally, replacing any number divisible by three with the word "fizz" and any number divisible by five with the word "buzz"

"""
 Fizz buzz pseudocode:

 number divisible by 3
 returns 'fizz'

 number divisible by 5
 return 'buzz'

 numbers divisible by 15
 return 'fizz buzz'

"""

# The test function for the fizzbuzz function
def testFizzbuzz():
    assert fizzbuzz(1) == ''
    assert fizzbuzz(2) == ''
    assert fizzbuzz(3) == 'fizz'
    assert fizzbuzz(4) == ''
    assert fizzbuzz(5) == 'buzz'
    assert fizzbuzz(6) == 'fizz'

def fizzbuzz(number):
    if number == 3:
        return 'fizz'
    elif number == 5:
        return 'buzz'
    else:
        return ''


testFizzbuzz()
