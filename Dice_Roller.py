import random
def dice() -> list:
    while True:
        dice_side: int = int(input("Enter the number of sides of the dice (We only support 4, 6, 8, 10, 12, 20): "))
        if dice_side in [4, 6, 8, 10, 12, 20]:
            dice: list = [i for i in range(1, dice_side + 1)]
            return dice
        else:
            print("We only support 4, 6, 8, 10, 12, 20 sided dice")
def num_of_dice() -> int:
    num_of_dice: int = int(input("Enter the number of dice you want to roll: "))
    return num_of_dice
if __name__ == "__main__":
    dice_list: list = dice()
    if dice_list:
        result: list = []
        num_of_dice: int = num_of_dice()
        for i in range(num_of_dice):
            result.append(random.choice(dice_list))
        print(f"The dice ypu rolled has the nimbers {result} and the sum is {sum(result)}")