#!/usr/bin/env python3

import argparse
import json
from datetime import datetime
import os

json_file = "tasks.json"

#Functions
def add_task(title, description):
    """Add a new task to the json file"""
    try:
        if not os.path.exists(json_file):
            # create the file if not exist
            with open(json_file, "w") as file:
                json.dump([{"id_count": 0}], file)

        with open(json_file, "r") as file:
            data = json.load(file)

        now = datetime.now()
        date = now.strftime("%d/%m/%Y %H:%M")
        id = data[0]["id_count"] 
        
        task = {
            "id": id + 1,
            "title": title,
            "description": description,
            "status": "todo",
            "created_at": str(date),
            "updated_at": None
            }
            
        data[0]["id_count"] += 1
        data.append(task)

        with open(json_file, "w") as file:
            json.dump(data, file, indent=4)
        print("Task created succesfully")
    except Exception as e:
        print(f"An error ocurred while creating the task {e}")

def list_tasks():
    """List all the tasks in the json file"""
    try:
        with open(json_file, "r") as file:
            data = json.load(file)

        if len(data) < 2:
            print("There are no tasks")
            return

        for num, task in enumerate(data):
            if "title" in task:
                print(f"- {num} | ID: {task['id']} | Title: {task['title']} | Description: {task['description']} | Status: {task['status']} | Created at: {task['created_at']} | Updated at: {task['updated_at']}")
    except Exception as e:
        print(f"An error occurred while listing the tasks: {e}")

def list_tasks_done():
    """List all the tasks done in the json file"""
    try:
        with open(json_file, "r") as file:
            data = json.load(file)

        tasks = [task for task in data if "status" in task and task["status"] == "done"]
        if not tasks:
            print("There are no tasks")
            return

        for num, task in enumerate(tasks):
            print(f"- {num+1} | ID: {task['id']} | Title: {task['title']} | Description: {task['description']} | Status: {task['status']} | Created at: {task['created_at']} | Updated at: {task['updated_at']}")
    except Exception as e:
        print(f"An error occurred while listing the tasks: {e}")

def list_tasks_in_progress():
    """List all the tasks in progress in the json file"""
    try:
        with open(json_file, "r") as file:
            data = json.load(file)

        tasks = [task for task in data if "status" in task and task["status"] == "in-progress"]
        if not tasks:
            print("There are no tasks")
            return

        for num, task in enumerate(tasks):
            print(f"- {num+1} | ID: {task['id']} | Title: {task['title']} | Description: {task['description']} | Status: {task['status']} | Created at: {task['created_at']} | Updated at: {task['updated_at']}")
    except Exception as e:
        print(f"An error occurred while listing the tasks: {e}")

def list_tasks_todo():
    """List all the tasks todo in the json file"""
    try:
        with open(json_file, "r") as file:
            data = json.load(file)

        tasks = [task for task in data if "status" in task and task["status"] == "todo"]
        if not tasks:
            print("There are no tasks")
            return

        for num, task in enumerate(tasks):
            print(f"- {num+1} | ID: {task['id']} | Title: {task['title']} | Description: {task['description']} | Status: {task['status']} | Created at: {task['created_at']} | Updated at: {task['updated_at']}")
    except Exception as e:
        print(f"An error occurred while listing the tasks: {e}")

def delete_task(id):
    """Delete a task from the json file"""
    with open(json_file, "r") as file:
        data = json.load(file)
        for task in data:
            if "id" in task and id == task["id"]:
                data.remove(task)
                print(f"Task {id} delete succesfully")
                with open(json_file, "w") as file2:
                    json.dump(data, file2, indent=4)
                return 
        print("The task not exist")
    with open(json_file, "w") as file:
        json.dump(data, file, indent=4)

def mark_task(id, status):
    """Mark a task with a given status"""
    with open(json_file, "r") as file:
        data = json.load(file)
        for task in data:
            if "id" in task and id == task["id"]:
                if task["status"] == status:
                    print(f"The task is already {status}")
                    return
                now = datetime.now()
                date = now.strftime("%d/%m/%Y %H:%M")
                task["status"] = status
                task["updated_at"] = date
                print(f"Task {id} is now {status}")

                with open(json_file, "w") as file2:
                    json.dump(data, file2, indent=4)
                    return
    print("The task does not exist")
    return

def update_task(id, new_title):
    """Update the title of a task"""
    with open(json_file, "r") as file:
        data = json.load(file)

        for task in data:
            if "id" in task and id == task["id"]:
                now = datetime.now()
                date = now.strftime("%d/%m/%Y %H:%M")
                task["title"] = new_title
                task["updated_at"] = date
                print(f"The task's title was change to: {new_title}")

                with open(json_file, "w") as file2:
                    json.dump(data, file2, indent=4)
                    return
    print("The task not exist")
    return


def main():

    #Parser
    parse = argparse.ArgumentParser("Task Tracker", description="Task manager")

    subparsers = parse.add_subparsers(dest="command")

    #Create Task
    add_task_parser = subparsers.add_parser("add", description="add a new task", help="title description")
    add_task_parser.add_argument("title", type=str, help="title of the task")
    add_task_parser.add_argument("description", type=str, help="description of the task")

    #List Tasks
    subparsers.add_parser("list", description="list all the tasks")

    #List Tasks Done
    subparsers.add_parser("list-done", description="list the tasks done")

    #List Tasks Done
    subparsers.add_parser("list-in-progress", description="list the tasks in-progress")

    #List Tasks Done
    subparsers.add_parser("list-todo", description="list the tasks todo")

    #delete Tasks
    delete_task_parser = subparsers.add_parser("delete", description="Delete one task", help="tasks_id")
    delete_task_parser.add_argument("id", type=int, help="task's id")

    #mark-in-progress
    mark_in_progress_parser = subparsers.add_parser("mark-in-progress", description="mark-in-progress a task", help="mark-in-progress task_id")
    mark_in_progress_parser.add_argument("id", type=int, help="task_id")

    #mark-done
    mark_done_parser = subparsers.add_parser("mark-done", description="mark-done a task", help="mark-done task_id")
    mark_done_parser.add_argument("id", type=int, help="task_id")

    #mark-todo
    mark_done_parser = subparsers.add_parser("mark-todo", description="mark-todo a task", help="mark-todo task_id")
    mark_done_parser.add_argument("id", type=int, help="task_id")

    #update task
    update_task_parser = subparsers.add_parser("update", description="update a task", help="update task_id new_title")
    update_task_parser.add_argument("id", type=int, help="task_id")
    update_task_parser.add_argument("new_title", type=str, help="new title of the task")


    args = parse.parse_args()

    if args.command == "add":
        add_task(args.title, args.description)
    elif args.command == "list":
        list_tasks()
    elif args.command == "list-done":
        list_tasks_done()
    elif args.command == "list-in-progress":
        list_tasks_in_progress()
    elif args.command == "list-todo":
        list_tasks_todo()
    elif args.command == "delete":
        delete_task(args.id)
    elif args.command == "mark-in-progress":
        mark_task(args.id, "in-progress")
    elif args.command == "mark-done":
        mark_task(args.id, "done")
    elif args.command == "mark-todo":
        mark_task(args.id, "todo")
    elif args.command == "update":
        update_task(args.id, args.new_title)

if __name__ == "__main__":
    main()