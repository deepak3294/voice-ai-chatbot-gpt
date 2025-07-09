import os                                       # to interact with operating system 
import sys                                      # for access to run-time system features
from gpt4all import GPT4All                     # uses gpt4all library used for LLM(language model)
 
# Suppress low-level stderr output (DLL load errors)
def load_model(model_name="orca-mini-3b-gguf2-q4_0.gguf"):
    devnull = os.open(os.devnull, os.O_WRONLY)
    stderr_fd = sys.stderr.fileno()
    saved_fd = os.dup(stderr_fd)
    os.dup2(devnull, stderr_fd)  # Hide errors

    model = GPT4All(model_name)

    os.dup2(saved_fd, stderr_fd)  # Restore stderr
    return model

