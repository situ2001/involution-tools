# the module is used before other modules load

from re import search
from load_from_cookies import load_from_cookies
import argparse

# initialize the args
parser = argparse.ArgumentParser()
parser.add_argument('mode', help='mode: query or parse')
#parser.add_argument('--stu-id', help='student ID which is used for login when using query mode')
parser.add_argument('--search', help="search specified student's score and rank (single mode)")
parser.add_argument('--query-mode', help='querying mode: single or multiple, the former one is default', default='single')
parser.add_argument('--begin', help='the beginning of the range (inclusive, multiple mode)', type=int)
parser.add_argument('--end', help='the end of range (inclusive, multiple mode)', type=int)
parser.add_argument('--export', help='choose which format(csv) to export, leave blank for exporting jpg', default='jpg')
args = parser.parse_args()

# check the mode (simply test)
# will be improved in next version
if args.mode == 'parse':
    from parse import parse
    if args.export == 'csv':
        parse('csv')
    elif args.export == 'jpg':
        parse()
    exit(0)

''' update: stu_id is optional
# do login (need stu_id from args)
if args.stu_id:
    stu_id = args.stu_id
    load_from_cookies(stu_id)
else:
    print ('You must provide a student ID for login!')
    #exit(0)
'''

# check other args

# check query_mode, begin and end
if args.mode == 'query':
    if args.query_mode:
        import query
        if args.query_mode == 'multiple':
            if args.begin and args.end:
                query.query_multiple(args.begin, args.end)
            else:
                print ('please provide argument begin and end!')
                exit(0)
        elif not args.search:
            print ('Please provide --search argument!')
            exit(0)
        elif args.query_mode == 'single':
            query.query_single(args.search)
        else:
            query.query_single(args.search)
        if args.export:
            from parse import parse
            if args.export == 'csv':
                parse('csv')
            elif args.export == 'jpg':
                parse()
