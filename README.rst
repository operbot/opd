README
######


**M A N P A G E**


**NAME**


 **OPD** - operator daemon


**SYNOPSIS**


 ``opd [cmd] [-c] [-i] [key=value] [key==value]``


**DESCRIPTION**

 **OPD** is a solid, non hackable, back after reboot, intended to be
 programmable in a static, only code, no popen, no imports and no reading
 modules from a directory bot, it's  source is :ref:`here <source>`.

 **OPD** is programmable, to program the bot you have to have the code
 available as employing your own code requires that you install your own bot as
 the system bot. This is to not have a directory to read modules from to add
 commands to the bot but include the own programmed modules directly into the
 python code, so only trusted code (your own written code) is included and
 runnable. Reading random code from a directory is what gets avoided.

 **OPD** stores it's data on disk where objects are time versioned and the
 last version saved on disk is served to the user layer. Files are JSON dumps
 that are read-only so thus should provide (disk) persistence more chance.
 Paths carry the type in the path name what makes reconstruction from filename
 easier then reading type from the object.


**INSTALL**


 ``pip3 install opd --upgrade --force-reinstall``

**CONFIGURATION**

 configuration is done by calling the ``cfg`` command of the bot.

 **irc**

 | ``opc cfg server=<server> channel=<channel> nick=<nick>``

 | (*) default channel/server is #opd on localhost

 **sasl**

 | ``opc pwd <nickservnick> <nickservpass>``
 | ``opc cfg password=<outputfrompwd>``

 **users**

 | ``opc cfg users=True``
 | ``opd met <userhost>``


 **rss**

 | ``opc rss <url>``
 |

**COMMANDS**

 here is a short description of the commands.

 | ``cmd`` - shows all commands
 | ``cfg`` - shows the irc configuration, also edits the config
 | ``dlt`` - removes a user from bot
 | ``dpl`` - sets display items for a rss feed
 | ``ftc`` - runs a rss feed fetching batch
 | ``fnd`` - allows you to display objects on the datastore, read-only json files on disk 
 | ``flt`` - shows a list of bot registered to the bus
 | ``log`` - logs some text
 | ``met`` - adds a users with there irc userhost
 | ``mre`` - displays cached output, channel wise.
 | ``nck`` - changes nick on irc
 | ``pwd`` - combines a nickserv name/password into a sasl password
 | ``rem`` - removes a rss feed by matching is to its url
 | ``rss`` - adds a feed to fetch, fetcher runs every 5 minutes
 | ``thr`` - show the running threads
 | ``tdo`` - adds a todo item, no options returns list of todo's
 |


**PROGRAMMING**


The ``opd`` package provides an Object class, that allows for save/load to/from
json files on disk. Objects can be searched with database functions and uses
read-only files to improve persistence and a type in filename for
reconstruction. Methods are factored out into functions to have a clean
namespace to read JSON data into.

``opd`` stores it's data on disk where objects are time versioned and the
last version saved on disk is served to the user layer. Files are JSON dumps
that are read-only so thus should provide (disk) persistence. Paths carry the
type in the path name what makes reconstruction from filename easier then
reading type from the object.

|

**INSTALL**

| ``pip3 install opd --upgrade --force-reinstall``
|

**PROGRAMMING**

basic usage is this::

 >>> import opd
 >>> o = opd.Object()
 >>> o.key = "value"
 >>> o.key
 >>> 'value'

Objects try to mimic a dictionary while trying to be an object with normal
attribute access as well. hidden methods are provided, the methods are
factored out into functions like get, items, keys, register, set, update
and values.

load/save from/to disk::

 >>> from opd import Object, load, save
 >>> o = Object()
 >>> o.key = "value"
 >>> p = save(o)
 >>> obj = Object()
 >>> load(obj, p)
 >>> obj.key
 >>> 'value'

great for giving objects peristence by having their state stored in files::

 >>> from opd import Object, save
 >>> o = Object()
 >>> save(o)
 'opd.obj.Object/2021-08-31/15:31:05.717063'


**AUTHOR**

 Bart Thate

**COPYRIGHT**

 **OPD** is placed in the Public Domain. No Copyright, No License.


