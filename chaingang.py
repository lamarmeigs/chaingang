import argparse


def read_corpus(path, ignore_pattern=None):
    pass


def build_model(*corpora, weights=None):
    pass


def write_model(model, path=None):
    pass


def load_model(path):
    pass


def create_model(args):
    """Create a new Markov model from the given command-line arguments."""
    pass


def generate_sentences(args):
    """Generate sentences from models in the given command-line arguments."""
    pass


if __name__ == '__main':
    parser = argparse.ArgumentParser(description='Play with Markov chains.')
    subparsers = parser.add_subparsers()

    # Arguments for building a new model
    model_parser = subparsers.add_parser('model', help='Create a Markov model')
    model_parser.set_defaults(run_command=create_model)
    model_parser.add_argument(
        '-c',
        '--corpora',
        nargs='+',
        help='Path to files containing the corpora to model',
    )
    model_parser.add_argument(
        '-w',
        '--weights',
        nargs='*',
        help='Relative weights to apply to each corpus',
    )
    model_parser.add_argument('-d', dest='pattern', help='Pattern to ignore in corpus')
    model_parser.add_argument(
        '-o',
        '--outfile',
        help='Path to which to save the model (if none, print to stdout)',
    )

    # Arguments for generate sentences off an existing model
    generate_parser = subparsers.add_parser('generate', help='Create sentences from a model')
    generate_parser.set_defaults(run_command=generate_sentences)
    generate_parser.add_argument(
        '-m',
        '--models',
        nargs='*',
        help='Path to files containing Markov models',
    )
    generate_parser.add_argument(
        '-n',
        '--num_sentences',
        type=int,
        help='Number of setences to generate'
    )

    # Parse & run
    args = parser.parse_args()
    args.run_command(args)
