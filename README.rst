stormpath-seed
==============

Seed your Stormpath Application with fake user data.

.. image:: https://img.shields.io/pypi/v/stormpath-seed.svg
    :alt: stormpath-seed Release
    :target: https://pypi.python.org/pypi/stormapth-seed

.. image:: https://img.shields.io/pypi/dm/stormpath-seed.svg
    :alt: stormpath-seed Downloads
    :target: https://pypi.python.org/pypi/stormpath-seed

.. image:: https://img.shields.io/travis/rdegges/stormpath-seed.svg
    :alt: stormpath-seed Build
    :target: https://travis-ci.org/rdegges/stormpath-seed

.. image:: https://github.com/rdegges/stormpath-seed/raw/master/assets/tree-sketch.png
   :alt: Tree Sketch


Meta
----

- Author: Randall Degges
- Email: r@rdegges.com
- Site: http://www.rdegges.com
- Status: maintained, active


Purpose
-------

If you're using `Stormpath <https://stormpath.com/>`_ to store your user
accounts (*which you should be!*), and you want to create a bunch of fake user
accounts for your application, **stormpath-seed** can help!

Whether you want to create fake users to:

- See how well Stormpath performs.
- Create a bunch of fake users for your "social" application (like `reddit
  <http://motherboard.vice.com/read/how-reddit-got-huge-tons-of-fake-accounts--2>`_).
- Or some other random reason.

**stormpath-seed** makes this process easy!  It creates fake user accounts for
you, is totally configurable, and is simple to use.  Bam.


Installation
------------

To install **stormpath-seed**, simply run:

.. code-block:: console

    $ pip install stormpath-seed

This will install the latest version automatically.

.. note::
    If you get a bunch of random errors and the install can't finish, try
    installing ``libevent-dev`` using your operating system's package manager.
    **stormpath-seed** uses `gevent <http://www.gevent.org/>`_ for concurrency,
    which is why that OS package must be installed.


Usage
-----

To use this tool, simply run ``$ stormpath-seed --help`` from the command line.
It provides all the documentation you need to get started.

**BUT**...  Since I know you're lazy and don't want to read the docs I slaved
over, here's a summary:

Run the following command to store / save your Stormpath API credentials (*this
isn't necessary, but makes things simpler*):

.. code-block:: console

    $ stormpath-seed --configure

This will prompt you for your credentials, and save them as
``~/.stormpath/seed.json``.

To use the tool to create fake users, here's a simple example:

.. code-block:: console

    $ stormpath-seed --application my-app --total-users 1000

This will create 1,000 fake user accounts in the Stormpath Application named
*"my-app"*.  If the *"my-app"* Application doesn't exist: it will be created
automatically.

Now, by default the above command will just create some **really fake**
accounts.  It'll use UUIDs as the account names / emails.  If you want something
a bit more real looking, you do this:

.. code-block:: console

    $ stormpath-seed --application my-app --total-users 1000 --real-users

This will create user accounts that look totally real and legit.  How does this
work?  It uses the amazing and awesome `randomuser.me <https://randomuser.me/>`_
API service.

.. note::
    Huge shout out to the randomuser.me team.  Ya'll are killin' it.  Your site
    is beautiful, I love the stats page, and your API is a pleasure to use.  If
    you're in the bay area `hit me up <mailto:r@rdegges.com>`_ for some free
    coffee!  <333

Want to create users faster?  You can control the concurrency like so:

.. code-block::

    $ stormpath-seed --application my-app --total-users 1000 --concurrency 20

*By default, stormpath-seed will create 100 users, with 5 concurrency, in an
Application named "stormpath-seed".*

Lastly, if you're using a private deployment of Stormpath, you can use the
``base-url`` flag like so:

.. code-block::

    $ stormpath-seed --application my-app --total-users 100000 --url https://api.myprivateapi.com/v1

Bam.


Contributing
------------

This project is only possible due to the amazing contributors who work on it!

If you'd like to improve this library, please send me a pull request! I'm happy
to review and merge pull requests.

The standard contribution workflow should look something like this:

- Fork this project on Github.
- Make some changes in the master branch (*this project is simple, so no need to
  complicate things*).
- Send a pull request when ready.


Change Log
----------

All library changes, in descending order.


Version 0.0.3
*************

**Released September 21, 2016.**

- Updating randomuser.me API endpoints to reflect their new API stuff.


Version 0.0.2
*************

**Released September 15, 2015.**

- Fixing bugs with latest release of docopt.
- Fixing poor --configure handling.
- Adding support for configuring the Stormpath base URL in the seed.json config
  file.
- Fixing small bugs.
- Adding Travis CI builds.
- Modifying options to be simpler.


Version 0.0.1
*************

**Released March 2, 2014.**

- First release!
