from flows.processing.flow import flow_func, task_func


def test_processing_task():
    assert task_func() == 'Task finished'


def test_processing_flow():
    assert flow_func() == 'Task finished and Flow finished'
