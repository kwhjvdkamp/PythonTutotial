import pandas as pd

data = {
    'Gender': ['Male', 'Male', 'Male', 'Male', 'Female', 'Male', 'Male', 'Male', 'Male', 'Male', 'Female', 'Male', 'Male', 'Male', 'Female', 'Male', 'Female', 'Male', 'Male', 'Male', 'Male', 'Male', 'Male', 'Male', 'Female', 'Male', 'Male', 'Male', 'Male', 'Male', 'Female', 'Male', 'Male', 'Male', 'Male', 'Female', 'Male', 'Female', 'Female', 'Female', 'Female', 'Male', 'Male', 'Female', 'Male', 'Male', 'Male', 'Female', 'Male', 'Male', 'Male', 'Male', 'Male', 'Male', 'Male', 'Male', 'Male', 'Male', 'Male'], 
    'Eye color': ['blue', 'blue', 'red', 'blue', 'white', 'yellow', 'blue', 'green', 'black', 'red', 'green', 'green', 'blue', 'white', 'red', 'red', 'blue', 'green', 'white', 'red', 'red', 'red', 'blue', 'red', 'yellow', 'blue', 'green', 'green', 'white', 'red', 'blue', 'red', 'red', 'blue', 'red', 'green', 'red', 'yellow', 'blue', 'white', 'green', 'purple', 'yellow', 'black', 'white', 'black', 'white', 'green', 'red', 'red', 'yellow', 'red', 'grey', 'black', 'yellow', 'green', 'gold', 'white', 'brown'],
    'Race': ['IcthyoSapien', 'Ungaran', 'Mutant', 'Mutant', 'Alien', 'Neyaphem', 'Mutant', 'Human', 'Bizarro', 'Demon', 'Mutant', 'Android', 'Human/Radiation', 'Alien', 'Mutant', 'NewGod', 'Human', 'Mutant', 'Human/Cosmic', 'Human/Altered', 'Demon', 'Alien', 'Mutant', 'Kakarantharaian', 'Zen-Whoberian', 'Strontian', 'Human/Radiation', 'Human', 'Android', 'Metahuman', 'Human', 'Bolovaxian', 'Human', 'Mutant', 'Czarnian', 'Human-Kree', 'Martian', 'Mutant', 'Luphomoid', 'Human/Cosmic', 'Human', 'Human', 'Human/Radiation', 'Talokite', 'Alien', 'Korugaran', 'God/Eternal', 'Tamaranean', 'NewGod', 'God/Eternal', 'Mutant', 'Eternal', 'Human', 'Mutant', 'God/Eternal', 'Inhuman', 'Android', 'FrostGiant', 'Yoda\'s species'],
    'Hair color': ['NoHair', 'NoHair', 'Black', 'Blond', 'Orange', 'Black', 'Blue', 'Green', 'Black', 'White', 'Magenta', 'NoHair', 'Silver', 'White', 'White', 'NoHair', 'Black', 'NoHair', 'NoHair', 'NoHair', 'NoHair', 'Black', 'Black', 'NoHair', 'Black', 'Blue', 'Green', 'Green', 'NoHair', 'NoHair', 'Blond', 'NoHair', 'NoHair', 'NoHair', 'Black', 'Black', 'NoHair', 'Orange', 'NoHair', 'Red', 'Red', 'Purple', 'Black', 'Black', 'NoHair', 'Black', 'NoHair', 'Auburn', 'Black', 'NoHair', 'NoHair', 'NoHair', 'NoHair', 'Brown', 'Black', 'NoHair', 'NoHair', 'NoHair', 'White'],
    'Publisher': ['DarkHorseComics', 'DCComics', 'MarvelComics', 'MarvelComics', 'MarvelComics', 'MarvelComics', 'MarvelComics', 'DCComics', 'DCComics', 'MarvelComics', 'MarvelComics', 'DCComics', 'DCComics', 'MarvelComics', 'MarvelComics', 'DCComics', 'MarvelComics', 'IDWPublishing', 'DCComics', 'MarvelComics', 'DCComics', 'MarvelComics', 'MarvelComics', 'MarvelComics', 'MarvelComics', 'MarvelComics', 'MarvelComics', 'DCComics', 'GeorgeLucas', 'DCComics', 'DCComics', 'DCComics', 'MarvelComics', 'IDWPublishing', 'DCComics', 'MarvelComics', 'DCComics', 'MarvelComics', 'MarvelComics', 'MarvelComics', 'DCComics', 'MarvelComics', 'MarvelComics', 'DCComics', 'MarvelComics', 'DCComics', 'DCComics', 'DCComics', 'DCComics', 'DCComics', 'MarvelComics', 'MarvelComics', 'MarvelComics', 'MarvelComics', 'DCComics', 'MarvelComics', 'MarvelComics', 'MarvelComics', 'GeorgeLucas'],
    'Skin color': ['blue', 'red', 'grey', 'blue', 'gold', 'red', 'blue', 'green', 'white', 'white', 'pink', 'green', 'silver', 'grey', 'blue', 'grey', 'white', 'green', 'blue', 'green', 'yellow', 'green', 'red', 'green', 'green', 'purple', 'green', 'white', 'gray', 'green', 'blue', 'pink', 'red', 'green', 'blue-white', 'green', 'green', 'blue', 'blue', 'gold', 'green', 'purple', 'red', 'blue', 'silver', 'red', 'white', 'orange', 'white', 'green', 'yellow', 'purple', 'grey', 'green', 'red', 'green', 'red', 'white', 'green'],
    'Alignment': ['good', 'good', 'bad', 'good', 'good', 'bad', 'good', 'good', 'neutral', 'bad', 'good', 'bad', 'good', 'good', 'neutral', 'bad', 'good', 'good', 'good', 'good', 'neutral', 'bad', 'bad', 'good', 'good', 'neutral', 'good', 'bad', 'good', 'bad', 'bad', 'good', 'bad', 'good', 'neutral', 'good', 'good', 'bad', 'bad', 'good', 'bad', 'bad', 'neutral', 'good', 'good', 'neutral', 'good', 'good', 'bad', 'bad', 'bad', 'bad', 'bad', 'neutral', 'bad', 'good', 'good', 'good', 'good']
}

names = ['AbeSapien', 'AbinSur', 'Apocalypse', 'Archangel', 'Ardina', 'Azazel', 'Beast', 'BeastBoy', 'Bizarro', 'Blackout', 'Blink', 'Brainiac', 'CaptainAtom', 'Century', 'Copycat', 'Darkseid', 'Domino', 'Donatello', 'DrManhattan', 'DraxtheDestroyer', 'Etrigan', 'Evilhawk', 'Exodus', 'FinFangFoom', 'Gamora', 'Gladiator', 'Hulk', 'Joker', 'K-2SO', 'KillerCroc', 'KillerFrost', 'Kilowog', 'Klaw', 'Leonardo', 'Lobo', 'Mantis', 'MartianManhunter', 'Mystique', 'Nebula', 'Nova', 'PoisonIvy', 'PurpleMan', 'RedHulk', 'ShadowLass', 'SilverSurfer', 'Sinestro', 'Spectre', 'Starfire', 'Steppenwolf', 'SwampThing', 'Swarm', 'Thanos', 'TigerShark', 'Toad', 'Trigon', 'Triton', 'Vision', 'Ymir', 'Yoda']

heroes = pd.DataFrame(data, index=names)

print("# ----")
print("Column names: ", heroes.columns)
print("# ----")
print("Count of Columns: ", len(heroes.columns))
print("# ----")
i = 3
print("First rows (", i,"): ", heroes.head(i))
print("# ----")
print("Count of Rows: ", len(heroes.values))
print("# ----")

column_counts = dict()

# Traverse through the columns in the heroes DataFrame
for column_name, series in heroes.iteritems(): 
    # Retrieve the values stored in series in a list form
    values = list(series)
    # print(column_name,": ", values)
    category_counts = dict()  
    # Traverse through unique categories in values
    for category in set(values):
         # Count the appearance of category in values
         category_counts[category] = values.count(category)
    
    column_counts[column_name] = category_counts
    
print(column_counts)