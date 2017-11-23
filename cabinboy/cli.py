#! /usr/bin/env python

import sys

import click
import crayons
import delegator
import yaml


def _exit(message, exit_code=1):
    sys.stderr.write(f'{message}\n')
    sys.exit(exit_code)


def _error_and_exit(message, exit_code=1):
    _exit(crayons.red(message), exit_code)


def _run_task(name, tasks):
    if name not in tasks.keys():
        _error_and_exit(f'Could not find job named "{name}" in your Taskfile.')

    task = tasks[name]

    if type(task) is str:
        process = delegator.run(task)
        print(process.out)
    elif type(task) is list:
        for subtask in task:
            if subtask in tasks.keys():
                _run_task(subtask, tasks)
            else:
                subtask_process = delegator.run(subtask)
                print(subtask_process.out)


@click.command()
@click.argument('task')
def run(task):
    with open('Taskfile') as taskfile:
        tasks = yaml.load(taskfile.read())

    if len(sys.argv) < 2:
        _error_and_exit(f'Please provide a task to run.')

    _run_task(task, tasks)


if __name__ == '__main__':
    run()
