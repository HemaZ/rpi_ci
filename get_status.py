import json
import sys
import time
import errno
import os


def get_status():
    os.system("sh get_stats.sh")
    f = open('projects.json',)
    data = json.load(f)
    return data


if __name__ == "__main__":
    status = "waiting"
    project_name = sys.argv[1]
    print(project_name)

    while(status == "waiting" or status == "building"):
        time.sleep(1)
        data = get_status()
        for project in data['projects']:
            if project['name'] == project_name:
                status = project['status']
                print(status)
                break

    if status == "error":
        sys.exit(errno.EACCES)
    else:
        sys.exit(0)
