// Auto-generated. Do not edit!

// (in-package acc_urban_service.srv)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------


//-----------------------------------------------------------

class YoloDataRequest {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.dataresponse = null;
    }
    else {
      if (initObj.hasOwnProperty('dataresponse')) {
        this.dataresponse = initObj.dataresponse
      }
      else {
        this.dataresponse = 0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type YoloDataRequest
    // Serialize message field [dataresponse]
    bufferOffset = _serializer.int8(obj.dataresponse, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type YoloDataRequest
    let len;
    let data = new YoloDataRequest(null);
    // Deserialize message field [dataresponse]
    data.dataresponse = _deserializer.int8(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 1;
  }

  static datatype() {
    // Returns string type for a service object
    return 'acc_urban_service/YoloDataRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'e8e1ed04d7ba0e0327b8fd9f5c992770';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    int8 dataresponse
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new YoloDataRequest(null);
    if (msg.dataresponse !== undefined) {
      resolved.dataresponse = msg.dataresponse;
    }
    else {
      resolved.dataresponse = 0
    }

    return resolved;
    }
};

class YoloDataResponse {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.datarequest = null;
    }
    else {
      if (initObj.hasOwnProperty('datarequest')) {
        this.datarequest = initObj.datarequest
      }
      else {
        this.datarequest = 0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type YoloDataResponse
    // Serialize message field [datarequest]
    bufferOffset = _serializer.int8(obj.datarequest, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type YoloDataResponse
    let len;
    let data = new YoloDataResponse(null);
    // Deserialize message field [datarequest]
    data.datarequest = _deserializer.int8(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 1;
  }

  static datatype() {
    // Returns string type for a service object
    return 'acc_urban_service/YoloDataResponse';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'b80a56dcde916e60c3c82cddd4361019';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    int8 datarequest
    
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new YoloDataResponse(null);
    if (msg.datarequest !== undefined) {
      resolved.datarequest = msg.datarequest;
    }
    else {
      resolved.datarequest = 0
    }

    return resolved;
    }
};

module.exports = {
  Request: YoloDataRequest,
  Response: YoloDataResponse,
  md5sum() { return 'ca9f53be18d1fb6d1c1bfa0848d05366'; },
  datatype() { return 'acc_urban_service/YoloData'; }
};
