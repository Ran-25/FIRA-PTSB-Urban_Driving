// Auto-generated. Do not edit!

// (in-package donkey_service.srv)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------


//-----------------------------------------------------------

class DistanceDataRequest {
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
    // Serializes a message object of type DistanceDataRequest
    // Serialize message field [dataresponse]
    bufferOffset = _serializer.byte(obj.dataresponse, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type DistanceDataRequest
    let len;
    let data = new DistanceDataRequest(null);
    // Deserialize message field [dataresponse]
    data.dataresponse = _deserializer.byte(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 1;
  }

  static datatype() {
    // Returns string type for a service object
    return 'donkey_service/DistanceDataRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'f4d21e51ccccd78f0f83658973688752';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    # request params
    byte dataresponse
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new DistanceDataRequest(null);
    if (msg.dataresponse !== undefined) {
      resolved.dataresponse = msg.dataresponse;
    }
    else {
      resolved.dataresponse = 0
    }

    return resolved;
    }
};

class DistanceDataResponse {
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
    // Serializes a message object of type DistanceDataResponse
    // Serialize message field [datarequest]
    bufferOffset = _serializer.byte(obj.datarequest, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type DistanceDataResponse
    let len;
    let data = new DistanceDataResponse(null);
    // Deserialize message field [datarequest]
    data.datarequest = _deserializer.byte(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 1;
  }

  static datatype() {
    // Returns string type for a service object
    return 'donkey_service/DistanceDataResponse';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'dd72dc7f3ab95b8a0d20f092cbdcef1d';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    # response params
    byte datarequest
    
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new DistanceDataResponse(null);
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
  Request: DistanceDataRequest,
  Response: DistanceDataResponse,
  md5sum() { return '89951c538fe0bce2d7e1746ebb68223c'; },
  datatype() { return 'donkey_service/DistanceData'; }
};
