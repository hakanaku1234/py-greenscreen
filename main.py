import os.path as osp
import sys
import time

import main_cfg as mc
from gs import config as cf
from gs import create_training_data as ctd
from gs import plot_tryout as plt
from gs import train_model as tm
from gs import train_model_opt as tmo
from gs import use_model as um


def _timestamp() -> str:
    return time.strftime("%Y%m%d_%H%M%S", time.localtime())


def _root_dir() -> str:
    return osp.dirname(sys.argv[0])


def fullRun():
    timestamp = _timestamp()
    root_dir = _root_dir()
    _id = sys.argv[1]

    print("Arguments")
    print("   id        : {}".format(_id))
    print("   rootdir   : {}".format(root_dir))
    print("   timestamp : {}".format(timestamp))

    cfg = cf.conf(_id, root_dir)

    ctd.create(work_dir=mc.work_dir, cfg=cfg)
    tm.train(cfg)
    um.use(cfg, timestamp)
    print("FINISHED")


def create():
    root_dir = _root_dir()
    _id = 'img500'

    print("STARTED create")
    print("   id        : {}".format(_id))
    print("   rootdir   : {}".format(root_dir))
    print("   workdir   : {}".format(mc.work_dir))
    cfg = cf.conf(_id, root_dir)
    ctd.create(mc.work_dir, cfg)
    print("FINISHED create")


def opt():
    root_dir = _root_dir()
    _id = 'img100'

    print("STARTED create")
    print("   id        : {}".format(_id))
    print("   rootdir   : {}".format(root_dir))
    print("   workdir   : {}".format(mc.work_dir))

    tmo.run(_id, work_dir=mc.work_dir, root_dir=root_dir)


def plot():
    plt.tryout_multi(mc.work_dir)
    plt.tryout(mc.work_dir)


# plot()
# opt()
create()
