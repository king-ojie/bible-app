# Variables
$RESOURCE_GROUP="bible-llm-rg"
$CLUSTER_NAME="bible-llm-cluster"
$LOCATION="eastus"
$NODE_COUNT=1

# Login to Azure
#az login

# Create resource group
# az group create --name $RESOURCE_GROUP --location $LOCATION

# Create AKS cluster
# az aks create --resource-group $RESOURCE_GROUP --name $CLUSTER_NAME --node-count $NODE_COUNT --enable-managed-identity --generate-ssh-keys

# Get AKS credentials
az aks get-credentials --resource-group $RESOURCE_GROUP --name $CLUSTER_NAME


