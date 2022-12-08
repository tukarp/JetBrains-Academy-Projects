# My solution to JetBrains Academy Honest Calculator Project


msg_0 = "Enter an equation \n"
msg_1 = "Do you even know what numbers are? Stay focused! \n"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you? \n"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n): \n"
msg_5 = "Do you want to continue calculations? (y / n): \n"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"
msg_10 = "Are you sure? It is only one digit! (y / n)"
msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"
msg_ = [msg_0, msg_1, msg_2, msg_3, msg_4, msg_5, msg_6, msg_7, msg_8, msg_9, msg_10, msg_11, msg_12]


operations = {
    "+": (lambda x, y: x + y),
    "-": (lambda x, y: x - y),
    "*": (lambda x, y: x * y),
    "/": (lambda x, y: x / y),
}


def store_result():
    if input(msg_[4]) == "y":
        return True
    else:
        return False


def continue_calculations():
    if input(msg_[5]) == "y":
        return True
    else:
        return False


def is_one_digit(v):
    if -10 < v < 10 and v.is_integer():
        return True
    else:
        return False


def check(v1, v2, v3):
    msg = ""
    if is_one_digit(v1) and is_one_digit(v2):
        msg = msg + msg_[6]
    if (v1 / v2 == 1) or (v2 / v1 == 1):
        msg = msg + msg_6
    if ((v1 == 1) or (v2 == 1)) and (v3 == "*"):
        msg = msg + msg_[7]
    if ((v1 == 0) or (v2 == 0)) and ((v3 == "*") or (v3 == "+") or (v3 == "-")):
        msg = msg + msg_[8]
    if msg != "":
        msg = msg_[9] + msg
        print(msg)



def saving_memory():
    if question:
        if is_one_digit(result):
            msg_index = 10

            while msg_index < 13:
                user_input = input(msg_[msg_index])

                if user_input == "y":
                    msg_index = msg_index + 1
                elif user_input == "n":
                    return False
        else:
            return True
    else:
        return False


running = True
memory = 0.0

while running:
    # Entering an equation
    x, operator, y = input(msg_[0]).split()

    try:
        # checking if x or y has to be memory
        if x == "M":
            x = memory
        else:
            x = float(x)

        if y == "M":
            y = memory
        else:
            y = float(y)

        # laziness test
        check(x, y, operator)

        # printing result
        result = operations[operator](x, y)
        print(result)

        # asking to store result
        question = store_result()

        # saving memory
        if saving_memory():
            memory = result

        # asking to continue calculations
        running = continue_calculations()

        # exceptions
    except ValueError:
        print(msg_[1])
    except KeyError:
        print(msg_[2])
    except ZeroDivisionError:
        print(msg_[3])
