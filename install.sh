mydir=$PWD
cd $TMPDIR
mkdir hacktech
cd hacktech
git clone git://github.com/kennethreitz/requests.git
cd requests
sudo python2.7 setup.py install
sudo python3 setup.py install
cd ..
git clone https://github.com/jdberry/tag.git
cd tag
make && sudo make install
cd $mydir
