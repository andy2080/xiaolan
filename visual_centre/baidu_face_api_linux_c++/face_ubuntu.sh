FACE_LIB=./facelib
LIB3=./lib3
OPENBLAS=$LIB3/openblas-linux/lib
OPENCV=$LIB3/opencv-linux/lib
CURL=$LIB3/curl-linux/lib-ubuntu
LIB64=$LIB3/lib64
LIB_SO=./so
FFMPEG=$LIB3/ffmpeg-linux/lib
JSON=$LIB3/json/lib-ubuntu
LIBS=$OPENBLAS:$OPENCV:$FACE_LIB:$CURL:$LIB64:$FFMPEG:$JSON
echo $LIBS
export LD_LIBRARY_PATH=$LIBS
#catchsegv ./face
./face
