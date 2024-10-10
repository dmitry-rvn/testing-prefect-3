from prefect import flow


@flow(name='Failing flow')
def flow_func():
    raise ValueError('Exception text')
