
from nornir import InitNornir
from nornir_netmiko.tasks import netmiko_send_command
from nornir_utils.plugins.functions import print_result
from nornir_utils.plugins.tasks.files import write_file
from nornir_netmiko.tasks import netmiko_send_config, netmiko_send_command
from datetime import date
import pathlib
from contextlib import redirect_stdout
import sys
import time


validation = ''
 
def backup_configurations(task):
    config_dir = "config-archive"
    date_dir = config_dir + "/" + str(date.today())
    pathlib.Path(config_dir).mkdir(exist_ok=True)
    pathlib.Path(date_dir).mkdir(exist_ok=True)
    r = task.run(task=netmiko_send_command,command_string="show run", enable=True)
    global validation
    global host_name
    host_name = task.host.name
    validation = task.run(
        task=write_file,
        append=False,
        content=r.result,
        filename=f"" + str(date_dir) + "/" + task.host.name + ".txt",
    )


    print(validation.changed)
    print(validation.diff)

    
 
nr = InitNornir(config_file="config.yaml")
 
 
result = nr.run(
    name="Creating Backup Archive", task=backup_configurations
)

if validation.changed == True:
    moment = time.strftime("-%YY-%bM-%dD_%Hh_%Mm_%Ss",time.localtime())
    final_name = host_name+moment
    with open(final_name+'.txt', 'w') as f:
        with redirect_stdout(f):
            print_result(result)

    with open('diff-'+final_name+'.txt', 'w') as g:
        with redirect_stdout(g):
            print(validation.diff)

else:
    print("No changes in configuration")

 
 
