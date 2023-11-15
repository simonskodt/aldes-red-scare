import sys
import parse as p
from problems import none, some, many, few, alternate   
import graph_visualizer as gv

should_visualize = False

def main(argv):
    global should_visualize
    
    results_file = open("results.txt", "w")
    results_file.write("Instance name, n, A, F, M, N, S\n")

    if len(argv) == 0:
        print(f"Provide a flag to run program\nE.g.")
        sys.exit(2)

    for i, arg in enumerate(argv):
        if i+1 > len(argv):
            print(f"Missing argument after flag {argv}")
            sys.exit(2)

        if arg == '--visualize':
            should_visualize = True
            continue

        if arg == '--prefix':
            print(f"Prefix: {argv[i+1]}")
            # for file in p.find_files(arg[i+1]):
            #     p.parse_file(file)
            break
        elif arg == '--file':
            file = argv[i+1]
            print(f"File: {file}")

            graph, red_keys,s,t, is_directed = p.parse_file(argv[i+1])
            delegate_problem(graph, red_keys,s,t, is_directed, file, results_file)
            break
        elif arg == '--all':
            print(f"All:\n")
            for file in p.find_all_files():
                print(f"-- {file} --")
                graph, red_keys,s,t, is_directed = p.parse_file(file)
                delegate_problem(graph, red_keys,s,t, is_directed, file, results_file)
            break
        else:
            print("Invalid option")
            sys.exit(2)

    results_file.close()

def delegate_problem(graph, red_keys, s, t, is_directed, instance_name, results_file):
    A = alternate.check_alternate_problem(graph, red_keys,s,t)
    F = few.check_few_problem(graph, red_keys,s,t)
    # M = many.check_many_problem(graph, red_keys,s,t)
    N = none.check_none_problem(graph, red_keys,s,t)
    # S = some.check_some_problem(graph, red_keys,s,t)

    print("Alternate:", A)
    print("Few:", F)
    print("None:", N)
    print()

    # make results.txt as .csv file for output

    results_file.write(f"{instance_name}, {len(graph)}, {A}, {F}, {N}\n")

    if should_visualize:
        visualize(graph, red_keys, s, t, is_directed)

def visualize(graph, red_keys, s, t, is_directed):
    gv.visualize(graph, red_keys, s, t, is_directed)

if __name__ == "__main__":
    sys.path.insert(1, 'problems/')
    main(sys.argv[1:])