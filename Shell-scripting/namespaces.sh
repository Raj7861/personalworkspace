#!/bin/bash


read -p "Enter the namespace: " NAMESPACE
namespace=$(echo "$NAMESPACE" | tr '[:upper:]' '[:lower:]')


if [[ $namespace == "scsm-uat" || $namespace == "wmsuat" ]]; then
  kubectl --context stagealot get ns $namespace
  echo "Valid namespace entered."
else
  echo "Invalid namespace entered."
fi
