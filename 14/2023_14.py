import utils.advent as advent

advent.setup(2023, 14)

def parse_input(lines):
    return lines
        
def part1(lines):  
    return 0

def part2(lines): 
    symbs, nums = parse_input(lines)   
    return 0
                
            
    
             
if __name__ == "__main__":
    with open("14/2023_14_debug.txt", "r") as file:
        lines = file.read().splitlines()
    # with advent.get_input() as file:
    #     lines = file.read().splitlines()

    print("############### Day 14 ###############")
    advent.print_answer(1, part1(lines))
    advent.print_answer(2, part2(lines))