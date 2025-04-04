from datetime import datetime
print(datetime.today())
print(datetime.now())

# name = "Victor"
# profession = "programmer"

# print("Hello, {}. You are a {}.".format(name, profession))
# print(f"Hello, {name}. You are a {profession}.")

# ice_cream_density = 10          # iceCreamDensity=10
 
# while ice_cream_density > 0:    # while iceCreamDensity>0 :
#     print('Drip...')
#     ice_cream_density -= 1      #     iceCreamDensity-=1

# print('The ice cream melted.')


# 4 * 5 + 3**2 / 10
# = 4 * 5 + 9 / 10
# = 20 + 0.9
# = 20.9

string = "Hello, World!"
substring = "o, Wor"
print(substring in string)

speed_limit = 60
current_speed = 80

if current_speed > speed_limit:
    print('"People are so bad at driving cars that '
          "computers don\'t have to be that good to be "
          'much better." -- Marc Andreessen')
    

tweet = 'Woohoo! :-)'

if len(tweet) > 140:
    print('Tweet is too long!')

length_of_tweet = len(tweet) + 5