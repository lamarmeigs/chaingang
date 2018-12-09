import argparse
import re
import sys

import markovify


def read_corpus(path, ignore_pattern=None):
    with open(path) as f:
        corpus = f.read()
    if ignore_pattern:
        corpus = re.sub(ignore_pattern, '', corpus)
    return corpus


def build_model(corpora, weights=None):
    models = [markovify.Text(corpus, retain_original=False) for corpus in corpora]
    model = markovify.combine(models, weights)
    return model


def write_model(model, path=None):
    serialized_model = model.to_json()
    if path:
        with open(path, 'w') as f:
            f.write(serialized_model)
    else:
        sys.stdout.write(serialized_model)


def load_model(path):
    pass


def create_model(args, parser):
    """Create a new Markov model from the given command-line arguments."""
    # TODO: allow command to read from stdin
    corpora = (read_corpus(path, args.pattern) for path in args.corpora)
    if args.weights and len(args.weights) != len(args.corpora):
        parser.error('Number of weights must match number of corpora')
    model = build_model(corpora, args.weights)
    write_model(model, path=args.outfile)


def generate_sentences(args, parser):
    """Generate sentences from models in the given command-line arguments."""
    pass


def _compile_regex(pattern):
    try:
        pattern = re.compile(pattern)
    except re.error:
        raise argparse.ArgumentTypeError(f'Invalid regex: {pattern}')
    return pattern


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Play with Markov chains.')
    subparsers = parser.add_subparsers()

    # Arguments for building a new model
    model_parser = subparsers.add_parser('model', help='Create a Markov model')
    model_parser.set_defaults(run_command=create_model)
    model_parser.add_argument(
        '-c',
        '--corpora',
        nargs='+',
        required=True,
        help='Path to files containing the corpora to model',
    )
    model_parser.add_argument(
        '-w',
        '--weights',
        nargs='*',
        type=int,
        help='Relative weights to apply to each corpus',
    )
    model_parser.add_argument(
        '-d',
        '--ignore-pattern',
        dest='pattern',
        type=_compile_regex,
        help='Pattern to ignore in corpora'
    )
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
        '--num-sentences',
        type=int,
        help='Number of setences to generate'
    )

    # Parse, validate, and run
    args = parser.parse_args()
    if not hasattr(args, 'run_command'):
        parser.print_usage()
        parser.exit()
    args.run_command(args, parser)
