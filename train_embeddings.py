#!/usr/bin/env python3
import os
import sys
import time
import json
import random

def main():
    # Require API_KEY
    api_key = os.environ.get("API_KEY")
    if not api_key:
        print("Error: API_KEY not set", file=sys.stderr)
        sys.exit(1)

    # Fake params
    params = {
        "random_seed": None,
        "force_mode": False,
        "number": None,
        "delay": 0,
        "extra": None
    }

    args = sys.argv[1:]
    i = 0
    while i < len(args):
        if args[i] == "-r":  # random seed
            params["random_seed"] = random.randint(1000, 9999)
        elif args[i] == "-f":  # force flag
            params["force_mode"] = True
        elif args[i] == "-n" and i+1 < len(args):  # number
            try:
                params["number"] = int(args[i+1])
            except ValueError:
                params["number"] = None
            i += 1
        elif args[i] == "-d" and i+1 < len(args):  # delay
            try:
                params["delay"] = int(args[i+1])
            except ValueError:
                params["delay"] = 0
            i += 1
        elif args[i] == "-x":  # mystery token
            params["extra"] = "".join(random.choice("abcdef123456") for _ in range(12))
        i += 1

    if params["delay"] > 0:
        time.sleep(params["delay"])

    result = {
        "cwd": os.getcwd(),
        "time": time.strftime("%Y-%m-%d %H:%M:%S"),
        "args": args,
        "params": params
    }

    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()

