import random


def results(correct_digits_and_position, correct_digits_only):
    print('Number of correct digits in correct place:     '+str(correct_digits_and_position))
    print('Number of correct digits not in correct place: '+str(correct_digits_only))


def has_duplicate_code(code):
    duplicate_code = len(code) != len(set(code))
    return duplicate_code


def create_code():
    code = [0,0,0,0]

    for i in range(4):
        value = random.randint(1, 8) # 8 possible digits
        while value in code:
            value = random.randint(1, 8)  # 8 possible digits
        code[i] = value
    if has_duplicate_code(code):
        return create_code()
    return code


def get_user_input():
    answer = input("Input 4 digit code: ")
    while len(answer) < 4 or len(answer) > 4:
        print("Please enter exactly 4 digits.")
        answer = input("Input 4 digit code: ")
    return answer


def correct_digits_and_position(code, answer):
    correct_digits_and_position = 0
    for i in range(len(answer)):
        if code[i] == int(answer[i]):
            correct_digits_and_position += 1
    return correct_digits_and_position


def correct_digits_only(code, answer):
    correct_digits = 0
    for i in range(len(answer)):    
        if int(answer[i]) in code:
            correct_digits += 1
    total_correct_digits_and_position = correct_digits_and_position(code, answer)
    total_correct_digits_only = correct_digits - total_correct_digits_and_position
    return total_correct_digits_only
    

def check_correctness(turns,code,answer):
    """Checks correctness of answer and show output to user"""
    total_correct_digits_and_position = correct_digits_and_position(code, answer)
    if total_correct_digits_and_position == 4:
        print('Congratulations! You are a codebreaker!')
        return True
    else:
        print('Turns left: ' + str(12 - turns))
        return False


def run_game():
    print('4-digit Code has been set. Digits in range 1 to 8. You have 12 turns to break it.')
    
    correct = False
    turns = 0
    code = create_code()
    # print (code)
    
    while not correct and turns < 12:
        answer = get_user_input()
        turns += 1
        total_correct_digits_and_position = correct_digits_and_position(code, answer)
        total_correct_digits_only = correct_digits_only(code, answer)
        results(total_correct_digits_and_position, total_correct_digits_only)
        correct = check_correctness(turns,code,answer)
    print('The code was: '+str(code))


if __name__ == "__main__":
    run_game()