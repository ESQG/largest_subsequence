
def largest_sum(numbers):

    positive_indices = [index for index, num in enumerate(numbers) if num > 0]
    maximum = max(numbers)
    if maximum <= 0:
        return []
    sublist = [maximum]

    for j, left_index in enumerate(positive_indices):
        for right_index in positive_indices[j+1:]:
            # print left_index, right_index
            candidate_sublist = numbers[left_index:right_index+1]
            candidate_sum = sum(candidate_sublist)
            if candidate_sum == maximum and len(candidate_sublist) < len(sublist):
                sublist = candidate_sublist
            elif candidate_sum > maximum:
                maximum = candidate_sum
                sublist = candidate_sublist

    return sublist
