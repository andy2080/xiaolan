
#include "liveness.h"
#include <iostream>
#include <string>
#include <stdio.h>
#include <regex>
#include <sstream>
#include <fstream>
#include <iterator>
#include <thread>
#include "baidu_face_api.h"
#include "image_base64.h"
#include "cv_help.h"
#include "json/json.h"
Liveness::Liveness()
{
}

Liveness::~Liveness()
{
}


// usb摄像头人脸检测
void Liveness::usb_track_face_info(BaiduFaceApi *api)
{
   
    int device = 1; // 默认检测摄像头为0,若不对，可依次修改为1-10,实际上为您设备接上摄像头后认定的图像设备id
    cv::VideoCapture cap(device);
    if (!cap.isOpened())
    {
        std::cout << "open camera error" << std::endl;
        return;
    }
    cv::Mat frame;
    bool stop = false;
    int index = 0;
    bool save_file = true; //可选择是否保存检测到的图片
    cv::RotatedRect box;
    std::vector<TrackFaceInfo> *track_info = new std::vector<TrackFaceInfo>();
    while ( !stop )
    {
        cap >> frame;
        track_info->clear();
        
        int size = api->track_max_face(track_info, frame, 1);
        if ( size > 0 )
        {
            TrackFaceInfo info = track_info->at(i);
            std::cout << "camera_track score is:" << info.score << std::endl;

            cv::imwrite("/home/pi/xiaolan/memory_center/face_img/train.jpg", frame);
            bool stop = true;
        }
        else
        {
            frame.release();
        };
    };
    return size;
    delete track_info;
}


int Liveness::image_track_face_info(BaiduFaceApi *api)
{
   
    cv::RotatedRect box;
    std::vector<TrackFaceInfo> *track_info = new std::vector<TrackFaceInfo>();
    std::string img_path = "/home/pi/xiaolan/memory_center/face_img/face.jpg";
    int size = api->track(track_info, img_path.c_str(), 2,1);

    if (size > 0)
    {
        for (int i = 0; i < size; i++)
	{
	    TrackFaceInfo info = track_info->at(i);
	    std::cout << "in Liveness::image_track_face_info score is:" << info.score << std::endl;
	    // 人脸框信息
	    FaceInfo ibox = info.box;
	    // 角度
	    std::cout << "in Liveness::image_track_face_info mAngle is:" << ibox.mAngle << std::endl;
	    // 人脸宽度
	    std::cout << "in Liveness::image_track_face_info mWidth is:" << ibox.mWidth << std::endl;
	    // 中心点X，Y坐标
	    std::cout << "in Liveness::image_track_face_info mCenter_x is:" << ibox.mCenter_x << std::endl;
	    std::cout << "in Liveness::image_track_face_info mCenter_y is:" << ibox.mCenter_y << std::endl;
	    std::vector<float> headPose = info.headPose;
	    // 返回x y z三个角度的人脸角度
	    for (int k = 0; k < headPose.size(); k++)
	    {
                float angle = headPose.at(k);
		std::cout << "in Liveness::image_track_face_info angle is:" << angle << std::endl;
	    }
	    // 画人脸框
	   // box = CvHelp::bounding_box(info.landmarks);
	   // CvHelp::draw_rotated_box(frame, box, cv::Scalar(0, 255, 0));
	    // 画关键点轮廓
	    //CvHelp::draw_shape(info.landmarks, frame, cv::Scalar(0, 255, 0));
	}
    }
    else
    {
	std::cout << "image has no face!" << std::endl;
    }


    
    delete track_info;
}

