# TOP 50
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
    19:{"nimi": "One Flew Over the Cuckoo's Nest", "arvio": 8.6, "ohjaaja": "Milos Forman", "vuosi": 1975},
    20:{"nimi": "One Flew Over the Cuckoo's Nest", "arvio": 8.6, "ohjaaja": "Milos Forman", "vuosi": 1975},
    21:{"nimi": "One Flew Over the Cuckoo's Nest", "arvio": 8.6, "ohjaaja": "Milos Forman", "vuosi": 1975},
    22:{"nimi": "One Flew Over the Cuckoo's Nest", "arvio": 8.6, "ohjaaja": "Milos Forman", "vuosi": 1975},
    23:
    24:
    25:
    26:
    27:
    28:
    29:
    30:
    31:
    32:
    33:
    34:
    35:
    36:
    37:
    38:
    39:
    40:
    41:
    42:
    43:
    44:
    45:
    46:
    47:
    48:
    49:
    50: {"nimi": "The Prestige", "arvio": 8.5, "ohjaaja": "Christopher Nolan", "vuosi": 2006}
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
        url = "https://www.imdb.com/"
        webbrowser.open(url)
        break
