#!/usr/bin/env python3

import os
import socket
import select
import re
import signal
import time
import logging

config = { 
    "acs_root" : "/opt/ACS_Server_2020",
    "acs_port" : 2020,
    "acs_ip" : "127.0.0.1",
    "timeout" :5,
    "ss_cmd" : "/usr/sbin/ss -tlpn|grep %s",
}

class RestartACS:
    def __init__(self):
        logging.Config()
        pass

    def check_acs(self, port):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.setblocking(True)
            s.connect((config['acs_ip'], port))
            s.send("TEST\n\r".encode("utf-8"))

            ready = select.select([s], [], [], config['timeout'])
            if ready[0]:
                # ok
                res = s.recv(1024).decode("utf-8").strip()
                if res == "无效指令":
                    s.close()
                    return True
            else:
                # not ok
                return False

        except Exception:
            return False

    def find_acs_process(self, port):
        cmd = config['ss_cmd'] % (port)
        pipe = os.popen(cmd, "r")
        out = pipe.readlines()
        pipe.close()
        for l in out:
            m = re.match(r'.*users:\(\("java",pid=(\d+),fd=(\d+)\)\)', l)
            pid = int(m.group(1))
            return pid
        return 0

    def kill_acs(self, port):
        pid = self.find_acs_process(port)
        if pid == 0:
            # ACS not running
            return 0
        os.kill(pid, signal.SIGTERM)
        time.sleep(0.5)
        try:
            os.kill(pid, 0)
            # 说明pid还在
            return -1  #无法kill
        except OSError:
            # 说明pid没有了
            print("killed")
            return 0   # kill完成

    def start_acs(self):
        cmd = config['acs_root'] + "/bin/startup.sh"
        system(cmd)

    def run(self):
        if self.check_acs(config['acs_port']) == False:  
            # ACS failed
            self.kill_acs(config['acs_port'])
            self.start_acs()



o = RestartACS()
o.run()