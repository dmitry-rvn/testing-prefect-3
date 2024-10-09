from pathlib import Path

from prefect import flow


FILEPATH = 'flows/file_sensoring/file_to_wait.txt'


@flow(name='Processing from file')
def flow_func():
    Path(FILEPATH).unlink()
