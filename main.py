import sys
import parse as p
from problems import none, some, many, few, alternate   
import graph_visualizer as gv
import time

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

            graph, red_keys,s,t, is_directed = p.parse_file(file)
            delegate_problem(graph, red_keys,s,t, is_directed, file, results_file)
            break
        elif arg == '--files':
            files = argv[i+1].split(",")
            print(f"File: {files}")
            for file in files:
                graph, red_keys,s,t, is_directed = p.parse_file(file)
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

def start_timer():
    return time.time()

def printTimeTaken(start_time, problem, instance_name):
    end_time = (time.time() - start_time)
    if end_time < 1:
        print(f"{problem} took: {round(end_time*1000,2)}ms for {instance_name}")
    else:
        print(f"{problem} took: {round(end_time,2)}s for {instance_name}")

# Test cases: bht,common-1-5757,common-2-5757,gnm-5000-10000-0,gnm-5000-10000-1,dodecahedron,grid-50-0,grid-50-1,grid-50-2,increase-n-500-1,increase-n-500-2,increase-n-500-3,p3,rusty-1-5757,rusty-2-5757,ski-level20-1,ski-level20-2,ski-level20-3,small-world-50-0,small-world-50-1,wall-n-10000,wall-p-10000,wall-z-10000


def delegate_problem(graph, red_keys, s, t, is_directed, instance_name, results_file):
    a_start_time = start_timer()
    A = alternate.check_alternate_problem(graph, red_keys,s,t)
    printTimeTaken(a_start_time, "A", instance_name)
    f_start_time = start_timer()
    F = few.check_few_problem(graph, red_keys,s,t)
    printTimeTaken(f_start_time, "F", instance_name)
    # M = many.check_many_problem(graph, red_keys,s,t)
    n_start_time = start_timer()
    N = none.check_none_problem(graph, red_keys,s,t)
    printTimeTaken(n_start_time, "N", instance_name)
    # S = some.check_some_problem(graph, red_keys,s,t)

    print("Alternate:", A)
    print("Few:", F)
    print("None:", N)
    print()

    # make results.txt as .csv file for output

    results_file.write(f"{instance_name}, {len(graph)}, {A}, {F}, ?, {N}, ?\n")

    if should_visualize:
        visualize(graph, red_keys, s, t, is_directed)

def visualize(graph, red_keys, s, t, is_directed):
    gv.visualize(graph, red_keys, s, t, is_directed)

if __name__ == "__main__":
    sys.path.insert(1, 'problems/')
    main(sys.argv[1:])