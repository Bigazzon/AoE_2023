import utils.advent as advent
import networkx as nx
from collections import defaultdict

advent.setup(2023, 25)


def parse_input(lines):
    return lines


def create_edges_dict(lines):
    edges_dict = defaultdict(set)
    for line in lines:
        start_node, end_nodes = line.split(":")
        for end_node in end_nodes.split():
            edges_dict[start_node].add(end_node)
            edges_dict[end_node].add(start_node)
    return edges_dict


def create_graph(edges_dict):
    graph = nx.DiGraph()
    for node, connected_nodes in edges_dict.items():
        for connected_node in connected_nodes:
            graph.add_edge(node, connected_node, capacity=1)
            graph.add_edge(connected_node, node, capacity=1)
    return graph


def find_minimum_cut(graph, edges_dict):
    for source_node in [list(edges_dict.keys())[0]]:
        for target_node in edges_dict.keys():
            if source_node != target_node:
                cut_value, (cut_set_source, cut_set_target) = nx.minimum_cut(
                    graph, source_node, target_node
                )
                if cut_value == 3:
                    return len(cut_set_source) * len(cut_set_target)


def part1(lines):
    lines = parse_input(lines)
    edges_dict = create_edges_dict(lines)
    graph = create_graph(edges_dict)
    return find_minimum_cut(graph, edges_dict)


if __name__ == "__main__":
    # with open("challenges/25/2023_25_debug.txt", "r") as file:
    #     lines = file.read().splitlines()
    with advent.get_input() as file:
        lines = file.read().splitlines()

    print("############### Day 25 ###############")
    advent.submit_answer(1, part1(lines))
