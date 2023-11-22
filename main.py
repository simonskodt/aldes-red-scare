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

            graph, red_keys,s,t, is_directed = p.parse_file(file)
            delegate_problem(graph, red_keys,s,t, is_directed, file)
            break
        elif arg == '--files':
            files = argv[i+1].split(",")
            print(f"File: {files}")
            for file in files:
                graph, red_keys,s,t, is_directed = p.parse_file(file)
                delegate_problem(graph, red_keys,s,t, is_directed, file)
            break
        elif arg == '--all':
            print(f"All:\n")
            for file in p.find_all_files():
                print(f"-- {file} --")
                graph, red_keys,s,t, is_directed = p.parse_file(file)
                if len(graph) >= 500:
                    delegate_problem(graph, red_keys,s,t, is_directed, file)
            break
        else:
            print("Invalid option")
            sys.exit(2)

    results_file.close()
    log_file.close()


def printTimeTaken(start_time, problem, instance_name):
    end_time = (time.time() - start_time)
    if end_time < 1:
        return f"{problem} took: {round(end_time*1000,2)}ms for {instance_name}"
    else:
        return f"{problem} took: {round(end_time,2)}s for {instance_name}"

# Test cases: bht,common-1-5757,common-2-5757,gnm-5000-10000-0,gnm-5000-10000-1,dodecahedron,grid-50-0,grid-50-1,grid-50-2,increase-n-500-1,increase-n-500-2,increase-n-500-3,p3,rusty-1-5757,rusty-2-5757,ski-level20-1,ski-level20-2,ski-level20-3,small-world-50-0,small-world-50-1,wall-n-10000,wall-p-10000,wall-z-10000


def delegate_problem(graph, red_keys, s, t, is_directed, instance_name):
    header_for_print = f"---- Instance: {instance_name}, n: {len(graph)} ----\n"
    a_start_time = time.time()
    A = alternate.check_alternate_problem(graph, red_keys,s,t)
    elapsed_time_A = printTimeTaken(a_start_time, "A", instance_name)
    a_string = f"Alternate: {A} with elapsed time: {elapsed_time_A}\n"
    print(a_string)
    f_start_time = time.time()
    F = few.check_few_problem(graph, red_keys, s, t)
    elapsed_time_F = printTimeTaken(f_start_time, "F", instance_name)
    f_string = f"Few: {F} with elapsed time: {elapsed_time_F}\n"
    print(f_string)

    # M = many.check_many_problem(graph, red_keys,s,t)
    
    n_start_time = time.time()
    N = none.check_none_problem(graph, red_keys, s, t)
    elapsed_time_N = printTimeTaken(n_start_time, "N", instance_name)
    n_string = f"None: {N} with elapsed time: {elapsed_time_N}\n"
    print(n_string)
    
    s_start_time = time.time()
    S = some.check_some_problem(graph, red_keys,s,t, is_directed)
    
    elapsed_time_S = printTimeTaken(s_start_time, "S", instance_name)
    s_string = f"Some: {S} with elapsed time: {elapsed_time_S}\n"
    print(s_string)

    # build strings
    print_string = header_for_print + a_string + f_string + n_string + s_string + "\n"
    result_string = f"{instance_name}, {len(graph)}, {A}, {F}, {N}, {S}\n"

    results_file.write(result_string)
    log_file.write(print_string)
    print(print_string)

    if should_visualize:
        visualize(graph, red_keys, s, t, is_directed)

def visualize(graph, red_keys, s, t, is_directed):
    gv.visualize(graph, red_keys, s, t, is_directed)

if __name__ == "__main__":
    sys.path.insert(1, 'problems/')
    main(sys.argv[1:])
