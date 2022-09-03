import imdb
import webbrowser

def movien():
    movie = input("\nMovie: ")
    ia = imdb.IMDb()
    results = ia.search_movie(movie)
    mv = results[0] #First result
    URL = ia.get_imdbURL(mv) #URL for first result
    imdurl = URL
    vidsrcurl = "https://v2.vidsrc.me/embed/"
    vidurlf = imdurl.replace("https://www.imdb.com/title/","https://v2.vidsrc.me/embed/")
    x = vidurlf 
    print("Playing in You Webbrowser...")
    webbrowser.open(x)
def series():
    seris = input("\nSeries: ")
    ia = imdb.IMDb()
    results = ia.search_movie(seris)
    mv = results[0] #First result
    URL = ia.get_imdbURL(mv) #URL for first result
    imdurl = URL
    seasonx = input("Season (in 01-15 format): ")
    episodex = input("Episode (in 01-15 format): ") 
    vidsrcurl = "https://v2.vidsrc.me/embed/"
    vidurlf = imdurl.replace("https://www.imdb.com/title/","https://v2.vidsrc.me/embed/")
    x = vidurlf + seasonx + "-" + episodex 
    print("Playing in You Webbrowser...")
    webbrowser.open(x)

print("\n                Visit: https://isg32.github.io/Home                     \n")

print("\n[1] Movie \n[2] Series")
decis = int(input("\n>> "))
if decis == 1:
    movien()
if decis == 2:
    series()

for i in range(30):
    print("\n(w)visit My Website")
    print("(r)Reselect")
    print("(q)Quit")
   
    rangeinput = input(">> ")
    
    if rangeinput == "w":
        webbrowser.open("isg32.github.io")
    while True:
        while True:
            answer = str(input('Anything else? (y/n): '))
            if answer in ('y', 'n'):
                break
            print("invalid input.")
        if answer == 'y':
            print("\n[1] Movie \n[2] Series")
            decis = int(input("\n>> "))
            if decis == 1:
                movien()
            if decis == 2:
                series()
        if answer == 'n':
            exit()
        else:
            print(" ")
            break
    
    if rangeinput == "q":
        exit()