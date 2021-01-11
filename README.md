# Godel Hashes

By definition, a Godel Hash is when you take a symbol, char, or string, and convert it to a prime number.
Once a collection of symbols, chars, or strings is produced, a Godel Hash converts each element into a unique prime number.  From there, the product is taken.
The cool thing about Godel Hashes are that to uncompress the end result, all there is to do is to take the prime factors of the product.
Because of this, Godel Hashes are only partial-order preserving.


For this project, I created two ways of creating Godel Hashes, and initially, even a third.  I originally had four nested for loops, which hurt my soul a little bit,
but I knew that method worked, and I used to it check me work.  I switched over to only using 2 for loops, and decided to map out the rest. This made the code
not only more efficient, but a lot more dynamic as well. In efforts to get rid of more for loops, I decided to implement another version of this project with
recursion.  It is only marginally faster than the looping version.

# Small Warning - Fixed

The recursive file only prints out the result, the dictionary is not stored as a variable.  When trying to return the dictionary from the recursive function,
I kept getting a NoneType instead of a dictionary. Despite my efforts, I couldn't find a solution. It works as is, but the information cannot be maninpulated
as easily as it can in the other version.

Fixed - I have recently learned that when passing non-primitive data structures to functions, they are passed by reference, not value.  Therefore, there need not be a
return for the data type to be updated, so long as it was passed into the function.  Because of this, the dictionary gets updated despite not having a return method
attached to it.  The fully-updated dictionary can now be accessed outside of its local function.

