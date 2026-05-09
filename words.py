import string
print("hello bitch")

fool_words = {'adventure', 'summer', 'opportunity',
              'change', 'progress', 'transition', 'hesitation'}
magic_words = {'experiment', 'trans', 'initiative', 'action', 'proactive'}
hp_words = {'intuition', 'stuck', 'midterm', 'exam', 'friendship'}
empress_words = {'project', 'idea', 'block', 'mpreg', 'health', 'inspiration'}
emperor_words = {'lockin', 'focus',
                 'procrastinate', 'study', 'monster', 'celsius'}
hiero_words = {'advice', 'guidance',
               'mothers day', 'parent', 'mother', 'father'}
lover_words = {'path', 'situationship', 'hinge', 'grindr',
               'tinder', 'divorce', 'breakup', 'scandal', 'confidence'}
chariot_words = {'goals', 'advisor', 'mentor', 'momentum',
                 'perseverance', 'promotion', 'responsibility', 'internship'}
strength_words = {'forgiveness', 'forgive', 'angry',
                  'anger', 'frustrated', 'grudge', 'revenge'}
hermit_words = {'professor', 'library', 'confused',
                'lonely', 'quiet', 'study', 'lockin'}
wheel_words = {'repeat', 'again', 'graduate', 'failure',
               'test', 'withdraw', 'adddrop', 'meaning of life'}
justice_words = {'protest', 'competition', 'war',
                 'revenge', 'compromise', 'opinion', 'argument'}
hanged_words = {'reflection', 'waiting',
                'realize', 'discovery', 'clarity', 'focus'}
death_words = {'graduation', 'graduate', 'summer',
               'quarter', 'end', 'moving', 'meaning of life'}
temp_words = {'grades', 'curve', 'mental health',
              'therapy', 'depressed','depression', 'canvas', 'assignment'}
devil_words = {'situationship', 'judge',
               'scav', 'procrastinate', 'lazy', 'laziness'}
tower_words = {'midterm', 'exam', 'grades', 'partner',
               'boyfriend', 'girlfriend', 'government'}
star_words = {'therapy', 'ex', 'again', 'another try', 'fresh start'}
moon_words = {'uncertain', 'confused',
              'experiment', 'tryout', 'try', 'interview'}
sun_words = {'stress', 'difficult', 'uchicago', 'scav',
             'weather', 'mothers day', 'meaning of life'}
judge_words = {'graduate', 'judgment', 'points', 'item', 'showcase', 'ida noyes',
               'david rubenstein', 'david m rubenstein', 'religion', 'church', 'god'}
world_words = {'victory', 'win', 'graduation',
               'judgeship', 'celebration', 'time'}
all_words_list = [fool_words, magic_words, hp_words, empress_words, emperor_words, hiero_words, lover_words, chariot_words, strength_words, hermit_words,
                  wheel_words, justice_words, hanged_words, death_words, temp_words, devil_words, tower_words, star_words, moon_words, sun_words, judge_words, world_words]
tarot_cards = ["fool", "magic", "highpriestess", "empress", "emperor", "hierophant", "lovers", "chariot", "strength", "hermit", "wheel", "justice", "hangedman", "death",
               "temperance", "devil", "tower", "star", "moon", "sun", "judgment", "world"]





def main():
    return None


def find_cards():
    question_asked = input("What question do you seek answered?")
    stripped_q = question_asked.lower().split(' ')
    final_q = [w.strip(string.punctuation) for w in stripped_q]
    card_set_dict = {x[0]: x[1] for x in zip(tarot_cards, all_words_list)}
    card_score_dict = {x: 0 for x in tarot_cards}
    for word in final_q:
        for cardname, wordset in card_set_dict.items():
            if word in wordset:
                card_score_dict[cardname] += 1
    selected=sorted(card_score_dict, key=card_score_dict.get, reverse=True)[0:2]
    return(selected)

def give_answers(cards):
    card_def={'fool':'leap of faith, step into the unknown', 'magician':'the tools are in front of you, you should act', 'high priestess':'hidden widsom covered by overthinking',
              'empress':'nurture creativity and joy','emperor':'structure, boundaries, authority', 'hierophant':'there is value in tradition, but which rules are you following and why?',
              'lovers':'romance, integrity, follow your heart, at a crossroad', 'chariot':'move forward with purpose, steer with will and wisdom','strength':'tenderness can be strength. rise from struggle',
              'hermit':'retreat to reflect, inner wisdom','wheel of fortune':'change is the only constant. life has ups and downs','justice':'balance the scales, truth will prevail',
              'hanged man':'new perspective needed, wait and see. stuck or stagnant','death':'endings, change, new beginnings. let go of the old to make room for new.',
              'temperance':"don't rush outcomes, you can't control them", 'devil'}

if __name__=="__main__":
    cards_found=find_cards()
    give_answers(cards_found)
