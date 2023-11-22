import sys
import time
import parse as p
from problems import none, some, many, few, alternate   
import graph_visualizer as gv

should_visualize = False
results_file = None
log_file = None

def main(argv):
    global should_visualize
    global results_file
    global log_file
    
    results_file = open("results.txt", "w")
    results_file.write("Instance name, n, A, F, M, N, S\n")

    log_file = open("log.txt", "w")

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
            delegate_problem(graph, red_keys,s,t, is_directed, file)
            break
        elif arg == '--all':
            print(f"All:\n")
            for file in p.find_all_files():
                print(f"-- {file} --")
                graph, red_keys,s,t, is_directed = p.parse_file(file)
                delegate_problem(graph, red_keys,s,t, is_directed, file)
            break
        else:
            print("Invalid option")
            sys.exit(2)

    results_file.close()
    log_file.close()

def delegate_problem(graph, red_keys, s, t, is_directed, instance_name):
    start_time_A = time.time()
    A = alternate.check_alternate_problem(graph, red_keys,s,t)
    end_time_A = time.time()

    start_time_F = time.time()
    F = few.check_few_problem(graph, red_keys,s,t)
    end_time_F = time.time()

    # M = many.check_many_problem(graph, red_keys,s,t)
    start_time_N = time.time()
    N = none.check_none_problem(graph, red_keys,s,t)
    end_time_N = time.time()
    # S = some.check_some_problem(graph, red_keys,s,t)

    header_for_print = f"---- Instance: {instance_name}, n: {len(graph)} ----\n"
    a_string = f"Alternate: {A} with elapsed time: {end_time_A - start_time_A}\n"
    f_string = f"Few: {F} with elapsed time: {end_time_F - start_time_F}\n"
    n_string = f"None: {N} with elapsed time: {end_time_N - start_time_N}\n"
    print_string = header_for_print + a_string + f_string + n_string + "\n"
    result_string = f"{instance_name}, {len(graph)}, {A}, {F}, {N}\n"

    # make results.txt as .csv file for output
    results_file.write(result_string)

    # write prints to log
    log_file.write(print_string)

    # print in terminal
    print(print_string)


    if should_visualize:
        visualize(graph, red_keys, s, t, is_directed)

def visualize(graph, red_keys, s, t, is_directed):
    gv.visualize(graph, red_keys, s, t, is_directed)

if __name__ == "__main__":
    sys.path.insert(1, 'problems/')
    main(sys.argv[1:])