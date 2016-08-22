#!/usr/bin/env bash

# Usage: bash deploy.sh <APPLICATION NAME>

APP_NAME=$1
ioxclient package .
ioxclient  application install $APP_NAME ./package.tar.gz
ioxclient application activate $APP_NAME --payload activation.json
ioxclient  application start $APP_NAME