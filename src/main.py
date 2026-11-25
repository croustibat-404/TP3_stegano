import argparse
from stego import hide

def main():
    parser = argparse.ArgumentParser(description='Steganography tool')
    subparsers = parser.add_subparsers(dest='command', required=True)

    hide_parser = subparsers.add_parser('hide', help='Cacher un message dans une image')
    hide_parser.add_argument('-i', '--input', required=True, help='Chemin de l\'image d\'entrée')
    hide_parser.add_argument('-o', '--output', required=True, help="Chemin de l'image de sortie")
    hide_parser.add_argument('-s', '--secret', required=True, help='Message à cacher')

    reveal_parser = subparsers.add_parser('reveal', help='Révéler un message caché dans une image')
    reveal_parser.add_argument('image', help='Chemin de l\'image d\'entrée')

    args = parser.parse_args()

    if args.command == 'hide':
        try:
            hide(args.input, args.output, args.secret)
        except ValueError as e:
            print(e)
        except FileNotFoundError:
            print("L\'image d\'entrée est introuvable.")
    elif args.command == 'reveal': 
        print(args.image)
        
if __name__ == '__main__':
    main()