"""
Deployment validation.
"""
import sys

import yaml


def validate_deployment_file_content(deployment_file_content: dict):
    assert 'deployments' in deployment_file_content
    for deployment in deployment_file_content['deployments']:
        for attribute in ('name', 'description', 'entrypoint', 'work_pool'):
            assert deployment.get(attribute) is not None, f'You should set `{attribute}` in each deployment'
        assert deployment.get('collision_strategy') == 'CANCEL_NEW', 'You should set `collision_strategy=CANCEL_NEW`'
        assert deployment.get('concurrency_limit') == 1, 'You should set `concurrency_limit=1`'


def validate_deployment_file(filepath: str):
    with open(filepath, encoding='utf-8') as f:
        deployment_file_content = yaml.safe_load(f)
    validate_deployment_file_content(deployment_file_content)


if __name__ == '__main__':
    deployment_filepath = sys.argv[-1]
    validate_deployment_file(deployment_filepath)
