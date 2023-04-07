import argparse
from dataclasses import dataclass

@dataclass
class InputArgParser:
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-p",
        "--use_proxy",
        dest="use_proxy",
        help="Run with proxy",
        default=False,
        action="store_true",
    )

    parser.add_argument(
        "-i",
        "--instance",
        dest="instance",
        help="Number of instance",
        default=1,
        type=int,
    )

    args = parser.parse_args()
    print(args)

    def with_proxy(self):
        return self.args.use_proxy

    def get_instance(self):
        return self.args.instance
