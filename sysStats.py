import cProfile
import sys

#### Let's check for execution time

# Time it takes to run sum of a list
print(cProfile.run('sum([x for x in range(10000)])'))

# Time it takes to run sum of a generator - way too many func calls causing time delays
print(cProfile.run('sum((x for x in range(10000)))'))

#### Let's take a look at the memory footprint

## list
obj = [x for x in range(10000)]
print(
    f"Object is type {type(obj)} and the memory footprint is {sys.getsizeof(obj)}"
)

## generator
obj = (x for x in range(10000))
print(
    f"Object is type {type(obj)} and the memory footprint is {sys.getsizeof(obj)}"
)

