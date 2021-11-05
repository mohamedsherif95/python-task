import webbrowser
from random import choice

websites = ['http://www.w3schools.com', 'http://www.google.com', 'http://www.stackoverflow.com',
            'https://github.com', 'https://getbootstrap.com', 'https://regex101.com/',
            'https://www.freecodecamp.org/', 'https://www.linkedin.com/', 'https://www.upwork.com/',
            'https://www.youtube.com/', 'https://www.udemy.com/']

webbrowser.open_new(choice(websites))