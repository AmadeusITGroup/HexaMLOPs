
# File names
AZURE_WORKSPACE="workspace.env"
PIPELINE="pipeline.yaml"
PIPELINE_NO_VALUE="pipeline_no_value.yaml"
TRAINING_DEPLOYMENT="training_deployment.yaml"
AZ_ONLINE_INFERENCE="online_inference_deployment.yaml"
AZ_BATCH_INFERENCE="batch_inference_deployment.yaml"
INPUTS_FILE = "inputs.yaml"
TRAINING_CONDA_FILE = "training_conda.yaml"
INFERENCE_CONDA_FILE = "inference_conda.yaml"

#General
ENGINE_ML = "engine_ml"

# AZURE ML
AZURE_ML = "azureml"

EXPERIMENT_NAME = "experiment_name"
RUN_NAME = "run_name"
DESCRIPTION = "description"
MODEL_NAME = "model_name"
MODEL_PATH = "model_path"
MODEL_VERSION = "model_version"
MODEL_TYPE = "model_type"
DEFAULT_MODEL_TYPE = "custom_model"
DEFAULT_EXPERIMENT_NAME = ""

TRAINING_FILE_PATH = "training_file_path"
SOURCE_CODE_PATH = "source_code_path"
ENVIRONMENT_DEPENDENCIES = "environment_dependencies"

# AZURE ML resource
RESOURCE_GROUP = "resource_group"
DEFAULT_RESOURCE_GROUP = ""
WORKSPACE_NAME = "workspace_name"
DEFAULT_WORKSPACE_NAME = ""
LOCATION = "location"
DEFAULT_LOCATION = ""
TAGS = "tags"
DEFAULT_TAGS = ""

TYPE = "type"
COMPUTE = "compute"
COMPUTE_NAME = "compute_name"
COMPUTE_TYPE = "compute_type"
DEFAULT_COMPUTE_TYPE = "amlcompute"
VM_SIZE = "vm_size"
DEFAULT_VM_SIZE = "STANDARD_D13_V2"
MAX_INSTANCES = "max_instances"
DEFAULT_MAX_INSTANCES = "2"
MIN_INSTANCES = "min_instances"
DEFAULT_MIN_INSTANCES = "0"
IDLE_SECONDS_BEFORE_SCALE_DOWN = "idle_seconds_before_scale_down"
DEFAULT_IDLE_SECONDS_BEFORE_SCALE_DOWN = "120"
TIER = "tier"
DEFAULT_TIER = "dedicated"
SUBNET = "subnet"
DEFAULT_SUBNET = ""

ENVIRONMENT = "environment"
ENVIRONMENT_NAME = "environment_name"
ENVIRONMENT_VERSION = "environment_version"
DEFAULT_ENVIRONMENT_VERSION = "latest"
ENVIRONMENT_IMAGE = "environment_image"
DEFAULT_ENVIRONMENT_IMAGE = "mcr.microsoft.com/azureml/intelmpi2018.3-ubuntu16.04:20200821.v1"

JOB_NAME = "name"
INPUTS = "inputs"
OUTPUTS = "outputs"
STEPS = "steps"
COMPONENT = "component"
CODE = "code"
COMMAND = "command"
PY_EXT = ".py"

EMPTY_CONSTANT = None
FALSE_CONSTANT = False

# AZURE ML template schema
BATCH_PIPELINE_COMPONENT_SCHEMA = "https://azuremlschemas.azureedge.net/latest/pipelineComponentBatchDeployment.schema.json"
PIPELINE_JOB_SCHEMA = "https://azuremlschemas.azureedge.net/latest/pipelineJob.schema.json"
MANAGED_ONLINE_INFERENCE_SCHEMA = "https://azuremlschemas.azureedge.net/latest/managedOnlineDeployment.schema.json"
MANAGED_BATCH_INFERENCE_SCHEMA = "https://azuremlschemas.azureedge.net/latest/batchDeployment.schema.json"

# AZURE ML DEPLOYMNENT

TRAINING_PHASE = "training"
INFERENCE_PHASE = "inference"
ENDPOINT_TYPE = "endpoint_type"
BATCH_INFERENCE = "batch"
ONLINE_INFERENCE = "online"
ENDPOINT_NAME = "endpoint_name"
DEPLOYMENT_NAME = "deployment_name"
MODEL = "model"
SCORING_SCRIPT_PATH = "scoring_script_path"
INSTANCE_COUNT = "instance_count"

#AZURE ML Batch Inference
BATCH_MODEL_TYPE = "model"
MAX_CONCURRENCY_PER_INSTANCE = "max_concurrency_per_instance"
ERROR_THRESHOLD = "error_threshold"
LOGGING_LEVEL = "logging_level"
MINI_BATCH_SIZE = "mini_batch_size"
MAX_RETRIES = "max_retries"
TIMEOUT = "timeout"
OUTPUT_ACTION = "output_action"
OUTPUT_FILE_NAME = "output_file_name"

# AZURE ML Online Inference 
DOCKER_FILE_PATH = "docker_file_path"
EGRESS_PUBLIC_NETWORK_ACCESS_DEFAULT = "disabled"
INSTANCE_TYPE = "instance_type"
ENVIRONMENT_VARIABLES= "environment_variables"
APP_INSIGHTS_ENABLED = "app_insights_enabled"
REQUEST_TIMEOUT_MS = "request_timeout_ms"
MAX_CONCURRENT_REQUESTS_PER_INSTANCE = "max_concurrent_requests_per_instance"
MAX_QUEUE_WAIT_MS = "max_queue_wait_ms"
LIVENESS_PROBE_INITIAL_DELAY = "liveness_probe_initial_delay"
READINESS_PROBE_INITIAL_DELAY = "readiness_probe_initial_delay"
LIVENESS_PROBE_PERIOD = "liveness_probe_period"
READINESS_PROBE_PERIOD = "readiness_probe_period"
LIVENESS_PROBE_TIMEOUT = "liveness_probe_timeout"
READINESS_PROBE_TIMEOUT = "readiness_probe_timeout"
LIVENESS_PROBE_FAILURE_THRESHOLD = "liveness_probe_failure_threshold"
READINESS_PROBE_FAILURE_THRESHOLD = "readiness_probe_failure_threshold"
LIVENESS_PROBE_SUCCESS_THRESHOLD = "liveness_probe_success_threshold"
READINESS_PROBE_SUCCESS_THRESHOLD = "readiness_probe_success_threshold"