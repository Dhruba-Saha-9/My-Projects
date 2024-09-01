from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Sample dataset of books with details for 10 authors
books_data = books_data = [
    {
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "genre": "Classic",
        "rating": 4.28,
        "description": "A novel set in the American South during the 1930s.",
    },
    {
        "title": "1984",
        "author": "George Orwell",
        "genre": "Dystopian",
        "rating": 4.16,
        "description": "A dystopian novel about totalitarianism.",
    },
    {
        "title": "Pride and Prejudice",
        "author": "Jane Austen",
        "genre": "Romance",
        "rating": 4.25,
        "description": "A timeless love story.",
    },
    {
        "title": "The Catcher in the Rye",
        "author": "J.D. Salinger",
        "genre": "Coming of Age",
        "rating": 3.81,
        "description": "A coming-of-age novel.",
    },
    {
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "genre": "Classic",
        "rating": 3.91,
        "description": "A classic novel about the American Dream.",
    },
    {
        "title": "Moby-Dick",
        "author": "Herman Melville",
        "genre": "Adventure",
        "rating": 3.48,
        "description": "A tale of obsession and revenge on the high seas.",
    },
    {
        "title": "Brave New World",
        "author": "Aldous Huxley",
        "genre": "Dystopian",
        "rating": 3.98,
        "description": "A dystopian novel about a future society.",
    },
    {
        "title": "The Odyssey",
        "author": "Homer",
        "genre": "Epic Poetry",
        "rating": 3.74,
        "description": "An ancient Greek epic poem about Odysseus' journey home.",
    },
    {
        "title": "Frankenstein",
        "author": "Mary Shelley",
        "genre": "Gothic",
        "rating": 3.78,
        "description": "A classic Gothic novel about the creation of a monster.",
    },
    {
        "title": "The Road",
        "author": "Cormac McCarthy",
        "genre": "Post-Apocalyptic",
        "rating": 3.96,
        "description": "A post-apocalyptic novel about a father and son's journey.",
    },
    {
        "title": "The Picture of Dorian Gray",
        "author": "Oscar Wilde",
        "genre": "Gothic",
        "rating": 4.07,
        "description": "A Gothic novel about a man's portrait that ages while he remains young.",
    },
    {
        "title": "The Martian",
        "author": "Andy Weir",
        "genre": "Science Fiction",
        "rating": 4.40,
        "description": "A science fiction novel about an astronaut stranded on Mars.",
    },
    {
        "title": "The Kite Runner",
        "author": "Khaled Hosseini",
        "genre": "Historical",
        "rating": 4.29,
        "description": "A historical novel set in Afghanistan.",
    },
    {
        "title": "The Hobbit",
        "author": "J.R.R. Tolkien",
        "genre": "Fantasy",
        "rating": 4.26,
        "description": "A classic fantasy adventure.",
    },
    {
        "title": "A Tale of Two Cities",
        "author": "Charles Dickens",
        "genre": "Historical",
        "rating": 3.82,
        "description": "A historical novel set during the French Revolution.",
    },
    {
        "title": "The Alchemist",
        "author": "Paulo Coelho",
        "genre": "Philosophical",
        "rating": 3.85,
        "description": "A philosophical novel about a shepherd's journey.",
    },
    {
        "title": "The Shining",
        "author": "Stephen King",
        "genre": "Horror",
        "rating": 4.20,
        "description": "A horror novel set in an isolated hotel.",
    },
    {
        "title": "The Hunger Games",
        "author": "Suzanne Collins",
        "genre": "Dystopian",
        "rating": 4.10,
        "description": "A dystopian series about survival and rebellion.",
    },
    {
        "title": "The Lord of the Rings",
        "author": "J.R.R. Tolkien",
        "genre": "Fantasy",
        "rating": 4.49,
        "description": "A high fantasy epic.",
    },
    {
        "title": "The Shining",
        "author": "Stephen King",
        "genre": "Horror",
        "rating": 4.18,
        "description": "A horror novel set in an isolated hotel.",
    },
    {
        "title": "Wuthering Heights",
        "author": "Emily Bronte",
        "genre": "Gothic",
        "rating": 3.88,
        "description": "A Gothic novel about love and revenge on the Yorkshire moors.",
    },
    {
        "title": "Crime and Punishment",
        "author": "Fyodor Dostoevsky",
        "genre": "Psychological Thriller",
        "rating": 4.21,
        "description": "A psychological thriller about a young man's descent into madness.",
    },
    {
        "title": "The Road Not Taken",
        "author": "Robert Frost",
        "genre": "Poetry",
        "rating": 4.38,
        "description": "A collection of iconic poems by Robert Frost.",
    },
    {
        "title": "The Time Machine",
        "author": "H.G. Wells",
        "genre": "Science Fiction",
        "rating": 3.88,
        "description": "A science fiction novel about time travel.",
    },
    {
        "title": "The Adventures of Sherlock Holmes",
        "author": "Arthur Conan Doyle",
        "genre": "Mystery",
        "rating": 4.31,
        "description": "A collection of detective stories featuring Sherlock Holmes.",
    },
    {
        "title": "War and Peace",
        "author": "Leo Tolstoy",
        "genre": "Historical",
        "rating": 4.12,
        "description": "An epic novel set during the Napoleonic Wars.",
    },
    {
        "title": "The Da Vinci Code",
        "author": "Dan Brown",
        "genre": "Mystery",
        "rating": 3.83,
        "description": "A mystery-thriller involving symbolism and art history.",
    },
    {
        "title": "The Girl with the Dragon Tattoo",
        "author": "Stieg Larsson",
        "genre": "Mystery",
        "rating": 4.12,
        "description": "A mystery novel featuring a hacker and journalist.",
    },
    {
        "title": "The Hitchhiker's Guide to the Galaxy",
        "author": "Douglas Adams",
        "genre": "Science Fiction",
        "rating": 4.21,
        "description": "A comedic science fiction series.",
    },
    {
        "title": "The Road Less Traveled",
        "author": "M. Scott Peck",
        "genre": "Self-Help",
        "rating": 4.07,
        "description": "A self-help book on personal growth and spiritual development.",
    },
    {
        "title": "The Godfather",
        "author": "Mario Puzo",
        "genre": "Crime",
        "rating": 4.42,
        "description": "A crime novel about the Corleone family.",
    },
    {
        "title": "The Grapes of Wrath",
        "author": "John Steinbeck",
        "genre": "Historical",
        "rating": 3.94,
        "description": "A novel about the Dust Bowl and the Great Depression.",
    },
    {
        "title": "The Little Prince",
        "author": "Antoine de Saint-Exupéry",
        "genre": "Children's",
        "rating": 4.31,
        "description": "A beloved children's book about a young prince's adventures.",
    },
    {
        "title": "The Silent Patient",
        "author": "Alex Michaelides",
        "genre": "Psychological Thriller",
        "rating": 4.05,
        "description": "A psychological thriller about a woman who hasn't spoken in years.",
    },
    {
        "title": "The Nightingale",
        "author": "Kristin Hannah",
        "genre": "Historical",
        "rating": 4.57,
        "description": "A historical novel about two sisters in Nazi-occupied France.",
    },
    {
        "title": "Educated",
        "author": "Tara Westover",
        "genre": "Memoir",
        "rating": 4.50,
        "description": "A memoir about a woman who grows up in a strict and abusive household but escapes to learn about the world.",
    },
    {
        "title": "The Help",
        "author": "Kathryn Stockett",
        "genre": "Historical",
        "rating": 4.47,
        "description": "A historical novel about African American maids in Mississippi during the early 1960s.",
    },
    {
        "title": "The Silent Wife",
        "author": "A.S.A. Harrison",
        "genre": "Psychological Thriller",
        "rating": 3.37,
        "description": "A psychological thriller about a disintegrating marriage.",
    },
    {
        "title": "Introduction to Electrical Engineering",
        "author": "Mulukutla S. Sarma",
        "genre": "Electrical Engineering",
        "rating": 4.2,
        "description": "A comprehensive introduction to electrical engineering principles and applications.",
    },
    {
        "title": "Mechanics of Materials",
        "author": "Russell C. Hibbeler",
        "genre": "Mechanical Engineering",
        "rating": 4.3,
        "description": "A fundamental text on the mechanics of materials and structural analysis.",
    },
    {
        "title": "Fundamentals of Heat and Mass Transfer",
        "author": "Frank P. Incropera and David P. DeWitt",
        "genre": "Thermal Engineering",
        "rating": 4.0,
        "description": "An in-depth study of heat and mass transfer phenomena in engineering.",
    },
    {
        "title": "Fundamentals of Fluid Mechanics",
        "author": "Bruce R. Munson and Theodore H. Okiishi",
        "genre": "Fluid Mechanics",
        "rating": 4.1,
        "description": "A foundational text on fluid mechanics for engineering students.",
    },
    {
        "title": "Structural Analysis",
        "author": "Russell C. Hibbeler",
        "genre": "Civil Engineering",
        "rating": 4.2,
        "description": "A comprehensive guide to structural analysis and design principles.",
    },
    {
        "title": "Engineering Mechanics: Statics",
        "author": "J.L. Meriam and L.G. Kraige",
        "genre": "Mechanical Engineering",
        "rating": 4.0,
        "description": "An essential textbook on engineering mechanics and statics.",
    },
    {
        "title": "Machine Design",
        "author": "Robert L. Norton",
        "genre": "Mechanical Engineering",
        "rating": 4.3,
        "description": "A thorough exploration of machine design and mechanical engineering.",
    },
    {
        "title": "Digital Signal Processing",
        "author": "John G. Proakis and Dimitris G. Manolakis",
        "genre": "Signal Processing",
        "rating": 4.1,
        "description": "A comprehensive guide to digital signal processing techniques.",
    },
    {
        "title": "Control Systems Engineering",
        "author": "Norman S. Nise",
        "genre": "Control Systems",
        "rating": 4.2,
        "description": "A textbook on control systems and their applications in engineering.",
    },
    {
        "title": "Engineering Thermodynamics",
        "author": "Michael J. Moran and Howard N. Shapiro",
        "genre": "Thermodynamics",
        "rating": 4.0,
        "description": "An exploration of thermodynamics and its relevance in engineering.",
    },
    {
        "title": "Introduction to Environmental Engineering",
        "author": "P.Aarne Vesilind and Susan M. Morgan",
        "genre": "Environmental Engineering",
        "rating": 4.1,
        "description": "A foundational text on environmental engineering principles and practices.",
    },
    {
        "title": "Fundamentals of Electric Circuits",
        "author": "Charles K. Alexander and Matthew N. O. Sadiku",
        "genre": "Electrical Engineering",
        "rating": 4.1,
        "description": "An introductory text on electric circuits and circuit analysis.",
    },
    {
        "title": "Fundamentals of Engineering Thermodynamics",
        "author": "Michael J. Moran, Howard N. Shapiro, Daisie D. Boettner, and Margaret B. Bailey",
        "genre": "Thermodynamics",
        "rating": 4.0,
        "description": "An in-depth study of engineering thermodynamics principles.",
    },
    {
        "title": "Introduction to Engineering Ethics",
        "author": "Mike W. Martin and Roland Schinzinger",
        "genre": "Engineering Ethics",
        "rating": 3.9,
        "description": "A guide to ethical issues in engineering and professional responsibility.",
    },
    {
        "title": "Materials Science and Engineering",
        "author": "William D. Callister Jr. and David G. Rethwisch",
        "genre": "Materials Science",
        "rating": 4.2,
        "description": "An exploration of materials science and engineering concepts.",
    },
    {
        "title": "Fundamentals of Heat and Mass Transfer",
        "author": "Theodore L. Bergman, Adrienne S. Lavine, Frank P. Incropera, and David P. DeWitt",
        "genre": "Heat Transfer",
        "rating": 4.0,
        "description": "An in-depth study of heat and mass transfer phenomena in engineering.",
    },
    {
        "title": "Introduction to Control Systems Engineering",
        "author": "Ajit K. Mandal",
        "genre": "Control Systems",
        "rating": 3.8,
        "description": "An introductory text on control systems engineering and analysis.",
    },
    {
        "title": "Introduction to Biomedical Engineering",
        "author": "John Enderle, Susan Blanchard, and Joseph Bronzino",
        "genre": "Biomedical Engineering",
        "rating": 3.9,
        "description": "An introduction to the field of biomedical engineering and its applications.",
    },
    {
        "title": "Introduction to Chemical Engineering",
        "author": "John P. O'Connell, John M. Kresta, and Ruth E. Weinert",
        "genre": "Chemical Engineering",
        "rating": 4.1,
        "description": "An introductory text on chemical engineering principles and processes.",
    },
    {
        "title": "Engineering Mechanics: Dynamics",
        "author": "J.L. Meriam and L.G. Kraige",
        "genre": "Mechanical Engineering",
        "rating": 4.0,
        "description": "A foundational text on engineering mechanics and dynamics.",
    },
    {
        "title": "Engineering Vibrations",
        "author": "William J. Bottega",
        "genre": "Mechanical Engineering",
        "rating": 4.3,
        "description": "A study of vibrations and their applications in engineering.",
    },
    {
        "title": "Introduction to Electrical Engineering",
        "author": "R.G. Carter and D.E. Pearson",
        "genre": "Electrical Engineering",
        "rating": 3.8,
        "description": "An introductory text on electrical engineering principles and applications.",
    },
    {
        "title": "The Night Circus",
        "author": "Erin Morgenstern",
        "genre": "Fantasy",
        "rating": 4.03,
        "description": "A fantasy novel about a magical competition between two young magicians.",
    },
    {
        "title": "The Goldfinch",
        "author": "Donna Tartt",
        "genre": "Literary Fiction",
        "rating": 3.90,
        "description": "A coming-of-age novel about a young boy who survives a terrorist attack at an art museum.",
    },
    {
        "title": "The Glass Castle",
        "author": "Jeannette Walls",
        "genre": "Memoir",
        "rating": 4.26,
        "description": "A memoir about a woman's unconventional and difficult childhood.",
    },
    {
        "title": "Algorithms and Data Structures",
        "author": "Sarah E. Johnson",
        "genre": "Computer Science",
        "rating": 4.6,
        "description": "A comprehensive guide to algorithms and data structures for computer science students and professionals.",
    },
    {
        "title": "Programming in Python",
        "author": "Michael A. Smith",
        "genre": "Computer Science",
        "rating": 4.2,
        "description": "A beginner's guide to programming in Python, with practical examples and exercises.",
    },
    {
        "title": "Artificial Intelligence Unleashed",
        "author": "David R. Anderson",
        "genre": "Computer Science",
        "rating": 4.4,
        "description": "Exploring the world of artificial intelligence and its applications in various fields.",
    },
    {
        "title": "Web Development Mastery",
        "author": "Emily K. Brown",
        "genre": "Computer Science",
        "rating": 4.5,
        "description": "A comprehensive guide to mastering web development technologies and practices.",
    },
    {
        "title": "Cybersecurity Essentials",
        "author": "Jason M. Clark",
        "genre": "Computer Science",
        "rating": 4.3,
        "description": "An essential read for understanding the fundamentals of cybersecurity and protecting digital assets.",
    },
    {
        "title": "Machine Learning Revolution",
        "author": "Lisa H. Roberts",
        "genre": "Computer Science",
        "rating": 4.7,
        "description": "A groundbreaking exploration of machine learning and its impact on technology and society.",
    },
    {
        "title": "Data Science Fundamentals",
        "author": "John D. Taylor",
        "genre": "Computer Science",
        "rating": 4.4,
        "description": "An introduction to the core concepts of data science, including data analysis and visualization.",
    },
    {
        "title": "Blockchain Decoded",
        "author": "Robert G. Wilson",
        "genre": "Computer Science",
        "rating": 4.5,
        "description": "Demystifying blockchain technology and its applications in finance and beyond.",
    },
    {
        "title": "Cloud Computing for Beginners",
        "author": "Laura M. King",
        "genre": "Computer Science",
        "rating": 4.1,
        "description": "A beginner-friendly guide to cloud computing and its role in modern technology.",
    },
    {
        "title": "Software Engineering Principles",
        "author": "Mark A. White",
        "genre": "Computer Science",
        "rating": 4.6,
        "description": "Exploring the principles and best practices of software engineering.",
    },
    {
        "title": "Game Development Masterclass",
        "author": "Ethan P. Gray",
        "genre": "Computer Science",
        "rating": 4.4,
        "description": "A comprehensive guide to mastering the art of game development, from concept to launch.",
    },
    {
        "title": "Big Data Analytics Handbook",
        "author": "Olivia S. Parker",
        "genre": "Computer Science",
        "rating": 4.3,
        "description": "A handbook for harnessing the power of big data for insights and decision-making.",
    },
    {
        "title": "Networking and Internet Protocols",
        "author": "Matthew J. Adams",
        "genre": "Computer Science",
        "rating": 4.2,
        "description": "An in-depth look at networking and internet protocols, including TCP/IP and more.",
    },
    {
        "title": "Human-Computer Interaction Design",
        "author": "Helen R. Lewis",
        "genre": "Computer Science",
        "rating": 4.5,
        "description": "Exploring the principles of designing intuitive and user-friendly computer interfaces.",
    },
    {
        "title": "Quantum Computing Revolution",
        "author": "Daniel W. Turner",
        "genre": "Computer Science",
        "rating": 4.8,
        "description": "A groundbreaking exploration of quantum computing and its potential to transform computing as we know it.",
    },
    {
        "title": "The World of Cyber Threats",
        "author": "Grace E. Mitchell",
        "genre": "Computer Science",
        "rating": 4.3,
        "description": "A comprehensive look at the evolving landscape of cyber threats and how to defend against them.",
    },
    {
        "title": "Compiler Design and Optimization",
        "author": "Brian A. Foster",
        "genre": "Computer Science",
        "rating": 4.6,
        "description": "An in-depth guide to compiler design and optimization techniques for programming languages.",
    },
    {
        "title": "Art of Data Visualization",
        "author": "Sophia L. Turner",
        "genre": "Computer Science",
        "rating": 4.4,
        "description": "Exploring the art and science of data visualization for effective communication of insights.",
    },
    {
        "title": "Computer Graphics Masterclass",
        "author": "Ryan C. Murphy",
        "genre": "Computer Science",
        "rating": 4.7,
        "description": "A comprehensive guide to creating stunning computer graphics and animations.",
    },
    {
        "title": "Ethical Hacking Handbook",
        "author": "Nina S. Johnson",
        "genre": "Computer Science",
        "rating": 4.5,
        "description": "A handbook for understanding ethical hacking techniques and securing digital systems.",
    }

]



@app.route('/')
def index():
    return render_template('index.html')

#@app.route('/get_recommendations', methods=['POST'])
#def get_recommendations():
#    author_name = request.form.get('author_name')
#    genre = request.form.get('genre')
#    min_rating = float(request.form.get('min_rating'))
#
#    recommendations = []
#
#    if author_name:
#        recommendations = [book for book in books_data if book['author'] == author_name]
#    elif genre:
#        recommendations = [book for book in books_data if book['genre'] == genre and book['rating'] >= min_rating]
#
#    return render_template('result.html', recommendations=recommendations)

@app.route('/get_recommendations', methods=['POST'])
def get_recommendations():
    author_name = request.form.get('author_name')
    genre = request.form.get('genre')
    min_rating = request.form.get('min_rating')

    recommendations = []

    for book in books_data:
        if (not author_name or book['author'] == author_name) and \
           (not genre or book['genre'] == genre) and \
           (not min_rating or float(min_rating) <= book['rating']):
            recommendations.append(book)

    return render_template('result.html', recommendations=recommendations)



if __name__ == '__main__':
    app.run(debug=True)
