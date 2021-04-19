class Alpaca(object):

    # this is the 'database' that you will be dealing with
    # this is a list of items that you would recieve from an
    # API and it is your duty to use this to implement the
    # functions that are specified in this Alpaca Model
    data = [
        {
            'id': 1,
            'name': 'Fred',
            'displayName': 'Fred The Menace',
            'bio': '''I am super athletic, love benching weights.
                In my spare time when I am not gaining muscle,
                I love going to the gym. Other alpaca's want to be me''',
            'age': 21,
            'hobbies': [
                'Gym',
                'Hikes',
                'Running',
                'Talking about my abs'
            ],
            'contact': {
                'phoneNumber': '203-123-0987',
                'email': 'fred@gym.com'
            },
            'sex': 'male'
        },
        {
            'id': 2,
            'name': 'John',
            'displayName': 'John The Artist',
            'bio': '''To draw or not to draw. All are amazed by my paintings and
                come from all around the field to see my canvas. Give me a brush
                and I will draw you the world! And P.S you must be an artist too''',
            'age': 16,
            'hobbies': [
                'Drawing',
                'Looking at the mirror',
                'Painting'
            ],
            'contact': {
                'phoneNumber': '203-432-6543',
                'email': 'john@artist.com'
            },
            'sex': 'male'
        },
        {
            'id': 3,
            'name': 'Fhil',
            'displayName': 'Fhil The Gamer',
            'bio': '''Gaming is in bro's. One vs One me in noughts and crosses
                and then we'll see who is laughing. Casual gamers not welcome.
                What's your APM?''',
            'age': 35,
            'hobbies': [
                'Winning',
                'Boasting',
                'Gaming',
                'Being a bad winner (all the time because I win all the time)'
            ],
            'contact': {
                'email': 'Fhil@gaming.com'
            },
            'sex': 'male'
        },
        {
            'id': 4,
            'name': 'Sonya',
            'displayName': 'Sonya The Politician',
            'bio': '''Politics is the way of life. I travel across the many fields and
                talk many languages. I communicate with Llamas, Pigs, Horses, everything.
                I maintain peace across the many fields and so you should vote for me.
                A vote for me is a fun time.''',
            'age': 19,
            'hobbies': [
                'Tactically kind',
                'Multi-lingual',
                'Nice attire',
                'My mom says I look good'
            ],
            'contact': {
                'email': 'Sonya@politcs.com'
            },
            'sex': 'female'
        },
        {
            'id': 5,
            'name': 'Richard',
            'displayName': 'Richard The Milkman',
            'bio': '''Milk is nice. Calcium is good for the bones. Shoulda woulda udda.''',
            'age': 25,
            'hobbies': [
                'Farming',
                'Milking'
            ],
            'contact': {
                'email': 'richard@milk.com'
            },
            'sex': 'male'
        },
        {
            'id': 6,
            'name': 'George',
            'displayName': 'George The Herder',
            'bio': '''Herding is an art. I like to herd. Herd immunity is the way to go.
                The more you herd, the more you learn. HMU if you wanna be herd ;)''',
            'age': 29,
            'hobbies': [
                'Herding',
                'Training animals',
                'Farming'
            ],
            'contact': {
                'email': 'george@herder.com'
            },
            'sex': 'male'
        },
        {
            'id': 7,
            'name': 'Ronald',
            'displayName': 'Ronald The Girl',
            'bio': '''I am most definitely a girl. I am not a clown and I only date alpaca's that
                are above 5'11 and super athletic. You must be smart and rich.''',
            'age': 19,
            'hobbies': [
                'Beautiful',
                'Bad Alpaca',
                'Looking good'
            ],
            'contact': {
                'email': 'ronald@girl.com'
            },
            'sex': 'female'
        }
    ]
    
    # TODO: Implement constructor for Alpaca Model
    def __init__(self, id, name, display_name, bio, age, hobbies, contact, sex):
        self.id = id
        self.name = name
        self.display_name = display_name
        self.bio = bio
        self.age = age
        self.hobbies = hobbies
        self.contact = contact
        self.sex = sex
    # TODO: Implement get filename
    # WHAT: Method that returns the filename using the name of the alpaca
    # RETURN: The path to the image file
    def get_filename(self):
        return '/assets/%s.png' % (self.name)

    # TODO: Implement get
    # WHAT: Gets the alpaca that matches the name
    # CONDITIONS: If alpaca does not match then returns nothing
    # RETURN: Must return Alpaca Model type (convert to Alpaca object)
    def get(name):
        chosen_alpaca = None
        for alpaca in Alpaca.data:
            if alpaca['name'] == name:
                chosen_alpaca = alpaca
            break
            if chosen_alpaca is None:
                return None
        return Alpaca(chosen_alpaca['id'], chosen_alpaca['name'], chosen_alpaca['displayName'], chosen_alpaca['bio'], chosen_alpaca['age'],chosen_alpaca['hobbies'], chosen_alpaca['contact'], chosen_alpaca['sex'])
    # read
    # TODO: Implement get all
    # WHAT: Gets all the alpacas that match the sex (male, female)
    # CONDITIONS: If sex is not specified then returns all of them!
    # RETURN: Must return Alpaca Model types (convert to Alpaca objects)
    def get_all(age):
        alpacas = []
        for alpaca in Alpaca.data:
            alpaca_age = alpaca['age']
            if age is None or age >= alpaca_age:
                alpacas.append(Alpaca(alpaca['id'],alpaca['name'], alpaca['displayName'], alpaca['bio'], alpaca['age'],alpaca['hobbies'], alpaca['contact'], alpaca['sex']))
        return alpacas
    def get_above(age):
        alpacas = []
        for alpaca in Alpaca.data:
            alpaca_age = alpaca['age']
            if age is None or age < alpaca_age:
                alpacas.append(Alpaca(alpaca['id'],alpaca['name'], alpaca['displayName'], alpaca['bio'], alpaca['age'],alpaca['hobbies'], alpaca['contact'], alpaca['sex']))
        return alpacas
    def get_below(age):
        alpacas = []
        for alpaca in Alpaca.data:
            alpaca_age = alpaca['age']
            if age is None or age >= alpaca_age:
                alpacas.append(Alpaca(alpaca['id'],alpaca['name'], alpaca['displayName'], alpaca['bio'], alpaca['age'],alpaca['hobbies'], alpaca['contact'], alpaca['sex']))
        return alpacas