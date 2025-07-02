# Todo Python

## Prerequisite

1. Python 3.12+
2. `uv` for local development

## Development

```shell
uv python pin 3.12
uv sync
uv run uvicorn app:app --host 0.0.0.0 --port 8080
```

## Deployment

### OpenShift

```shell
oc apply -k ./openshift
```

### 3scale

Optionally to use 3scale, follow the steps below.

1. `oc adm policy add-cluster-role-to-user view system:serviceaccount:3scale-project:amp`

2. Import the product

3. Create application plan, name it something like `Basic`

4. Create application and name it something like `Great Todo` and join the default `John Doe` user and application plan you just created together
