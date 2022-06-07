peeps = [ "He ", "Alex", "Andrew" , "Yo MAMA" , ]
Compliments = [ "is hot" , "is cool" , "is tall"]

import random
num_peeps = random.randrange(0, len(peeps))
num_comps = random.randrange(0, len(Compliments))

print(peeps[num_peeps]) + " " + Compliments[num_comps]