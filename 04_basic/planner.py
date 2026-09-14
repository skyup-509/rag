import json

from prompts import PLANNER_PROMPT


FUNCTIONS = [
    "get_files",
    "save_file"
]


def make_plan(llm, user_request, out_dir, files):
    prompt = PLANNER_PROMPT.format(
        user_request=user_request,
        functions=FUNCTIONS
    )

    response = llm.invoke(prompt)

    plan = json.loads(response.content)

    return plan