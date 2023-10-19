import argparse
import importlib.metadata


def default_output(output: str):
    print(output)

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('--default_output', default='default')
    args = parser.parse_args()
    print(args.default_output)
    eps = importlib.metadata.entry_points()['hello_world.output']
    
    outputers = {
        entrypoint.name: entrypoint for entrypoint in eps
    }
    try:
        default_output = outputers[args.default_output].load()
    except KeyError:
        print(f'outputer {args.default_output} is not available!')
        return 1
    print(default_output)
    default_output("Hello world-Siraj")


    return 0

if __name__ == '__main__':
    exit(main())
