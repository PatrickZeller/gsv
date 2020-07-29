import os
import re
import ast

def expand_vars(filename):
    """expands environment variables and gsv.
    """

    ## deal with env vars first ;)
    expanded_path = os.path.expandvars(filename)

    ## now we deal with gsvs
    pattern = re.compile('@\{[a-zA-Z]*\}')
    gsv_matches = re.findall(pattern, filename)
    gsv = ast.literal_eval(os.environ['GSV'])
    for i in gsv_matches:
        gsv_expanded_path = expanded_path.replace(i, gsv[i.replace("@{", "").replace("}", "")],)
        expanded_path = gsv_expanded_path

    return expanded_path 