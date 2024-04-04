from js import inputFileName
from gwas_sumstats_tools.format import format
from datetime import datetime
from pathlib import Path
import json

# local file system is mounted in /data
input_path = Path("/data") / inputFileName
startTime = datetime.now()
output=format(filename=input_path,generate_config=True)
print("this if the output:", output)
f"{json.dumps(output, indent=4)}"