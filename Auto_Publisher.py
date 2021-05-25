import pyautogui as pyg
import time


teste=["Vnidoidera", "Vniteste"]

# GENERAL SCIENCE
sci1 = ["science lovers", "science and facts"]

scienceandastronomy1 = ["Astronomy and Science", "science and astronomy"]

# SPACE ASTRONOMY ASTROPHYSICS COSMOLOGY
space1 = ['Science & Astronomy', "ASTRONOMY KNOWLEDGE", "Visions of Astronomy", "physics_astronomy", "astronomy and cosmology"]
space2 = ["Physics_astronomy group", "Astronomy and Science", "The Space Lovers", "Space Science"]
space3 = ["NASA - National Aeronautics And Space Administration", "Hubble", "cosmology"]
space4 = ["we love space", "astronomy and geography", "cosmology & astrophysics news", "cosmology & astrophysics no"]
space5 = []

universe1 = ['beauties of the universe', "interstellar universe", "the universe knowledge"]


# AI, data science
lixo = ['Data Science - Machine Learning, Artificial intelligence, Deep Learning' ,
        'Data Science, Machine Learning, Deep Learning and Artificial Intelligence',
        'Collaborate on Artificial Intelligence, Machine Learning & Deep Learning.',
       'Python | Artificial Intelligence | Data Science | Deep and Machine Learning',
        'Machine Learning/Artificial Intelligence /Data Science /Deep Learning',
        'Beginning Data Science, Analytics, Machine Learning, Data Mining, R, Python',
        'Artificial Intelligence: Deep Learning, Machine Learning & Neural Networks',
        'AI & Machine Learning for Everyone']

AI1 = ['Artificial Intelligence & Deep Learning', "Artificial Intelligence", 'artificial intelligence: deep']
AI2 = ['Math for Artificial Intelligence & Big Data']
AI4 = ['Machine Learning/Artificial Intelligence /Data Science /Deep Learning']

DL1 = ['Deep Learning and Machine Learning', 'neural network']

# BIOINFORMATICS
BioInfo1 = ['Bioinformatics Information Center', 'World of Bioinformatics', 'BioInformatics Group (BIG)', 'Bioinformatics and Biomedicine Research']
# BioInfo2 = ['BioSys:Bioinformatics and System Biology'] QUEBRADO

# math1=["Math and Physics", "Math Artists"]
math1=["Math and Physics", 'mathematics (applied', "Math for Artificial Intelligence", "Math Puzzles"]
math2=["Math Facts",  "Advance calculus", "Research on pure mathematics"]
math3=["MATHEMATICS ONLY", "Mathematics", "Mathematics Worldwide", "Pure mathematics"]
# math4 = [ ]

mathart1 = ["Visual Math", "Math Artists"]

lixomath = ['Art Of Mathematics Group']


# ECOLOGY
forest1 = ['forests of the world', 'forest ecology group', 'ancient forests', 'the amazon rainforest']
tree1 = ['big tree seekers', 'unique trees']
ecology1 = ['ecology', 'movement ecology', 'landscape ecology', 'reciprocal ecology']
environment1 = ['environment activist', 'environment and earth']

# CLIMATE
climate1 = ["climate & capitalism", "climate & environment", "climate change"]

# SUSTAINABLE
sustainable1 = ["sustainable living", "sustainable development goals", "social entrepreneurship", "inspired by nature"]
sustainable2 = ['green, renewable', "eco-friendly"]

def press_tab(n):
    i=0
    while (i < n):
        pyg.press("tab")
        time.sleep(1.5)
        i+=1

def press_shifttab(n):
    i = 0
    while (i < n):
        pyg.hotkey("shift", "tab")
        time.sleep(1.5)
        i += 1

def reach_search(n):
    # pyg.press("enter")
    pyg.click()
    time.sleep(1.5)
    press_tab(n)
    pyg.press("enter")
    time.sleep(1.5)
    press_tab(3)
    time.sleep(1.5)

def write_groupname(name):
    pyg.write(name)
    time.sleep(3)
    pyg.press("tab")
    time.sleep(2)
    pyg.press("enter")
    time.sleep(2)

def publish_post(n):
    press_shifttab(n)
    pyg.press("enter")
    time.sleep(2)

def post_togroup(group):
    time.sleep(5)
    reach_search(4)
    write_groupname(group)
    publish_post(4)

def post_to_many(group_list):
    for group_name in group_list:
        post_togroup(group_name)


# post_to_many(teste)

# post_to_many(math1)
# post_to_many(math2)
# post_to_many(math3)
# post_to_many(math4)
# post_to_many(mathart1)


# post_to_many(sci1)

# post_to_many(scienceandastronomy1)

# post_to_many(space1)
# post_to_many(space2)
# post_to_many(space3)
# post_to_many(space4)

# post_to_many(AI1)
# post_to_many(AI   2)
# post_to_many(AI3)
# post_to_many(AI4)

# post_to_many(DL1)


# post_to_many(BioInfo1)
# post_to_many(BioInfo2)

# post_to_many(forest1)
# post_to_many(tree1)
# post_to_many(ecology1)


# post_to_many(sustainable1)

# post_to_many(sustainable2)
# post_to_many()
# post_to_many()

# post_to_many(climate1)
# post_to_many(environment1)
# post_to_many()
# post_to_many()

# post_to_many()
# post_to_many()
# post_to_many()
# post_to_many()




