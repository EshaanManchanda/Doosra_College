import re
import long_responses


def message_probability(user_message, recognised_words, single_response=False, required_words=None):
    if required_words is None:
        required_words = []
    message_certainty = 0
    has_required_words = True
    # Counts how many words are present in each predefined message
    for word in user_message:
        if word in recognised_words:
            message_certainty += 1
        # Calculates the percent of recognised words in a user message
    percentage = float(message_certainty) / float(len(recognised_words))
    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break
    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0


def check_all_messages(message):
    highest_prob_list = {}

    def response(bot_respones, list_of_words, single_response, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_respones] = message_probability(message, list_of_words, single_response, required_words)

        response('Hello!', ['hi', 'hello', 'whatapp', 'hey', 'heyo'], single_response=True)
        response('I\'am doing fine, and you?', ['how', 'are', 'you', 'doing'], required_words=['how'])

        best_match = max(highest_prob_list, key=highest_prob_list.get())
        print(highest_prob_list)
        return best_match


def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    return check_all_messages(split_message)


while True:
    k=input('You: ')
    print('Bot: ' + get_response(k))
