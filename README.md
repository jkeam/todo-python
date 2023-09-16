# Todo Python

## Prerequisite

1. OpenShift with 3scale installed
2. You must have cluster-admin access

## Setup

### OpenShift

Prepare for import

    ```shell
    # deploy app
    oc apply -f ./openshift

    # give 3scale service account access to see openshift services
    oc adm policy add-cluster-role-to-user view system:serviceaccount:3scale-project:amp
    ```

### 3scale

1. Import the product

2. Create application plan, something like Basic

3. Create application and join the default user and application plan together
