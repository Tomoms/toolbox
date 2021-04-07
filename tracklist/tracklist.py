#!/usr/bin/env python3

import os
import sys
from tinytag import TinyTag

def updateOffset(duration, hours, minutes, seconds: int):
    hours += duration // 3600
    left = duration % 3600
    minutes += left // 60
    if minutes > 59:
        hours += minutes // 60
        minutes = minutes % 60
    seconds += left % 60
    if seconds > 59:
        minutes += seconds // 60
        seconds = seconds % 60
    return hours, minutes, seconds

if __name__ == '__main__':
    folder = sys.argv[1]
    tracklist = open(folder + '/tracklist.txt', 'w+')

    hours = 0
    minutes = 0
    seconds = 0

    for song in os.listdir(folder):
        if song != 'tracklist.txt':
            audio = TinyTag.get(folder + "/" + song)
            title = audio.title
            if hours > 0:
                tracklist.write('%02d:' % hours)
            tracklist.write('%02d:%02d ' % (minutes, seconds))
            tracklist.write(title + '\n')
            hours, minutes, seconds = updateOffset(audio.duration, hours, minutes, seconds)

    tracklist.close()
