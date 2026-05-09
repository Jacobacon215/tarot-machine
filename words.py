print("hello bitch")
import string

fool_words=['adventure', 'summer', 'opportunity', 'change', 'progress', 'transition', 'hesitation']
magic_words=['experiment', 'trans', 'initiative', 'action', 'proactive']
hp_words=['intuition','stuck','midterm','exam','friendship']
empress_words=['project', 'idea','block','mpreg','health','inspiration']
emperor_words=['lockin','focus','procrastinate','study','monster','celsius']
hiero_words=['advice','guidance','mothers day','parent','mother','father']
lover_words=['path','situationship','hinge','grindr','tinder','divorce','breakup','scandal','confidence']
chariot_words=['goals','advisor','mentor','momentum','perseverance','promotion','responsibility','internship']
strength_words=['forgiveness','forgive','angry','anger','frustrated','grudge','revenge']
hermit_words=['professor','library','confused','lonely','quiet','study','lockin']
wheel_words=['repeat','again','graduate','failure','test','withdraw','adddrop', 'meaning of life']
justice_words=['protest','competition','war','revenge','compromise','opinion','argument']
hanged_words=['reflection','waiting','realize','discovery','clarity','focus']
death_words=['graduation','graduate','summer','quarter','end','moving','meaning of life']
temp_words=['grades','curve','mental health','therapy','depress','canvas','assignment']
devil_words=['situationship','judge','scav','procrastinate','lazy','laziness']
tower_words=['midterm','exam','grades','partner','boyfriend','girlfriend','government']
star_words=['therapy','ex','again','another try','fresh start']
moon_words=['uncertain','confused','experiment','tryout', 'try','interview']
sun_words=['stress','difficult','uchicago','scav','weather','mothers day','meaning of life']
judge_words=['graduate','judgment','points','item','showcase','ida noyes','david rubenstein','david m rubenstein','religion','church','god']
world_words=['victory','win','graduation','judgeship','celebration','time']

question_asked = input("What question do you seek answered?")
stripped_q = question_asked.lower().split(' ')
final_q = [w.strip(string.punctuation) for w in stripped_q]