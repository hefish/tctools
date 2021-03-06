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
    "acs_pid" : "/opt/ACS_Server_2020/bin/acs.pid",
}

class RestartACS:
    def __init__(self):
        logging.basicConfig(
            filename=os.path.dirname(__file__) + "/logs/restart-acs.log",
            filemode="a",
            format="%(asctime)s %(message)s", 
            level=logging.INFO
        )
        pass

    def check_acs(self, port):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.setblocking(True)
            s.connect((config['acs_ip'], port))
            s.send("9300CN123456|CO654321|AY1AZF9C5\n".encode("utf-8"))

            ready = select.select([s], [], [], config['timeout'])
            if ready[0]:
                # ok
                res = s.recv(1024).decode("utf-8").strip()
                if res == "941AY3AZFDFA":
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

    def kill_acs(self):
        try:
            pid = int(open(config['acs_pid']).read(1000))
        except :
            return  
        if pid == 0:
            # ACS not running
            return 0
        try:
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
        except OSError:
            return 0

    def start_acs(self):
        cmd = config['acs_root'] + "/bin/startup.sh"
        os.system("su - hefish -c \""+cmd+"\"")

    def run(self):
        if self.check_acs(config['acs_port']) == False:  
            # ACS failed
            logging.info("ACS failed, restarting...")
            self.kill_acs()
            self.start_acs()



o = RestartACS()
o.run()
