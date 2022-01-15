import os
import csv
from functools import total_ordering
from math import dist


def main():
    print("Financial analysis")
    print("------------------")

    total_amount = 0.0
    average_change = 0.0
    greatest_inc = None

    with open("budget_data.csv") as file:
        reader = csv.reader(file)
        next(reader)
        data = dict(reader)
        total_amount = calc_total_amount(data)
        # extracting values from dictionary
        monthly_amounts = list(map(int, data.values()))
        monthly_changes = get_list_of_monthly_changes(
            monthly_amounts)
        average_change = find_avg_change(monthly_changes)
        greatest_inc = find_greatest_increase(
            monthly_changes=monthly_changes, data=data)
        greatest_dec = find_greatest_decrease(
            monthly_changes=monthly_changes, data=data)

    print(f"Total months = {len(data)}")
    print(f"Total amount : $ {total_amount}")
    formated_avg = "{:.2f}".format(average_change)  # formatting to 2dp
    print(f"Average change : ${formated_avg}")
    print(
        f"Greatest increase in profit : {greatest_inc[0]} ($ {greatest_inc[1]}))")
    print(
        f"Greatest change decrease : {greatest_dec[0]} ($ {greatest_dec[1]})")


def calc_total_amount(data):
    total_amount = 0.0
    for month in data:
        total_amount += float(data.get(month))
    return total_amount


def get_list_of_monthly_changes(monthly_amounts):
    return [monthly_amounts[i+1] - monthly_amounts[i]
            for i in range(len(monthly_amounts) - 1)]


def find_avg_change(monthly_changes):
    return sum(monthly_changes)/len(monthly_changes)


def find_greatest_increase(monthly_changes, data):
    print("The app now")
    max_change = max(monthly_changes)
    max_change_index = monthly_changes.index(max_change)
    return find_item_with_index(max_change_index, max_change, data)


def find_greatest_decrease(monthly_changes, data):
    min_change = min(monthly_changes)
    min_change_index = monthly_changes.index(min_change)
    return find_item_with_index(min_change_index, min_change, data)


def find_item_with_index(index, value, data):
    for x, date in enumerate(data):
        if((x - 1) == index):  # setting the index backwards
            return (date, value)


main()
