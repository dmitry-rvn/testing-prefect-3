from prefect import flow, task


@task
def task_func():
    return 'Task finished'


@flow(name='Processing')
def flow_func():
    task_out = task_func()
    return f'{task_out} and Flow finished'
