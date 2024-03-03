
def candy(ratings: list[int]) -> int:
    lenght = len(ratings)
    candies = [1]*lenght

    for i in range(1, lenght):

        if ratings[i] > ratings[i-1]:
            candies[i] = candies[i-1] + 1

    for i in range(lenght-2, -1, -1):
        if ratings[i] > ratings[i+1]:
            candies[i] = max(candies[i], candies[i+1]+1)

    print(f'{candies=}')

    return sum(candies)


ratings = [1, 2, 3]
ratings = [3, 2, 1]
# ratings = [29, 51, 87, 87, 72, 12]
# ratings = [1, 3, 2, 2, 1]
# ratings = [1, 2, 87, 87, 87, 2, 1]
print(candy(ratings))
