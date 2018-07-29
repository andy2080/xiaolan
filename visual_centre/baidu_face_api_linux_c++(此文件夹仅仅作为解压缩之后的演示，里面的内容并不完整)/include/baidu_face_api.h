#ifndef __BAIDU_FACE_API_H__
#define __BAIDU_FACE_API_H__

#include "opencv2/opencv.hpp"
//#include "i_face_api.h"

#ifdef __cplusplus
extern "C" {
#endif

struct FaceInfo
{
    float mWidth;     // rectangle width
    float mAngle;     // rectangle tilt angle [-45 45] in degrees
    float mCenter_y;  // rectangle center y
    float mCenter_x;  // rectangle center x
    float mConf;
};
struct TrackFaceInfo
{
    TrackFaceInfo() {}

    FaceInfo box;
    std::vector<int> landmarks;
    float score;
    unsigned long face_id;
    std::vector<float> headPose;

};
	

class BaiduFaceApi
{
public:
   BaiduFaceApi();
    ~BaiduFaceApi();
    int sdk_init();
    bool is_auth();

    //人脸特性 
    const char* face_attr(const char* image,int img_type);
    // 质量评分
    const char* face_quality(const char* image,int img_type);
    // 1:1 对比(img_type为1表示传入base64图片，为2表示传入文件路径）
    const char* match(const char* image1, int img_type1, const char* image2, \
			int img_type2);
    // 1:1 对比(img_type为1表示传入base64图片，为2表示传入文件路径,mat为opencv的视频帧）    
    const char* match_by_img_and_frame(const char* image1, int img_type1, const cv::Mat &mat);
    // 1:1 对比(// 1:1 对比(img_type为1表示传入base64图片，为2表示传入文件路径,f1为512个浮点值的人脸特征） 
    const char* match_by_feature(const std::vector<float>& f1, const char* image2, \
	        int img_type2);
	    
    
    //以下为采集函数设置
    // 设置是否执行质量检测，默认为false
    void set_isCheckQuality(bool flag=false);
    // 光照阈值，取值范围0~255，默认40，越大代表脸部越亮
    void set_illum_thr(float thr = 40);
    // 模糊阈值，取值范围0~1，默认0.7，越小代表图像越清晰
    // 当设置为1时，模糊检测不进行且结果不通过；当设置为0时，模糊检测不进行且结果通过
    void set_blur_thr(float thr=0.7);
    // 右眼、左眼、鼻子、嘴巴、左脸颊、右脸颊、下巴的遮挡阈值，取值范围0~1，默认0.5，值越小代表遮挡程序越小
    // 当设置为1时，遮挡检测不进行且结果不通过；当设置为0时，遮挡检测不进行且结果通过
    void set_occlu_thr(float thr=0.5);
    // 设置pitch、yaw、roll等角度的阈值，默认都为15&deg;，越大代表可采集的人脸角度越大，但是角度越大识别效果会越差
    void set_eulur_angle_thr(int pitch_thr=15, int yaw_thr=15, int roll_thr=15);

    // 非人脸的置信度阈值，取值范围0~1，取0则认为所有检测出来的结果都是人脸，默认0.5
    void set_notFace_thr(float thr=0.5);
    // 最小人脸尺寸：需要检测到的最小人脸尺寸，比如需要检测到30*30的人脸则设置为30，
    // 该尺寸占图像比例越小则检测速度越慢，具体请参考性能指标章节。默认值30
    void set_min_face_size(int size =30);
    // 跟踪到目标后执行检测的时间间隔，单位毫秒，默认300，值越小越会更快发现新目标，但是cpu占用率会提高、处理速度变慢
    void set_track_by_detection_interval(int interval_in_ms = 300);
    // 未跟踪到目标时的检测间隔，单位毫秒，默认300，值越小越快发现新目标，但是cpu占用率会提高、处理速度变慢
    void set_detect_in_video_interval(int interval_in_ms=300);
    // 设置抠图大小，默认256像素
    //void set_cropFaceSize(int width = 256);
    // 获取人脸抠图的大小，以像素为单位
    //int get_cropFaceSize();
    // 设置抠图时截取的人脸大小倍数，默认3.0
    //void set_cropFace_enlarge_ratio(float ratio=3.0);
    /*
    * std::vector<TrackFaceInfo> *& out:传出的检测后人脸信息
	* const char* img  : Input img,1 is base64 img, 2 is file path
	* int imgType : Input img's coding type ,1 is base64 img, 2 is file path
	* int maxTrackObjNum: 最多要tracking人数，例如设置为1则只tracking一个人，如果设置为3则最多tracking 3个人。
	* return 为返回的检测人脸数量
    */
    int track(std::vector<TrackFaceInfo> *& out,const char* image, int img_type, int maxTrackObjNum);

    int track(std::vector<TrackFaceInfo> *& out,const cv::Mat &mat, int maxTrackObjNum);

    // 只跟踪最大人脸，参数同track
    int track_max_face(std::vector<TrackFaceInfo> *& out,const char* image, int img_type);
    int track_max_face(std::vector<TrackFaceInfo> *& out, const cv::Mat &mat);
    //清除已跟踪到的人脸信息
    void clearTrackedFaces();

    std::vector<TrackFaceInfo> *get_faces();
   

    //设置是否是激活工具
    void set_is_tools(bool is_tool);
    //获取检测到的人脸信息，返回int为人脸个数
    int get_tracked_faces(std::vector<TrackFaceInfo> *& vec);
    //获取人脸特征值(传入图片)
    int get_face_feature(const char* image,int img_type,const float* &feature);
    //获取人脸特征值(传入opencv视频帧）
    int get_face_feature(const cv::Mat &mat,const float*& feature);
    //特征值比对，返回比对分值
    float compare_feature(const std::vector<float>& f1,const std::vector<float>& f2);

    // 获取设备id
    const char* get_device_id();
private:
    std::string m_res;
    bool m_is_tool = false; 
    std::vector<TrackFaceInfo> m_tracked_faces;   
};


#ifdef __cplusplus
}
#endif


#endif
