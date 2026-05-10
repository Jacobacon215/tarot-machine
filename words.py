import string
import random
fool_words = {'adventure', 'summer', 'opportunity',
              'change', 'progress', 'transition', 'hesitation', 'new',
              'study abroad', 'profess'}
magic_words = {'experiment', 'trans', 'initiative', 'action', 'proactive','willpower','block','job','career'}
hp_words = {'intuition', 'stuck', 'midterms', 'exams', 'friendship', 'relationship', 'friend'}
empress_words = {'project', 'idea', 'block', 'mpreg', 'health', 'inspiration','nature', 'intuition','job','career'}
emperor_words = {'lockin', 'focus',
                 'procrastinate', 'study', 'monster', 'celsius', 'purpose', 'boundaries','boundary', 'career', 'cuck'}
hiero_words = {'advice', 'guidance',
               'mothers day', 'parent', 'mother', 'father','tradition'}
lover_words = {'path', 'situationship', 'hinge', 'grindr',
               'tinder', 'divorce', 'breakup', 'scandal', 'confidence',
               'date', 'dating', 'ask out', 'rizz', 'red flag','relationship','wedding','love'}
chariot_words = {'goals', 'advisor', 'mentor', 'momentum',
                 'perseverance', 'promotion', 'responsibility', 'internship',
                 'grindset', 'job', 'direction', 'success','purpose','profess', 'interview'}
strength_words = {'forgiveness', 'forgive', 'angry',
                  'anger', 'frustrated', 'grudge', 'revenge','focus', 'success', 'ida', 'noyes','career', 'virtue'}
hermit_words = {'professor', 'library', 'confused',
                'lonely', 'quiet', 'study', 'lockin', 'the reg', 'think','intuition','block','nerd'}
wheel_words = {'repeat', 'again', 'graduate', 'failure',
               'test', 'withdraw', 'adddrop', 'meaning of life','change', 'where','convocation'}
justice_words = {'protest', 'competition', 'war',
                 'revenge', 'compromise', 'opinion', 'argument', 'republican', 'effect'}
hanged_words = {'reflection', 'waiting',
                'realize', 'discovery', 'clarity', 'focus','release', 'seek','purpose'}
death_words = {'graduation', 'graduate', 'summer',
               'quarter', 'end', 'moving', 'meaning of life','change','beginning', 'obstacle','future','terror'}
temp_words = {'grades', 'curve', 'mental health',
              'therapy', 'depressed','depression', 'canvas', 'assignments', 
              'finals', 'midterms','patience', 'outcome','terror'}
devil_words = {'situationship', 'judge',
               'scav', 'procrastinate', 'lazy', 'laziness', 
               'business','economics', 'finance', 'quant', 'relationship', 'bizcon'}
tower_words = {'midterm', 'exam', 'exams', 'grades','grade', 'partner',
               'boyfriend', 'girlfriend', 'government','disaster', 'relationship','connection','future', 'david', 'rubenstein','obama','love',
               'terror'}
star_words = {'therapy', 'ex', 'again', 'another', 'fresh start','faith','new','try', 'red', 'flag','year'}
moon_words = {'uncertain', 'confused',
              'experiment', 'tryout', 'try', 'interview',
              'what the fuck', 'understand','confused','illusion','unsure','unclear','intuition', 'obstacles','block', 'where'}
sun_words = {'stress', 'difficult', 'uchicago', 'scav',
             'weather', 'mothers day', 'meaning of life','positiv','success','celebrate', 'celebration','friend', 'future','virtue'}
judge_words = {'graduate', 'judgment', 'points', 'item', 'showcase', 'ida', 'noyes',
               'david', 'rubenstein', 'religion', 'church', 'god','reflect'}
world_words = {'victory', 'win', 'graduation',
               'judgeship', 'celebration', 'time','complete','completion', 'success', 'years', 'convocation','career'}
all_words_list = [fool_words, magic_words, hp_words, empress_words, emperor_words, hiero_words, lover_words, chariot_words, strength_words, hermit_words,
                  wheel_words, justice_words, hanged_words, death_words, temp_words, devil_words, tower_words, star_words, moon_words, sun_words, judge_words, world_words]
tarot_cards = ["fool", "magician", "highpriestess", "empress", "emperor", "hierophant", "lovers", "chariot", "strength", "hermit", "wheel of fortune", "justice", "hangedman", "death",
               "temperance", "devil", "tower", "star", "moon", "sun", "judgment", "world"]

def main():
    return None


def find_cards():
    question_asked = input("What question do you seek answered?")
    stripped_q = question_asked.lower().split(' ')
    final_q = [w.strip(string.punctuation) for w in stripped_q]
    card_set_dict = {x[0]: x[1] for x in zip(tarot_cards, all_words_list)}
    card_score_dict = {x: 0 for x in tarot_cards}
    tower=False
    for word in final_q:
        for cardname, wordset in card_set_dict.items():
            if word in wordset:
                card_score_dict[cardname] += 1
    selected=sorted(card_score_dict, key=card_score_dict.get, reverse=True)[0:3]
    if "tower" not in selected: 
        tower_chance=random.random()
        if tower_chance > 0.8:
         tower=True
        if tower:
            victim=random.randint(1,3)
            selected[victim]="tower"
    return(selected)

def give_answers(cards):
    card_def={'fool':'leap of faith, step into the unknown', 'magician':'the tools are in front of you, you should act', 'highpriestess':'hidden wisdom covered by overthinking',
              'empress':'nurture creativity and joy','emperor':'structure, boundaries, authority', 'hierophant':'there is value in tradition, but which rules are you following and why?',
              'lovers':'romance, integrity, follow your heart, at a crossroad', 'chariot':'move forward with purpose, steer with will and wisdom','strength':'tenderness can be strength. rise from struggle',
              'hermit':'retreat to reflect, inner wisdom','wheel of fortune':'change is the only constant. life has ups and downs','justice':'balance the scales, truth will prevail',
              'hanged man':'new perspective needed, wait and see. stuck or stagnant','death':'endings, change, new beginnings. let go of the old to make room for new.',
              'temperance':"don't rush outcomes, you can't control them", 'devil':'trapped in your own thoughts, a self-prison', 'tower':'sudden upheaval. current structure was built on shaky foundations.',
              'star':'hope after upheaval. healing, renewal.', 'moon':'truth will be revealed. cloudy at the moment, but trust your instincts.', 'sun':'optimism, release self-doubt. welcome joy into your life.',
              'judgment':'evolution, clarity, a rise to the next stage', 'world':'success, completion, reflection. the world is at your feet!'}
    result=[]
    for cardpicked in cards:
        print(cardpicked, ":")
        print(card_def[cardpicked])
        result.append((cardpicked, card_def[cardpicked]))
    return result

def pick_reading(cards):
    adjectives={'fool':'new', 'magician':'capable','highpriestess':'wise','empress':'creative','emperor':'authoritative','hierophant':'traditional',
                'lovers':'emotional','chariot':'purposeful','strength':'gentle','hermit':'introspective','wheel of fortune':'cyclical','justice':'balanced',
                'hanged man':'stuck','death':'changing','temperance':'patient','devil':'trapped','tower':'chaotic','star':'hopeful','moon':'instinctive',
                'sun':'optimistic','judgment':'evolved','world':'complete'}
    nouns={'fool':'step forward', 'magician':'option','highpriestess':'wisdom','empress':'creation','emperor':'boundary','hierophant':'rules',
                'lovers':'heart','chariot':'purpose','strength':'tenderness','hermit':'self','wheel of fortune':'change','justice':'truth',
                'hanged man':'perspective','death':'beginning','temperance':'outcome','devil':'freedom','tower':'upheaval','star':'light','moon':'path',
                'sun':'joy','judgment':'clarity','world':'success'}
    verbs={'fool':'leap', 'magician':'act','highpriestess':'realize','empress':'nurture','emperor':'control','hierophant':'follow',
                'lovers':'feel','chariot':'proceed','strength':'guide','hermit':'reflect','wheel of fortune':'rotate','justice':'balance',
                'hanged man':'understand','death':'begin','temperance':'wait','devil':'escape','tower':'fall','star':'renew','moon':'intuit',
                'sun':'enjoy','judgment':'progress','world':'complete'}
    
    verb=verbs[random.choice(cards)]
    adjective=adjectives[random.choice(cards)]        
    noun=nouns[random.choice(cards)]
    reading1=f"the {noun} holding you back makes you {adjective} so you should {verb}"
    reading2=f"trust the {adjective} {noun} that will {verb} you"
    reading3=f"you are {adjective} so you should {verb} the {noun}"
    reading4=f"if you {verb} the {noun} you might find that you are {adjective}"
    reading5=f"your {adjective} {noun} is {verb}ing, so {verb} too"
    reading6=f"the {adjective} {noun} is on its way so {verb}"
    all_readings=[reading1, reading2, reading3, reading4, reading5, reading6]
    selection=random.choice(all_readings)
    return selection


if __name__=="__main__":
    cards_found=find_cards()
    answered=give_answers(cards_found)
    print(pick_reading(cards_found))