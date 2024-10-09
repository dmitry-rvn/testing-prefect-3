from datetime import datetime

from prefect import get_client
from prefect.runtime import flow_run, deployment
from prefect.client.schemas.filters import FlowFilter, FlowRunFilter, DeploymentFilter, FlowFilterName, DeploymentFilterName, FlowRunFilterStartTime
from prefect.client.schemas.objects import FlowRun


def get_today_flow_runs(flow_name: str = None, deployment_name: str = None) -> list[FlowRun]:
    flow_name = flow_name or flow_run.flow_name
    deployment_name = deployment_name or deployment.name
    client = get_client(sync_client=True)
    flow_runs = client.read_flow_runs(
        flow_filter=FlowFilter(name=FlowFilterName(any_=[flow_name])),
        deployment_filter=DeploymentFilter(name=DeploymentFilterName(any_=[deployment_name])),
        flow_run_filter=FlowRunFilter(start_time=FlowRunFilterStartTime(after_=datetime.now().date()))
    )
    return flow_runs
