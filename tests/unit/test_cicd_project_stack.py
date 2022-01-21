import aws_cdk as core
import aws_cdk.assertions as assertions

from cicd_project.cicd_project_stack import CicdProjectStack

# example tests. To run these tests, uncomment this file along with the example
# resource in cicd_project/cicd_project_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = CicdProjectStack(app, "cicd-project")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
