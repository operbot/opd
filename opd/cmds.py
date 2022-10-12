# This file is placed in the Public Domain.
# pylint: disable=E1101,C0115,C0116,R0903


"object programming commands"


import threading
import time


from .cls import Class
from .dbs import find, fntime
from .fnc import name, printable
from .obj import Object, update
from .jsn import save
from .utl import elapsed
from .run import Bus, Command


starttime = time.time()


class Log(Object):

    def __init__(self):
        Object.__init__(self)
        self.txt = ""


Class.add(Log)


class Todo(Log):

    pass


Class.add(Todo)


def cmd(event):
    event.reply(",".join(sorted(Command.cmd)))


Command.add(cmd)


def dne(event):
    if not event.args:
        return
    selector = {"txt": event.args[0]}
    for _fn, obj in find("todo", selector):
        obj.__deleted__ = True
        save(obj)
        event.reply("ok")
        break


Command.add(dne)


def flt(event):
    try:
        index = int(event.args[0])
        event.reply(Bus.objs[index])
        return
    except (KeyError, TypeError, IndexError, ValueError):
        pass
    event.reply(" | ".join([name(o) for o in Bus.objs]))


Command.add(flt)


def log(event):
    if not event.rest:
        _nr = 0
        for _fn, obj in find("log"):
            event.reply("%s %s %s" % (
                                      _nr,
                                      obj.txt,
                                      elapsed(time.time() - fntime(_fn)))
                                     )
            _nr += 1
        return
    obj = Log()
    obj.txt = event.rest
    save(obj)
    event.reply("ok")


Command.add(log)


def sts(event):
    for bot in Bus.objs:
        try:
            event.reply("%s: %s (%s)" % (
                                         bot.cfg.server,
                                         printable(bot.state, skip="last"),
                                         elapsed(time.time()-bot.state.last))
                                        )
        except AttributeError:
            continue


Command.add(sts)


def tdo(event):
    if not event.rest:
        nmr = 0
        for _fn, obj in find("todo"):
            event.reply("%s %s %s" % (
                                      nmr,
                                      obj.txt,
                                      elapsed(time.time() - fntime(_fn)))
                                     )
            nmr += 1
        return
    obj = Todo()
    obj.txt = event.rest
    save(obj)
    event.reply("ok")


Command.add(tdo)


def thr(event):
    result = []
    for thread in sorted(threading.enumerate(), key=lambda x: x.getName()):
        if str(thread).startswith("<_"):
            continue
        obj = Object()
        update(obj, vars(thread))
        if getattr(obj, "sleep", None):
            uptime = obj.sleep - int(time.time() - obj.state.latest)
        else:
            uptime = int(time.time() - obj.starttime)
        result.append((uptime, thread.getName()))
    res = []
    for uptime, txt in sorted(result, key=lambda x: x[0]):
        res.append("%s/%s" % (txt, elapsed(uptime)))
    if res:
        event.reply(" ".join(res))
    else:
        event.reply("no threads running")


Command.add(thr)


def upt(event):
    event.reply(elapsed(time.time()-starttime))


Command.add(upt)
