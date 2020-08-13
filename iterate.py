# Qn: Given a range of first 10 numbers, Iterate from start number to the end number and print the sum of the current number and previous number

def iteration(num):
    prev_num = 0

    for i in range(num):
        sum_num = prev_num + i
        print("Current number: {}\t Previous Number: {}\t Sum: {}".format(i, prev_num, sum_num))
        # replace previous number with current iteration number before continuing the loop
        prev_num = i

iteration(10)