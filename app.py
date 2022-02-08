#!/usr/bin/env python3
import os
from aws_cdk import core
from cicd_project.cicd_project_stack import MyPipelineStack

app = core.App()
MyPipelineStack(app, "MyPipelineStack", 
    env={'account' : '465444432665', 'region' : 'us-east-1'}
)

app.synth()