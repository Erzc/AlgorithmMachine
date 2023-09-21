

class GreedyAlgo:
    def __init__(self): #Initialize objects state


        def find_min_coins(coin_tps, coin_gl):
            
            #Sort coins from large to small
            coin_tps.sort(reverse=True)

            #Array for change
            num_coins = 0
            change = []

            #For loop to iterate through coins array
            for coin in coin_tps:
                #While loop as long as target is greater than coins
                while coin_gl >= coin:
                    #Subtract coin
                    coin_gl -= coin
                    num_coins += 1
                    change.append(coin)

            #Return change
            return num_coins, change

        #Display story to user:
        #
        #

        #Coins array - pennies, nickels, dimes, and quarters
        coin_types = [1, 5, 10, 25]
        #Define target
        coin_goal = 91

        #Call find_min_coins function
        num, change = find_min_coins(coin_types, coin_goal)

        #Display results
        print("Min number of coins to reach target:", num)
        print("Coins used:", change)