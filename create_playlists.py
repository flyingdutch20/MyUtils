#!/usr/bin/env python3
"""create playlists from a directory of song files"""

import argparse
import os


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='create playlists from a directory of song files',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('directory',
                        metavar='directory',
                        help='Top-level directory or drive')

    args = parser.parse_args()

    if not os.path.isdir(args.directory):
        parser.error(f'Directory "{args.directory}" not found')

    return args

# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    os.chdir(args.directory)
    artists = os.listdir(os.curdir)

    for artist in sorted(artists):
        if artist[0] != '.' and os.path.isdir(artist):
            artist_playlist = []
            albums = os.listdir(os.path.join(os.curdir, artist))
            for album in sorted(albums):
                if os.path.isdir(os.path.join(os.curdir,artist,album)):
                    album_playlist = []
                    files = os.listdir(os.path.join(os.curdir, artist, album))
                    for file in sorted(files):
                        if os.path.splitext(file)[1] == '.mp3':
                            song = os.path.join(artist, album, file) + '\n'
                            album_playlist.append(song)
                            artist_playlist.append(song)
                    if len(album_playlist) > 0:
                        filename = '{}-{}.m3u'.format(artist, album)
                        outfile = open(filename, 'w', newline='')
                        outfile.writelines(album_playlist)
                        outfile.close()
            if len(artist_playlist) > 0:
                filename = '{}.m3u'.format(artist)
                outfile = open(filename, 'w', newline='')
                outfile.writelines(artist_playlist)
                outfile.close()


# --------------------------------------------------
if __name__ == '__main__':
    main()
