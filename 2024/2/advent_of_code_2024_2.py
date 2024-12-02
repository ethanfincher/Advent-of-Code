lines = open("2024/2/input.txt").read().strip().split("\n")
reports = [[int(num) for num in line.split(" ")] for line in lines]

good_reports = 0

def check_report(report):
    # all possible reports is the current report plus the report with each index missing
    possible_reports = [report] + [report[:i] + report[i+1:] for i in range(len(report))]
    for current_report in possible_reports:
        for index, num in enumerate(current_report):
            # if we hit the last index, then all the indexes pass the rule, and we can return a successful report
            if index == len(current_report) - 1:
                return 1
            else:
                # if this is the first elem, we need to figure out if we're going up or down
                if index == 0:
                    if num > current_report[index+1]:
                        is_increase = False
                    else:
                        is_increase = True
                # then we check if the difference between the numbers is within the given range, and if we are going in the right direction
                if 1 <= abs(num - current_report[index+1]) <= 3 and (num - current_report[index+1] < 0 if is_increase else num - current_report[index+1] > 0):
                    # if so, continue on to the next index
                    continue
                else:
                    # if not, move onto the next next possible sub_report
                    break
    # if none of the possible reports return a good one, return a failure
    return 0
    
for report in reports:
    good_reports += check_report(report)

print(good_reports)