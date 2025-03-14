// Generated by gencpp from file acc_urban_service/YoloData.msg
// DO NOT EDIT!


#ifndef ACC_URBAN_SERVICE_MESSAGE_YOLODATA_H
#define ACC_URBAN_SERVICE_MESSAGE_YOLODATA_H

#include <ros/service_traits.h>


#include <acc_urban_service/YoloDataRequest.h>
#include <acc_urban_service/YoloDataResponse.h>


namespace acc_urban_service
{

struct YoloData
{

typedef YoloDataRequest Request;
typedef YoloDataResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;

}; // struct YoloData
} // namespace acc_urban_service


namespace ros
{
namespace service_traits
{


template<>
struct MD5Sum< ::acc_urban_service::YoloData > {
  static const char* value()
  {
    return "ca9f53be18d1fb6d1c1bfa0848d05366";
  }

  static const char* value(const ::acc_urban_service::YoloData&) { return value(); }
};

template<>
struct DataType< ::acc_urban_service::YoloData > {
  static const char* value()
  {
    return "acc_urban_service/YoloData";
  }

  static const char* value(const ::acc_urban_service::YoloData&) { return value(); }
};


// service_traits::MD5Sum< ::acc_urban_service::YoloDataRequest> should match
// service_traits::MD5Sum< ::acc_urban_service::YoloData >
template<>
struct MD5Sum< ::acc_urban_service::YoloDataRequest>
{
  static const char* value()
  {
    return MD5Sum< ::acc_urban_service::YoloData >::value();
  }
  static const char* value(const ::acc_urban_service::YoloDataRequest&)
  {
    return value();
  }
};

// service_traits::DataType< ::acc_urban_service::YoloDataRequest> should match
// service_traits::DataType< ::acc_urban_service::YoloData >
template<>
struct DataType< ::acc_urban_service::YoloDataRequest>
{
  static const char* value()
  {
    return DataType< ::acc_urban_service::YoloData >::value();
  }
  static const char* value(const ::acc_urban_service::YoloDataRequest&)
  {
    return value();
  }
};

// service_traits::MD5Sum< ::acc_urban_service::YoloDataResponse> should match
// service_traits::MD5Sum< ::acc_urban_service::YoloData >
template<>
struct MD5Sum< ::acc_urban_service::YoloDataResponse>
{
  static const char* value()
  {
    return MD5Sum< ::acc_urban_service::YoloData >::value();
  }
  static const char* value(const ::acc_urban_service::YoloDataResponse&)
  {
    return value();
  }
};

// service_traits::DataType< ::acc_urban_service::YoloDataResponse> should match
// service_traits::DataType< ::acc_urban_service::YoloData >
template<>
struct DataType< ::acc_urban_service::YoloDataResponse>
{
  static const char* value()
  {
    return DataType< ::acc_urban_service::YoloData >::value();
  }
  static const char* value(const ::acc_urban_service::YoloDataResponse&)
  {
    return value();
  }
};

} // namespace service_traits
} // namespace ros

#endif // ACC_URBAN_SERVICE_MESSAGE_YOLODATA_H
