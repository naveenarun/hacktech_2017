currdir=$PWD
cd $TMPDIR
mkdir hacktech
cd hacktech
git clone https://github.com/jdberry/tag.git
cd tag
make && sudo make install
cd $currdir
