#!/usr/bin/env python3

import os

config = { 
    "acs_startup" : "/opt/ACS_Server_2020/bin/startup.sh",
    "acs_port" : 2020,
    "ss_cmd" : "/usr/sbin/ss"

}

class RestartACS:
    def __init__(self):
        pass

    def is_acs_running(self):
        # 返回 0 ，acs没有在运行
        # 返回一个整数，acs运行时的pid
        cmd = "%s -tnpl|grep %d" %(config['ss_cmd'], config['acs_port'])
        out = os.popen(cmd, "r")
        for l in out.split(""):
            print(l)


    def run(self):
        pass

o = RestartACS()
o.is_acs_running()