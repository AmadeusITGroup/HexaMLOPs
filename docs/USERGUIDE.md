# USER GUIDE 

## 1. Prerequisites



| File/Folder       | Description                                                                 |
|-------------------|-----------------------------------------------------------------------------|
| config.yaml     | This file includes the configuration details of your AML workspace.         |
| training.yaml     | Specifics regarding the training pipeline job on the AML workspace.         |
| src folder        | Contains the source code for all the steps involved in your training pipeline. The number of folders corresponds to the number of steps within your pipeline. For instance, if you have preprocess, train, and evaluate steps, you need to organize your source code for those steps in 3 folders. The name of each folder should match the source code file. |

 
## 2. Using config.yaml
This file contains the configuration of infrastructure and resources. It is served as input for available command lines of the framework in order to generate `.yaml` files which are required as inputs for common ML operations using Azure ML CLI such as:
- model training
- model register
- model deployment

### 2.1 Model training
This file is used with `training.yaml` file to generate `pipeline.yaml` file which is the input file for Azure ML CLI `az ml job create -f`

####
| Fields                       | Configuration                                                                 | Description                                                                 | Default value                                                                 |
|------------------------------|-------------------------------------------------------------------------------|-----------------------------------------------------------------------------|-------------------------------------------------------------------------------|
| resource_group               | Resource group of AML workspace                                               |                                                                             |                                               |
| workspace_name               | Name of AML workspace                                                         |                                                                             |                                                        |
| location                     | Location of AML workspace                                                     |                                                                             |                                                                   |
| experiment_name              | Name of the experiment. It will group your job runs on AML workspace under the same folder. |                                                                             |                                                                  |
| tags                         | key:value pair, e.g “tag:tag_value”                                     |                                                                             |                                                                               |

#### Training Phase specific fields



| Fields                       | Configuration                                                                 | Description                                                                 | Default value                                                                 |
|------------------------------|-------------------------------------------------------------------------------|-----------------------------------------------------------------------------|-------------------------------------------------------------------------------|
| source_code_path             | Reference source code starting from the root repo            |                                                                             |                                                                               |
| compute                      | Compute is to be checked and created if not yet available on Azure ML         | Note: unprovisioned nodes still contribute to quota usage even when compute clusters are not in use |                                                                               |
| compute_name                 | Name of the compute. If already created, only name needs to be mentioned in the template file. For a new compute cluster, refer to the following config and declare them in the template file |                                                                             |                                                                               |
| compute_type                 | Type of compute that runs AZ job. The default value is Az managed compute.     | Link for compute types available on AML : Understand compute targets - Azure Machine Learning | amlcompute                                                                    |
| vm_size                      | Size of the VM                                                                | Link for available VM types: Understand compute targets - Azure Machine Learning | Note: some VMs types might not available at your region quota. This needs to be checked before creating new compute target. | STANDARD_D13_V2                                                               |
| max_instances                | Maximum number of instances of your compute cluster                           |                                                                             | 2                                                                             |
| min_instances                | Minimum number of instances of your compute cluster                           |                                                                             | 0                                                                             |
| idle_seconds_before_scale_down | Number of seconds of a vm before scaling down                                 |                                                                             | 120                                                                           |
| tier                         | Tier of your compute cluster:dedicated or low_priority                        | Low-priority vms can lower your cost but don’t have guaranteed availability and might be preempted while in used. | dedicated                                                                     |
| subnet                       | Subnet to be used for this particular compute cluster.  Ensure you use the correct subnet as incorrect subnet will not let your compute pull images from container registry. |     |  |

#### Environment

| Fields                       | Configuration                                                                 | Description                                                                 | Default value                                                                 |
|------------------------------|-------------------------------------------------------------------------------|-----------------------------------------------------------------------------|-------------------------------------------------------------------------------|
| environment_name             | Name of the environment                                                       | Like compute, if you want to use your current environment, you can declare its name in the template file |                                                                               |
| environment_version          | Version of the environment                                                    | You can create a new version of your environment by bumping up the version number. If you want to use current environment, remember to specify the version you want to use | latest                                                                        |
| environment_image            | A new image will be built on the base image and dependencies you need to specify in the field below. Depends on your job, you can choose a different image |                                                                             | mcr.microsoft.com/azureml/intelmpi2018.3-ubuntu16.04:20200821.v1              |
| environment_dependencies     | Conda dependencies                                                            | The dependencies will be used to create a conda.yaml file. You can follow this format: |                                                                               |
|                              |                                                                               | environment_dependencies: Packages under the first indentation are ones to be installed using conda. For ones to be installed with pip, you can declare it under pip. |                                                                               |

### 2.2 Model register

Specify the following configuration in the config file to generate input for Azure ML command line `az ml model create ` : 

| Configuration | Type    | Description                                              |
|---------------|---------|----------------------------------------------------------|
| model_name    | str     | name of the model                                        |
| model_version | integer | version of the model                                     |
| model_path    | str     | path of the model to register                            |
| model_type    | str     | options: custom_model, mlflow_model, and triton_model    |

#### Supported model_path types

| Type               | Format                              | Syntax                                                      |
|--------------------|-------------------------------------|-------------------------------------------------------------|
| local file         | model path relative to the location of the config file |                                                             |
| output of a job    | reference from the job name         | azureml://jobs/<job_id>/outputs/<folder_name>/              |
| reference from datastore path |                         | azureml://datastores/<datastore-name>/paths/<path_on_datastore> |

### 2.3 Model deployment

#### Batch deployment
The generated file using these configuration is to be used with this Azure ML CLI `az ml batch-deployment create -f`
In addition to  the below configuration, details of `compute` and `environment` need to be added as well. Please refer to the previous section for more information.


| Fields                       | Configuration                                                                 | Type    | Description                                                                 | Default value                                                                 |
|------------------------------|-------------------------------------------------------------------------------|---------|-----------------------------------------------------------------------------|-------------------------------------------------------------------------------|
| inference                   | endpoint_type: batch                                                          | object  | In order to declare the configuration of your endpoint, you can add the following fields under inference phase, batch type. All configurations below should be inside this inference object. |                                                                               |
| endpoint_name                |                                                                               | string  | Name of the endpoint. This name will be referenced in the API url as : "https://{{endpoint_name}}.{{location}}.inference.ml.azure.com/score". Note that your endpoint name is required to be unique in your region |                                                                               |
| deployment_name              |                                                                               | string  | Name of the deployment under your endpoint. You can have many deployment under the endpoint. The default endpoint will be called once you call the endpoint |                                                                               |
| model                        |                                                                               | string  | azureml:<model-name>:<model-version>                                        |                                                                               |
| max_concurrency_per_instance |                                                                               | integer | Maximum number of parallel batch job runs per instance                      | 1                                                                             |
| error_threshold              |                                                                               | integer | The number of file failures that should be ignored                          | -1                                                                            |
| logging_level                |                                                                               | string  | Log verbosity                                                               | warning, info, debug                                                          | info                                                                          |
| mini_batch_size              |                                                                               | integer | The number of files the code_configuration.scoring_script can process in one run() call | 10                                                                            |
| max_retries                  |                                                                               | integer | The maximum number of retries for a failed or timed-out mini batch          | 3                                                                             |
| timeout                      |                                                                               | integer | The timeout in seconds for scoring a single mini batch. Use larger values when the mini-batch size is bigger or the model is more expensive to run. | 30                                                                            |
| output_action                |                                                                               |         | Indicates how the output should be organized in the output file. Use summary_only if you are generating the output files as indicated at Customize outputs in model deployments. Use append_row if you are returning predictions as part of the run() function return statement. | append_row, summary_only                                                      | append_row                                                                    |
| output_file_name             |                                                                               | string  | Name of the batch scoring output file                                       | predictions.csv                                                               |
| environment_variables        |                                                                               | object  | Dictionary of environment variable key-value pairs to set for each batch scoring job. |                                                                               |
| score_script                 |                                                                               | string  | Path of your scoring script                                                 |                                                                               |

#### Online deployment
Similarly, the generated file using these configuration is to be used with this Azure ML CLI `az ml online-deployment create -f`


| Fields                              | Configuration                                                                 | Type    | Description                                                                 | Default value                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------|---------|-----------------------------------------------------------------------------|-------------------------------------------------------------------------------|
| inference                           | endpoint_type: online                                                         | object  | In order to declare the configuration of your endpoint, you can add the following fields under inference phase, online type. All configurations below should be inside this inference object. |                                                                               |
| endpoint_name                       |                                                                               | string  | Name of the endpoint. This name will be referenced in the API url as : "https://{{endpoint_name}}.{{location}}.inference.ml.azure.com/score". Note that your endpoint name is required to be unique in your region. Endpoint names must: Begin with a letter, Be 3-32 characters in length, Only consist of letters and numbers. |                                                                               |
| deployment_name                     |                                                                               | string  | Name of the deployment under your endpoint. You can have many deployment under the endpoint. The default endpoint will be called once you call the endpoint. Deployment names must: Begin with a letter, Be 3-32 characters in length, Only consist of letters and numbers. |                                                                               |
| model                               |                                                                               | string  | azureml:<model-name>:<model-version>                                        |                                                                               |
| app_insights_enabled                |                                                                               | boolean | Whether to enable integration with the Azure Application Insights instance associated with your workspace. | false                                                                         |
| environment_variables               |                                                                               | object  | Dictionary of environment variable key-value pairs to set in the deployment container. You can access these environment variables from your scoring scripts. |                                                                               |
| score_script                        |                                                                               | string  | Path of your scoring script                                                 |                                                                               |
| request                             |                                                                               |         | Scoring request settings for the deployment                                 |                                                                               |
| request_timeout_ms                  |                                                                               | integer | The scoring timeout in milliseconds. Note that the maximum value allowed is 180000 milliseconds. See limits for online endpoints for more. | 5000                                                                          |
| max_concurrent_requests_per_instance|                                                                               | integer | The maximum number of concurrent requests per instance allowed for the deployment. | 1                                                                             |
| probe settings                      |                                                                               |         | Liveness probe settings for monitoring the health of the container regularly. Readiness probe settings for validating if the container is ready to serve traffic. |                                                                               |
| initial_delay                       |                                                                               | integer | The number of seconds after the container has started before the probe is initiated. Minimum value is 1. | 10                                                                            |
| period                              |                                                                               | integer | How often (in seconds) to perform the probe.                                | 10                                                                            |
| timeout                             |                                                                               | integer | The number of seconds after which the probe times out. Minimum value is 1.  | 2                                                                             |
| success_threshold                   |                                                                               | integer | The minimum consecutive successes for the probe to be considered successful after having failed. Minimum value is 1 for readiness probe. The value for liveness probe is fixed as 1. | 1                                                                             |
| failure_threshold                   |                                                                               | integer | When a probe fails, the system will try failure_threshold times before giving up. Giving up in the case of a liveness probe means the container will be restarted. In the case of a readiness probe the container will be marked Unready. Minimum value is 1. | 30                                                                            |


## 3. training.yaml

This file includes the steps of your training job pipeline, inputs and outputs of the pipeline. Together with `config.yaml` as inputs, you can generate a `pipeline.yaml` to be used with the command of Azure ML CLI `az ml job create -f`

### Inputs

| Fields   | Configuration                                                                 | Description                                                                 | Default value                                                                 |
|----------|-------------------------------------------------------------------------------|-----------------------------------------------------------------------------|-------------------------------------------------------------------------------|
| inputs   | A list of dictionaries which are inputs to the pipeline job. They are global pipeline inputs and can be referenced in step job input as parent.inputs.<pipeline_input_name>. For each input, 3 key and value pairs are required: name, type (optional if use default value), and path. |                                                                             |                                                                               |
| name     | Name of the input                                                             | It is recommended that you have the same name as the parameter that uses this input in your source code |                                                                               |
| type     | Allowed values: uri_file, uri_folder, mltable, mlflow_model. Since this workflow specifically support training pipeline job on AML, we only support the above values following AML standard. If the type is uri_folder, you do not need to specify anything. | uri_folder                                                                    |
| path     | Path of the input. If the input is a local file/folder in your repo and to be uploaded to AML workspace, you can reference it as a relative path : ../path_from_root. Take Example Project above as an example, if you want to use hyperparameter.yaml as input, you can reference it as: ../TST/src/train/hyperparameter.yaml |                                                                             |                                                                               |


### Output

| Fields   | Configuration                                                                 | Description                                                                 | Default value                                                                 |
|----------|-------------------------------------------------------------------------------|-----------------------------------------------------------------------------|-------------------------------------------------------------------------------|
| name     | Name of the output                                                            | Similar to input, it is recommended that you have the same name as the argument that uses this input in your source code. |                                                                               |
| type     | Similar to input type                                                         |                                                                             | uri_folder                                                                    |
| mode     | This indicates how to deliver outputs to the destination storage. Supported mode: rw_mount: read-write mount, the output directory will be a mounted directory upload: outputs will be uploaded at the end of the job | rw_mount                                                                     |

### Steps

| Fields   | Configuration                                                                 | Description                                                                 | Default value                                                                 |
|----------|-------------------------------------------------------------------------------|-----------------------------------------------------------------------------|-------------------------------------------------------------------------------|
| steps    | A list of dictionaries which are sub tasks in your training pipeline. Currently, we are supporting the definition of the same compute and environment for all pipeline steps. For each step, name, input and output fields need to be declared |                                                                             |                                                                               |
| name     | Name of the step                                                              | This name is required to be the same as the folder under src that contains the source code of this step |                                                                               |
| inputs   | Inputs is a list of dictionaries. Under each input, you need to declare a key value pair mapping. Key is the parameter of the .py script (source code) that will take the input. Value is either a pipeline input or output from a previous step. Pipeline input: parent.inputs.<input_name> Step output: <step_name>.outputs.<output_name> |                                                                             |                                                                               |
| outputs  | Outputs is a list of dictionaries. Same as input, for each output you need to declare a key value pair mapping. However, output does not need to be already declared in previous step. Therefore, the value can be empty if this is a new folder. Note that keys are the same as the arguments use them in the source code. |                                                                             |                                                                               |



 

