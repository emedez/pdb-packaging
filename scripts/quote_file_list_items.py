#!/usr/bin/env python
import sys


def main(argv=None)
    if not argv:
        argv = sys.argv[1:]

    filename = argv[0]
    f = open(filename)
    lines = []
    for line in f:
        line = line.rstrip()
        if line:
            line =  '"%s"' % line
        lines.append(line)
    f.close()

    f = open(filename)
    f.write('\n'.join(lines))
    f.close()

    return 0


if __name__ == '__main__':
    sys.exit(main())