# the module is used before other modules load

from load_from_cookies import load_from_cookies
import argparse

# initialize the args
parser = argparse.ArgumentParser()
parser.add_argument('mode', help='mode: query or parse')
parser.add_argument('--stu-id', help='student ID which is used for login when using query mode')
parser.add_argument('--query-mode', help='querying mode: single or multiple, the former one is default')
parser.add_argument('--begin', help='the beginning of the range (inclusive)', type=int)
parser.add_argument('--end', help='the end of range (inclusive)', type=int)
args = parser.parse_args()

# check the mode (simply test)
# will be improved in next version
if args.mode == 'parse':
    import rank_parser
    exit(0)

# do login (need stu_id from args)
if args.stu_id:
    stu_id = args.stu_id
    load_from_cookies(stu_id)
else:
    print ('You need to provide a student ID for login!')
    exit(0)

# check other args

# check query_mode, begin and end
if args.query_mode:
    import query
    if args.query_mode == 'single':
        query.query_single(stu_id)
    elif args.query_mode == 'multiple':
        if args.begin and args.end:
            query.query_multiple(stu_id, args.begin, args.end)
        else:
            print ('please provide argument begin and end!')
            exit(0)
    else:
        print ('query_mode arg error!')
        exit(0)
else:
    query.query_single(stu_id)