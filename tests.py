import sys

import glob2

for filename in glob2.glob('./**'):
    lower_filename = filename.lower()
    is_suite = lower_filename.find('src')
    if is_suite > -1:
        sys.path.append(filename)

if __name__ == '__main__':
    from engine.testsrc.SystemSuite import SystemSuite
    SystemSuite.test()
