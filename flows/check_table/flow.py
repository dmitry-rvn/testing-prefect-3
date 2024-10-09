from pathlib import Path

from prefect import flow, task
from prefect.states import Cancelled
from prefect.events import emit_event

from utils.common import get_today_flow_runs


@task(retries=60, retry_delay_seconds=60)
def check(table: str):
    with open(Path(__file__).parent / 'readiness.txt') as f:
        data = f.read().strip()
    if table not in data:
        raise ValueError(f'Table {table} not ready yet')


@flow(name='Table readiness checker')
def flow_func(table: str, skip_if_ran_today: bool = True):
    if skip_if_ran_today:
        if get_today_flow_runs():
            return Cancelled()

    check(table)
    resource = f'dwh.{table}'
    event = f'{resource}.ready'
    emit_event(event=event, resource={'prefect.resource.id': resource})
