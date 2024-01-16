if __name__ == "__main__":
    # Read input from the user
    n = int(input())
    scores = list(map(int, input().split()))

    # Remove duplicates and sort the scores in descending order
    unique_sorted_scores = sorted(set(scores), reverse=True)

    # Find and print the runner-up score
    runner_up_score = unique_sorted_scores[1]
    print(runner_up_score)
