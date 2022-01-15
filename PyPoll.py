import os
import csv
import math


def main():
    print("Election Results")
    print("----------------")

    total_votes = 0

    with open("election_data.csv") as file:
        reader = csv.reader(file)
        next(reader)
        data = tuple(reader)
        canditates = dict()

        for outter in data:  # Picking candidates
            if(outter[2] in canditates):
                continue
            else:
                canditates[outter[2]] = 0

        for outter in data:  # counting votes for each candiate
            for canditate in canditates:
                if(canditate == outter[2]):
                    canditates[canditate] += 1

        for cand in canditates:
            total_votes += canditates[cand]

        print(f"Total votes : {total_votes}")
        print("----------------")

        percentage = 0.0
        most_votes = 0
        winner = None

        for key in canditates:
            # finding percentage for each candidate
            percentage = (canditates[key]/total_votes) * 100
            if(percentage > most_votes):  # Checking if the canditate has the most votes
                winner = key
                most_votes = percentage
            print(f"{key} {round(percentage)}% ({canditates[key]})")

        print("----------------")
        print(f"Winner : {winner}")
        print("----------------")


main()
