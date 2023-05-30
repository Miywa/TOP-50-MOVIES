# TOP 50
import webbrowser
elokuvat = {
    1:{"nimi": "The Shawshank Redemption", "arvio": 9.3, "ohjaaja": "Frank Darabont", "vuosi": 1994},
    2:{"nimi": "The Godfather", "arvio": 9.2, "ohjaaja": "Francis Ford Coppola", "vuosi": 1972},
    3:{"nimi": "The Dark Knight", "arvio": 9.0, "ohjaaja": "Christopher Nolan", "vuosi": 2008},
    4:{"nimi": "The Godfather Part II", "arvio": 9.0, "ohjaaja": "Francis Ford Coppola", "vuosi": 1974},
    5:{"nimi": "12 Angry Men", "arvio": 9.0, "ohjaaja": "Sidney Lumet", "vuosi": 1957},
    6:{"nimi": "Schindler's List", "arvio": 8.9, "ohjaaja": "Steven Spielberg", "vuosi": 1993},
    7:{"nimi": "The Lord of the Rings: The Return of the King", "arvio": 8.9, "ohjaaja": "Peter Jackson", "vuosi": 2003},
    8:{"nimi": "Pulp Fiction", "arvio": 8.8, "ohjaaja": "Quentin Tarantino", "vuosi": 1994},
    9:{"nimi": "The Lord of the Rings: The Fellowship of the Ring", "arvio": 8.8, "ohjaaja": "Peter Jackson", "vuosi": 2001},
    10:{"nimi": "The Good, the Bad and the Ugly", "arvio": 8.8, "ohjaaja": "Sergio Leone", "vuosi": 1966},
    11:{"nimi": "Forrest Gump", "arvio": 8.8, "ohjaaja": "Robert Zemeckis", "vuosi": 1994},
    12:{"nimi": "Fight Club", "arvio": 8.7, "ohjaaja": "David Fincher", "vuosi": 1999},
    13:{"nimi": "The Lord of the Rings: The Two Towers", "arvio": 8.7, "ohjaaja": "Peter Jackson", "vuosi": 2002},
    14:{"nimi": "Inception", "arvio": 8.7, "ohjaaja": "Christopher Nolan", "vuosi": 2010},
    15:{"nimi": "Star Wars: Episode V - The Empire Strikes Back", "arvio": 8.7, "ohjaaja": "Irvin Kershner", "vuosi": 1980},
    16:{"nimi": "The Matrix", "arvio": 8.7, "ohjaaja": "The Wachowski Brothers", "vuosi": 1999},
    17:{"nimi": "Goodfellas", "arvio": 8.7, "ohjaaja": "Martin Scorsese", "vuosi": 1990},
    18:{"nimi": "One Flew Over the Cuckoo's Nest", "arvio": 8.6, "ohjaaja": "Milos Forman", "vuosi": 1975},
    19:{"nimi": "Se7en", "arvio": 8.6, "ohjaaja": "David Fincher", "vuosi": 1995},
    20:{"nimi": "It's a Wonderful Life", "arvio": 8.6, "ohjaaja": "Frank Capra", "vuosi": 1946},
    21:{"nimi": "Seven Samurai", "arvio": 8.6, "ohjaaja": "Akira Kurosawa", "vuosi": 1954},
    22:{"nimi": "The Silence of the Lambs", "arvio": 8.6, "ohjaaja": "Jonathan Demme", "vuosi": 1991},
    23:{"nimi": "Saving Private Ryan", "arvio": 8.6, "ohjaaja": "Steven Spielberg", "vuosi": 1998},
    24:{"nimi": "City of God", "arvio": 8.6, "ohjaaja": "Fernando Meirelles", "vuosi": 2002},
    25:{"nimi": "Interstellar", "arvio": 8.6, "ohjaaja": "Christopher Nolan", "vuosi": 2014},
    26:{"nimi": "Life Is Beautiful", "arvio": 8.6, "ohjaaja": "Roberto Benigni", "vuosi": 1997},
    27:{"nimi": "The Green Mile", "arvio": 8.5, "ohjaaja": "Frank Darabont", "vuosi": 1999},
    28:{"nimi": "Star Wars: Episode IV - A New Hope", "arvio": 8.5, "ohjaaja": "George Lucas", "vuosi": 1977},
    29:{"nimi": "Terminator 2: Judgement Day", "arvio": 8.5, "ohjaaja": "James Cameron", "vuosi": 1991},
    30:{"nimi": "Back to the Future", "arvio": 8.5, "ohjaaja": "Robert Zemeckis", "vuosi": 1985},
    31:{"nimi": "Spirited Away", "arvio": 8.5, "ohjaaja": "Hayao Miyazaki", "vuosi": 2001},
    32:{"nimi": "The Pianist", "arvio": 8.5, "ohjaaja": "Roman Polanski", "vuosi": 2002},
    33:{"nimi": "Psycho", "arvio": 8.5, "ohjaaja": "Alfred Hitchcock", "vuosi": 1960},
    34:{"nimi": "Parasite", "arvio": 8.5, "ohjaaja": "Bong Joon Ho", "vuosi": 2019},
    35:{"nimi": "Léon: The Professional", "arvio": 8.5, "ohjaaja": "Luc Besson", "vuosi": 1994},
    36:{"nimi": "Gladiator", "arvio": 8.5, "ohjaaja": "Ridley Scott", "vuosi": 2000},
    37:{"nimi": "The Lion King", "arvio": 8.5, "ohjaaja": "Roger Allers", "vuosi": 1994},
    38:{"nimi": "American History X", "arvio": 8.5, "ohjaaja": "Tony Kaye", "vuosi": 1998},
    39:{"nimi": "The Departed", "arvio": 8.5, "ohjaaja": "Martin Scorsese", "vuosi": 2006},
    40:{"nimi": "Whiplash", "arvio": 8.5, "ohjaaja": "Damien Chazelle", "vuosi": 2014},
    41:{"nimi": "The Prestige", "arvio": 8.5, "ohjaaja": "Christopher Nolan", "vuosi": 2006},
    42:{"nimi": "The Usual Suspects", "arvio": 8.5, "ohjaaja": "Bryan Singer", "vuosi": 1995},
    43:{"nimi": "Casablanca", "arvio": 8.5, "ohjaaja": "Michael Curtiz", "vuosi": 1942},
    44:{"nimi": "Grave of the Fireflies", "arvio": 8.5, "ohjaaja": "Isao Takahata", "vuosi": 1988},
    45:{"nimi": "Harakiri", "arvio": 8.5, "ohjaaja": "Masaki Kobayashi", "vuosi": 1962},
    46:{"nimi": "The Intouchables", "arvio": 8.5, "ohjaaja": "Olivier Nakache", "vuosi": 2011},
    47:{"nimi": "Modern Times", "arvio": 8.4, "ohjaaja": "Charles Chaplin", "vuosi": 1936},
    48:{"nimi": "Once Upon a Time in the West", "arvio": 8.4,"ohjaaja": "Sergio Leone", "vuosi": 1968},
    49:{"nimi": "Cinema Paradiso", "arvio": 8.4, "ohjaaja": "Giuseppe Tornatore", "vuosi": 1988},
    50: {"nimi": "Rear Window", "arvio": 8.4, "ohjaaja": "Alfred Hitchcock", "vuosi": 1954}
}

while True:
    luku = int(input("Anna luku 1-50: "))
    
    if luku <= 0:
        print("Listalta ei löydy negatiivisia sijoituksia")
    elif luku <= 50:
        elokuva = elokuvat[luku]
        print(f"Elokuva: {elokuva['nimi']}")
        print(f"Arvio: {elokuva['arvio']}")
        
        lisatieto = input("Haluatko lisätietoa elokuvasta? (Kyllä/Ei): ")
        if lisatieto.lower() == "kyllä":
            print(f"Ohjaaja: {elokuva['ohjaaja']}")
            print(f"Julkaisuvuosi: {elokuva['vuosi']}")
        else:
            print("Kiitos!")
            break
    else:
        link = "https://www.imdb.com/chart/top/"
        print("Lisää elokuvien sijoituksia tästä linkistä:", link)
        break
