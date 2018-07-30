//
// Created by DELL on 2018/7/28.
//
#include "test_face.h"
#include <iostream>
#include <string>
#include <stdio.h>
#include <regex>
#include <sstream>
#include <fstream>
#include <iterator>
#include <thread>
#include "opencv2/opencv.hpp"
#include "baidu_face_api.h"
#include "image_base64.h"
#include "cv_help.h"
#include "json/json.h"
#include "liveness.h"
#include "compare.h"
#include "setting.h"
#include <chrono>
#include <sys/time.h>

// 获取毫秒时间戳

int xiaolan_face_track_image(img)
{
    BaiduFaceApi *api = new BaiduFaceApi();
    api->sdk_init();
    cv::RotatedRect box;
    std::vector<TrackFaceInfo> *track_info = new std::vector<TrackFaceInfo>();
    return api->track_max_face(track_info, img, 2);
    delete api;
    delete track_info;
}

int xiaolan_face_track_video()
{
    BaiduFaceApi *api = new BaiduFaceApi();
    api->sdk_init();
    Liveness* liveptr = new Liveness();
    return liveptr->usb_track_face_info(api);
    delete liveptr;
}

int xiaolan_face_match(imgf, imgs)
{
    BaiduFaceApi *api = new BaiduFaceApi();
    api->sdk_init();
    return api->match(imgf, 2, imgs, 1);
    delete api;
}
