import sys
import parse as p
from problems import none, some, many, few, alternate

def main(argv):
    if len(argv) == 0:
        print(f"Provide a flag to run program\nE.g.")
        sys.exit(2)

    for i, arg in enumerate(argv):
        print(argv[i+1])
        if i+1 > len(argv):
            print(f"Missing argument after flag {argv}")
            sys.exit(2)
            
        if arg == '--prefix':
            print(f"Prefix: {argv[i+1]}")
            # for file in p.find_files(arg[i+1]):
            #     p.parse_file(file)
            break
        elif arg == '--file':
            print(f"File: {argv[i+1]}")
            graph, red_keys,s,t, is_directed = p.parse_file(argv[i+1])
            delegate_problem(graph, red_keys,s,t, is_directed)
            break
        elif arg == '--all':
            print(f"All")
            for file in p.find_all_files():
                p.parse_file(file)
            break
        else:
            print("Invalid option")
            sys.exit(2)


def delegate_problem(graph, red_keys, s, t, is_directed):
    # solve for None
    print("None:", none.check_none_problem(graph, red_keys,s,t))

if __name__ == "__main__":
    sys.path.insert(1, 'problems/')
    main(sys.argv[1:])