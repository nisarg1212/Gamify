"""Pre-built Learning Quests - Guaranteed to work without API calls!"""

from gamification.models import Story, Quiz, QuizQuestion, MasterPractice, MasterQuestion, DetectiveCase, Clue

# ============================================
# 🐍 LEARN PYTHON QUEST
# ============================================

PYTHON_QUEST = {
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
        case_title="The Case of the Broken Loop",
        scenario="Junior developer Sam's code isn't working! They wrote a loop to print numbers 1 to 5, but nothing appears on screen. Here's their code:\n\n```python\nfor i in range(5):\n    print(i)\n```\n\nSam says 'It should print 1, 2, 3, 4, 5!' but the output shows 0, 1, 2, 3, 4 instead.",
        clues=[
            Clue(id=1, description="range(5) generates numbers starting from 0", is_key_clue=True),
            Clue(id=2, description="range(start, stop) can specify a starting number", is_key_clue=True),
            Clue(id=3, description="The stop value in range() is exclusive (not included)", is_key_clue=True)
        ],
        question="What should Sam change to print 1, 2, 3, 4, 5?\n\nA. range(1, 6)\nB. range(1, 5)\nC. range(0, 5)\nD. range(5, 1)",
        correct_answer="range(1, 6)",
        explanation="range(1, 6) starts at 1 and stops before 6, giving us 1, 2, 3, 4, 5! Remember: the stop value is exclusive.",
        xp_reward=100
    )
}

# ============================================
# 🌌 BLACK HOLES QUEST
# ============================================

BLACK_HOLES_QUEST = {
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
        correct_answer="Sagittarius A* (supermassive black hole)",
        explanation="You solved it! This describes the star S2 orbiting Sagittarius A*, the supermassive black hole at our galaxy's center. This discovery helped prove Einstein's theories!",
        xp_reward=100
    )
}

# ============================================
# 🦖 DINOSAUR DISCOVERY QUEST
# ============================================

DINOSAURS_QUEST = {
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
        correct_answer="Many dinosaurs had feathers, including T. rex relatives",
        explanation="Brilliant deduction! Fossilized feathers prove many theropods had feathers. Even T. rex may have had feathers as a juvenile! This links dinosaurs directly to modern birds.",
        xp_reward=100
    )
}

# ============================================
# 🧬 DNA & GENETICS QUEST
# ============================================

DNA_QUEST = {
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
        correct_answer="Genes strongly influence personality and preferences",
        explanation="Excellent deduction! Twin studies prove that DNA significantly influences personality, interests, and even the types of people we're attracted to. While environment matters, our genes provide a powerful blueprint!",
        xp_reward=100
    )
}

# ============================================
# 🤖 INTRODUCTION TO AI QUEST
# ============================================

AI_QUEST = {
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
        correct_answer="It learned historical bias from the training data",
        explanation="Brilliant analysis! This is a real case (Amazon, 2018). ML models learn from data—if historical data contains bias, the AI learns that bias. This is why diverse, clean training data and bias testing are crucial in AI development!",
        xp_reward=100
    )
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

def get_featured_quest(quest_id: str) -> dict | None:
    """Get a featured quest by ID"""
    if quest_id in FEATURED_QUESTS:
        return FEATURED_QUESTS[quest_id]
    return None

def get_all_quest_info() -> list:
    """Get info for all featured quests (for UI display)"""
    return list(QUEST_INFO.values())

def is_featured_quest(topic: str) -> str | None:
    """Check if a topic matches a featured quest, return quest_id if match"""
    topic_lower = topic.lower().strip()
    
    # Python matches
    if "python" in topic_lower:
        return "python"
    
    # Black Holes matches (including "Explore Black Holes" from featured cards)
    if "black hole" in topic_lower or "blackhole" in topic_lower or "explore black" in topic_lower:
        return "black_holes"
    
    # Dinosaurs matches
    if "dinosaur" in topic_lower or "dino" in topic_lower:
        return "dinosaurs"
    
    # DNA matches
    if "dna" in topic_lower or "genetic" in topic_lower:
        return "dna"
    
    # AI matches (including "Introduction to AI" from featured cards)
    if "artificial intelligence" in topic_lower or "machine learning" in topic_lower or "introduction to ai" in topic_lower:
        return "ai"
    if topic_lower in ["ai", "ml"]:
        return "ai"
    
    return None

