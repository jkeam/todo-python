# Todo Python

## Prerequisite

1. OpenShift with 3scale installed
2. You must have cluster-admin access

## Setup

```shell
# deploy app
oc apply -f ./openshift

# give 3scale service account access to see openshift services
oc adm policy add-cluster-role-to-user view system:serviceaccount:3scale-project:amp
```
