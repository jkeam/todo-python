# Todo Python

## Prerequisite

1. OpenShift with 3scale installed
2. You must have cluster-admin access

## Setup

### OpenShift

Prepare for import

    # deploy app
    oc apply -f ./openshift

    # give 3scale service account access to see openshift services
    oc adm policy add-cluster-role-to-user view system:serviceaccount:3scale-project:amp

### 3scale

1. Import the product

2. Create application plan, name it something like `Basic`

3. Create application and name it something like `Great Todo` and join the default `John Doe` user and application plan you just created together
