def get_high_score():
    file_path = 'high_score.txt'
    try:
        with open(file_path, 'r') as file:
            return int(file.read())
    except:
        with open(file_path, 'w') as file:
            file.write('0')
            return 0


def set_high_score(score, high_score):
    if score > high_score:
        with open('high_score.txt', 'w') as file:
            file.write(str(score))


