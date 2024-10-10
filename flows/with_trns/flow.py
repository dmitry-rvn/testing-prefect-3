from prefect import flow, task, get_run_logger
from prefect.transactions import transaction

from utils.common import generate_flow_run_name


@task
def download():
    return 'New data downloaded'


@task
def backup_old_data():
    logger = get_run_logger()
    logger.info('Old data backuped')


@task
def delete_old_data():
    logger = get_run_logger()
    backup_old_data()
    logger.info('Old data deleted')


@task
def insert_new_data(fail: bool = False):
    logger = get_run_logger()
    if fail:
        raise ValueError('Error while inserting data')
    logger.info('Data inserted')


@insert_new_data.on_commit
def delete_old_data_backup(txn):
    logger = get_run_logger()
    logger.info('Temp table with old (deleted) data removed')


@backup_old_data.on_rollback
def restore_deleted_data(txn):
    logger = get_run_logger()
    # copy data from temp to original table
    logger.info('Old (deleted) data restored')
    delete_old_data_backup(txn)


@flow(
    name='Pipe with transaction',
    timeout_seconds=60 * 60 * 5,
    flow_run_name=generate_flow_run_name
)
def flow_func(fail_on_insert: bool = False):
    """
    Flow description
    """
    download()
    with transaction():
        delete_old_data()
        insert_new_data(fail=fail_on_insert)
