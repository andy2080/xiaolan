#!/bin/bash
sudo apt-get install omxplayer pulseaudio fswebcam cmake g++ gcc python2.7 python3 git python-dev python3-dev python-pyaudio python3-pyaudio sox python-demjson
sudo apt-get install python-wxgtk3.0
pip install pyaudio requests hyper crypto
sudo apt-get install python-opencv libatlas-base-dev
sudo apt-get install libevent-dev
sudo apt-get install memcached
echo "Installing SWIG"

if [ ! -e swig-3.0.10.tar.gz ]; then
  cp exteral_tools/swig-3.0.10.tar.gz ./ || \
  wget -T 10 -t 3 \
    http://prdownloads.sourceforge.net/swig/swig-3.0.10.tar.gz || exit 1;
fi

tar -xovzf swig-3.0.10.tar.gz || exit 1
ln -s swig-3.0.10 swig

cd swig

# We first have to install PCRE.
if [ ! -e pcre-8.37.tar.gz ]; then
  cp ../exteral_tools/pcre-8.37.tar.gz ./ || \
  wget -T 10 -t 3 \
    https://sourceforge.net/projects/pcre/files/pcre/8.37/pcre-8.37.tar.gz || exit 1;
fi
Tools/pcre-build.sh

./configure --prefix=`pwd` --with-pic
make
make install

cd ..
echo "请输入root账号的密码："
echo "如果输入完毕之后，停止了运行，在本脚本文件里找到本行，往下数第二行一直拖到最底复制带命令行中执行"
su root
cp /home/pi/xiaolan/memory_center/more/autostartxl /etc/init.d/
chmod +777 /etc/init.d/autostartxl
sudo update-rc.d autostartxl defaults
