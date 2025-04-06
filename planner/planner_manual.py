from semantic_kernel import Kernel, Planner

# Initialize the kernel
kernel = Kernel()


# Define some example functions
def add_task(task):
    print(f"Adding task: {task}")


def complete_task(task):
    print(f"Completing task: {task}")


# Register the functions with the kernel
kernel.register_function("add_task", add_task)
kernel.register_function("complete_task", complete_task)

# Create a planner
planner = Planner(kernel)

# Define a goal
goal = "manage my to-do list"

# Generate a plan
plan = planner.create_plan(goal)

# Execute the plan
for step in plan.steps:
    kernel.invoke_function(step.function_name, *step.args)

print("To-do list managed successfully!")
