import spacy  # importing spacy
nlp = spacy.load('en_core_web_md') # specify the model to use

movies = {}
movies_similarity = {}

compared_desc = """Will he save
their world or destroy it? When the Hulk becomes too dangerous for the
Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a
planet where the Hulk can live in peace. Unfortunately, Hulk land on the
planet Sakaar where he is sold into slavery and trained as a gladiator."""

with open("movies.txt", "r", encoding="UTF-8") as file:
    m_file = file.readlines()
    for line in m_file:
        movie_name, desc = line.strip("\n").split(" :")
        movies[movie_name.strip()] = desc.strip()
    
token_1 = nlp(compared_desc)

for key, value in movies.items():
    token_2 = nlp(value)
    sim_value = token_1.similarity(token_2)
    movies_similarity[key]=sim_value
    
    
print("\n-------------Movies similarity--------------- \n")

most_similar_movie = max(zip(movies_similarity.values(), movies_similarity.keys()))[1]
# https://www.geeksforgeeks.org/python-get-key-with-maximum-value-in-dictionary/?ref=lbp

print(f"Based on the last movie you've watched, you may like to see {most_similar_movie}. Enjoy!")
  
    