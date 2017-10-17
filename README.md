README for apt-dater-host
=========================

Setup hosts managed by apt-dater:
---------------------------------

  You need a SSH server and `sudo` installed. Create a user (`the-user` in this
  example) which will be used to install updates (using root is NOT recommended).

    useradd the-user

  Modify the sudoers rules, e.g. `/etc/sudoers` or `/etc/sudoers.d/apt-dater-host`:

	Defaults env_reset,env_keep=MAINTAINER
	the-user ALL=NOPASSWD: /usr/bin/apt-get, /usr/bin/aptitude, /usr/sbin/needrestart

  For non apt-based distributions you need to replace
  `/usr/bin/apt-get, /usr/bin/aptitude` with the equivalent, e.g. `/usr/bin/yum`.

  You can verify the setup by calling

    sudo -l -U the-user

Additional steps for a manual `apt-dater-host` installation:
------------------------------------------------------------

  Put `apt-dater-host` on the managed host (folder must be present in `$PATH` of `the-user`).

  Put `apt-dater-host.conf` to `$CFGFILE` (default is `/etc/apt-dater-host.conf`).

At your management server:
--------------------------

  Create a user on your management server which perform updates on your
  hosts.

  Generate a SSH keypair:

    ssh-keygen [..] -f ~/.ssh/apt-dater

  Distribute the public key(s) e.g.:

    ssh-copy-id -i ~/.ssh/apt-dater.pub the-user@managed-host
