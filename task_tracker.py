import json
import argparse
import os
import datetime

def file_and_date_time():
    file_name = "TaskList.json"
    currentTime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(currentTime)





def main():
    parser = argparse.ArgumentParser() #Creating a Parsing Object 

    parser.add_argument("-a", "--add", help="To add a task", required=False)
    parser.add_argument("-u", "--update", help="To update a task", required=False)
    parser.add_argument("-d", "--delete", help="To delete a task", required=False)
    parser.add_argument("-m", "--mark", 
                        help="Change status to 'todo' or 'in-progress' or 'done'", required=False)
    parser.add_argument("-l", "--list", help="To filter type 'todo' or 'in-progress' or 'done' or 'all'", required=False)
    parser.add_argument("--id", help="Type and ID for any operation")

    args = parser.parse_args()

    print(f"New Task Added: {args.add if args.add else 'Nothing has been added.'}")
    print(f"Task {args.id} Updated {args.update if args.update else 'Nothing has been updated.'}")
    print(f"Task {args.id} Deleted {args.delete if args.delete else 'Nothing has been deleted.'}")
    print(f"Task Selected With ID: {args.id if args.id else 'ID Required'}")
    print(f"Selected List with status filter: {args.list if args.list else 'No list has been chosen'}")

    file_and_date_time()


main()

