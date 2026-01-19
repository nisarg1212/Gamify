"""Pre-built Learning Quests - Guaranteed to work without API calls!"""

from gamification.models import Story, Quiz, QuizQuestion, MasterPractice, MasterQuestion, DetectiveCase, Clue

# ============================================
# 🐍 LEARN PYTHON QUEST
# ============================================

PYTHON_QUEST = {
    1: {
        "topic": "Python Programming",
        "story": Story(
            topic="Python Programming",
            title="The Serpent's Code: A Python Adventure",
            content="""In the digital realm of Codeville, young apprentice Alex discovered an ancient scroll containing the secrets of Python—the most beloved programming language in all the kingdoms.

"Python was created by Guido van Rossum in 1991," the scroll read, "designed to be simple, readable, and powerful. Unlike the cryptic languages of old, Python reads almost like English!"

Alex learned that Python uses indentation to define code blocks, making it visually clean. Variables don't need type declarations—you simply write `name = "Alex"` and Python figures out the rest.

The scroll revealed Python's secret weapons: lists for storing collections `[1, 2, 3]`, dictionaries for key-value pairs `{"name": "Alex"}`, and loops that repeat tasks effortlessly.

"Remember," the scroll concluded, "in Python, we use `print()` to display output, `input()` to receive data, and `#` to write comments. With these tools, you can build anything from games to AI!"

Alex smiled, ready to write their first line of code: `print("Hello, World!")`""",
            key_facts=[
                "Python was created by Guido van Rossum in 1991",
                "Python uses indentation to define code blocks",
                "Variables don't need type declarations in Python",
                "Lists use square brackets: [1, 2, 3]",
                "print() displays output, input() receives user data"
            ],
            xp_reward=15
        ),
        "quiz": Quiz(
            topic="Python Programming",
            questions=[
                QuizQuestion(
                    question="Who created Python?",
                    options=["Guido van Rossum", "Mark Zuckerberg", "Elon Musk", "Bill Gates"],
                    correct_index=0,
                    explanation="Guido van Rossum created Python in 1991!"
                ),
                QuizQuestion(
                    question="What does Python use to define code blocks?",
                    options=["Indentation (spaces/tabs)", "Curly braces {}", "Parentheses ()", "Square brackets []"],
                    correct_index=0,
                    explanation="Python uses indentation to define code blocks, making it visually clean!"
                ),
                QuizQuestion(
                    question="How do you display output in Python?",
                    options=["print()", "echo()", "display()", "show()"],
                    correct_index=0,
                    explanation="print() is the function used to display output in Python!"
                ),
                QuizQuestion(
                    question="Which symbol is used for comments in Python?",
                    options=["#", "//", "/*", "--"],
                    correct_index=0,
                    explanation="The # symbol starts a comment in Python!"
                ),
                QuizQuestion(
                    question="How do you create a list in Python?",
                    options=["[1, 2, 3]", "{1, 2, 3}", "(1, 2, 3)", "<1, 2, 3>"],
                    correct_index=0,
                    explanation="Lists use square brackets: [1, 2, 3]"
                )
            ],
            difficulty="basic",
            total_xp=70
        ),
        "master": MasterPractice(
            topic="Python Programming",
            questions=[
                MasterQuestion(
                    question="What would `len([1, 2, 3, 4, 5])` return?",
                    question_type="multiple_choice",
                    options=["5", "4", "6", "Error"],
                    correct_answer="5",
                    explanation="len() returns the number of items in a list. This list has 5 items!",
                    xp_reward=20
                ),
                MasterQuestion(
                    question="Which data type would you use to store a person's name and age together?",
                    question_type="multiple_choice",
                    options=["Dictionary", "List", "Integer", "String"],
                    correct_answer="Dictionary",
                    explanation="Dictionaries store key-value pairs like {'name': 'Alex', 'age': 25}",
                    xp_reward=20
                ),
                MasterQuestion(
                    question="What does `'hello'.upper()` return?",
                    question_type="multiple_choice",
                    options=["'HELLO'", "'Hello'", "'hello'", "Error"],
                    correct_answer="'HELLO'",
                    explanation="The .upper() method converts all characters to uppercase!",
                    xp_reward=20
                )
            ],
            total_xp=110
        ),
        "detective": DetectiveCase(
            topic="Python Programming",
            case_title="The Case of the Missing Indent",
            scenario="Codeville's traffic light system has crashed! The lights are stuck on red, causing massive gridlock. The lead engineer left a note: 'I added a new condition to the traffic loop, but now nothing works!' You check the code and see an `if` statement that looks a bit flat.",
            clues=[
                Clue(id=1, description="The traffic loop uses a `while True:` statement.", is_key_clue=False),
                Clue(id=2, description="Inside the loop, there is an `if traffic == 'heavy':` check.", is_key_clue=False),
                Clue(id=3, description="The line `light = 'green'` is directly under the `if`, but aligned with the `while`.", is_key_clue=True),
                Clue(id=4, description="Python relies on visual alignment to know what code belongs where.", is_key_clue=True)
            ],
            question="Why is the traffic light code failing to execute the logic inside the `if` statement?",
            correct_answer="Indentation Error",
            explanation="In Python, code inside an `if` block MUST be indented (shifted right). The engineer forgot to indent the code, so it wasn't part of the conditional logic!",
            xp_reward=100
        )
    },
    2: {
        "topic": "Python Level 2: Control Flow",
        "story": Story(
            topic="Python Level 2",
            title="The Loop of Eternity",
            content="""Alex returned to Codeville to find the Great Clock tower spinning wildly out of control. 'The While Loop is stuck!' cried the Mayor.

Alex approached the central terminal. The code governing the clock was trapped in an infinite loop: `while True: spin_clock()`. There was no `break` condition!

"To control the flow of time," a holographic guide appeared, "you must master `if`, `elif`, and `else`. And most importantly, know when to `break` a loop."

Alex learned that `for` loops are perfect for iterating over known sequences: `for hour in range(12):`. But `while` loops run forever unless stopped.

With shaking hands, Alex added a condition: `if time == 'midnight': break`. The code parsed, the logic held, and the Great Clock slowed to a rhythmic tick-tock.

"You have mastered Control Flow," the hologram nodded. "But the data structures of the old library are still in chaos. That is your next trial." """,
            key_facts=[
                "while loops run as long as the condition is True",
                "An infinite loop never ends unless broken",
                "The `break` statement exits a loop immediately",
                "for loops are used to iterate over a sequence (like range or list)",
                "elif allows checking multiple conditions in a sequence"
            ],
            xp_reward=20
        ),
        "quiz": Quiz(
            topic="Python Level 2",
            questions=[
                QuizQuestion(
                    question="Which keyword exits a loop immediately?",
                    options=["break", "stop", "exit", "quit"],
                    correct_index=0,
                    explanation="break is used to exit a loop immediately."
                ),
                QuizQuestion(
                    question="What does range(5) generate?",
                    options=["0, 1, 2, 3, 4", "1, 2, 3, 4, 5", "0, 1, 2, 3, 4, 5", "1, 2, 3, 4"],
                    correct_index=0,
                    explanation="range(n) generates numbers from 0 up to (but not including) n."
                ),
                QuizQuestion(
                    question="How do you write 'else if' in Python?",
                    options=["elif", "elseif", "else if", "if else"],
                    correct_index=0,
                    explanation="Python uses the keyword `elif`."
                ),
                QuizQuestion(
                    question="What happens if a while loop condition never becomes False?",
                    options=["Infinite loop", "Syntax Error", "Computer explodes", "Nothing"],
                    correct_index=0,
                    explanation="It creates an infinite loop that runs forever (until crashed/stopped)."
                ),
                QuizQuestion(
                    question="Which loop is best for iterating over a list of items?",
                    options=["for loop", "while loop", "do-while loop", "if loop"],
                    correct_index=0,
                    explanation="for loops are designed for iterating over sequences."
                )
            ],
            difficulty="intermediate",
            total_xp=80
        ),
        "master": MasterPractice(
            topic="Python Level 2",
            questions=[
                MasterQuestion(
                    question="Write a loop that prints numbers 0 to 4.",
                    question_type="multiple_choice",
                    options=["for i in range(5): print('i')", "for i in range(4): print('i')", "while i < 5: print('i')", "loop 5 times: print('i')"],
                    correct_answer="for i in range(5): print('i')",
                    explanation="range(5) goes 0-4. The for loop iterates through each.",
                    xp_reward=25
                ),
                MasterQuestion(
                    question="What is the output of: `x = 10; if x > 5: print('A'); else: print('B')`",
                    question_type="multiple_choice",
                    options=["A", "B", "Error", "None"],
                    correct_answer="A",
                    explanation="10 is greater than 5, so the if block executes.",
                    xp_reward=25
                ),
                MasterQuestion(
                    question="Which statement skips the current iteration and goes to the next?",
                    question_type="multiple_choice",
                    options=["continue", "break", "pass", "skip"],
                    correct_answer="continue",
                    explanation="continue skips the rest of the current loop code and jumps to the next iteration.",
                    xp_reward=25
                )
            ],
            total_xp=120
        ),
        "detective": DetectiveCase(
            topic="Python Level 2",
            case_title="The Infinite Toaster",
            scenario="A smart toaster is burning all the bagels! It just keeps toasting forever. You check the code: `while bread.is_toasted == False: heat_on()`. But users complain the bread turns to charcoal.",
            clues=[
                Clue(id=1, description="The loop checks `is_toasted == False`.", is_key_clue=False),
                Clue(id=2, description="The function `heat_on()` applies heat.", is_key_clue=False),
                Clue(id=3, description="Nowhere in the loop does `bread.is_toasted` explicitly change to True.", is_key_clue=True),
                Clue(id=4, description="The toaster has no sensor to update the bread's status inside the loop.", is_key_clue=True)
            ],
            question="Why is the toaster loop infinite?",
            correct_answer="State not updated",
            explanation="The condition `bread.is_toasted` never changes inside the loop, so it stays False forever, and the loop never ends!",
            xp_reward=110
        )
    },
    3: {
        "topic": "Python Level 3: Advanced Structures",
        "story": Story(
            topic="Python Level 3",
            title="The Library of Objects",
            content="""The Grand Library of Codeville was in disarray. Books (data) were scattered everywhere. "We need a Class system!" allowed the Librarian.

Alex discovered Object-Oriented Programming (OOP). Instead of loose variables, he could define a `class Book:` with attributes like `self.title` and `self.author`.

"Functions inside classes are called Methods," the Librarian explained. "Like `def read(self):`".

Alex built a `class Library:` to manage the books. He learned about `__init__`, the constructor that builds new objects. He even touched on Inheritance, creating `class DigitalBook(Book):`.

By organizing the chaos into Objects and Classes, order was restored to the Library. Alex was no longer just a coder; he was a Software Architect.

"You have conquered Python," the Librarian smiled. "The world is yours to build." """,
            key_facts=[
                "Classes are blueprints for creating objects",
                "__init__ is the constructor method in Python",
                "Functions inside classes are called methods",
                "self refers to the current instance of the class",
                "Inheritance allows a class to derive features from another"
            ],
            xp_reward=25
        ),
        "quiz": Quiz(
            topic="Python Level 3",
            questions=[
                QuizQuestion(
                    question="What keyword is used to define a class?",
                    options=["class", "def", "struct", "object"],
                    correct_index=0,
                    explanation="The `class` keyword defines a new class."
                ),
                QuizQuestion(
                    question="What is `__init__` used for?",
                    options=["Initializing a new object", "Ending a class", "Importing a library", "Deleting values"],
                    correct_index=0,
                    explanation="__init__ is the constructor method run when a new object is created."
                ),
                QuizQuestion(
                    question="What does `self` represent?",
                    options=["The current object instance", "The parent class", "The global variable", "Nothing"],
                    correct_index=0,
                    explanation="self refers to the specific object instance being operated on."
                ),
                QuizQuestion(
                    question="What is inheritance?",
                    options=["A child class deriving properties from a parent", "Getting money from relatives", "Importing a module", "A type of loop"],
                    correct_index=0,
                    explanation="Inheritance allows a new class to use logic from an existing class."
                ),
                QuizQuestion(
                    question="How do you call a method `bark` on object `dog`?",
                    options=["dog.bark()", "bark(dog)", "dog->bark()", "Class.bark(dog)"],
                    correct_index=0,
                    explanation="Dot notation `object.method()` is used in Python."
                )
            ],
            difficulty="advanced",
            total_xp=90
        ),
        "master": MasterPractice(
            topic="Python Level 3",
            questions=[
                MasterQuestion(
                    question="Define a class 'Dog' with a method 'bark'.",
                    question_type="multiple_choice",
                    options=["class Dog: def bark(self): print('Woof')", "def Dog: bark()", "class Dog: bark()", "Dog = class(bark)"],
                    correct_answer="class Dog: def bark(self): print('Woof')",
                    explanation="Correct syntax uses `class` keyword and indent method definition.",
                    xp_reward=30
                ),
                MasterQuestion(
                    question="How do you create an instance of class `Car`?",
                    question_type="multiple_choice",
                    options=["my_car = Car()", "my_car = new Car()", "Car my_car", "instance Car"],
                    correct_answer="my_car = Car()",
                    explanation="Python doesn't use `new`. Just call the class like a function.",
                    xp_reward=30
                ),
                MasterQuestion(
                    question="What variable holds the data for a specific object inside the class?",
                    question_type="multiple_choice",
                    options=["self", "this", "it", "my"],
                    correct_answer="self",
                    explanation="Instance variables are accessed via `self.variable`.",
                    xp_reward=30
                )
            ],
            total_xp=140
        ),
        "detective": DetectiveCase(
            topic="Python Level 3",
            case_title="The Ghost Object",
            scenario="A banking system uses `class Account`. But when `acc1` withdraws money, `acc2`'s balance also goes down! It's a disaster. You look at the code: `balance = 0` is defined directly under `class Account:` not inside `__init__`.",
            clues=[
                Clue(id=1, description="`balance` is defined at the class level.", is_key_clue=True),
                Clue(id=2, description="Class variables are shared by ALL instances.", is_key_clue=True),
                Clue(id=3, description="Instance variables (unique to each object) should be in `__init__` using `self`.", is_key_clue=True),
                Clue(id=4, description="The engineer forgot to use `self.balance`.", is_key_clue=False)
            ],
            question="Why are the accounts sharing the same balance?",
            correct_answer="Class Variable Shared",
            explanation="The variable was defined as a Class Variable (shared by all) instead of an Instance Variable (unique to each). It should have been `self.balance = 0` inside `__init__`.",
            xp_reward=120
        )
    }
}

# ============================================
# 🌌 BLACK HOLES QUEST
# ============================================

BLACK_HOLES_QUEST = {
    1: {
        "topic": "Black Holes",
        "story": Story(
            topic="Black Holes",
            title="Journey to the Edge of Darkness",
            content="""Captain Nova guided her starship toward humanity's greatest mystery—a black hole named Cygnus X-1, lurking 6,000 light-years from Earth.

"A black hole," she explained to her crew, "is what remains when a massive star dies. The star collapses under its own gravity, crushing matter into an infinitely dense point called a singularity."

As they approached, the ship's sensors detected the event horizon—the invisible boundary from which nothing, not even light, can escape. "That's why they're black," Nova said. "Light itself gets trapped!"

The crew observed the accretion disk, a swirling ring of superheated gas spinning around the black hole at nearly the speed of light. The friction made it glow brighter than a billion suns.

"Einstein predicted these in 1915," the science officer noted, "but we didn't photograph one until 2019—the M87 black hole, 55 million light-years away!"

Nova smiled at the cosmic monster before them. "Black holes aren't vacuums that suck everything in. They have gravity like any object—you'd only fall in if you got too close. The supermassive one at our galaxy's center is 4 million times the mass of our Sun!"

The universe's darkest secrets lay before them, waiting to be understood.""",
            key_facts=[
                "Black holes form when massive stars collapse under their own gravity",
                "The event horizon is the boundary from which nothing can escape",
                "The singularity is an infinitely dense point at the center",
                "The first black hole photograph was taken in 2019 (M87)",
                "The supermassive black hole at our galaxy's center is 4 million solar masses"
            ],
            xp_reward=15
        ),
        "quiz": Quiz(
            topic="Black Holes",
            questions=[
                QuizQuestion(
                    question="What is the event horizon?",
                    options=["The boundary from which nothing can escape", "The center of a black hole", "A type of star", "A galaxy"],
                    correct_index=0,
                    explanation="The event horizon is the invisible boundary—cross it, and there's no return!"
                ),
                QuizQuestion(
                    question="What is at the center of a black hole?",
                    options=["A singularity", "A star", "Empty space", "A planet"],
                    correct_index=0,
                    explanation="The singularity is an infinitely dense point where all the mass is concentrated!"
                ),
                QuizQuestion(
                    question="When was the first black hole photographed?",
                    options=["2019", "1915", "2000", "1969"],
                    correct_index=0,
                    explanation="The first image of a black hole (M87) was captured in 2019!"
                ),
                QuizQuestion(
                    question="Why are black holes black?",
                    options=["Light cannot escape them", "They're made of dark matter", "They absorb all colors", "They're very cold"],
                    correct_index=0,
                    explanation="Black holes are black because their gravity is so strong that even light cannot escape!"
                ),
                QuizQuestion(
                    question="How massive is the black hole at our galaxy's center?",
                    options=["4 million times the Sun's mass", "4 times the Sun's mass", "400 times the Sun's mass", "4 billion times the Sun's mass"],
                    correct_index=0,
                    explanation="Sagittarius A* is about 4 million times the mass of our Sun!"
                )
            ],
            difficulty="basic",
            total_xp=70
        ),
        "master": MasterPractice(
            topic="Black Holes",
            questions=[
                MasterQuestion(
                    question="What determines the size of a black hole's event horizon?",
                    question_type="multiple_choice",
                    options=["Its mass", "Its age", "Its temperature", "Its spin direction"],
                    correct_answer="Its mass",
                    explanation="The more massive a black hole, the larger its event horizon (Schwarzschild radius)!",
                    xp_reward=20
                ),
                MasterQuestion(
                    question="What happens to time near a black hole?",
                    question_type="multiple_choice",
                    options=["Time slows down", "Time speeds up", "Time stops completely", "Time goes backward"],
                    correct_answer="Time slows down",
                    explanation="Due to gravitational time dilation, time slows down near massive objects like black holes!",
                    xp_reward=20
                ),
                MasterQuestion(
                    question="What is Hawking radiation?",
                    question_type="multiple_choice",
                    options=["Energy slowly leaking from black holes", "Light from the accretion disk", "Radiation from dying stars", "Cosmic background radiation"],
                    correct_answer="Energy slowly leaking from black holes",
                    explanation="Stephen Hawking theorized that black holes slowly emit radiation and can eventually evaporate!",
                    xp_reward=20
                )
            ],
            total_xp=110
        ),
        "detective": DetectiveCase(
            topic="Black Holes",
            case_title="The Invisible Giant",
            scenario="Astronomers at the Stellar Observatory have detected something strange: a star is orbiting... nothing! The star completes a full orbit every 16 years, reaching speeds of 7,000 km/s at its closest approach. But there's no visible companion.",
            clues=[
                Clue(id=1, description="The star's orbit suggests an invisible object with 4 million solar masses", is_key_clue=True),
                Clue(id=2, description="Radio waves are detected from the center of the orbit", is_key_clue=True),
                Clue(id=3, description="The object is located at the center of our Milky Way galaxy", is_key_clue=True)
            ],
            question="What is the star orbiting?\n\nA. Sagittarius A* (supermassive black hole)\nB. A dark matter cloud\nC. An invisible neutron star\nD. A brown dwarf",
            correct_answer="A. Sagittarius A* (supermassive black hole)",
            explanation="You solved it! This describes the star S2 orbiting Sagittarius A*, the supermassive black hole at our galaxy's center. This discovery helped prove Einstein's theories!",
            xp_reward=100
        )
    },
    2: {
        "topic": "Black Holes Level 2",
        "story": Story(
            topic="Black Holes Level 2",
            title="The Time Distortion",
            content="""Nova's ship moved closer. The communication signals from Earth were arriving... slowly.

"Gravitational Time Dilation," Nova warned. "Gravity is warping space-time itself. One hour down here is seven years back on Earth."

They deployed a probe. As it fell toward the Event Horizon, it didn't disappear. Instead, its image froze and turned red. "Redshift," the science officer gasped. "The light is losing energy climbing out of the gravity well."

The probe was undergoing 'Spaghettification'—the tidal forces were so strong that the probe's front was being pulled harder than its back, stretching it like a noodle!

"If we cross the horizon," Nova said, "space and time swap roles. Moving forward in time would mean moving inward toward the singularity. There is no path back."

They fired thrusters, escaping the trap. They had glimpsed the edge of reality itself.""",
            key_facts=[
                "Gravity warps space and time (Time Dilation)",
                "For an outside observer, objects falling in appear to freeze and redshift",
                "Spaghettification is the stretching caused by extreme tidal forces",
                "Inside the event horizon, all paths lead to the singularity",
                "Time moves slower the closer you get to a massive object"
            ],
            xp_reward=20
        ),
        "quiz": Quiz(
            topic="Black Holes Level 2",
            questions=[
                QuizQuestion(
                    question="What happens to an object falling into a black hole (from an outside view)?",
                    options=["It appears to freeze and fade", "It disappears instantly", "It explodes", "It bounces off"],
                    correct_index=0,
                    explanation="To an outsider, the light takes forever to escape, so the object seems to freeze and redshift!"
                ),
                QuizQuestion(
                    question="What is Spaghettification?",
                    options=["Stretching by tidal forces", "Cooking pasta in space", "Compression into a ball", "Turning into energy"],
                    correct_index=0,
                    explanation="You get stretched long and thin because gravity pulls your feet harder than your head!"
                ),
                QuizQuestion(
                    question="Why does time slow down near a black hole?",
                    options=["Gravity curves space-time", "It's too cold", "The spin speed affects clocks", "Magnetic fields stop time"],
                    correct_index=0,
                    explanation="According to Relativity, strong gravity curves space-time, slowing the passage of time."
                ),
                QuizQuestion(
                    question="What happens to light trying to escape a black hole?",
                    options=["It loses energy (Redshift)", "It gains speed", "It turns blue", "It becomes solid"],
                    correct_index=0,
                    explanation="The light loses energy fighting gravity, shifting its wavelength to red."
                ),
                QuizQuestion(
                    question="Once inside the event horizon, where must you go?",
                    options=["To the singularity", "Back out", "In a circle", "To another dimension"],
                    correct_index=0,
                    explanation="Space-time is so curved that all future paths lead inward to the singularity."
                )
            ],
            difficulty="intermediate",
            total_xp=80
        ),
        "master": MasterPractice(
            topic="Black Holes Level 2",
            questions=[
                MasterQuestion(
                    question="If you watched a clock fall into a black hole, what would you see?",
                    question_type="multiple_choice",
                    options=["It ticks slower and slower", "It ticks faster", "It runs backwards", "It explodes"],
                    correct_answer="It ticks slower and slower",
                    explanation="Time dilation makes the clock appear to slow down until it freezes at the horizon.",
                    xp_reward=25
                ),
                MasterQuestion(
                    question="What causes spaghettification?",
                    question_type="multiple_choice",
                    options=["Difference in gravity between head and feet", "Extreme heat", "Rotation speed", "Dark energy"],
                    correct_answer="Difference in gravity between head and feet",
                    explanation="Tidal forces: The pull on your feet is much stronger than on your head.",
                    xp_reward=25
                ),
                MasterQuestion(
                    question="Can you escape a black hole if you move faster than light?",
                    question_type="multiple_choice",
                    options=["Nothing can move faster than light", "Yes, easily", "Only in a wormhole", "No"],
                    correct_answer="Nothing can move faster than light",
                    explanation="Since the escape velocity exceeds the speed of light, and nothing exceeds light speed, escape is impossible.",
                    xp_reward=25
                )
            ],
            total_xp=120
        ),
        "detective": DetectiveCase(
            topic="Black Holes Level 2",
            case_title="The Frozen Astronaut",
            scenario="You receive a distress signal from a ship near a black hole. They claim their captain went on a spacewalk 10 years ago to fix an antenna and hasn't returned. You look through the telescope and see the captain... barely moving, frozen near the ship's hull.",
            clues=[
                Clue(id=1, description="The ship is orbiting very close to the event horizon.", is_key_clue=True),
                Clue(id=2, description="The captain looks like a statue but is still breathing (very slowly).", is_key_clue=True),
                Clue(id=3, description="Clocks on the ship show only 2 days have passed for them.", is_key_clue=True),
                Clue(id=4, description="On Earth, 10 years have passed.", is_key_clue=True)
            ],
            question="Why does the captain appear frozen in time?",
            correct_answer="Gravitational Time Dilation",
            explanation="The massive gravity near the black hole has slowed time significantly for the ship relative to the outside universe. They are experiencing time much slower than you!",
            xp_reward=110
        )
    },
    3: {
        "topic": "Black Holes Level 3",
        "story": Story(
            topic="Black Holes Level 3",
            title="The Information Paradox",
            content="""Deep within the academy, Nova studied the ultimate riddle: The Information Paradox.

"Quantum mechanics says information is never destroyed," the Professor said. "But General Relativity says anything that falls into a black hole is lost forever. These two laws contradict each other!"

Then came Stephen Hawking. He realized black holes aren't truly black. They emit 'Hawking Radiation' due to quantum effects at the horizon. Over eons, the black hole loses mass and evaporates.

"But if it evaporates," Nova asked, "where does the information go? Did the book I threw in just disappear?"

"That is the paradox!" The solution might be the Holographic Principle—that information is stored on the 2D surface of the event horizon, like a hologram, even if the object falls in 3D.

Or perhaps black holes lead to white holes in other universes. The truth waits in the math of Quantum Gravity.""",
            key_facts=[
                "The Information Paradox is a conflict between Quantum Mechanics and Relativity",
                "Hawking Radiation causes black holes to slowly evaporate",
                "The Holographic Principle suggests info is stored on the event horizon",
                "Quantum Gravity tries to unite the physics of the very big and very small",
                "Black holes may obscure the true nature of the universe"
            ],
            xp_reward=25
        ),
        "quiz": Quiz(
            topic="Black Holes Level 3",
            questions=[
                QuizQuestion(
                    question="What is the Information Paradox?",
                    options=["Conflict between Quantum Mechanics and Relativity", "A computer error", "A puzzle in a newspaper", "Nobody knows"],
                    correct_index=0,
                    explanation="It's the conflict: Quantum mechanics says info endures, Relativity says black holes destroy everything."
                ),
                QuizQuestion(
                    question="What is Hawking Radiation?",
                    options=["Particles emitted by black holes", "Heat from the sun", "Radio waves", "Laser beams"],
                    correct_index=0,
                    explanation="Quantum particles escaping the event horizon, causing the black hole to lose mass."
                ),
                QuizQuestion(
                    question="What might happen to a black hole over trillions of years?",
                    options=["It evaporates completely", "It grows forever", "It turns into a star", "It becomes a planet"],
                    correct_index=0,
                    explanation="Due to Hawking Radiation, it will eventually lose all mass and vanish."
                ),
                QuizQuestion(
                    question="What is the Holographic Principle?",
                    options=["Info is stored on the 2D surface", "The universe is fake", "Holograms are cool", "3D glasses work everywhere"],
                    correct_index=0,
                    explanation="The theory that 3D volume information can be encoded on a 2D boundary (surface)."
                ),
                QuizQuestion(
                    question="What theory is needed to solve this paradox?",
                    options=["Quantum Gravity", "Newtonian Physics", "Chemistry", "Biology"],
                    correct_index=0,
                    explanation="A theory uniting Quantum Mechanics and Gravity is the holy grail of physics."
                )
            ],
            difficulty="advanced",
            total_xp=90
        ),
        "master": MasterPractice(
            topic="Black Holes Level 3",
            questions=[
                MasterQuestion(
                    question="Which particle pair comes into existence near the event horizon?",
                    question_type="multiple_choice",
                    options=["Particle and Antiparticle", "Proton and Electron", "Two Neutrons", "Two Photons"],
                    correct_answer="Particle and Antiparticle",
                    explanation="Virtual particle-antiparticle pairs pop in and out. If one falls in, the other escapes as radiation.",
                    xp_reward=30
                ),
                MasterQuestion(
                    question="Does a black hole violate the Second Law of Thermodynamics (Entropy)?",
                    question_type="multiple_choice",
                    options=["No, it has entropy proportional to surface area", "Yes, it destroys entropy", "Entropy doesn't apply", "Only on Tuesdays"],
                    correct_answer="No, it has entropy proportional to surface area",
                    explanation="Bekenstein and Hawking showed black hole entropy is related to the area of its event horizon.",
                    xp_reward=30
                ),
                MasterQuestion(
                    question="What is a 'firewall' in black hole theory?",
                    question_type="multiple_choice",
                    options=["A wall of high-energy particles at the horizon", "Computer security", "The accretion disk", "A burning star"],
                    correct_answer="A wall of high-energy particles at the horizon",
                    explanation="A controversial solution to the paradox suggesting a burning wall of energy destroys anything falling in.",
                    xp_reward=30
                )
            ],
            total_xp=140
        ),
        "detective": DetectiveCase(
            topic="Black Holes Level 3",
            case_title="The Vanishing Library",
            scenario="A mad scientist drops a rare book into a black hole. Years later, the black hole evaporates due to Hawking Radiation. He claims the book is gone forever, violating the laws of physics!",
            clues=[
                Clue(id=1, description="Quantum mechanics says information is conserved.", is_key_clue=True),
                Clue(id=2, description="Relativity says nothing escapes.", is_key_clue=False),
                Clue(id=3, description="The radiation that came out was seemingly random heat.", is_key_clue=True),
                Clue(id=4, description="If the randomness contained subtle patterns, the info might be saved.", is_key_clue=True)
            ],
            question="How could the book's information theoretically be recovered?",
            correct_answer="Encoded in the radiation",
            explanation="According to recent theories, the information isn't lost but scrambled and encoded in the Hawking Radiation escaping the black hole, like ashes from a burnt book.",
            xp_reward=120
        )
    }
}

# ============================================
# 🦖 DINOSAUR DISCOVERY QUEST
# ============================================

DINOSAURS_QUEST = {
    1: {
        "topic": "Dinosaurs",
        "story": Story(
            topic="Dinosaurs",
            title="Echoes of the Ancient Rulers",
            content="""Dr. Maya Chen brushed away the Montana dust to reveal what she'd spent twenty years searching for—a perfectly preserved Tyrannosaurus rex skull, 67 million years old.

"Dinosaurs ruled Earth for over 165 million years," she told her students. "They first appeared about 230 million years ago during the Triassic Period. Humans? We've been here for just 300,000 years!"

The T. rex before them was a apex predator—40 feet long, with teeth the size of bananas and a bite force of 12,800 pounds. "But not all dinosaurs were giants," Maya explained. "Compsognathus was the size of a chicken!"

She pointed to the fossil's hip bones. "Dinosaurs split into two groups: Saurischians like T. rex with lizard-hips, and Ornithischians like Triceratops with bird-hips. Ironically, modern birds evolved from the lizard-hipped group!"

A student asked about their extinction. "65 million years ago, an asteroid 6 miles wide struck Mexico's Yucatan Peninsula. The impact created a nuclear winter—blocking sunlight and killing 75% of all species. But birds survived, making them living dinosaurs!"

Maya smiled at the skull. "We've discovered over 1,000 dinosaur species, and scientists estimate there could be thousands more waiting to be found!""",
            key_facts=[
                "Dinosaurs ruled Earth for over 165 million years",
                "They first appeared about 230 million years ago in the Triassic Period",
                "An asteroid impact 65 million years ago caused their extinction",
                "Modern birds are living dinosaurs, evolved from theropods",
                "Over 1,000 dinosaur species have been discovered"
            ],
            xp_reward=15
        ),
        "quiz": Quiz(
            topic="Dinosaurs",
            questions=[
                QuizQuestion(
                    question="How long did dinosaurs rule Earth?",
                    options=["Over 165 million years", "65 million years", "1 million years", "1 billion years"],
                    correct_index=0,
                    explanation="Dinosaurs dominated Earth for an incredible 165+ million years!"
                ),
                QuizQuestion(
                    question="What caused the dinosaur extinction?",
                    options=["An asteroid impact", "A volcanic eruption", "Climate change alone", "A disease"],
                    correct_index=0,
                    explanation="A 6-mile wide asteroid struck Earth 65 million years ago, creating a catastrophic extinction event!"
                ),
                QuizQuestion(
                    question="Which animals are living dinosaurs today?",
                    options=["Birds", "Crocodiles", "Lizards", "Snakes"],
                    correct_index=0,
                    explanation="Birds are direct descendants of theropod dinosaurs—they're living dinosaurs!"
                ),
                QuizQuestion(
                    question="When did dinosaurs first appear?",
                    options=["230 million years ago", "65 million years ago", "1 billion years ago", "1 million years ago"],
                    correct_index=0,
                    explanation="Dinosaurs first appeared during the Triassic Period, about 230 million years ago!"
                ),
                QuizQuestion(
                    question="What was special about T. rex's bite?",
                    options=["12,800 pounds of force", "Could breathe fire", "Was venomous", "Had no teeth"],
                    correct_index=0,
                    explanation="T. rex had one of the strongest bites ever—12,800 pounds of crushing force!"
                )
            ],
            difficulty="basic",
            total_xp=70
        ),
        "master": MasterPractice(
            topic="Dinosaurs",
            questions=[
                MasterQuestion(
                    question="Which period came FIRST in the Age of Dinosaurs?",
                    question_type="multiple_choice",
                    options=["Triassic", "Jurassic", "Cretaceous", "Permian"],
                    correct_answer="Triassic",
                    explanation="The Mesozoic Era went: Triassic → Jurassic → Cretaceous!",
                    xp_reward=20
                ),
                MasterQuestion(
                    question="Why is it ironic that birds evolved from 'lizard-hipped' dinosaurs?",
                    question_type="multiple_choice",
                    options=["Birds have bird-hips but came from lizard-hipped ancestors", "Lizards came from birds", "T. rex had feathers", "Pterodactyls were birds"],
                    correct_answer="Birds have bird-hips but came from lizard-hipped ancestors",
                    explanation="Despite the name 'Ornithischia' meaning bird-hipped, birds actually evolved from Saurischians (lizard-hipped)!",
                    xp_reward=20
                ),
                MasterQuestion(
                    question="Where did the extinction asteroid impact Earth?",
                    question_type="multiple_choice",
                    options=["Yucatan Peninsula, Mexico", "Siberia, Russia", "Arizona, USA", "Sahara Desert, Africa"],
                    correct_answer="Yucatan Peninsula, Mexico",
                    explanation="The Chicxulub crater in Mexico's Yucatan is the impact site of the dinosaur-killing asteroid!",
                    xp_reward=20
                )
            ],
            total_xp=110
        ),
        "detective": DetectiveCase(
            topic="Dinosaurs",
            case_title="The Feathered Mystery",
            scenario="A new fossil has been discovered in China. It's clearly a small dinosaur, but it has something unexpected covering its body. Paleontologists are debating what this means for our understanding of dinosaurs.",
            clues=[
                Clue(id=1, description="The fossil shows clear impressions of feather-like structures", is_key_clue=True),
                Clue(id=2, description="The dinosaur is a theropod, the same group that includes T. rex", is_key_clue=True),
                Clue(id=3, description="Modern birds are theropod descendants", is_key_clue=True)
            ],
            question="What does this fossil prove?\n\nA. Many dinosaurs had feathers, including T. rex relatives\nB. Birds evolved before dinosaurs\nC. All dinosaurs could fly\nD. Dinosaurs were warm-blooded mammals",
            correct_answer="A. Many dinosaurs had feathers, including T. rex relatives",
            explanation="Brilliant deduction! Fossilized feathers prove many theropods had feathers. Even T. rex may have had feathers as a juvenile! This links dinosaurs directly to modern birds.",
            xp_reward=100
        )
    },
    2: {
        "topic": "Dinosaurs Level 2",
        "story": Story(
            topic="Dinosaurs Level 2",
            title="The Three Eras",
            content="""Dr. Chen projected a timeline. "The Mesozoic Era is divided into three parts: Triassic, Jurassic, and Cretaceous."

"In the Triassic (250-200 MYA), all land was one supercontinent: Pangea. The first dinosaurs were small, quick runners like Eoraptor."

"The Jurassic (200-145 MYA) saw Pangea split. The climate became humid, allowing giants like Brachiosaurus to evolve. This was the Golden Age of giants!"

"The Cretaceous (145-66 MYA) brought flowers, insects, and the most famous dinosaurs: T. rex, Triceratops, and Velociraptor. It ended with fire."

"Wait," a student said, "So T. rex never met a Stegosaurus?"

"Correct!" Maya nodded. "Stegosaurus lived in the Jurassic. T. rex lived in the Cretaceous. In fact, T. rex is closer in time to humans than it is to Stegosaurus!" """,
            key_facts=[
                "The Mesozoic Era consists of Triassic, Jurassic, and Cretaceous periods",
                "Pangea existed during the Triassic period",
                "Jurassic was the age of giant sauropods like Brachiosaurus",
                "T. rex lived in the Cretaceous period",
                "Stegosaurus and T. rex never met (separated by millions of years)"
            ],
            xp_reward=20
        ),
        "quiz": Quiz(
            topic="Dinosaurs Level 2",
            questions=[
                QuizQuestion(
                    question="Which period was the age of the first small dinosaurs?",
                    options=["Triassic", "Jurassic", "Cretaceous", "Devonian"],
                    correct_index=0,
                    explanation="The Triassic Period saw the rise of the first, small dinosaurs."
                ),
                QuizQuestion(
                    question="Did T. rex and Stegosaurus live together?",
                    options=["No, millions of years apart", "Yes, they fought constantly", "Yes, they were friends", "Maybe on weekends"],
                    correct_index=0,
                    explanation="They were separated by more time than separates T. rex from us!"
                ),
                QuizQuestion(
                    question="What was the supercontinent called?",
                    options=["Pangea", "Gondwana", "Laurasia", "Atlantis"],
                    correct_index=0,
                    explanation="Pangea was the single supercontinent during the Triassic."
                ),
                QuizQuestion(
                    question="Which period saw the evolution of flowering plants?",
                    options=["Cretaceous", "Triassic", "Jurassic", "Cambrian"],
                    correct_index=0,
                    explanation="Flowering plants (Angiosperms) appeared in the Cretaceous."
                ),
                QuizQuestion(
                    question="In which period did Brachiosaurus live?",
                    options=["Jurassic", "Triassic", "Cretaceous", "Modern"],
                    correct_index=0,
                    explanation="The giant Sauropods like Brachiosaurus thrived in the Jurassic."
                )
            ],
            difficulty="intermediate",
            total_xp=80
        ),
        "master": MasterPractice(
            topic="Dinosaurs Level 2",
            questions=[
                MasterQuestion(
                    question="Order these periods from oldest to newest.",
                    question_type="multiple_choice",
                    options=["Triassic → Jurassic → Cretaceous", "Jurassic → Triassic → Cretaceous", "Cretaceous → Jurassic → Triassic", "Triassic → Cretaceous → Jurassic"],
                    correct_answer="Triassic → Jurassic → Cretaceous",
                    explanation="Timeline: Triassic (Start) → Jurassic (Middle) → Cretaceous (End).",
                    xp_reward=25
                ),
                MasterQuestion(
                    question="Which event marked the end of the Cretaceous Period?",
                    question_type="multiple_choice",
                    options=["K-Pg Extinction Event", "Great Dying", "Ice Age", "Continental Drift"],
                    correct_answer="K-Pg Extinction Event",
                    explanation="The K-Pg (Cretaceous-Paleogene) extinction event wiped out the non-avian dinosaurs.",
                    xp_reward=25
                ),
                MasterQuestion(
                    question="Why were Jurassic dinosaurs so big?",
                    question_type="multiple_choice",
                    options=["High oxygen and lush vegetation", "Low gravity", "They ate asteroids", "Magic"],
                    correct_answer="High oxygen and lush vegetation",
                    explanation="Rich plant life and atmospheric conditions supported massive body sizes.",
                    xp_reward=25
                )
            ],
            total_xp=120
        ),
        "detective": DetectiveCase(
            topic="Dinosaurs Level 2",
            case_title="The Wrong Movie",
            scenario="A famous movie shows a T. rex fighting a Spinosaurus. But Dr. Chen shakes her head. 'This fight is impossible,' she says. You check the fossil records.",
            clues=[
                Clue(id=1, description="T. rex lived in North America.", is_key_clue=True),
                Clue(id=2, description="Spinosaurus lived in North Africa.", is_key_clue=True),
                Clue(id=3, description="They lived at slightly different times in the Cretaceous.", is_key_clue=False),
                Clue(id=4, description="Continents were separated by oceans.", is_key_clue=True)
            ],
            question="Why couldn't they fight in real life?",
            correct_answer="Wrong Place (Geography)",
            explanation="T. rex and Spinosaurus lived on completely different continents separated by an ocean! They could never have met.",
            xp_reward=110
        )
    },
    3: {
        "topic": "Dinosaurs Level 3",
        "story": Story(
            topic="Dinosaurs Level 3",
            title="Warm Blood, Cold Truth",
            content="""The biggest debate in paleontology isn't about size—it's about metabolism. "For decades," Dr. Chen lectured, "we thought dinosaurs were cold-blooded (ectothermic), like modern lizards: slow, sluggish, needing sun to warm up."

"But look at this bone slice." She showed a microscope image. "It has Haversian canals—structures found in fast-growing, warm-blooded animals (endotherms)!"

"If dinosaurs were active, warm-blooded hunters, they needed huge amounts of food. And feathers makes more sense—feathers trap body heat!"

"But," she paused, "Sauropods were too big. If they were fully warm-blooded, they'd overheat/cook themselves from the inside! So we think they were 'Mesotherms'—somewhere in the middle."

"Dinosaurs weren't just monsters," she concluded. "They were complex, active, successful animals that dominated the planet purely on merit." """,
            key_facts=[
                "Ectothermic means cold-blooded (dependent on external heat)",
                "Endothermic means warm-blooded (generate own heat)",
                "Bone structures suggest many dinosaurs were active and warm-blooded",
                "Feathers likely evolved for insulation (to keep warm)",
                "Mesotherms are a middle ground between warm and cold-blooded"
            ],
            xp_reward=25
        ),
        "quiz": Quiz(
            topic="Dinosaurs Level 3",
            questions=[
                QuizQuestion(
                    question="What does 'Endothermic' mean?",
                    options=["Warm-blooded (internal heat)", "Cold-blooded (external heat)", "Living in water", "Eating plants"],
                    correct_index=0,
                    explanation="Endotherms generate their own body heat!"
                ),
                QuizQuestion(
                    question="Why did feathers likely evolve first?",
                    options=["For insulation (warmth)", "For flight", "For swimming", "For camouflage"],
                    correct_index=0,
                    explanation="Feathers trap heat. Flight came much later!"
                ),
                QuizQuestion(
                    question="What evidence suggests dinosaurs were active?",
                    options=["Bone structure (Haversian canals)", "They are green", "They lay eggs", "They are big"],
                    correct_index=0,
                    explanation="Fast-growth bone structures are typical of active, warm-blooded animals."
                ),
                QuizQuestion(
                    question="What is a Mesotherm?",
                    options=["Between warm and cold-blooded", "Only cold-blooded", "Only warm-blooded", "A type of fish"],
                    correct_index=0,
                    explanation="Mesotherms can raise body temp but not as strictly as mammals."
                ),
                QuizQuestion(
                    question="Why would a giant Sauropod overheat if fully warm-blooded?",
                    options=["Square-cube law (too much volume)", "They ate hot food", "The sun was hotter", "They ran too fast"],
                    correct_index=0,
                    explanation="Their massive volume would generate more heat than their skin could release."
                )
            ],
            difficulty="advanced",
            total_xp=90
        ),
        "master": MasterPractice(
            topic="Dinosaurs Level 3",
            questions=[
                MasterQuestion(
                    question="How does the 'Square-Cube Law' affect giant dinosaurs?",
                    question_type="multiple_choice",
                    options=["As size doubles, volume triples (heat trap)", "It makes them square", "It made them lighter", "It helped them fly"],
                    correct_answer="As size doubles, volume triples (heat trap)",
                    explanation="Massive volume generates heat, but relative surface area shrinks, making cooling hard.",
                    xp_reward=30
                ),
                MasterQuestion(
                    question="Which dinosaur group lost their teeth and evolved beaks?",
                    question_type="multiple_choice",
                    options=["Oviraptorosaurs", "Tyrannosaurs", "Sauropods", "Stegosaurs"],
                    correct_answer="Oviraptorosaurs",
                    explanation="Many bird-like dinosaurs evolved beaks, similar to modern birds.",
                    xp_reward=30
                ),
                MasterQuestion(
                    question="What is the connection between dinosaurs and birds?",
                    question_type="multiple_choice",
                    options=["Birds ARE avian dinosaurs", "Birds are cousins", "No relation", "Birds ate dinosaurs"],
                    correct_answer="Birds ARE avian dinosaurs",
                    explanation="Taxonomically, birds are classified as surviving theropod dinosaurs.",
                    xp_reward=30
                )
            ],
            total_xp=140
        ),
        "detective": DetectiveCase(
            topic="Dinosaurs Level 3",
            case_title="The Egg Thief",
            scenario="A fossil named 'Oviraptor' (Egg Thief) was found on top of a nest of eggs. For decades, scientists thought it was stealing them. But a new scan of the eggs reveals something shocking inside.",
            clues=[
                Clue(id=1, description="The Oviraptor was found directly over the nest.", is_key_clue=False),
                Clue(id=2, description="The eggs inside the nest contain baby Oviraptors.", is_key_clue=True),
                Clue(id=3, description="Modern birds sit on their nests to protect them.", is_key_clue=True),
                Clue(id=4, description="The dinosaur wasn't attacking; it was in a brooding posture.", is_key_clue=True)
            ],
            question="Was the Oviraptor stealing the eggs?",
            correct_answer="No, it was protecting them",
            explanation="The 'Egg Thief' was actually a caring parent sitting on its own nest to protect/incubate its eggs! It died protecting its babies.",
            xp_reward=120
        )
    }
}

# ============================================
# 🧬 DNA & GENETICS QUEST
# ============================================

DNA_QUEST = {
    1: {
        "topic": "DNA & Genetics",
        "story": Story(
            topic="DNA & Genetics",
            title="The Code of Life",
            content="""In 1953, two scientists named James Watson and Francis Crick made a discovery that would change biology forever—the structure of DNA, the instruction manual for all living things.

DNA stands for Deoxyribonucleic Acid. It's a twisted ladder called a double helix, held together by pairs of chemical bases: Adenine (A) always pairs with Thymine (T), and Guanine (G) always pairs with Cytosine (C).

Inside nearly every cell of your body, there are 46 chromosomes containing about 3 billion base pairs of DNA. If you stretched out all the DNA from just one cell, it would be about 6 feet long!

Your genes are sections of DNA that provide instructions to build proteins, the workers of your body. You have about 20,000 genes, and 99.9% of your DNA is identical to every other human. That 0.1% difference makes you unique!

Mutations are changes in DNA. Most are harmless, but some can cause diseases or give survival advantages. Natural selection acts on these variations—it's how evolution works.

Today, scientists can read, edit, and even write DNA. The CRISPR technology lets us edit genes with incredible precision, offering hope for curing genetic diseases. The secret of life is now in our hands!""",
            key_facts=[
                "DNA was discovered by Watson and Crick in 1953",
                "DNA is a double helix with base pairs: A-T and G-C",
                "Humans have about 20,000 genes and 3 billion base pairs",
                "99.9% of human DNA is identical between all people",
                "CRISPR technology allows precise gene editing"
            ],
            xp_reward=15
        ),
        "quiz": Quiz(
            topic="DNA & Genetics",
            questions=[
                QuizQuestion(
                    question="What does DNA stand for?",
                    options=["Deoxyribonucleic Acid", "Dynamic Nuclear Atom", "Dual Nitrogen Amplifier", "Digital Nucleic Array"],
                    correct_index=0,
                    explanation="DNA stands for Deoxyribonucleic Acid!"
                ),
                QuizQuestion(
                    question="Which bases pair together in DNA?",
                    options=["A-T and G-C", "A-G and T-C", "A-C and G-T", "All bases pair with each other"],
                    correct_index=0,
                    explanation="Adenine pairs with Thymine (A-T) and Guanine pairs with Cytosine (G-C)!"
                ),
                QuizQuestion(
                    question="What shape is DNA?",
                    options=["Double helix", "Single strand", "Triple helix", "Circular"],
                    correct_index=0,
                    explanation="DNA forms a twisted ladder shape called a double helix!"
                ),
                QuizQuestion(
                    question="How much of your DNA is identical to other humans?",
                    options=["99.9%", "50%", "75%", "25%"],
                    correct_index=0,
                    explanation="99.9% of human DNA is identical—we're all incredibly similar!"
                ),
                QuizQuestion(
                    question="What technology allows precise gene editing?",
                    options=["CRISPR", "DNA printer", "Gene scanner", "Mutation detector"],
                    correct_index=0,
                    explanation="CRISPR is a revolutionary gene-editing technology!"
                )
            ],
            difficulty="basic",
            total_xp=70
        ),
        "master": MasterPractice(
            topic="DNA & Genetics",
            questions=[
                MasterQuestion(
                    question="If one strand of DNA has the sequence ATGC, what is the complementary strand?",
                    question_type="multiple_choice",
                    options=["TACG", "ATGC", "GCTA", "CGAT"],
                    correct_answer="TACG",
                    explanation="A pairs with T, T pairs with A, G pairs with C, C pairs with G → TACG!",
                    xp_reward=20
                ),
                MasterQuestion(
                    question="What is a mutation?",
                    question_type="multiple_choice",
                    options=["A change in DNA sequence", "A new protein", "A type of cell", "A chromosome copy"],
                    correct_answer="A change in DNA sequence",
                    explanation="Mutations are changes in the DNA sequence that can be passed to offspring!",
                    xp_reward=20
                ),
                MasterQuestion(
                    question="Where in the cell is DNA primarily located?",
                    question_type="multiple_choice",
                    options=["Nucleus", "Cell membrane", "Cytoplasm", "Ribosomes"],
                    correct_answer="Nucleus",
                    explanation="DNA is stored in the cell's nucleus, protected by the nuclear membrane!",
                    xp_reward=20
                )
            ],
            total_xp=110
        ),
        "detective": DetectiveCase(
            topic="DNA & Genetics",
            case_title="The Identical Twins Mystery",
            scenario="Two identical twins were separated at birth and raised by different families. At age 30, they reunited and discovered they had the same job, similar hobbies, and married people with the same first name! Scientists are amazed.",
            clues=[
                Clue(id=1, description="Identical twins share 100% of their DNA", is_key_clue=True),
                Clue(id=2, description="Genes influence personality traits and preferences", is_key_clue=True),
                Clue(id=3, description="Environment also plays a role but DNA provides the blueprint", is_key_clue=True)
            ],
            question="What explains their remarkable similarities?\n\nA. Genes strongly influence personality and preferences\nB. It's pure coincidence\nC. They secretly communicated\nD. Environment determines everything",
            correct_answer="A. Genes strongly influence personality and preferences",
            explanation="Excellent deduction! Twin studies prove that DNA significantly influences personality, interests, and even the types of people we're attracted to. While environment matters, our genes provide a powerful blueprint!",
            xp_reward=100
        )
    },
    2: {
        "topic": "DNA & Genetics Level 2",
        "story": Story(
            topic="DNA & Genetics Level 2",
            title="Mendel's Garden",
            content="""Before we knew about DNA, a monk named Gregor Mendel discovered the rules of inheritance in his garden.

He crossed tall pea plants with short ones. He expected medium plants, but got... all tall plants! The 'Tall' trait was DOMINANT, and 'Short' was RECESSIVE.

"Traits come in pairs," Mendel realized. We now call these 'Alleles'. You get one from Mom and one from Dad.

If you have two dominant alleles (TT) or one dominant and one recessive (Tt), you show the dominant trait (Tall). You only show the recessive trait if you have two recessive alleles (tt).

He created the 'Punnett Square', a simple grid to predict what traits babies will have.

Mendel's work was ignored for 30 years, but today he is the Father of Genetics. His rules explain why you might have your grandfather's blue eyes even if your parents have brown eyes!""",
            key_facts=[
                "Gregor Mendel is the Father of Genetics (studied pea plants)",
                "Traits are controlled by alleles (variations of genes)",
                "Dominant traits hide Recessive traits",
                "Punnett Squares predict probability of offspring traits",
                "Genotype is your DNA (Tt), Phenotype is what you look like (Tall)"
            ],
            xp_reward=20
        ),
        "quiz": Quiz(
            topic="DNA & Genetics Level 2",
            questions=[
                QuizQuestion(
                    question="Who is the Father of Genetics?",
                    options=["Gregor Mendel", "Charles Darwin", "Albert Einstein", "Isaac Newton"],
                    correct_index=0,
                    explanation="Gregor Mendel discovered the laws of inheritance in his monastery garden."
                ),
                QuizQuestion(
                    question="If 'T' is Tall (Dominant) and 't' is Short (Recessive), what is a 'Tt' plant?",
                    options=["Tall", "Short", "Medium", "Dead"],
                    correct_index=0,
                    explanation="Since T is dominant, Tt results in a Tall plant."
                ),
                QuizQuestion(
                    question="What is a Punnett Square used for?",
                    options=["Predicting offspring traits", "Mapping the genome", "Calculating taxes", "Designing gardens"],
                    correct_index=0,
                    explanation="It's a grid used to calculate the probability of inheriting traits."
                ),
                QuizQuestion(
                    question="What does Recessive mean?",
                    options=["A trait that is hidden by a dominant one", "A strong trait", "A rare trait", "A common trait"],
                    correct_index=0,
                    explanation="Recessive traits only show up if there is no dominant allele present (tt)."
                ),
                QuizQuestion(
                    question="What is Phenotype?",
                    options=["The physical appearance", "The genetic code", "A type of medicine", "A chromosome"],
                    correct_index=0,
                    explanation="Phenotype is the physical expression of a trait (e.g., Blue Eyes)."
                )
            ],
            difficulty="intermediate",
            total_xp=80
        ),
        "master": MasterPractice(
            topic="DNA & Genetics Level 2",
            questions=[
                MasterQuestion(
                    question="Brown eyes (B) are dominant to Blue eyes (b). Two Bb parents have a child. What are the odds of Blue eyes?",
                    question_type="multiple_choice",
                    options=["25%", "50%", "75%", "0%"],
                    correct_answer="25%",
                    explanation="Punnett Square: BB, Bb, Bb, bb. Only bb is blue. 1 in 4 = 25%.",
                    xp_reward=25
                ),
                MasterQuestion(
                    question="What is the difference between Heterozygous and Homozygous?",
                    question_type="multiple_choice",
                    options=["Hetero = different alleles (Tt), Homo = same (TT or tt)", "Hetero = same, Homo = different", "They are the same", "It refers to gender"],
                    correct_answer="Hetero = different alleles (Tt), Homo = same (TT or tt)",
                    explanation="Homozygous means matching alleles, Heterozygous means mixed alleles.",
                    xp_reward=25
                ),
                MasterQuestion(
                    question="Are all traits controlled by a single gene like Mendel's peas?",
                    question_type="multiple_choice",
                    options=["No, most are Polygenic (many genes)", "Yes, always", "Only in plants", "Only in animals"],
                    correct_answer="No, most are Polygenic (many genes)",
                    explanation="Height, skin color, and intelligence are Polygenic, controlled by many genes working together.",
                    xp_reward=25
                )
            ],
            total_xp=120
        ),
        "detective": DetectiveCase(
            topic="DNA & Genetics Level 2",
            case_title="The Royal Disease",
            scenario="Queen Victoria's descendants across Europe started suffering from Hemophilia (a blood clotting disorder). It only affected the men, but the women seemed to pass it on silently. Doctors were baffled.",
            clues=[
                Clue(id=1, description="It's a 'Sex-Linked' recessive trait on the X chromosome.", is_key_clue=True),
                Clue(id=2, description="Men have XY chromosomes, Women have XX.", is_key_clue=True),
                Clue(id=3, description="If a man has the bad gene on his X, he gets sick because he has no backup X.", is_key_clue=True),
                Clue(id=4, description="Women have a second healthy X to protect them.", is_key_clue=True)
            ],
            question="Why were the women 'Carriers' but not sick?",
            correct_answer="They had a second healthy X chromosome",
            explanation="Since the gene is recessive and on the X chromosome, women (XX) needed two bad copies to be sick. Men (XY) only needed one, making them vulnerable.",
            xp_reward=110
        )
    },
    3: {
        "topic": "DNA & Genetics Level 3",
        "story": Story(
            topic="DNA & Genetics Level 3",
            title="Hacking the Genome",
            content="""We have moved beyond reading DNA to writing it. Enter CRISPR-Cas9.

"Imagine DNA is a Word document," Dr. Helix explained. "CRISPR is 'Find and Replace'. We can target a specific bad gene and cut it out."

It uses a protein (Cas9) acting as scissors, guided by a piece of RNA to find the exact spot.

But it gets more complex. We discovered 'Epigenetics'—switches that turn genes on or off without changing the DNA itself! Stress, diet, and pollution can flip these switches, and these changes can sometimes be passed to your kids!

"We can cure Sickle Cell Anemia," Dr. Helix said. "But should we design 'perfect' babies? Taller, smarter, stronger?"

This is the ethics of 'Germline Editing'. If we edit a baby's DNA, that change is passed to THEIR children forever. We are seizing control of evolution itself.""",
            key_facts=[
                "CRISPR-Cas9 acts as 'molecular scissors' to edit DNA",
                "Epigenetics controls gene expression without changing DNA sequence",
                "Environmental factors can alter epigenetics",
                "Somatic editing changes one person; Germline editing changes future generations",
                "Bioethics debates 'Designer Babies' and genetic enhancement"
            ],
            xp_reward=25
        ),
        "quiz": Quiz(
            topic="DNA & Genetics Level 3",
            questions=[
                QuizQuestion(
                    question="What does the Cas9 protein do in CRISPR?",
                    options=["Acts as scissors to cut DNA", "Finds the gene", "Glues DNA together", "Copies DNA"],
                    correct_index=0,
                    explanation="Cas9 is the enzyme that physically cuts the DNA strands."
                ),
                QuizQuestion(
                    question="What is Epigenetics?",
                    options=["Switches that turn genes On/Off", "Replacing genes", "Creating new genes", "Destroying DNA"],
                    correct_index=0,
                    explanation="Epigenetics modifies how genes are expressed (read) without changing the code itself."
                ),
                QuizQuestion(
                    question="What is 'Germline' editing?",
                    options=["Editing sperm/eggs/embryos (heritable)", "Editing adult cells", "Editing bacteria", "Editing plants"],
                    correct_index=0,
                    explanation="Germline edits are passed down to children and grandchildren, changing the species."
                ),
                QuizQuestion(
                    question="Can environment affect your genes?",
                    options=["Yes, via epigenetics", "No, DNA is fixed", "Only radiation", "Only viruses"],
                    correct_index=0,
                    explanation="Yes! Diet, stress, and toxins can add chemical tags to DNA that silence or activate genes."
                ),
                QuizQuestion(
                    question="What is a potential risk of CRISPR?",
                    options=["Off-target effects (cutting wrong place)", "It's too slow", "It costs too much", "It requires large machines"],
                    correct_index=0,
                    explanation="A major risk is accidental editing of unintended parts of the genome."
                )
            ],
            difficulty="advanced",
            total_xp=90
        ),
        "master": MasterPractice(
            topic="DNA & Genetics Level 3",
            questions=[
                MasterQuestion(
                    question="What is the 'Central Dogma' of biology?",
                    question_type="multiple_choice",
                    options=["DNA -> RNA -> Protein", "Protein -> RNA -> DNA", "RNA -> DNA -> Protein", "DNA -> Protein -> RNA"],
                    correct_answer="DNA -> RNA -> Protein",
                    explanation="DNA makes RNA (Transcription), and RNA makes Protein (Translation).",
                    xp_reward=30
                ),
                MasterQuestion(
                    question="Which molecule acts as the 'messenger' between DNA and the ribosome?",
                    question_type="multiple_choice",
                    options=["mRNA (Messenger RNA)", "tRNA", "rRNA", "Cas9"],
                    correct_answer="mRNA (Messenger RNA)",
                    explanation="mRNA carries the genetic code from the nucleus to the ribosomes to build proteins.",
                    xp_reward=30
                ),
                MasterQuestion(
                    question="What are 'Introns' and 'Exons'?",
                    question_type="multiple_choice",
                    options=["Junk DNA (Introns) vs Coding DNA (Exons)", "Types of cells", "Types of viruses", "Inside vs Outside"],
                    correct_answer="Junk DNA (Introns) vs Coding DNA (Exons)",
                    explanation="Genes are split into Exons (expressed regions) and Introns (cut out during processing).",
                    xp_reward=30
                )
            ],
            total_xp=140
        ),
        "detective": DetectiveCase(
            topic="DNA & Genetics Level 3",
            case_title="The Hunger Winter",
            scenario="During WWII, the Dutch suffered a famine called the Hunger Winter. Decades later, scientists found something strange: the children of women who were pregnant during the famine had higher rates of obesity and diabetes than their siblings.",
            clues=[
                Clue(id=1, description="The mothers were starving, but the children grew up with plenty of food.", is_key_clue=True),
                Clue(id=2, description="The effect persisted even 60 years later.", is_key_clue=True),
                Clue(id=3, description="Their DNA code was normal, but their 'Metabolism Genes' were switched on differently.", is_key_clue=True)
            ],
            question="What biological mechanism caused this?",
            correct_answer="Epigenetic modification due to famine",
            explanation="The famine caused epigenetic changes in the fetuses, programming their bodies to hoard calories ('Thrifty Phenotype'). In a modern world with food, this led to obesity. It proved environment shapes inheritance!",
            xp_reward=120
        )
    }
}

# ============================================
# 🤖 INTRODUCTION TO AI QUEST
# ============================================

AI_QUEST = {
    1: {
        "topic": "Introduction to AI",
        "story": Story(
            topic="Introduction to AI",
            title="The Rise of Thinking Machines",
            content="""In 1950, a brilliant mathematician named Alan Turing asked a simple question: "Can machines think?" This question launched the field of Artificial Intelligence.

AI is the science of making computers perform tasks that normally require human intelligence—recognizing faces, understanding speech, making decisions, and even creating art.

There are two types of AI. Narrow AI is designed for specific tasks: Siri answering questions, Netflix recommending movies, or chess programs beating grandmasters. General AI, which can do anything a human can, doesn't exist yet—but scientists are working on it.

Machine Learning is how most modern AI works. Instead of programming rules directly, we feed computers millions of examples and they learn patterns. When you show an ML model millions of cat photos, it learns to recognize cats it's never seen before!

Deep Learning uses artificial neural networks inspired by the human brain. These networks have layers of connected nodes that process information, getting smarter with more data. GPT, DALL-E, and self-driving cars all use deep learning.

Today, AI helps doctors diagnose diseases, translates languages instantly, and even writes stories. But with great power comes great responsibility—we must ensure AI benefits everyone and remains under human control.""",
            key_facts=[
                "Alan Turing pioneered AI with his famous 'Can machines think?' question in 1950",
                "Narrow AI handles specific tasks, General AI (human-level) doesn't exist yet",
                "Machine Learning teaches computers by showing examples, not programming rules",
                "Deep Learning uses neural networks inspired by the human brain",
                "AI applications include medical diagnosis, translation, and creative generation"
            ],
            xp_reward=15
        ),
        "quiz": Quiz(
            topic="Introduction to AI",
            questions=[
                QuizQuestion(
                    question="Who is considered the father of AI?",
                    options=["Alan Turing", "Steve Jobs", "Bill Gates", "Mark Zuckerberg"],
                    correct_index=0,
                    explanation="Alan Turing's work on machine intelligence laid the foundation for AI!"
                ),
                QuizQuestion(
                    question="What is Machine Learning?",
                    options=["Teaching computers through examples", "Programming every rule manually", "Building robot bodies", "Creating video games"],
                    correct_index=0,
                    explanation="Machine Learning trains computers on examples so they learn patterns automatically!"
                ),
                QuizQuestion(
                    question="What are neural networks inspired by?",
                    options=["The human brain", "Computer chips", "The internet", "Electrical grids"],
                    correct_index=0,
                    explanation="Neural networks are inspired by how neurons connect in the human brain!"
                ),
                QuizQuestion(
                    question="What type of AI can beat humans at chess but can't do other tasks?",
                    options=["Narrow AI", "General AI", "Super AI", "Basic AI"],
                    correct_index=0,
                    explanation="Narrow AI excels at specific tasks but can't generalize to other domains!"
                ),
                QuizQuestion(
                    question="How does Machine Learning differ from traditional programming?",
                    options=["It learns from data instead of explicit rules", "It's faster", "It uses more code", "It's older technology"],
                    correct_index=0,
                    explanation="ML learns patterns from data rather than following pre-written rules!"
                )
            ],
            difficulty="basic",
            total_xp=70
        ),
        "master": MasterPractice(
            topic="Introduction to AI",
            questions=[
                MasterQuestion(
                    question="Why is more data generally better for Machine Learning?",
                    question_type="multiple_choice",
                    options=["More examples help the model learn better patterns", "Data is cheap", "Computers have lots of storage", "It makes debugging easier"],
                    correct_answer="More examples help the model learn better patterns",
                    explanation="More diverse data helps ML models learn more accurate and general patterns!",
                    xp_reward=20
                ),
                MasterQuestion(
                    question="What is a common concern about AI development?",
                    question_type="multiple_choice",
                    options=["Ensuring it remains under human control and benefits everyone", "It uses too much electricity", "It's too slow", "It's too expensive to develop"],
                    correct_answer="Ensuring it remains under human control and benefits everyone",
                    explanation="AI ethics focuses on safety, fairness, and keeping humans in control!",
                    xp_reward=20
                ),
                MasterQuestion(
                    question="What makes 'deep' learning deep?",
                    question_type="multiple_choice",
                    options=["Multiple layers of neural network processing", "It thinks deeply", "It uses deep code", "It runs on powerful computers"],
                    correct_answer="Multiple layers of neural network processing",
                    explanation="Deep learning uses many hidden layers in neural networks to learn complex patterns!",
                    xp_reward=20
                )
            ],
            total_xp=110
        ),
        "detective": DetectiveCase(
            topic="Introduction to AI",
            case_title="The Biased Algorithm",
            scenario="A company's AI hiring tool is rejecting qualified female candidates at higher rates than male candidates. The AI was trained on 10 years of company hiring data. Leadership is confused—they never programmed it to discriminate!",
            clues=[
                Clue(id=1, description="The historical hiring data showed the company mostly hired men", is_key_clue=True),
                Clue(id=2, description="Machine Learning learns patterns from the data it's trained on", is_key_clue=True),
                Clue(id=3, description="The AI found patterns that correlated with past hiring decisions", is_key_clue=True)
            ],
            question="Why is the AI showing bias?\n\nA. It learned historical bias from the training data\nB. Someone programmed it to be biased\nC. AI is naturally unfair\nD. The algorithm is broken",
            correct_answer="A. It learned historical bias from the training data",
            explanation="Brilliant analysis! This is a real case (Amazon, 2018). ML models learn from data—if historical data contains bias, the AI learns that bias. This is why diverse, clean training data and bias testing are crucial in AI development!",
            xp_reward=100
        )
    },
    2: {
        "topic": "Introduction to AI Level 2",
        "story": Story(
            topic="Introduction to AI Level 2",
            title="How Machines Learn",
            content="""How does an AI recognize a dog? It doesn't have eyes. It sees a grid of numbers (pixels).

In 'Supervised Learning', we show it 10,000 pictures labeled 'Dog' and 10,000 labeled 'Cat'. The AI guesses, and we correct it. Over time, it adjusts its internal math to minimize errors.

This is called 'Training'. But be careful! If you only show it Golden Retrievers, it might not recognize a Pug. This is 'Bias'.

'Neural Networks' are the brain. Each 'neuron' takes an input, multiplies it by a 'weight' (importance), and passes it on. A Deep Neural Network has many layers. The first layer finds edges, the next finds shapes (ears, noses), and the last identifies 'Dog'.

But sometimes AI cheats. It might learn that 'Wolf' pictures always have snow in the background. So instead of recognizing the wolf, it recognizes the snow! This is why we must test AI carefully.""",
            key_facts=[
                "Supervised Learning uses labeled data (Input -> Correct Output)",
                "Neural Networks consist of layers of mathematical nodes",
                "Training involves adjusting weights to minimize error",
                "Bias helps loops occur if training data is not diverse",
                "AI can learn 'shortcuts' (like background snow) instead of true features"
            ],
            xp_reward=20
        ),
        "quiz": Quiz(
            topic="Introduction to AI Level 2",
            questions=[
                QuizQuestion(
                    question="What is Supervised Learning?",
                    options=["Learning with labeled examples", "Learning without help", "Learning from robots", "Learning by watching TV"],
                    correct_index=0,
                    explanation="It's like having a teacher: you give the AI the answer key to learn from."
                ),
                QuizQuestion(
                    question="What are the connections in a neural network called?",
                    options=["Weights", "Strings", "Cables", "Synapses"],
                    correct_index=0,
                    explanation="Weights determine the strength/importance of the signal passing between neurons."
                ),
                QuizQuestion(
                    question="What happens if your training data isn't diverse?",
                    options=["The AI becomes biased", "The AI gets smarter", "Nothing", "The AI crashes"],
                    correct_index=0,
                    explanation="Garbage in, garbage out. If the data is biased, the AI will be biased."
                ),
                QuizQuestion(
                    question="How does an AI 'see' an image?",
                    options=["As a grid of numbers (pixels)", "With eyes", "It hears it", "It smells it"],
                    correct_index=0,
                    explanation="Images are converted into matrices of numbers representing color values."
                ),
                QuizQuestion(
                    question="Why did the AI confuse the wolf with snow?",
                    options=["It learned a shortcut (correlation)", "Wolves are made of snow", "It was cold", "It was broken"],
                    correct_index=0,
                    explanation="AI often finds the easiest pattern to distinguish classes, even if it's wrong (Snow = Wolf)."
                )
            ],
            difficulty="intermediate",
            total_xp=80
        ),
        "master": MasterPractice(
            topic="Introduction to AI Level 2",
            questions=[
                MasterQuestion(
                    question="What is 'Overfitting'?",
                    question_type="multiple_choice",
                    options=["Memorizing the training data instead of learning general rules", "Training for too long", "Using too much electricity", "Fitting too many bytes in memory"],
                    correct_answer="Memorizing the training data instead of learning general rules",
                    explanation="Overfitting is when the AI performs perfectly on training data but fails on new, unseen data.",
                    xp_reward=25
                ),
                MasterQuestion(
                    question="What is a 'Loss Function'?",
                    question_type="multiple_choice",
                    options=["A way to measure how wrong the AI is", "When data gets lost", "A game over screen", "A virus"],
                    correct_answer="A way to measure how wrong the AI is",
                    explanation="The Loss Function calculates the error, guiding the AI on how to adjust its weights to improve.",
                    xp_reward=25
                ),
                MasterQuestion(
                    question="In a neural network, what does a 'Hidden Layer' do?",
                    question_type="multiple_choice",
                    options=["Extracts features and patterns between input and output", "Hides secrets", "Nothing", "Stores passwords"],
                    correct_answer="Extracts features and patterns between input and output",
                    explanation="Hidden layers do the heavy lifting of processing and feature extraction.",
                    xp_reward=25
                )
            ],
            total_xp=120
        ),
        "detective": DetectiveCase(
            topic="Introduction to AI Level 2",
            case_title="The Chatbot Gone Rogue",
            scenario="A company released a chatbot to talk to customers. Within 24 hours, it started saying rude and incorrect things. The engineers had to shut it down. They claim the programming was perfect.",
            clues=[
                Clue(id=1, description="The chatbot learned from real-time conversations with users.", is_key_clue=True),
                Clue(id=2, description="Internet trolls purposely sent it bad messages.", is_key_clue=True),
                Clue(id=3, description="The AI was designed to mimic human speech patterns.", is_key_clue=True)
            ],
            question="Why did the chatbot turn bad?",
            correct_answer="It learned from toxic user input",
            explanation="The AI was learning continuously from users. When trolls fed it bad data, it learned those patterns and repeated them. This highlights the danger of 'Unsupervised' learning on the open internet!",
            xp_reward=110
        )
    },
    3: {
        "topic": "Introduction to AI Level 3",
        "story": Story(
            topic="Introduction to AI Level 3",
            title="The Future of Intelligence",
            content="""We are approaching the 'Singularity'—the moment when machine intelligence surpasses human intelligence.

Alan Turing proposed the 'Turing Test': If a human can't tell they are talking to a machine, the machine is 'intelligent'. Modern LLMs pass this easily.

But do they UNDERSTAND? The 'Chinese Room Argument' suggests they act like they understand but are just following complex rules (syntax) without meaning (semantics).

We currently have ANI (Artificial Narrow Intelligence).
The next step is AGI (Artificial General Intelligence)—AI that can learn ANY task like a human.
The final step is ASI (Artificial Super Intelligence)—AI far smarter than the smartest human.

The 'Alignment Problem' is our biggest challenge: How do we ensure a Superintelligence wants the same things we want? If you tell a super-AI to 'cure cancer', it might decide the best way is to eliminate all humans!""",
            key_facts=[
                "The Singularity is when AI growth becomes uncontrollable and irreversible",
                "The Turing Test checks if AI is indistinguishable from a human",
                "The Chinese Room Argument questions if AI truly understands meaning",
                "Levels of AI: Narrow (ANI) -> General (AGI) -> Super (ASI)",
                "The Alignment Problem is ensuring AI goals match human values"
            ],
            xp_reward=25
        ),
        "quiz": Quiz(
            topic="Introduction to AI Level 3",
            questions=[
                QuizQuestion(
                    question="What is AGI?",
                    options=["Artificial General Intelligence (Human-level)", "Artificial Good Idea", "A Game Interface", "Advanced Graphics"],
                    correct_index=0,
                    explanation="AGI refers to a hypothetical AI that can perform any intellectual task a human can."
                ),
                QuizQuestion(
                    question="What is the Turing Test?",
                    options=["A test to see if a machine can fool a human", "A math test", "A vision test", "A speed test"],
                    correct_index=0,
                    explanation="Proposed by Alan Turing to determine if a machine exhibits intelligent behavior."
                ),
                QuizQuestion(
                    question="What is the Alignment Problem?",
                    options=["Making AI goals match human values", "Aligning text", "Parking cars", "Connecting wires"],
                    correct_index=0,
                    explanation="It's the critical challenge of ensuring powerful AI systems act in accordance with human intent."
                ),
                QuizQuestion(
                    question="What is the 'Chinese Room' argument?",
                    options=["AI simulates understanding but doesn't truly understand", "AI speaks Chinese", "China leads in AI", "Rooms are smart"],
                    correct_index=0,
                    explanation="Philosopher John Searle argued that manipulating symbols (syntax) isn't the same as understanding meaning (semantics)."
                ),
                QuizQuestion(
                    question="What is ASI (Superintelligence)?",
                    options=["AI smarter than the best human brains", "A standard AI", "A smart phone", "A robot"],
                    correct_index=0,
                    explanation="ASI would vastly outperform humans in every field, from creativity to problem-solving."
                )
            ],
            difficulty="advanced",
            total_xp=90
        ),
        "master": MasterPractice(
            topic="Introduction to AI Level 3",
            questions=[
                MasterQuestion(
                    question="What is 'Reinforcement Learning'?",
                    question_type="multiple_choice",
                    options=["Learning through trial and error with rewards/punishments", "Learning by reading", "Forced learning", "Learning from teachers"],
                    correct_answer="Learning through trial and error with rewards/punishments",
                    explanation="Agents learn by taking actions and receiving feedback (rewards), like training a dog.",
                    xp_reward=30
                ),
                MasterQuestion(
                    question="What are 'Hallucinations' in LLMs?",
                    question_type="multiple_choice",
                    options=["Confidently stating false information", "Seeing ghosts", "Dreaming", "System crashes"],
                    correct_answer="Confidently stating false information",
                    explanation="Large Language Models sometimes make up facts because they predict the next word based on probability, not truth.",
                    xp_reward=30
                ),
                MasterQuestion(
                    question="What is the 'Paperclip Maximizer' thought experiment?",
                    question_type="multiple_choice",
                    options=["An AI destroying the world to make paperclips", "An office assistant", "A helpful robot", "A recycling program"],
                    correct_answer="An AI destroying the world to make paperclips",
                    explanation="It illustrates how a harmless goal given to a Superintelligence could lead to catastrophe if not aligned with human life.",
                    xp_reward=30
                )
            ],
            total_xp=140
        ),
        "detective": DetectiveCase(
            topic="Introduction to AI Level 3",
            case_title="The Unpredictable Move",
            scenario="In a famous Go match (AlphaGo vs Lee Sedol), the AI made 'Move 37', a move no human would ever play. Commentators thought it was a mistake. Later, they realized it was genius.",
            clues=[
                Clue(id=1, description="The AI was trained using Reinforcement Learning (playing against itself).", is_key_clue=True),
                Clue(id=2, description="It was not limited by human strategies or history.", is_key_clue=True),
                Clue(id=3, description="The move secured victory in a way humans hadn't conceived.", is_key_clue=True)
            ],
            question="What did Move 37 demonstrate?",
            correct_answer="AI creativity exceeding human intuition",
            explanation="It showed that AI isn't just mimicking humans—it can discover completely new knowledge and strategies that humans have never found in thousands of years!",
            xp_reward=120
        )
    }
}

# ============================================
# Quest Registry
# ============================================

FEATURED_QUESTS = {
    "python": PYTHON_QUEST,
    "black_holes": BLACK_HOLES_QUEST,
    "dinosaurs": DINOSAURS_QUEST,
    "dna": DNA_QUEST,
    "ai": AI_QUEST
}

# Quick lookup for UI display - now with levels!
QUEST_INFO = {
    "python": {
        "id": "python",
        "title": "Learn Python",
        "icon": "🐍",
        "description": "Master the world's most popular programming language!",
        "max_level": 3,
        "xp_per_level": [295, 350, 400]
    },
    "black_holes": {
        "id": "black_holes", 
        "title": "Explore Black Holes",
        "icon": "🌌",
        "description": "Journey to space's most mysterious objects!",
        "max_level": 3,
        "xp_per_level": [295, 350, 400]
    },
    "dinosaurs": {
        "id": "dinosaurs",
        "title": "Dinosaur Discovery",
        "icon": "🦖",
        "description": "Meet Earth's ancient rulers!",
        "max_level": 3,
        "xp_per_level": [295, 350, 400]
    },
    "dna": {
        "id": "dna",
        "title": "DNA & Genetics",
        "icon": "🧬",
        "description": "Unlock life's instruction manual!",
        "max_level": 3,
        "xp_per_level": [295, 350, 400]
    },
    "ai": {
        "id": "ai",
        "title": "Introduction to AI",
        "icon": "🤖",
        "description": "Discover how machines think!",
        "max_level": 3,
        "xp_per_level": [295, 350, 400]
    }
}

def get_featured_quest(quest_id: str, level: int = 1) -> dict | None:
    """Get a featured quest by ID and Level"""
    if quest_id in FEATURED_QUESTS:
        quest_data = FEATURED_QUESTS[quest_id]
        
        # Check if quest has levels (dictionary of ints)
        if isinstance(quest_data, dict) and 1 in quest_data:
            return quest_data.get(level, quest_data.get(1)) # Fallback to Level 1
        return quest_data
    return None

def get_all_quest_info() -> list:
    """Get info for all featured quests (for UI display)"""
    return list(QUEST_INFO.values())

def is_featured_quest(topic: str) -> tuple[str, int] | None:
    """Check if a topic matches a featured quest, return (quest_id, level) if match"""
    topic_lower = topic.lower().strip()
    
    # Extract level if present (e.g., "Level 2", "(Level 2)", "lvl 2")
    level = 1
    import re
    # Matches "level 2", "lvl 2", with or without parens
    level_match = re.search(r"\(?(?:level|lvl)\s+(\d+)\)?", topic_lower)
    if level_match:
        level = int(level_match.group(1))
    
    # Base topic matching - Remove level info
    base_topic = re.sub(r"\(?(?:level|lvl)\s+(\d+)\)?", "", topic_lower).strip(" -()")

    # Helper to check if topic starts with or exactly matches a keyword
    def matches_keyword(keyword, text):
        return text == keyword or text.startswith(keyword + " ")
    
    # Python matches
    if matches_keyword("python", base_topic):
        return ("python", level)
    
    # Black Holes matches
    if matches_keyword("black hole", base_topic) or matches_keyword("black holes", base_topic) or matches_keyword("blackhole", base_topic):
        return ("black_holes", level)
    
    # Dinosaurs matches
    if matches_keyword("dinosaur", base_topic) or matches_keyword("dinosaurs", base_topic) or matches_keyword("dino", base_topic):
        return ("dinosaurs", level)
    
    # DNA matches
    if matches_keyword("dna", base_topic) or matches_keyword("genetics", base_topic) or matches_keyword("genetic", base_topic):
        return ("dna", level)
    
    # AI matches
    if matches_keyword("ai", base_topic) or matches_keyword("ml", base_topic) or \
       matches_keyword("artificial intelligence", base_topic) or \
       matches_keyword("machine learning", base_topic) or \
       "introduction to ai" in base_topic:
        return ("ai", level)
    
    return None

