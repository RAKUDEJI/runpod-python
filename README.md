<div align="center">
<h1>RunPod | Python Library </h1>

[![CI | Code Quality](https://github.com/runpod/runpod-python/actions/workflows/ci_pylint.yml/badge.svg)](https://github.com/runpod/runpod-python/actions/workflows/ci_pylint.yml)
&nbsp;
[![CI | Unit Tests](https://github.com/runpod/runpod-python/actions/workflows/CI_tests.yml/badge.svg)](https://github.com/runpod/runpod-python/actions/workflows/CI_tests.yml)

</div>

Official Python library for RunPod API &amp; SDK.

## Table of Contents

- [Table of Contents](#table-of-contents)
- [Installation](#installation)
- [SDK - Serverless Worker](#sdk---serverless-worker)
  - [Quick Start](#quick-start)
- [API Language Library](#api-language-library)
- [Directory](#directory)
- [Community and Contributing](#community-and-contributing)

## Installation

```bash
pip install runpod
```

## SDK - Serverless Worker

This python package can also be used to create a serverless worker that can be deployed to RunPod as a custom endpoint API.

### Quick Start

Create an python script in your project that contains your model definition and the RunPod worker start code. Run this python code as your default container start command:

```python
import runpod

MODEL = 'YOUR_MODEL'

def run(job):
    # Your inference code here
    return MODEL.predict(job.input)

runpod.serverless.start({"handler": run})
```

Make sure that this file is ran when your container starts. This can be accomplished by calling it in the docker command when you setup a template at [runpod.io/console/serverless/user/templates](https://www.runpod.io/console/serverless/user/templates) or by setting it as the default command in your Dockerfile.

See our [blog post](https://www.runpod.io/blog/serverless-create-a-basic-api) for creating a basic Serverless API, or view the [details docs](https://docs.runpod.io/serverless-ai/custom-apis) for more information.

## API Language Library

When interacting with the RunPod API you can use this library to make requests to the API.

```python
import runpod

runpod.api_key = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```

## Directory

```
.
├── docs               # Documentation
├── runpod             # Package source code
└── tests              # Package tests
```

## Community and Contributing

We welcome both pull requests and issues on [GitHub](https://github.com/runpod/runpod-python). Bug fixes and new features are encouraged.

<div align="center">

<a target="_blank" href="https://discord.gg/pJ3P2DbUUq">![Discord Banner 2](https://discordapp.com/api/guilds/912829806415085598/widget.png?style=banner2)</a>

</div>
