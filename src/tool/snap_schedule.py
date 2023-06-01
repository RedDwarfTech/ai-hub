import os
import sched
import time


def delete_old_files(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)
            if os.stat(file_path).st_mtime < time.time() - 86400:
                os.remove(file_path)


s = sched.scheduler(time.time, time.sleep)


def delete_files(scheduler, path):
    delete_old_files(path)
    s.enter(3600, 1, delete_files, (scheduler, path))  # 每隔1小时执行一次


path_list = ['/opt/snap/photo']
for path in path_list:
    s.enter(0, 1, delete_files, (s, path))

s.run()
