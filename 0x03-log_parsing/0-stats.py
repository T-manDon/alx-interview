#!/usr/bin/python3
"""
This script: will read standard input line by line with the computes metrics
"""
def parseLogs():
    """
    Read the logs from standard input and gives output report
    Reports:
        * Prints the log size then  reads the 10 linespt
    Raises:
        KeyboardInterrupt (Exception): handles  exception plus  raises it
    """
    stdin = __import__('sys').stdin
    lineNumber = 0
    fileSize = 0
    statusCodes = {}
    codes = ('200', '301', '400', '401', '403', '404', '405', '500')
    try:
        for line in stdin:
            lineNumber += 1
            line = line.split()
            try:
                fileSize += int(line[-1])
                if line[-2] in codes:
                    try:
                        statusCodes[line[-2]] += 1
                    except KeyError:
                        statusCodes[line[-2]] = 1
            except (IndexError, ValueError):
                pass
            if lineNumber == 10:
                report(fileSize, statusCodes)
                lineNumber = 0
        report(fileSize, statusCodes)
    except KeyboardInterrupt as e:
        report(fileSize, statusCodes)
        raise


def report(fileSize, statusCodes):
    """
    Generates report through standard output
    Args:
        fileSize (int): total log size after every 10 successfully read line
        statusCodes (dict): dictionary of status codes and counts
    """
    print("File size: {}".format(fileSize))
    for key, value in sorted(statusCodes.items()):
        print("{}: {}".format(key, value))

if __name__ == '__main__':
    parseLogs()
