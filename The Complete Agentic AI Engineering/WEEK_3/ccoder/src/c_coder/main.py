#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from c_coder.crew import CCoder

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")



def run():
    """
    Run the crew.
    """
    result = CCoder().crew().kickoff()
    print(result.raw)

if __name__ == "__main__":
    run()