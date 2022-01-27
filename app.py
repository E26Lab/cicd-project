#!/usr/bin/env python3
import aws_cdk as cdk
from cicd_project.cicd_project_stack import MyPipelineStack

app = cdk.App()
MyPipelineStack(app, "MyPipelineStack", 
<<<<<<< HEAD
    env=cdk.Environment(account="465444432665", region="us-east-1")
=======
    env=cdk.Environment(account="465444432665", region="us-east-2")
>>>>>>> 3a851f396ff19d01bdef4f7a64ac86b5ec61f3a1
)

app.synth()
