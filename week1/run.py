## Calculate some stats for the Great North Run 2018
times = []
print(len(times))
# open input file
# input_file = open('run_times.in', 'r')
#
# # read contents of the file into a temporary list `timestamps`
# times = input_file.readlines()
# input_file.close()


with open('run_times.in', 'r') as f:
    times = f.readlines()

print(len(times))

# sanitize the list for further use.
timestamps_clean = [time.strip() for time in times]
times = timestamps_clean

def get_top_ten_fastest(timestamps):
    return sorted(timestamps)[:10]

fastest = get_top_ten_fastest(times)
print(fastest)

def get_times_in_seconds(timestamps):
    """

    :param timestamps: list : A list of times in M:S:MS format
    :return: list : A list of times in seconds

    Idea / functionality : use datetime to extract hrs, min and secs.
    convert all to secs and sum them.
    append to a new list and return it.
    """

    times_in_seconds = []
    for time in timestamps:
        stamp_split = time.split(':')
        if len(stamp_split) == 3:
            hrs_to_sec = int(stamp_split[0]) * 60 * 60
            mins_to_sec = int(stamp_split[1]) * 60
            sec = int(stamp_split[2])
            times_in_seconds.append(hrs_to_sec + mins_to_sec + sec)

    return times_in_seconds
times_in_seconds = get_times_in_seconds(times)

