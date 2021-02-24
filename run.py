# the module is used before other modules load

from re import search
from load_from_cookies import load_from_cookies
import argparse

# initialize the args
parser = argparse.ArgumentParser()
parser.add_argument('mode', help='mode: query or parse')
#parser.add_argument('--stu-id', help='student ID which is used for login when using query mode')
parser.add_argument('--search', help="search specified student's score and rank")
parser.add_argument('--begin', help='the beginning of the range (inclusive)', type=int)
parser.add_argument('--end', help='the end of range (inclusive)', type=int)
parser.add_argument('--export', help='choose which format(csv, jpg) to export')
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

if args.mode == 'query':
    if args.search and args.begin and args.end:
        print ('please do not provide them at the same time!')
        exit(0)
    
    if args.search or (args.begin and args.end):
        import query
        if args.search:
            query.query_single(args.search)
        else:
            query.query_multiple(args.begin, args.end)
    else:
        print ('please provide --search or (--begin AND --end)!')
        exit(0)
    
    if args.export:
        from parse import parse
        if args.export == 'csv':
            parse('csv')
        elif args.export == 'jpg':
            parse()