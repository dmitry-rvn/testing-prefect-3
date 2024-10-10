from prefect import flow, task

from utils.common import generate_flow_run_name


@task
def task_func():
    return 'Task finished'


@flow(
    name='Processing',
    timeout_seconds=60 * 60 * 5,
    flow_run_name=generate_flow_run_name
)
def flow_func():
    """
    Flow description
    """
    task_out = task_func()
    return f'{task_out} and Flow finished'
