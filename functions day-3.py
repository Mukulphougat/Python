def make_album(artist_name, album_name):
    music = {'Artist name: ':artist_name.title(),'Album name: ':album_name.title()}
    return music
while True:
    print("\nEnter Informatipn about your favourite music album.")
    print("(enter 'q' any time to exit)")
    singer = input("Enter Artist: ")
    if singer == 'q':
        break
    album = input("Enter Album: ")
    if album == 'q':
        break
    music = make_album(singer, album)
    print("MY favourite music album is:"),print(music)

