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
        print_instructions()

    for i, arg in enumerate(argv):
        if i+1 > len(argv):
            print(f"Missing argument after flag {argv}")
            sys.exit(2)

        if arg == '--visualize':
            should_visualize = True
            continue
        elif arg == '--help':
            print_instructions
        elif arg == '--file':
            file = argv[i+1]
            print(f"File: {file}")

            graph, red_keys,s,t, is_directed, has_no_incoming_edges = p.parse_file(file)
            delegate_problem(graph, red_keys,s,t, is_directed,file, has_no_incoming_edges)
            break
        elif arg == '--files':
            files = argv[i+1].split(",")
            print(f"File: {files}")
            for file in files:
                graph, red_keys,s,t, is_directed, has_no_incoming_edges = p.parse_file(file)
                delegate_problem(graph, red_keys,s,t, is_directed,file, has_no_incoming_edges)
            break
        elif arg == '--all':
            print(f"All:\n")
            for file in p.find_all_files():
                print(f"-- {file} --")
                graph, red_keys, s, t, is_directed, has_no_incoming_edges = p.parse_file(file)
                if len(graph) >= 500: 
                    delegate_problem(graph, red_keys, s, t, is_directed,file, has_no_incoming_edges)
            break
        else:
            print("Invalid option")
            sys.exit(2)

    results_file.close()
    log_file.close()

def print_instructions():
    print("\n< ======================= RED SCARE FLAGS ======================= >\n")
    print(f"Provide a flag to run program: python --... --...\n")
    print("E.g.")
    print("\t--visualize (to visualize the graph)") 
    print("\t--file { file_name } (provide the file name without the path")
    print("\t--files { file_name_1 } { ... } { file_name_n } (multiple files)")
    print("\t--all (run all implementations on files with n >= 500)\n")
    print("< =============================================================== >\n")
    sys.exit(2)
# Test cases: bht,common-1-5757,common-2-5757,gnm-5000-10000-0,gnm-5000-10000-1,dodecahedron,grid-50-0,grid-50-1,grid-50-2,increase-n-500-1,increase-n-500-2,increase-n-500-3,p3,rusty-1-5757,rusty-2-5757,ski-level20-1,ski-level20-2,ski-level20-3,small-world-50-0,small-world-50-1,wall-n-10000,wall-p-10000,wall-z-10000

def delegate_problem(graph, red_keys, s, t, is_directed, instance_name, has_no_directed_edges):
    if alternate.bfs(graph, s, t) is None:
        print_no_path(instance_name, s, t)
        return
    
    a_string, A = wrap_check_problem(lambda: alternate.check_alternate_problem(graph, red_keys,s,t), "Alternate", instance_name)
    print(a_string)

    f_string, F = wrap_check_problem(lambda: few.check_few_problem(graph, red_keys, s, t), "Few", instance_name)
    print(f_string)

    m_string, M = wrap_check_problem(lambda: many.check_many_problem(graph, red_keys, s, t,is_directed, has_no_directed_edges), "Many", instance_name)
    print(m_string)

    n_string, N = wrap_check_problem(lambda: none.check_none_problem(graph, red_keys, s, t), "None", instance_name)
    print(n_string)
    
    s_string, S = wrap_check_problem(lambda: some.check_some_problem(graph, red_keys, s, t, is_directed, has_no_directed_edges), "Some", instance_name)
    print(s_string)

    # build strings
    header_for_print = f"---- Instance: {instance_name}, n: {len(graph)} ----\n"
    print_string = header_for_print + a_string + f_string + m_string + n_string + s_string  + "\n"
    result_string = f"{instance_name}, {len(graph)}, {A}, {F}, {M}, {N}, {S}\n"

    results_file.write(result_string)
    log_file.write(print_string)
    print(print_string)

    if should_visualize:
        visualize(graph, red_keys, s, t, is_directed)

def visualize(graph, red_keys, s, t, is_directed):
    gv.visualize(graph, red_keys, s, t, is_directed)

def wrap_check_problem(function, problem_name, instance_name):
    start_time = time.time()
    problem = function()
    elapsed_time = printTimeTaken(start_time, problem_name[0], instance_name)
    problem_string = f"{problem_name}: {problem} with elapsed time: {elapsed_time}\n"
    return problem_string, problem

def printTimeTaken(start_time, problem, instance_name):
    end_time = (time.time() - start_time)
    if end_time < 1:
        return f"{problem} took: {round(end_time*1000,2)}ms for {instance_name}"
    else:
        return f"{problem} took: {round(end_time,2)}s for {instance_name}"

def print_no_path(instance_name, s, t):
    no_path = f"No path from '{s}' to '{t}'"
    result_string = f"{instance_name}: {no_path}\n"
    results_file.write(result_string)
    print_string = f"---- Instance: {instance_name}, {no_path}\n"
    log_file.write(print_string)
    print(print_string)

if __name__ == "__main__":
    sys.path.insert(1, 'problems/')
    main(sys.argv[1:])