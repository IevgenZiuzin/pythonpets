"""Consider the software that runs on a self-checkout machine.
One task that it must be able to perform is to determine
how much change to provide when the shopper pays for a purchase with cash.
Write a program that begins by reading a number of cents from the user as an integer.
Then your program should compute and display the denominations of the coins
that should be used to give that amount of change to the shopper.
The change should be given using as few coins as possible."""

coins_rate = [200, 100, 25, 10, 5, 1]
coins_left = [5, 5, 5, 5, 5, 5]
"""setting coins rate and amount"""
while True:
    coins_to_give = []
    sum_change = int(input('Type sum of change in cents: '))
    sum_left = 0
    for c in range(len(coins_rate)):
        coins_amount = sum_change // coins_rate[c]
        """computing coins to give pro rate"""
        if coins_amount >= coins_left[c] > 0:
            """need more than left in rate"""
            coins_to_give.append(coins_left[c])
            sum_change = sum_change - (coins_left[c] * coins_rate[c])
            coins_left[c] -= coins_left[c]
        elif coins_left[c] >= coins_amount:
            """left enough in rate"""
            coins_to_give.append(coins_amount)
            sum_change = sum_change % coins_rate[c]
            coins_left[c] = coins_left[c] - coins_amount
        else:
            """appending zero in rate"""
            coins_to_give.append(0)
        sum_left += (coins_left[c] * coins_rate[c])
        """computing sum left"""
    print("Coins to give: " + str(coins_to_give) + "\n"
          "Coins left: " + str(coins_left) + "\n"
          "Sum left: " + str(sum_left) + "\n")
#TODO
#message for empty box
#break
#given coin pro rate view