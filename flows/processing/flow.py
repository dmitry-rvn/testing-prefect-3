from prefect import flow, task


@task
def task_func():
    return 'Task finished'


@flow(name='Processing', timeout_seconds=60 * 60 * 5)
def flow_func():
    """
    Flow description
    """
    task_out = task_func()
    return f'{task_out} and Flow finished'
