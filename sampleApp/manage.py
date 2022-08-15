import argparse
import subprocess
import sys


ALLOWED_OPERATION_TYPES = ('core', 'local', 'docker')

def install_libraries(file_name: str) -> None:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', f'requirements/{file_name}.txt'])


cli_parser = argparse.ArgumentParser()
cli_parser.add_argument('-i', '--install', default='core')

args = cli_parser.parse_args()
operation_type: str = args.install.lower()

if operation_type in ALLOWED_OPERATION_TYPES:
    install_libraries('core')
    match operation_type:
        case "local":
            install_libraries('local')
        case "docker":
            install_libraries('docker')
else:
    print(f'Operation {operation_type} is not allowed')
