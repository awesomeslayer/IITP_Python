
from pathlib import Path
import stat
import argparse
import pwd
import grp
import datetime
import math

def myls(targets, all_files=False, long_format=False, verbose=False, recursive=False, human_readable=False):
    """
    List files and directories.
    
    targets: list
        List of file(s) or directory(s) to list.
    
    all_files: bool
        Include hidden files and directories.
    
    long_format: bool
        Display file information in long format.
    
    verbose: bool
        Show verbose output for directories.
    
    recursive: bool
        Recursively list subdirectories.
    
    human_readable: bool
        Display file sizes in human-readable format.
        
    help: bool
        Show ls function help message
    """
    for target in targets:
        path = Path(target)
        if not path.exists():
            print(f"{target}: No such file or directory")
        else:
            if long_format:
                file_info = path.stat()
                permissions = stat.filemode(file_info.st_mode)
                file_size = file_info.st_size
                creation_time = format_time(file_info.st_ctime, human_readable)
                modified_time = format_time(file_info.st_mtime, human_readable)
                owner = pwd.getpwuid(file_info.st_uid).pw_name
                group = grp.getgrgid(file_info.st_gid).gr_name
                if human_readable:
                    file_size = get_human_readable_size(file_size)
                print(f"{permissions} {file_size:>8} {creation_time:>20} {modified_time:>20} {owner:<10} {group:<10} {path.name}")
            else:
                print(path.name)
            
            if path.is_dir() and (recursive or verbose):
                for item in path.iterdir():
                    if not all_files and item.name.startswith("."):
                        continue
                    
                    file_info = item.stat()
                    permissions = stat.filemode(file_info.st_mode)
                    file_size = file_info.st_size
                    creation_time = format_time(file_info.st_ctime, human_readable)
                    modified_time = format_time(file_info.st_mtime, human_readable)
                    owner = pwd.getpwuid(file_info.st_uid).pw_name
                    group = grp.getgrgid(file_info.st_gid).gr_name
                    if human_readable:
                        file_size = get_human_readable_size(file_size)
                    print(f"{permissions} {file_size:>8} {creation_time:>20} {modified_time:>20} {owner:<10} {group:<10} {item.name}")
                    if item.is_dir() and recursive:
                        myls([item], all_files, long_format, verbose, recursive, human_readable)

def get_human_readable_size(size):
    units = ["B", "KB", "MB", "GB", "TB"]
    unit_index = 0
    while size >= 1024 and unit_index < len(units) - 1:
        size /= 1024
        unit_index += 1
    return f"{size:.1f} {units[unit_index]}"

def format_time(timestamp, human_readable=False):
    dt = datetime.datetime.fromtimestamp(timestamp)
    if human_readable:
        return dt.strftime("%b %d %Y %H:%M:%S")
    else:
        return dt.strftime("%Y-%m-%d %H:%M:%S")

def main():
    description = myls.__doc__
    parser = argparse.ArgumentParser(description=description, formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument("targets", nargs="*", default=["."], help="file(s) or directory(s) to list (default: current directory)")
    parser.add_argument("-a", "--all", action="store_true", help="include hidden files and directories")
    parser.add_argument("-l", "--long", action="store_true", help="display file information in long format")
    parser.add_argument("-v", "--verbose", action="store_true", help="show verbose output for directories")
    parser.add_argument("-r", "--recursive", action="store_true", help="recursively list subdirectories")
    parser.add_argument("-H", "--human-readable", action="store_true", help="display file sizes in human-readable format")
    parser.add_argument("-help", action="store_true", help="show ls function help message")
    
    args, unknown_args = parser.parse_known_args()

    print("=== ls Function Information ===")
    print(description)
    print("=== ls Function Information ===")
    if unknown_args:
        print(f"\nUnrecognized argument(s): {' '.join(unknown_args)}")
    print("Arguments:")
    for arg in vars(args):
        print(f"- {arg}: {getattr(args, arg)}")
    print("")
   
    myls(args.targets, all_files=args.all, long_format=args.long, verbose=args.verbose, recursive=args.recursive, human_readable=args.human_readable)
    
if __name__ == "__main__":
    main()
