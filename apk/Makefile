clean:

check:
	./test-apt-dater-host

install:
	install -D -m0755 apt-dater-host \
		$(DESTDIR)/usr/bin/apt-dater-host

	install -m0755 -d $(DESTDIR)/etc/
	install -m0644 apt-dater-host.conf \
		$(DESTDIR)/etc/apt-dater-host.conf

	install -m0750 -d $(DESTDIR)/etc/sudoers.d
	install -m0640 apt-dater-host-sudoers \
		$(DESTDIR)/etc/sudoers.d/apt-dater-host

	install -m0750 -d $(DESTDIR)/etc/doas.d
	install -m0640 apt-dater-host-doas \
		$(DESTDIR)/etc/doas.d/apt-dater-host.conf
