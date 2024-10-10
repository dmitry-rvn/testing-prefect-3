"""
Flows validation.
"""
import importlib.util
import inspect
import os
import sys

from prefect.flows import Flow


def get_flows_from_module(module_path: str) -> list[Flow]:
    module_name = os.path.basename(module_path).replace('.py', '')
    spec = importlib.util.spec_from_file_location(module_name, module_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    flows = [obj for name, obj in inspect.getmembers(module) if isinstance(obj, Flow)]
    return flows


def validate_flow(flow: Flow):
    for attribute in ('name', 'description', 'timeout_seconds'):
        assert getattr(flow, attribute) is not None, f'You should set {attribute} in `flow` decorator'


def validate_flows_from_module(module_path: str):
    flows = get_flows_from_module(module_path)
    for flow in flows:
        validate_flow(flow)


if __name__ == '__main__':
    module_path = sys.argv[-1]
    validate_flows_from_module(module_path)
