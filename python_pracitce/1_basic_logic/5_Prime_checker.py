try:
    num = int(input("Enter number to check prime: "))  # Taking an input and checking if its prime

    if num <= 1:
        print("Not Prime")

    else:
        for i in range(2,num):
            if num%i == 0:
                print("Not prime")
                break
        else:
                print("Prime")
except ValueError:
    print("Please enter correct datatype!")