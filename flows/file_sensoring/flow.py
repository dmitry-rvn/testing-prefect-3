from pathlib import Path

from prefect import flow
from prefect.events import emit_event


@flow(name='File sensoring')
def flow_func(filepath: str, resource_key: str):
    if Path(filepath).exists():
        resource = f'file.{resource_key}'
        event = f'{resource}.exists'
        emit_event(event=event, resource={'prefect.resource.id': resource})
