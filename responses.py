import random

def handle_message(message) -> str:
    LoweredMessage = message.lower()

    if LoweredMessage == 'flip':
        if(FlipCoin() == 'Heads'):
            return 'Heads'
        else:
            return 'Tails'

    if LoweredMessage == 'roll':
        return str(RollDie(1, 6))

    if LoweredMessage[0] == 'r' and LoweredMessage[1].isdigit():
        MessageCursor = 1
        HowManyString = ''
        while(LoweredMessage[MessageCursor].isdigit()):
            HowManyString = HowManyString + str(LoweredMessage[MessageCursor])
            MessageCursor = MessageCursor + 1
        HowMany = int(HowManyString)
        print(HowMany)
        if LoweredMessage[MessageCursor] != 'd':
            return 'error: command should follow this order - r [number of dice] d [type of die]'
        else:
            MessageCursor = MessageCursor + 1
        PossibleDice = ['4', '6', '8', '10', '12', '20', '100']
        if not LoweredMessage[MessageCursor].isdigit():
            return 'error: command should follow this order - r [number of dice] d [type of die]'
        else:
            DieString = ''
        while(LoweredMessage[MessageCursor].isdigit() and MessageCursor < len(LoweredMessage)):
            DieString = DieString + str(LoweredMessage[MessageCursor])
            if MessageCursor < len(LoweredMessage) - 1:
                MessageCursor = MessageCursor + 1
            else:
                break
        if DieString in PossibleDice:
            return str(RollDie(HowMany, int(DieString)))
        else:
            return 'This die does not exist. Try again rolling either a D4, D6, D8, D10, D12, D20 or the percentile dice (D100)'

    if LoweredMessage == 'commands' or LoweredMessage == 'command':
        return 'flip: flips a coin \n to roll a die, enter r [number of dice] d [4, 6, 8, 10, 12, 20, or 100] or just enter roll to roll 1 D6'
        
def FlipCoin() -> str:
    coin = random.randint(1, 2)
    if(coin == 1):
        return 'Tails'
    else:
        return 'Heads'

def RollDie(amount, die) -> int:
    roll = random.randint(1, die)
    if(amount == 1):
        return roll
    else:
        return str(roll) + ' ' + str(RollDie(amount - 1, die))

