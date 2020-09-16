# -*- coding: utf-8 -*-
"""
# @file       error.py
# @brief      error definitions
"""

#
# Base HTTP Errors
#

class WebapiError(object):
    """
    Web API Base Error
    """
    status = 500
    code = 0
    message = 'Internal server error.'


class BadRequest(WebapiError):
    """
    Bad Request
    """
    status = 400
    message = 'The request had bad syntax.'


class Unauthorized(WebapiError):
    """
    Unauthorized
    """
    status = 401
    message = 'Authentication required.'


class Forbidden(WebapiError):
    """
    Forbidden
    """
    status = 403
    message = 'The request is forbidden.'


class Notfound(WebapiError):
    """
    Not found
    """
    status = 404
    message = 'The resource is not found.'


class Conflict(WebapiError):
    """
    Conflict
    """
    status = 409
    message = 'The request is not conflicted.'


class MethodNotAllowed(WebapiError):
    """
    Method Not Allowed
    """
    status = 405
    message = 'The request is not allowed.'


class LengthRequired(WebapiError):
    """
    Length Required
    """
    status = 411
    message = 'Length Required.'

class UnsupportedMediaType(WebapiError):
    """
    Unsupported Media Type
    """
    status = 415
    message = 'The media type is unsupported.'


class InternalServerError(WebapiError):
    """
    Internal Server Error
    """
    status = 500
    message = 'Internal server error.'


#
# 00xx: Generic Errors
#

class BadRequestFormat(BadRequest):
    """
    Invalid parameter
    """
    code = 1
    message = 'Invalid request format.'


class InvalidParameter(BadRequest):
    """
    Invalid parameter
    """
    code = 2
    message = 'Invalid request parameter.'


class InvalidParameterFmt(BadRequest):
    """
    Invalid parameter
    """
    code = 2
    message = 'Invalid request parameter: {0}.'


class MissingParameter(BadRequest):
    """
    Invalid parameter
    """
    code = 3
    message = 'Missing required parameter.'


class MissingParameterFmt(BadRequest):
    """
    Invalid parameter
    """
    code = 3
    message = 'Missing required parameter: {0}.'


class UnauthorizedRequest(Unauthorized):
    """
    UnauthorizedRequest
    """
    code = 4
    message = 'The request need to be authorized.'


class ForbiddenRequest(Unauthorized):
    """
    ForbiddenRequest
    """
    code = 5
    message = 'The request is forbidden.'


class ResourceNotFound(Notfound):
    """
    Resource is not found
    """
    code = 6
    message = 'The desired resource is not found.'


class UnsupportedOperation(MethodNotAllowed):
    """
    The operation is not supported
    """
    code = 7
    message = 'Unsupported operation.'


class InvalidState(Conflict):
    """
    Invalid state
    """
    code = 8
    message = 'Request can not be complished at this state.'


class TimeoutError(InternalServerError):
    """
    Request is timeout
    """
    code = 9
    message = 'This request is timeout.'


class UpdateResourceFail(InternalServerError):
    """
    Fail to update the resource
    """
    code = 10
    message = 'Fail to update the resource.'


class UpdateResourceSettingFail(InternalServerError):
    """
    Fail to update the resource
    """
    code = 11
    message = 'Fail to update the resource setting: {0}.'


class AddResourceFail(InternalServerError):
    """
    Fail to add a new resource
    """
    code = 12
    message = 'Fail to add a new resource.'


class RemoveResourceFail(InternalServerError):
    """
    Fail to remove the resource
    """
    code = 13
    message = 'Fail to remove the resource.'


class RestartServiceFail(InternalServerError):
    """
    Fail to restart the service
    """
    code = 14
    message = 'Fail to restart the service.'

class InsufficientStorage(InternalServerError):
    """
    Insufficient Storage
    """
    code = 15
    message = 'Insufficient storage.'


#
# 01XX: Authentication
#


class AuthenticationFail(Unauthorized):
    """
    AuthenticationFail
    """
    code = 101
    message = 'Incorrect user name or password.'


class MaxSessionExceeded(Unauthorized):
    """
    MaxSessionExceeded
    """
    code = 102
    message = 'Server has exceeded the maximum number of sessions.'


class RequestIsUnauthorized(Unauthorized):
    """
    RequestIsUnauthorized
    """
    code = 103
    message = 'This request is unauthorized.'

class RequestIsForbidden(Forbidden):
    """
    RequestIsForbidden
    """
    code = 104
    message = 'This request is forbidden.'

class MaxLoginTriesExceeded(Forbidden):
    """
    MaxErrorTriesExceeded
    """
    code = 105
    message = 'Client exceeded maximum login tries. please wait {0} seconds.'

class UsernamePasswordNeedChange(Forbidden):
    """
    UsernamePasswordNeedChange
    """
    code = 106
    message = 'Please log in with administrator and change default password first.'