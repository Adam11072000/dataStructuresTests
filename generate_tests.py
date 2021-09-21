import random
import generate_output as GO

NUM_OF_TESTS = 100
BASE_DIR = ""
CURRENT_IMAGES = {}
MAX_ID = 250


def add_image(num_pixels):
    options = ['valid image', 'non positive image', 'existing image']
    if len(CURRENT_IMAGES) == 0:
        probs = [0.75, 0.25, 0]
    else:
        probs = [0.6, 0.2, 0.2]
    rand_op = random.choices(population=options, weights=probs, k=1)[0]
    image_id = 0
    if rand_op == options[0]:
        image_id = random.randint(1, MAX_ID)
        CURRENT_IMAGES[image_id] = GO.emptyPixels(num_pixels)
    elif rand_op == options[1]:
        image_id = random.randint(-10, 0)
    else:
        if len(CURRENT_IMAGES) != 0:
            image_id = random.choice(list(CURRENT_IMAGES.keys()))
        else:
            image_id = random.randint(1, MAX_ID)
    return ("addImage %s\n") % image_id


def delete_image(numPixels):
    options = ['valid image', 'non positive image', 'non-existing image']
    if len(CURRENT_IMAGES) == 0:
        probs = [0, 0.25, 0.75]
    else:
        probs = [0.4, 0.3, 0.3]
    rand_op = random.choices(population=options, weights=probs, k=1)[0]
    image_id = 0
    if rand_op == options[0]:
        image_id = random.choice(list(CURRENT_IMAGES.keys()))
        CURRENT_IMAGES.pop(image_id)
    elif rand_op == options[1]:
        image_id = random.randint(-10, 0)
    else:
        while (True):
            image_id = random.randint(1, MAX_ID)
            if image_id not in CURRENT_IMAGES.keys():
                break
    return ("deleteImage %s\n") % image_id


def set_label_score(numPixels):
    options = ['valid', 'non positive image', 'non-existing image', 'big pixel',
               'negative pixel', 'invalid label', 'invalid score']
    if len(CURRENT_IMAGES) == 0:
        probs = [0, 0.2, 0.2, 0.2, 0.2, 0.1, 0.1]
    else:
        probs = [0.6, 0.05, 0.1, 0.05, 0.05, 0.1, 0.05]
    rand_op = random.choices(population=options, weights=probs, k=1)[0]
    image_id = 0
    pixel = 0
    label = 0
    score = 0
    if rand_op == options[0]:
        image_id = random.choice(list(CURRENT_IMAGES.keys()))
        pixel = random.randint(0, numPixels - 1)
        label = random.randint(1, MAX_ID)
        score = random.randint(1, MAX_ID)
        for i in range(0, len(CURRENT_IMAGES[image_id])):
            if pixel in CURRENT_IMAGES[image_id][i][0]:
                CURRENT_IMAGES[image_id][i][1][label] = score
                break
    elif rand_op == options[1]:
        image_id = random.randint(-10, 0)
        pixel = random.randint(0, numPixels - 1)
        label = random.randint(1, MAX_ID)
        score = random.randint(1, MAX_ID)
    elif rand_op == options[2]:
        pixel = random.randint(0, numPixels - 1)
        label = random.randint(1, MAX_ID)
        score = random.randint(1, MAX_ID)
        while True:
            image_id = random.randint(1, MAX_ID)
            if image_id not in CURRENT_IMAGES.keys():
                break
    elif rand_op == options[3]:
        image_id = random.randint(1, MAX_ID)
        pixel = random.randint(numPixels, numPixels + 10)
        label = random.randint(1, MAX_ID)
        score = random.randint(1, MAX_ID)
    elif rand_op == options[4]:
        image_id = random.randint(1, MAX_ID)
        pixel = random.randint(-10, -1)
        label = random.randint(1, MAX_ID)
        score = random.randint(1, MAX_ID)
    elif rand_op == options[5]:
        image_id = random.randint(1, MAX_ID)
        pixel = random.randint(0, numPixels - 1)
        label = random.randint(-10, 0)
        score = random.randint(1, MAX_ID)
    else:
        image_id = random.randint(1, MAX_ID)
        pixel = random.randint(0, numPixels - 1)
        label = random.randint(1, MAX_ID)
        score = random.randint(-10, 0)
    return ("setLabelScore %s %s %s %s\n") % (image_id, pixel, label, score)


def reset_label_score(numPixels):
    options = ['valid', 'non positive image', 'non-existing image', 'big pixel',
               'negative pixel', 'negative label', 'label not found']
    if len(CURRENT_IMAGES) == 0:
        probs = [0, 0.2, 0.2, 0.2, 0.2, 0.1, 0.1]
    else:
        probs = [0.4, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]
    rand_op = random.choices(population=options, weights=probs, k=1)[0]
    image_id = 0
    pixel = 0
    label = 0
    flag = True
    if rand_op == options[0]:
        image_id = random.choice(list(CURRENT_IMAGES.keys()))
        pixel = random.randint(0, numPixels - 1)
        for i in range(0, len(CURRENT_IMAGES[image_id])):
            if len(CURRENT_IMAGES[image_id][i]) == 0:
                if flag:
                    while 1:
                        label = random.randint(1, MAX_ID)
                        if pixel in CURRENT_IMAGES[image_id][i][0] and label in CURRENT_IMAGES[image_id][i][1]:
                            CURRENT_IMAGES[image_id][i][1].pop(label)
                            flag = False
                            break
                else:
                    break
    elif rand_op == options[1]:
        image_id = random.randint(-10, 0)
        pixel = random.randint(0, numPixels - 1)
        label = random.randint(1, MAX_ID)
    elif rand_op == options[2]:
        while True:
            image_id = random.randint(1, MAX_ID)
            if image_id not in CURRENT_IMAGES.keys():
                break
        pixel = random.randint(0, numPixels - 1)
        label = random.randint(1, MAX_ID)
    elif rand_op == options[3]:
        image_id = random.randint(1, MAX_ID)
        pixel = random.randint(numPixels, numPixels + 10)
        label = random.randint(1, MAX_ID)
    elif rand_op == options[4]:
        image_id = random.randint(1, MAX_ID)
        pixel = random.randint(-10, -1)
        label = random.randint(1, MAX_ID)
    elif rand_op == options[5]:
        image_id = random.randint(1, MAX_ID)
        pixel = random.randint(0, numPixels - 1)
        label = random.randint(-10, 0)
    else:  ####
        image_id = random.randint(1, MAX_ID)
        pixel = random.randint(0, numPixels - 1)
        label = random.randint(1, MAX_ID)
    return ("resetLabelScore %s %s %s\n") % (image_id, pixel, label)


def get_highest_scored_label(numPixels):
    options = ['valid', 'non-positive image', 'non-existing image', 'negative pixel', 'big pixel',
               'unlabeled super-pixel']
    if len(CURRENT_IMAGES) == 0:
        probs = [0, 0.2, 0.2, 0.2, 0.2, 0.2]
    else:
        probs = [0.4, 0.1, 0.1, 0.05, 0.05, 0.3]
    rand_op = random.choices(population=options, weights=probs, k=1)[0]
    image_id = 0
    pixel = 0
    if rand_op == options[0]:
        image_id = random.choice(list(CURRENT_IMAGES.keys()))
        for i in range(0, len(CURRENT_IMAGES[image_id])):
            pixel = random.randint(0, numPixels - 1)
            if pixel in CURRENT_IMAGES[image_id][i][0] and len(CURRENT_IMAGES[image_id][i][1]) != 0:
                break
    if rand_op == options[1]:
        image_id = random.randint(-10, 0)
        pixel = random.randint(0, numPixels - 1)
    if rand_op == options[2]:
        pixel = random.randint(0, numPixels - 1)
        while 1:
            image_id = random.randint(1, MAX_ID)
            if image_id not in CURRENT_IMAGES.keys():
                break
    if rand_op == options[3]:
        image_id = random.randint(1, MAX_ID)
        pixel = random.randint(-10, -1)
    if rand_op == options[4]:
        pixel = random.randint(numPixels, numPixels + 10)
    else:
        if len(CURRENT_IMAGES) != 0:
            image_id = random.choice(list(CURRENT_IMAGES.keys()))
            for i in range(0, len(CURRENT_IMAGES[image_id])):
                pixel = random.randint(0, numPixels - 1)
                if pixel in CURRENT_IMAGES[image_id][i][0] and len(CURRENT_IMAGES[image_id][i][1]) == 0:
                    break
        else:
            image_id = random.randint(1, MAX_ID)
            pixel = random.randint(-10, -1)
    return ("getHighestScoredLabel %s %s\n") % (image_id, pixel)


def findSuperPixel(superPixelsList, pixel):
    for i in range(0, len(superPixelsList)):
        if pixel in superPixelsList[i][0]:
            return i


def merge_super_pixels(numPixels):
    options = ['valid', 'non positive image', 'pixel1 big', 'pixel2 big', 'pixel1 negative', 'pixel2 negative',
               'image not exist', 'pixels in same super pixel']
    count = 0
    if len(CURRENT_IMAGES) == 0:
        probs = [0, 0.2, 0.2, 0.1, 0.2, 0.2, 0.05, 0.05]
    else:
        probs = [0.6, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.1]
    image_id = 0
    pixel1 = 0
    pixel2 = 0
    rand_op = random.choices(population=options, weights=probs, k=1)[0]
    if rand_op == options[0]:
        image_id = random.choice(list(CURRENT_IMAGES.keys()))
        if len(CURRENT_IMAGES[image_id]) == 1:
            pixel1 = random.randint(0, numPixels - 1)
            pixel2 = random.randint(0, numPixels - 1)
        else:
            pixel1 = random.randint(0, numPixels - 1)
            superPixel1 = GO.findSuperPixel(CURRENT_IMAGES[image_id], pixel1)
            for i in range(0, len(CURRENT_IMAGES[image_id])):
                if pixel1 not in CURRENT_IMAGES[image_id][i][0]:
                    pixel2 = random.choice(list(CURRENT_IMAGES[image_id][i][0]))
                    GO.unionLablDictionaries(CURRENT_IMAGES[image_id][superPixel1][1], CURRENT_IMAGES[image_id][i][1])

                    CURRENT_IMAGES[image_id][superPixel1][0] =\
                        CURRENT_IMAGES[image_id][superPixel1][0].union(CURRENT_IMAGES[image_id][i][0])
                    CURRENT_IMAGES[image_id].pop(i)
                    break
    elif rand_op == options[1]:
        image_id = random.randint(-10, -1)
        pixel1 = random.randint(0, numPixels - 1)
        pixel2 = random.randint(0, numPixels - 1)
    elif rand_op == options[2]:
        image_id = random.randint(1, MAX_ID)
        pixel1 = random.randint(numPixels, numPixels + 10)
        pixel2 = random.randint(0, numPixels - 1)
    elif rand_op == options[3]:
        image_id = random.randint(1, MAX_ID)
        pixel2 = random.randint(numPixels, numPixels + 10)
        pixel1 = random.randint(0, numPixels - 1)
    elif rand_op == options[4]:
        image_id = random.randint(1, MAX_ID)
        pixel2 = random.randint(-10, -1)
        pixel1 = random.randint(0, numPixels - 1)
    elif rand_op == options[5]:
        image_id = random.randint(1, MAX_ID)
        pixel1 = random.randint(-10, -1)
        pixel2 = random.randint(0, numPixels - 1)
    elif rand_op == options[6]:
        pixel1 = random.randint(0, numPixels - 1)
        pixel2 = random.randint(0, numPixels - 1)
        while 1:
            image_id = random.randint(1, MAX_ID)
            if image_id not in CURRENT_IMAGES.keys():
                break
    else:
        if len(CURRENT_IMAGES) != 0:
            image_id = random.choice(list(CURRENT_IMAGES.keys()))
            for i in range(0, len(CURRENT_IMAGES[image_id])):
                pixel1 = random.randint(0, numPixels - 1)
                pixel2 = random.randint(0, numPixels - 1)
                if pixel1 in CURRENT_IMAGES[image_id][i][0] and pixel2 in CURRENT_IMAGES[image_id][i][0]:
                    break
        else:
            image_id = random.randint(1, MAX_ID)
            pixel1 = random.randint(0, numPixels - 1)
            pixel2 = random.randint(0, numPixels - 1)
    return ("mergeSuperPixels %s %s %s\n") % (image_id, pixel1, pixel2)


OPS_DICT = {
    'quit': {'func': None, 'prob': 0.001, 'prob_when_empty': 0.1},
    'addImage': {'func': add_image, 'prob': 0.35, 'prob_when_empty': 0.5},
    'deleteImage': {'func': delete_image, 'prob': 0.05, 'prob_when_empty': 0.1},
    'setLabelScore': {'func': set_label_score, 'prob': 0.55, 'prob_when_empty': 0.1},
    'resetLabelScore': {'func': reset_label_score, 'prob': 0.3, 'prob_when_empty': 0.1},
    'getHighestScoredLabel': {'func': get_highest_scored_label, 'prob': 0.2, 'prob_when_empty': 0.1},
    'mergeSuperPixels': {'func': merge_super_pixels, 'prob': 0.4, 'prob_when_empty': 0.1}
}
OPS_ITEMS = OPS_DICT.items()
OP_NAMES = [item[0] for item in OPS_ITEMS]
OPS_PROBS = [item[1]['prob'] for item in OPS_ITEMS]
OPS_PROBS_WHEN_EMPTY = [item[1]['prob_when_empty'] for item in OPS_ITEMS]
print(OPS_PROBS_WHEN_EMPTY)


def randomize_test(f):
    numOfPixels = random.randint(1, MAX_ID)
    f.write('init ' + str(numOfPixels) + '\n')
    while True:
        if len(CURRENT_IMAGES) > 3:
            probs = OPS_PROBS
        else:  # System is relatively empty
            probs = OPS_PROBS_WHEN_EMPTY
        rand_op = random.choices(population=OP_NAMES, weights=probs, k=1)[0]
        if rand_op == 'quit':
            break
        op_string = OPS_DICT[rand_op]['func'](numOfPixels)
        f.write(op_string)
    f.write('quit')


def main():
    for i in range(NUM_OF_TESTS):
        filename = '.input/'.join((BASE_DIR, '%s.txt' % (i + 1)))
        with open(filename, 'w') as f:
            randomize_test(f)
        print('Generated file %s' % (i + 1))
        CURRENT_IMAGES.clear()


if __name__ == '__main__':
    main()

# I AM IN RESETLABELSCORE
