import pyperclip,subprocess,argparse


def startup():
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', '--magnet', default='null')
    args = parser.parse_args()
    if args.magnet == 'null':
        launch(pyperclip.paste())
    elif 'magnet:' in args.magnet:
         launch(args.magnet)

def launch(magnet):
    if not 'magnet:' in magnet:
        print('magnet link not found..')
    else:
        subprocess.call('webtorrent "'+magnet+'" --mpv',shell=True)


if __name__ == '__main__':
    startup()
