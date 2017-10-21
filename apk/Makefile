clean:

check:
	./test-apt-dater-host

install:
	install -D -m0755 apt-dater-host \
		$(DESTDIR)/usr/bin/apt-dater-host

	install -m0750 -d $(DESTDIR)/etc/sudoers.d
	install -m0640 apt-dater-host-sudoers \
		$(DESTDIR)/etc/sudoers.d/apt-dater-host
