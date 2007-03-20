all:
	echo 'make install - Installation'
	echo 'make restart - Restart Apache'

install:
	cp cgi/pymweb.py /usr/lib/cgi-bin/
	cp dtd/table.dtd /var/www/
	cp www/pymweb.html /var/www/
	cp -r www/images/ /var/www/
	cp conf/pymweb.conf /etc/apache/conf/

restart:
	/etc/init.d/apache restart