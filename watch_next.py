# Importing spacy and loading medium package
import spacy 
nlp = spacy.load('en_core_web_md') 

# Creating empty dictionary to store movies 
# and empty dictionary to store movie similarity to Hulk movie
movies = {}
movies_similarity = {}

# Hulk movie description as a string variable
hulk_movie = """Will he save
their world or destroy it? When the Hulk becomes too dangerous for the
Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a
planet where the Hulk can live in peace. Unfortunately, Hulk land on the
planet Sakaar where he is sold into slavery and trained as a gladiator."""

# This opens movie file in read mode and adds all data to dictionary
with open("movies.txt", "r", encoding="UTF-8") as file:
    m_file = file.readlines()
    for line in m_file:
        movie_name, desc = line.strip("\n").split(" :")
        movies[movie_name.strip()] = desc.strip()

# This assigns nlp model to Hulk movie description    
token_1 = nlp(hulk_movie)

# This checks similarity between Hulk movie and description 
# and movie from list discription, adds to dictionary
for key, value in movies.items():
    token_2 = nlp(value)
    sim_value = token_1.similarity(token_2)
    movies_similarity[key]=sim_value
    
"""Below helped me to understand how to get max value from dictionary
https://www.geeksforgeeks.org/python-get-key-with-maximum-value-in-dictionary/
"""

# This finds the most similar movie to the hulk movie and prints name
most_similar_movie = max(zip(movies_similarity.values(), 
                             movies_similarity.keys()))[1]
print("Based on the last movie you've watched, "
      f"you may like to see {most_similar_movie}. Enjoy!")
    
