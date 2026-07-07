# LeetCode Tracker

A CLI app to track your LeetCode progress. Organize problems by status, flag problems to redo, and filter your list by category.

## Requirements

- Python 3.x

## Setup

1. Clone the repository
2. Navigate to the project folder
3. Run the app: `python tracker.py`

No external dependencies required.

## Usage

When you run the app you'll see a summary of your progress and a menu:

```
Todo: 3 | In Progress: 1 | Done: 12 | Redo Queue: 2

--- LeetCode Tracker ---
1. Add problem
2. Update status
3. List problems
4. Mark for redo
5. Quit
```

### Adding a problem

Choose option `1` and enter the problem ID, title, and difficulty. Problems initially have the status of `todo`.

### Updating status

Choose option `2`, enter the problem ID, and set the new status. Valid statuses are: `todo`, `in_progress`, and `done`

### Listing problems

Choose option `3` to filter problems by their status or view redo list.

### Marking for redo

Choose option `4` and enter the problem ID to flag a problem for review. It will appear in the redo list when listing problems.

## Data

Progress will be saved to `data.json` in the project folder.
