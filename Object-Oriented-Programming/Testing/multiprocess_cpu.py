# -*- coding: utf-8 -*-

from multiprocessing import Process, cpu_count
import time
import os


class MuchCpu(Process):

    def run(self):
        print(os.getpid())
        for i in range(200000000):
            pass

if __name__ == '__main__':
    proc = [MuchCpu() for f in range(cpu_count())]
    t = time.time()
    for p in proc:
        p.start()
    for p in procs:
        p.join()
    print('work took {} seconds'.format(time.time() - t))
