# Task Manager CLI

A command-line interface (CLI) application for managing tasks written in Python. This tool allows you to create, list, update, and manage tasks with different statuses.

## Features

- Create new tasks with title and description
- List all tasks
- Filter tasks by status (todo, in-progress, done)
- Update task titles
- Change task status
- Delete tasks
- Persistent storage using JSON

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Yisusocanto/CLI-with-Python.git
cd CLI-with-Python
```

2. Make sure you have Python 3.x installed

## Usage

### Basic Commands

```bash
# Add a new task
python my-cli.py add "Task Title" "Task Description"

# List all tasks
python my-cli.py list

# List tasks by status
python my-cli.py list-todo
python my-cli.py list-in-progress
python my-cli.py list-done

# Update task status
python my-cli.py mark-todo <task_id>
python my-cli.py mark-in-progress <task_id>
python my-cli.py mark-done <task_id>

# Update task title
python my-cli.py update <task_id> "New Title"

# Delete a task
python my-cli.py delete <task_id>
```

### Task Structure

Each task contains:
- Unique ID
- Title
- Description
- Status (todo/in-progress/done)
- Creation timestamp
- Last update timestamp

## Data Storage

Tasks are stored in a `tasks.json` file in the same directory as the script. The file is created automatically when adding the first task.

## Error Handling

The application includes basic error handling for:
- File operations
- Invalid task IDs
- Invalid commands

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is licensed under the MIT License - see the LICENSE file for details.