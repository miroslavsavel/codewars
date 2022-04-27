# https://www.codewars.com/kata/515decfd9dcfc23bb6000006/train/python

def is_valid_IP(strng):
    # split string by .
    list = strng.split('.')

    # check if octets are number
    # https://www.geeksforgeeks.org/python-converting-all-strings-in-list-to-integers/
    try:
        for i in range(0, len(list)):
            list[i] = int(list[i])
    except ValueError:
        # https://stackoverflow.com/questions/19265128/how-to-handlevalueerror-invalid-literal-for-int-with-base-10-a-without-try
        return False


    # check if each octet is number between 0-255

    # check if there is no leading 0

    # https://stackoverflow.com/questions/16603282/how-to-compare-each-item-in-a-list-with-the-rest-only-once
    return True


print(is_valid_IP('12.255.56.1'))
#print(is_valid_IP('ahoj.255.56.1'))