FACE_LIB=./facelib
LIB3=./lib3
CURL=$LIB3/curl-linux/lib-ubuntu
JSON=$LIB3/json/lib-ubuntu
OPENBLAS=$LIB3/openblas-linux/lib
OPENCV=$LIB3/opencv-linux/lib
FFMPEG=$LIB3/ffmpeg-linux/lib
LIB64=$LIB3/lib64
LIBS=$OPENBLAS:$OPENCV:$FACE_LIB:$CURL:$LIB64:$FFMPEG:$JSON
echo $LIBS
export LD_LIBRARY_PATH=$LIBS
./tool-ubuntu 5WUM-DFOR-EKMD-WB74
