"""
Author: Duong Vu Tuan Minh
Application: Music player
Date: 7/5/2020

"""

#Creating a defined music player

# from playsound import playsound

class Track:
    def __init__ (self,number,track_title, author, location):
        self.number = number
        self.track_title = track_title
        self.author = author
        self.location = location


def read_file():
    # with open(input("Enter the file name: "),"r") as the_file:
    #     tfile = the_file
    tfile = open(input("Enter the file name: "), "r")
    count = tfile.readline()
    tracks  = []
    index = 0
    while index < int(count):
        track = read_track(tfile)
        tracks.append(track)
        index += 1
    return tracks

def read_track(tfile):
    number = tfile.readline()
    track_title = tfile.readline()
    author = tfile.readline()
    location = tfile.readline()
    track = Track(number,track_title, author, location) 
    return track

def display_track(track):
    print("{}. {} - {}".format(str(track.number).strip(), str(track.track_title).strip(), str(track.author).strip()))
    
def dipslay_tracks(tracks):
    i = 0
    while i < len(tracks):
        display_track(tracks[i])
        i += 1

def play_track(tracks,num):
    # playsound("{}".format(tracks[int(num)-1].location))
    print("{}".format(tracks[int(num)-1].location))

if __name__ == "__main__":
    
    print("Hello to the music player!!")
    while True:  #should be implement break somewhere
        print("Make an option:\n\t1. Import music file\n\t2. Display all tracks\n\t3. Play a particular track\n\t4. Exit the program") 
        choice = input()
        if choice == "1":
            tracks = read_file()
            print("Import successfully!")
        elif choice == "2":
            dipslay_tracks(tracks)
        elif choice == "3":
            print("Enter the number of the song you want to play: ")
            inp_number = input()
            play_track(tracks, inp_number)
        elif choice == "4":
            print("Thanks for using MP3 player!!")
            break
        else: 
            continue
