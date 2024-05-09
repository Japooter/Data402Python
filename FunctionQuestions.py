print("\nQ1a\n")
# Q1a: Write a function which takes in an integer as an argument and returns the divisors of that number as a list
# e.g. f(12) = [1, 2, 3, 4, 6, 12]
# hint: range(1, n) returns a collection of the numbers from 1 to n-1

# A1a:
def A1a(n):
    a1a_list = []
    for i in range (1, (n+1)):
        if (n % i) == 0:
            a1a_list.append(i)
    print(a1a_list)
    return a1a_list

A1a(12)




print("\nQ1b\n")
# Q1b: Write a function which takes in two integers as arguments and returns true if one of the numbers
# is a factor of the other, false otherwise
# (bonus points if you call your previous function within this function

# A1b:
def A1b(m, o):
    a1b_list = []
    for i in range (1, (m+1)):
        if (m % i) == 0:
            a1b_list.append(i)
    a1b_flag = False
    for k in range(len(a1b_list)):
        if a1b_list[k] == o:
            a1b_flag = True
    if a1b_flag:
        print(True)
    else:
        print(False)

A1b(34, 99)






# -------------------------------------------------------------------------------------- #

print("\nQ2a\n")
# Q2a: write a function which takes a letter (as a string) as an input and outputs it's position in the alphabet
# alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
#             "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]

# A2a:
def a2a(lett):
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]
    letter = lett.lower()
    alphabet_flag = False
    for i in range(len(alphabet)):
        if letter == alphabet[i]:

            alphabet_flag = True
    if alphabet_flag:
        if alphabet.index(letter) == 26:
            print("This is a space, not a letter.")
        else:
            print((alphabet.index(letter) + 1))
    else:
        raise Exception("Not a valid letter.")


        #    print(alphabet.index(i) + 1)
        #print(alphabet[i])
        #print(type(alphabet[alphabet.index(i)]))
    #print(alphabet[2])
a2a("o")


print("\nQ2b\n")
# Q2b: create a function which takes a persons name as an input string and returns an
# ID number consisting of the positions of each letter in the name
# e.g. f("bob") = "1141" as "b" is in position 1 and "o" is in position 14

# A2b:
def a2b(name):
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
                "v", "w", "x", "y", "z", " "]
    final_id = ""
    numbers_list = []
    for i in range(len(name)):
        #print(i)
        letter = name[i]
        id_number = str(alphabet.index(letter))
        numbers_list.append(alphabet.index(letter))
        final_id = final_id + id_number
    print("Your ID number is:\n")
    final_id = int(final_id)
    print(final_id)
    #print(numbers_list)
    return final_id, numbers_list



a2b("bob")





print("\nQ2c\n")
# Q2c: Create a function which turns this ID into a password. The function should subtract
# the sum of the numbers in the id that was generated from the whole number of the id.
# e.g. f("bob") -> 1134 (because bob's id was 1141 and 1+1+4+1 = 7 so 1141 - 7 = 1134)

# A2c:
def a2c(name):
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
                "v", "w", "x", "y", "z", " "]


    final_id = ""
    numbers_list = []
    for i in range(len(name)):
    # print(i)
        letter = name[i]
        id_number = str(alphabet.index(letter))
        numbers_list.append(alphabet.index(letter))
        final_id = final_id + id_number
#def a2c(ID, list_to_sum):
    ID_numbers_sum = 0
    final_id = int(final_id)
    for i in numbers_list:
        ID_numbers_sum += i
    pass_from_ID = (final_id - ID_numbers_sum)
    print(pass_from_ID)
    return pass_from_ID

a2c("bob")




# -------------------------------------------------------------------------------------- #

print("\nQ3a\n")
# Q3a: Write a function which takes an integer as an input, and returns true if the number is prime, false otherwise.

# A3a:
def a3a_primes(number):
    is_prime = True
    if number <= 1:
        is_prime = False
        print(is_prime)
        return is_prime
    else:
        for i in range(2, number):
            if (number % i) == 0:
                is_prime = False
                break

        if is_prime is True:
            print(is_prime)
            return is_prime
        else:
            print(is_prime)
            return(is_prime)


a3a_primes(4)




print("\nQ3b\n")
# Q3b: Now add some functionality to the function which does not error if the user inputs something other than a digit

# A3b:
def a3b_primes_nerror(number):
    number = str(number)
    if number.isdigit() == False:
        print("Invalid input, please input a digit")
        return 0
    is_prime = True
    number = int(number)
    if number <= 1:
        is_prime = False
        print(is_prime)
        return is_prime
    else:
        for i in range(2, number):
            if (number % i) == 0:
                is_prime = False
                break

        if is_prime is True:
            print(is_prime)
            return is_prime
        else:
            print(is_prime)
            return(is_prime)

a3b_primes_nerror(23.2)




# -------------------------------------------------------------------------------------- #






