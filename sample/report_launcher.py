#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""This is a sample launcher file."""

import argparse
from airtest.report.report import main as report_main
from airtest.utils.compat import decode_path, script_dir_name
from airtest.report.report import get_parger as report_parser
import os
import time
import subprocess
import logging
import sys
import platform

LOGDIR = "log"
if __name__ == "__main__":
    import sys
    ap = argparse.ArgumentParser()
    ap = report_parser(ap)
    args = ap.parse_args(sys.argv[1:])

    #----- S.Dan ---------------------
    path, name = script_dir_name(args.script)
    log_root = decode_path(args.log_root) or decode_path(os.path.join(path, LOGDIR))
    export = args.export
    script = args.script

    osname = True if platform.system() == "Windows" else False

    if not export: 
        if osname:
            export = log_root[0:log_root.rfind("\\")] + "\\ExportReport\\" + name[0:name.rfind(".")] + "_" + time.strftime("%Y%m%d_%H%M", time.localtime())
            cmd = sys.executable + " " + os.path.dirname(os.path.abspath(__file__)) + "\\report_launcher_ide.py " + script + " --log_root " + log_root + " --export " + export
            p = subprocess.Popen(cmd)
        else:
            export = log_root[0:log_root.rfind("/")] + "/ExportReport/" + name[0:name.rfind(".")] + "_" + time.strftime("%Y%m%d_%H%M", time.localtime())
            cmd = sys.executable + " " + os.path.dirname(os.path.abspath(__file__)) + "/report_launcher_ide.py " + script + " --log_root " + log_root + " --export " + export
            p = subprocess.Popen(cmd, shell=True)
        p.wait()
    #----- S.Dan ---------------------

    report_main(args)

